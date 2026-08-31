#!/usr/bin/env python3
"""Groq/OpenAI Whisper transcription (pure stdlib, vendored for raio-x-ad).

Extracts mono 16kHz mp3 audio and uploads to whichever Whisper API has a key.
Returns segments with per-segment timestamps (start/end/text) plus the detected
language, so the caller can anchor a block map to real speech.

Portable: no `pip install` needed. Only requires ffmpeg on PATH and a key in
the environment or in one of the .env files probed by load_api_key().
"""
from __future__ import annotations

import io
import json
import mimetypes
import os
import shutil
import ssl
import subprocess
import sys
import time
import urllib.error
import uuid
from pathlib import Path
from urllib.request import Request, urlopen


GROQ_ENDPOINT = "https://api.groq.com/openai/v1/audio/transcriptions"
GROQ_MODEL = "whisper-large-v3"

OPENAI_ENDPOINT = "https://api.openai.com/v1/audio/transcriptions"
OPENAI_MODEL = "whisper-1"


def load_api_key(preferred: str | None = None) -> tuple[str, str] | tuple[None, None]:
    """Return (backend, api_key). Prefers Groq, falls back to OpenAI.

    Probes, in order: process env, ~/.config/raio-x-ad/.env,
    ~/.config/watch/.env (shared with the watch skill), and ./.env.
    """
    def _from_env(name: str) -> str | None:
        value = os.environ.get(name)
        return value.strip() if value else None

    def _from_dotenv(path: Path, name: str) -> str | None:
        if not path.exists():
            return None
        try:
            for line in path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                if key.strip() != name:
                    continue
                value = value.strip()
                if len(value) >= 2 and value[0] in ('"', "'") and value[-1] == value[0]:
                    value = value[1:-1]
                return value or None
        except OSError:
            return None
        return None

    dotenv_paths = [
        Path.home() / ".config" / "raio-x-ad" / ".env",
        Path.home() / ".config" / "watch" / ".env",
        Path.cwd() / ".env",
    ]

    candidates = (("GROQ_API_KEY", "groq"), ("OPENAI_API_KEY", "openai"))
    if preferred is not None:
        candidates = tuple(c for c in candidates if c[1] == preferred)

    for key_name, backend in candidates:
        value = _from_env(key_name)
        if not value:
            for candidate in dotenv_paths:
                value = _from_dotenv(candidate, key_name)
                if value:
                    break
        if value:
            return backend, value

    return None, None


def extract_audio(video_path: str, out_path: Path) -> Path:
    """Extract mono 16kHz 64kbps mp3 (~480 kB/min, fits any Whisper limit)."""
    if shutil.which("ffmpeg") is None:
        raise SystemExit("ffmpeg is not installed. Install with: brew install ffmpeg")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(Path(video_path).resolve()),
        "-vn", "-acodec", "libmp3lame", "-ar", "16000", "-ac", "1", "-b:a", "64k",
        str(out_path.resolve()),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f"ffmpeg audio extraction failed: {result.stderr.strip()}")
    if not out_path.exists() or out_path.stat().st_size == 0:
        raise SystemExit("ffmpeg produced no audio (video may have no audio track)")
    return out_path


def _build_multipart(fields: dict[str, str], file_path: Path) -> tuple[bytes, str]:
    boundary = f"----RaioXBoundary{uuid.uuid4().hex}"
    eol = b"\r\n"
    buf = io.BytesIO()
    for name, value in fields.items():
        buf.write(f"--{boundary}".encode()); buf.write(eol)
        buf.write(f'Content-Disposition: form-data; name="{name}"'.encode()); buf.write(eol)
        buf.write(eol)
        buf.write(str(value).encode()); buf.write(eol)
    mimetype = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    buf.write(f"--{boundary}".encode()); buf.write(eol)
    buf.write(f'Content-Disposition: form-data; name="file"; filename="{file_path.name}"'.encode())
    buf.write(eol)
    buf.write(f"Content-Type: {mimetype}".encode()); buf.write(eol)
    buf.write(eol)
    buf.write(file_path.read_bytes())
    buf.write(eol)
    buf.write(f"--{boundary}--".encode()); buf.write(eol)
    return buf.getvalue(), boundary


MAX_ATTEMPTS = 4
MAX_429_RETRIES = 2
RETRY_BASE_DELAY = 2.0


def _read_error_body(exc: urllib.error.HTTPError) -> str:
    try:
        body = exc.read()
    except Exception:
        return ""
    if not body:
        return ""
    try:
        return f" — {body.decode('utf-8', errors='replace')[:400]}"
    except Exception:
        return ""


def _retry_after(exc: urllib.error.HTTPError) -> float | None:
    header = exc.headers.get("Retry-After") if getattr(exc, "headers", None) else None
    if not header:
        return None
    try:
        return float(header)
    except ValueError:
        return None


