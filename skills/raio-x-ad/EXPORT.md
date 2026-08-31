# Como empacotar a raio-x-ad para outras pessoas

A skill é auto-suficiente: não depende de nenhuma outra skill. Quem receber precisa só de ffmpeg, yt-dlp (para URLs), python3 e uma chave Groq.

## Gerar o pacote

```bash
cd ~/.claude/skills
zip -r ~/Documents/Copywriting/skill-para-exportar/raio-x-ad.zip raio-x-ad \
  -x "*/__pycache__/*" "*/.DS_Store" "*/wk_*/*" "*/.git/*" "*.bak-*"
```

## Instalação (para quem recebe)

1. Descompacte em `~/.claude/skills/` (deve virar `~/.claude/skills/raio-x-ad/`).
2. Instale as dependências:
   ```bash
   brew install ffmpeg yt-dlp
   ```
3. Configure a chave Whisper em `~/.config/raio-x-ad/.env`:
   ```bash
   mkdir -p ~/.config/raio-x-ad
   printf 'GROQ_API_KEY=%s\n' "SUA_CHAVE" > ~/.config/raio-x-ad/.env
   chmod 600 ~/.config/raio-x-ad/.env
   ```
   Pegue a chave gratuita em https://console.groq.com/keys
4. Verifique: `bash ~/.claude/skills/raio-x-ad/scripts/check-deps.sh`
5. Use: `/raio-x-ad /caminho/do/anuncio.mp4`

## O que NÃO vai no pacote

- `__pycache__/`, `.DS_Store`, workspaces de teste (`wk_*`), qualquer `.env` com chave.
- Nunca inclua a sua chave Groq no zip. Cada pessoa usa a própria.
