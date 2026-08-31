#!/usr/bin/env python3
"""raio-x-ad: prepare an ad video for a full teardown.

Given a local file or a URL, this builds a workspace with:
  - frames/         smart-sampled JPEGs (scene changes + dense hook + interval + end)
  - transcript.json Groq/OpenAI Whisper segments with timestamps + language
  - transcript.txt  readable [mm:ss] transcript in the original language
  - manifest.json   everything Claude needs to write the report

Frame strategy (tuned for direct-response ads, 15s to 3min):
  1. Scene-change detection  -> one frame per distinct shot (format/avatar/proof/product/CTA)
  2. Hook zone (0..HOOK s)   -> dense (catches the 4-layer hook)
  3. Interval baseline       -> guarantees coverage inside long continuous takes
  4. End zone (last 3s)      -> the CTA / cliffhanger frame
Frames are merged, de-duplicated by timestamp, capped, and named by timestamp.

Pure stdlib + ffmpeg/ffprobe (+ yt-dlp only when the input is a URL).
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import whisper_lib  # noqa: E402


# ------------------------------ helpers ------------------------------

def _require(binary: str, hint: str) -> None:
    if shutil.which(binary) is None:
        raise SystemExit(f"'{binary}' not found on PATH. {hint}")


def format_mmss(seconds: float) -> str:
    total = int(round(seconds))
    m, s = divmod(total, 60)
    return f"{m:02d}m{s:02d}s"


def is_url(value: str) -> bool:
    return value.startswith("http://") or value.startswith("https://")


def download(url: str, workdir: Path) -> Path:
    _require("yt-dlp", "Install with: brew install yt-dlp (only needed for URLs).")
    out = workdir / "source.%(ext)s"
    cmd = [
        "yt-dlp", "-f", "mp4/best", "--no-playlist",
        "-o", str(out), url,
    ]
    print(f"[raio-x-ad] downloading {url} …", file=sys.stderr)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f"yt-dlp failed: {result.stderr.strip()[:500]}")
    files = sorted(workdir.glob("source.*"))
    if not files:
        raise SystemExit("yt-dlp reported success but produced no file.")
    return files[0]


def probe(video: Path) -> dict:
    _require("ffprobe", "Install with: brew install ffmpeg.")
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json",
         "-show_format", "-show_streams", str(video)],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise SystemExit(f"ffprobe failed: {result.stderr.strip()}")
    data = json.loads(result.stdout or "{}")
    streams = data.get("streams", [])
    fmt = data.get("format", {})
    v = next((s for s in streams if s.get("codec_type") == "video"), {})
    a = next((s for s in streams if s.get("codec_type") == "audio"), None)
    w, h = v.get("width"), v.get("height")
    duration = float(fmt.get("duration") or v.get("duration") or 0)
    if w and h:
        ratio = w / h
        if ratio < 0.9:
            orientation = "Vertical 9:16"
        elif ratio > 1.1:
            orientation = "Horizontal 16:9"
        else:
            orientation = "Quadrado 1:1"
    else:
        orientation = "NÃO IDENTIFICADO"
    return {
        "duration_seconds": round(duration, 2),
        "duration_mmss": format_mmss(duration),
        "width": w, "height": h,
        "orientation": orientation,
        "has_audio": a is not None,
    }


# ------------------------------ frames ------------------------------

def _ffmpeg_range(video: Path, out_dir: Path, prefix: str, fps: float,
                  resolution: int, start: float | None, end: float | None) -> list[tuple[float, Path]]:
    """Uniform fps sampling within [start,end]. Returns (timestamp, path) pairs."""
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
    if start is not None:
        cmd += ["-ss", f"{start:.3f}"]
    if end is not None:
        cmd += ["-to", f"{end:.3f}"]
    pattern = str(out_dir / f"{prefix}_%04d.jpg")
    cmd += ["-i", str(video), "-vf", f"fps={fps},scale={resolution}:-2", "-q:v", "3", pattern]
    subprocess.run(cmd, capture_output=True, text=True)
    offset = start or 0.0
    pairs = []
    for i, p in enumerate(sorted(out_dir.glob(f"{prefix}_*.jpg"))):
        ts = offset + (i / fps if fps > 0 else 0.0)
        pairs.append((round(ts, 2), p))
    return pairs


def _ffmpeg_scene(video: Path, out_dir: Path, threshold: float,
                  resolution: int) -> list[tuple[float, Path]]:
    """Scene-change frames. Timestamps parsed from showinfo pts_time."""
    pattern = str(out_dir / "scene_%04d.jpg")
    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "info", "-y",
        "-i", str(video),
        "-vf", f"select='gt(scene,{threshold})',showinfo,scale={resolution}:-2",
        "-vsync", "vfr", "-q:v", "3", pattern,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    times = [float(m) for m in re.findall(r"pts_time:([0-9.]+)", result.stderr)]
    files = sorted(out_dir.glob("scene_*.jpg"))
    pairs = []
    for i, p in enumerate(files):
        ts = times[i] if i < len(times) else 0.0
        pairs.append((round(ts, 2), p))
    return pairs


def build_frames(video: Path, frames_dir: Path, duration: float,
                 threshold: float, hook_seconds: float, interval: float,
                 resolution: int, max_frames: int) -> list[dict]:
    _require("ffmpeg", "Install with: brew install ffmpeg.")
    frames_dir.mkdir(parents=True, exist_ok=True)
    for old in frames_dir.glob("*.jpg"):
        old.unlink()

    raw_dir = frames_dir / "_raw"
    raw_dir.mkdir(exist_ok=True)

    collected: list[tuple[float, Path, str]] = []

    # 1. scene changes (primary)
    for ts, p in _ffmpeg_scene(video, raw_dir, threshold, resolution):
        collected.append((ts, p, "cena"))

    # 2. dense hook
    hook_end = min(hook_seconds, duration)
    for ts, p in _ffmpeg_range(video, raw_dir, "hook", 2.5, resolution, 0.0, hook_end):
        collected.append((ts, p, "hook"))

    # 3. interval baseline
    if duration > interval:
        fps = 1.0 / interval
        for ts, p in _ffmpeg_range(video, raw_dir, "intv", fps, resolution, None, None):
            collected.append((ts, p, "intervalo"))

    # 4. end zone (last 3s), if the ad is long enough to have a distinct end
    if duration > 6:
        for ts, p in _ffmpeg_range(video, raw_dir, "end", 1.5, resolution, max(0.0, duration - 3), None):
            collected.append((ts, p, "fim"))

    # de-dup by 0.5s bucket, prefer scene > hook > end > interval
    priority = {"cena": 0, "hook": 1, "fim": 2, "intervalo": 3}
    best: dict[int, tuple[float, Path, str]] = {}
    for ts, p, src in collected:
        bucket = int(round(ts * 2))
        cur = best.get(bucket)
        if cur is None or priority[src] < priority[cur[2]]:
            best[bucket] = (ts, p, src)

    ordered = sorted(best.values(), key=lambda t: t[0])

    # cap: if over budget, drop interval frames first, then thin evenly
    if len(ordered) > max_frames:
        non_interval = [t for t in ordered if t[2] != "intervalo"]
        if len(non_interval) <= max_frames:
            keep = set(id(t) for t in non_interval)
            interval_slots = max_frames - len(non_interval)
            intervals = [t for t in ordered if t[2] == "intervalo"]
            if interval_slots > 0 and intervals:
                step = max(1, len(intervals) // interval_slots)
                for t in intervals[::step][:interval_slots]:
                    keep.add(id(t))
            ordered = [t for t in ordered if id(t) in keep]
        else:
            step = len(ordered) / max_frames
            ordered = [ordered[int(i * step)] for i in range(max_frames)]

    # rename to final timestamped names, build manifest
    manifest = []
    for idx, (ts, src_path, src) in enumerate(ordered, 1):
        final = frames_dir / f"frame_{idx:03d}_{format_mmss(ts)}.jpg"
        shutil.copyfile(src_path, final)
        manifest.append({
            "index": idx,
            "timestamp_seconds": ts,
            "timestamp_mmss": format_mmss(ts),
            "source": src,
            "path": str(final),
        })

    shutil.rmtree(raw_dir, ignore_errors=True)
    return manifest


# ------------------------------ transcript ------------------------------

def write_transcript(video: Path, workdir: Path,
                     language: str | None = None, vocab: str | None = None) -> dict:
    audio_out = workdir / "audio.mp3"
    segments, language, backend = whisper_lib.transcribe_video(
        str(video), audio_out, language=language, prompt=vocab)
    (workdir / "transcript.json").write_text(
        json.dumps({"language": language, "backend": backend, "segments": segments},
                   indent=2, ensure_ascii=False), encoding="utf-8")
    lines = [f"# Transcrição bruta (idioma: {language}, via {backend})", ""]
    for seg in segments:
        lines.append(f"[{format_mmss(seg['start'])}] {seg['text']}")
    (workdir / "transcript.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    try:
        audio_out.unlink()
    except OSError:
        pass
    return {"language": language, "backend": backend, "segments": len(segments),
            "json": str(workdir / "transcript.json"), "txt": str(workdir / "transcript.txt")}


# ------------------------------ main ------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description="Prepare an ad video for a raio-x teardown.")
    ap.add_argument("input", help="local video file or URL")
    ap.add_argument("workdir", help="output workspace directory")
    ap.add_argument("--country", default=None, help="target country (helps facial recognition)")
    ap.add_argument("--niche", default=None, help="niche hint")
    ap.add_argument("--scene-threshold", type=float, default=0.30)
    ap.add_argument("--hook-seconds", type=float, default=3.0)
    ap.add_argument("--interval", type=float, default=2.5)
    ap.add_argument("--max-frames", type=int, default=55)
    ap.add_argument("--resolution", type=int, default=720)
    ap.add_argument("--no-transcribe", action="store_true")
    ap.add_argument("--language", default=None,
                    help="ISO-639-1 do áudio (pt, en, es). Omita em lote multi-idioma "
                         "para deixar o Whisper detectar sozinho.")
    ap.add_argument("--vocab", default=None,
                    help="Vocabulário para o Whisper priorizar: nomes próprios, marcas, "
                         "jargão. Ex: \"Renda Extra, Mercedes G63, Hotmart\".")
    args = ap.parse_args()

    workdir = Path(args.workdir).resolve()
    workdir.mkdir(parents=True, exist_ok=True)
    frames_dir = workdir / "frames"

    # resolve input
    if is_url(args.input):
        video = download(args.input, workdir)
    else:
        video = Path(args.input).resolve()
        if not video.exists():
            raise SystemExit(f"Input file not found: {video}")

    meta = probe(video)
    print(f"[raio-x-ad] {meta['duration_mmss']} · {meta['orientation']} · "
          f"audio={'sim' if meta['has_audio'] else 'não'}", file=sys.stderr)

    frames = build_frames(
        video, frames_dir, meta["duration_seconds"],
        threshold=args.scene_threshold, hook_seconds=args.hook_seconds,
        interval=args.interval, resolution=args.resolution, max_frames=args.max_frames,
    )
    print(f"[raio-x-ad] {len(frames)} frames -> {frames_dir}", file=sys.stderr)

    transcript_info = None
    if meta["has_audio"] and not args.no_transcribe:
        try:
            transcript_info = write_transcript(video, workdir,
                                               language=args.language, vocab=args.vocab)
        except SystemExit as e:
            print(f"[raio-x-ad] transcription skipped: {e}", file=sys.stderr)
            transcript_info = {"error": str(e)}

    manifest = {
        "input": args.input,
        "video_path": str(video),
        "country_hint": args.country,
        "niche_hint": args.niche,
        "meta": meta,
        "frames": frames,
        "frames_dir": str(frames_dir),
        "transcript": transcript_info,
    }
    manifest_path = workdir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    # human summary on stdout
    print("\n=== RAIO-X-AD: EXTRACT OK ===")
    print(f"workdir:    {workdir}")
    print(f"duração:    {meta['duration_mmss']}  |  orientação: {meta['orientation']}")
    print(f"frames:     {len(frames)} em {frames_dir}")
    if transcript_info and "error" not in transcript_info:
        print(f"transcrição: {transcript_info['segments']} segmentos "
              f"(idioma: {transcript_info['language']}) em {transcript_info['txt']}")
    elif transcript_info:
        print(f"transcrição: FALHOU ({transcript_info['error']})")
    else:
        print("transcrição: pulada (sem áudio)")
    print(f"manifest:   {manifest_path}")
    print("Próximo passo: leia os frames (Read) + transcript.txt e escreva o relatório.")


if __name__ == "__main__":
    main()
