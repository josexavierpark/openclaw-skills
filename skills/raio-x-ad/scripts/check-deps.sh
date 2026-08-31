#!/usr/bin/env bash
# raio-x-ad: verify everything the skill needs before a run.
set -u

ok=0; fail=0
check() { if command -v "$1" >/dev/null 2>&1; then echo "  ok   $1 ($(command -v "$1"))"; ok=$((ok+1)); else echo "  MISS $1 — $2"; fail=$((fail+1)); fi; }

echo "== binários =="
check ffmpeg  "brew install ffmpeg"
check ffprobe "brew install ffmpeg"
check python3 "brew install python"
check yt-dlp  "brew install yt-dlp (só necessário para URLs; arquivo local dispensa)"

echo
echo "== chave Whisper (Groq preferido, OpenAI fallback) =="
key_found=0
if [ -n "${GROQ_API_KEY:-}" ]; then echo "  ok   GROQ_API_KEY na env"; key_found=1; fi
if [ -n "${OPENAI_API_KEY:-}" ]; then echo "  ok   OPENAI_API_KEY na env"; key_found=1; fi
for f in "$HOME/.config/raio-x-ad/.env" "$HOME/.config/watch/.env" "./.env"; do
  if [ -f "$f" ] && grep -qE '^(GROQ|OPENAI)_API_KEY=.+' "$f"; then
    echo "  ok   chave em $f"; key_found=1
  fi
done
if [ "$key_found" -eq 0 ]; then
  echo "  MISS nenhuma chave Whisper. Crie ~/.config/raio-x-ad/.env com:"
  echo "         GROQ_API_KEY=sua_chave_aqui"
  echo "       (pegue em https://console.groq.com/keys). Sem chave, a transcrição e o mapa de blocos não rodam; o relatório visual e as 7 camadas ainda funcionam com --no-transcribe."
  fail=$((fail+1))
fi

echo
if [ "$fail" -eq 0 ]; then echo "TUDO PRONTO ($ok itens ok)."; exit 0
else echo "FALTAM $fail item(ns). Veja acima."; exit 1; fi