def _post_whisper(
    endpoint: str,
    api_key: str,
    model: str,
    audio_path: Path,
    language: str | None = None,
    prompt: str | None = None,
) -> dict:
    fields = {
        "model": model,
        "response_format": "verbose_json",
        "temperature": "0",
    }
    # Fixing the language skips auto-detection, which Whisper gets wrong on short
    # or noisy audio. Leave it None for multi-language batches.
    if language:
        fields["language"] = language
    # The prompt primes the decoder's vocabulary. Feed it proper nouns, brand and
    # product names, jargon: it is where Whisper misreads most.
    if prompt:
        fields["prompt"] = prompt[:880]
    body, boundary = _build_multipart(fields, audio_path)
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        # Groq sits behind Cloudflare: the default Python-urllib UA trips WAF
        # rule 1010 (403) before auth. Any non-default UA clears it.
        "User-Agent": "raio-x-ad/1.0 (+claude-code; python-urllib)",
    }
    context = ssl.create_default_context()
    rate_limit_hits = 0
    last_exc: Exception | None = None
    last_detail = ""

    for attempt in range(MAX_ATTEMPTS):
        request = Request(endpoint, data=body, headers=headers, method="POST")
        try:
            with urlopen(request, timeout=300, context=context) as response:
                payload = response.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:
            detail = _read_error_body(exc)
            last_exc, last_detail = exc, detail
            if 400 <= exc.code < 500 and exc.code != 429:
                raise SystemExit(f"Whisper request failed: {exc}{detail}")
            if exc.code == 429:
                rate_limit_hits += 1
                if rate_limit_hits >= MAX_429_RETRIES:
                    raise SystemExit(f"Whisper request failed: {exc}{detail}")
                delay = _retry_after(exc) or RETRY_BASE_DELAY * (2 ** attempt) + 1
            else:
                delay = RETRY_BASE_DELAY * (2 ** attempt)
            if attempt < MAX_ATTEMPTS - 1:
                print(f"[raio-x-ad] whisper HTTP {exc.code} — retry in {delay:.1f}s "
                      f"(attempt {attempt + 2}/{MAX_ATTEMPTS})", file=sys.stderr)
                time.sleep(delay)
            continue
        except (urllib.error.URLError, TimeoutError, ConnectionResetError, OSError) as exc:
            last_exc, last_detail = exc, ""
            if attempt < MAX_ATTEMPTS - 1:
                delay = RETRY_BASE_DELAY * (attempt + 1)
                print(f"[raio-x-ad] whisper network error ({type(exc).__name__}) — "
                      f"retry in {delay:.1f}s (attempt {attempt + 2}/{MAX_ATTEMPTS})", file=sys.stderr)
                time.sleep(delay)
            continue
        try:
            return json.loads(payload)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Whisper returned non-JSON: {exc}: {payload[:200]}")

    raise SystemExit(f"Whisper failed after {MAX_ATTEMPTS} attempts: {last_exc}{last_detail}")


def _segments_from_response(data: dict) -> list[dict]:
    out: list[dict] = []
    for seg in data.get("segments") or []:
        text = (seg.get("text") or "").strip()
        if not text:
            continue
        out.append({
            "start": round(float(seg.get("start") or 0.0), 2),
            "end": round(float(seg.get("end") or 0.0), 2),
            "text": text,
        })
    if not out:
        full = (data.get("text") or "").strip()
        if full:
            out.append({"start": 0.0, "end": 0.0, "text": full})
    return out


def transcribe_video(
    video_path: str,
    audio_out: Path,
    backend: str | None = None,
    api_key: str | None = None,
    language: str | None = None,
    prompt: str | None = None,
) -> tuple[list[dict], str, str]:
    """Extract audio, upload, parse. Returns (segments, language, backend).

    language: ISO-639-1 hint ("pt", "en", "es"). None keeps auto-detection,
        which is what a multi-language batch needs.
    prompt: vocabulary primer (brand names, jargon, proper nouns).
    """
    if backend is None or api_key is None:
        detected_backend, detected_key = load_api_key()
        backend = backend or detected_backend
        api_key = api_key or detected_key

    if not backend or not api_key:
        raise SystemExit(
            "No Whisper API key. Set GROQ_API_KEY (preferred) or OPENAI_API_KEY in the "
            "environment or in ~/.config/raio-x-ad/.env (or ~/.config/watch/.env)."
        )

    print(f"[raio-x-ad] extracting audio for Whisper ({backend})…", file=sys.stderr)
    audio_path = extract_audio(video_path, audio_out)
    size_kb = audio_path.stat().st_size / 1024
    print(f"[raio-x-ad] audio: {size_kb:.0f} kB — uploading to {backend} Whisper…", file=sys.stderr)

    if backend == "groq":
        response = _post_whisper(GROQ_ENDPOINT, api_key, GROQ_MODEL, audio_path, language, prompt)
    elif backend == "openai":
        response = _post_whisper(OPENAI_ENDPOINT, api_key, OPENAI_MODEL, audio_path, language, prompt)
    else:
        raise SystemExit(f"Unknown whisper backend: {backend}")

    segments = _segments_from_response(response)
    detected = (response.get("language") or "desconhecido").strip()
    language = language or detected
    if not segments:
        raise SystemExit("Whisper returned no transcript segments")
    print(f"[raio-x-ad] transcribed {len(segments)} segments ({language}) via {backend}", file=sys.stderr)
    return segments, language, backend


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: whisper_lib.py <video-path> [<audio-out.mp3>]", file=sys.stderr)
        raise SystemExit(2)
    video = sys.argv[1]
    audio_out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("audio.mp3")
    segments, language, backend = transcribe_video(video, audio_out)
    print(json.dumps({"backend": backend, "language": language, "segments": segments}, indent=2, ensure_ascii=False))
