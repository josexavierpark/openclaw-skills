#!/usr/bin/env bash
# Instala as skills deste repo no Claude Code (~/.claude/skills).
# Uso: bash install.sh [--link] [--dest CAMINHO]
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="$HOME/.claude/skills"
MODE="copy"

while [ $# -gt 0 ]; do
  case "$1" in
    --link) MODE="link"; shift ;;
    --dest) DEST="$2"; shift 2 ;;
    *) echo "opcao desconhecida: $1"; exit 1 ;;
  esac
done

mkdir -p "$DEST"
n=0
for d in "$REPO"/skills/*/; do
  s="$(basename "$d")"
  if [ -e "$DEST/$s" ] || [ -L "$DEST/$s" ]; then
    echo "  ja existe, pulando: $s   (apague $DEST/$s para reinstalar)"
    continue
  fi
  if [ "$MODE" = "link" ]; then ln -s "${d%/}" "$DEST/$s"
  else cp -R "${d%/}" "$DEST/$s"; fi
  echo "  ok: $s"
  n=$((n+1))
done

echo
echo "$n skill(s) instalada(s) em $DEST"
echo "Reinicie o Claude Code para carregar."
