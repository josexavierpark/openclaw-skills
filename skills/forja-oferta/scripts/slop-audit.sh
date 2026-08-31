#!/bin/bash
# Auditoria de slop para as skills da Forja.
# Acha o validador, roda contra o histórico compartilhado e devolve o relatório.
# Uso: bash slop-audit.sh <arquivo.md> [mais arquivos...]
set -u

resolve_home () {
  [ -n "${FORJA_ANTISLOP_HOME:-}" ] && [ -f "$FORJA_ANTISLOP_HOME/slop_copy.py" ] && { echo "$FORJA_ANTISLOP_HOME"; return; }
  local aqui; aqui="$(cd "$(dirname "$0")" && pwd)"
  [ -f "$aqui/slop_copy.py" ] && { echo "$aqui"; return; }
  for c in "$HOME/Documents/Copywriting/anti-slop" "$HOME/.claude/forja-antislop"; do
    [ -f "$c/slop_copy.py" ] && { echo "$c"; return; }
  done
  return 1
}

HOME_AS="$(resolve_home)" || {
  echo "anti-slop não encontrado. Pule a auditoria de slop e siga o resto do audit." >&2
  exit 3
}

# histórico compartilhado entre TODAS as skills: é justamente o reuso de
# esqueleto entre um anúncio e uma VSL de outro projeto que precisa aparecer.
HIST="${FORJA_ANTISLOP_HIST:-$HOME/.claude/forja-antislop/historico}"
mkdir -p "$HIST"

[ $# -ge 1 ] || { echo "uso: slop-audit.sh <arquivo.md>"; exit 2; }

python3 "$HOME_AS/slop_copy.py" score "$@" \
  --baseline "$HOME_AS/baseline.json" --historico "$HIST"
