# Skills de copy (Claude Code + OpenClaw)

13 skills de copywriting de resposta direta em PT-BR. O formato `SKILL.md` é o mesmo nos dois
lados, então o conteúdo roda igual no Claude Code e no OpenClaw, sem nenhuma alteração.

## O que tem aqui

| Skill | Para que serve |
|---|---|
| `copy-ads` | anúncios cold que não parecem anúncio, sempre pro clique (VSL/quiz) |
| `forja-ads` | modelagem, cirurgia e criação de ads em 16 modos |
| `master-hooks` | biblioteca master de hooks: 9 elementos, 8 pilares, 7 fórmulas, 955 templates |
| `hooks-nativos` | hooks de vídeo curto (Reels, TikTok, Shorts) no método hook nativo |
| `copy-email` | sequências e e-mails de resposta direta |
| `fala-simples` | escreve e audita roteiro falado, com validador métrico por nicho |
| `forja-oferta` | briefing completo de oferta e VSL antes da primeira linha de copy |
| `forja-vsl` | VSL longa de 9 blocos, escrita middle-out, com swipe de 35 VSLs |
| `forja-mini-vsl` | mini-VSL pós-quiz de 5 blocos para low ticket |
| `forja-quiz-nhb` | funil de quiz que cria o problema e pré-vende a oferta |
| `lowticket-content` | conteúdo e estrutura de produto low ticket |
| `forja-skill` | meta-skill: gera novas skills de copy no padrão da casa |
| `raio-x-ad` | teardown completo de anúncio em vídeo: frames, transcrição, 7 camadas |

## Dependências

Doze das treze rodam só com `python3`, porque os scripts usam apenas a biblioteca padrão.

A exceção é a `raio-x-ad`, que precisa de:

- `ffmpeg` e `ffprobe`
- `yt-dlp`, só para analisar vídeo por URL
- uma chave Whisper em `~/.config/raio-x-ad/.env`:

```bash
mkdir -p ~/.config/raio-x-ad
printf 'GROQ_API_KEY=%s\n' "SUA_CHAVE" > ~/.config/raio-x-ad/.env
```

A chave gratuita sai em https://console.groq.com/keys. Sem chave, rode com `--no-transcribe`:
as seções visual e de 7 camadas ainda saem completas.

Confira o ambiente com `bash skills/raio-x-ad/scripts/check-deps.sh`.

## Instalar no OpenClaw

Escolha um dos três caminhos.

**A. Nativo (recomendado).** Instala direto do git:

```bash
openclaw skills install git:josexavierpark/openclaw-skills@main --global
openclaw skills list
```

**B. Clonar e apontar.** Deixa o repo em qualquer pasta e registra como raiz extra:

```bash
git clone https://github.com/josexavierpark/openclaw-skills.git ~/openclaw-skills
openclaw config set skills.load.extraDirs '["'"$HOME"'/openclaw-skills/skills"]'
```

**C. Copiar pro workspace.** Mais simples, porém manual:

```bash
cp -R skills/* ~/.openclaw/workspace/skills/
```

Depois de qualquer um dos três, reinicie o gateway e valide:

```bash
openclaw skills list
openclaw agent --agent main --message "/skill master-hooks" --model claude-cli/claude-sonnet-5
```

Com o backend `claude-cli`, o OpenClaw materializa estas skills como plugin temporário do
Claude Code e passa via `--plugin-dir`, então elas entram no Claude Code de verdade.

## Instalar no Claude Code

```bash
bash install.sh              # copia para ~/.claude/skills/
bash install.sh --link       # cria symlink, para editar direto no repo
```

## Manutenção

```bash
git pull                      # nas máquinas que clonaram
openclaw skills update --all  # nas que instalaram pelo modo A
```

## Sobre o conteúdo

Nenhuma chave de API, token ou credencial entra aqui. Também não entram os caminhos absolutos
da máquina de origem nem o corpus bruto usado para calibrar o validador anti-slop: os
`baseline.json` guardam apenas as estatísticas, que é o que o score consome.

Os swipes trazem anúncios, VSLs e funis de terceiros transcritos para estudo de estrutura.
Use o blueprint, nunca as frases.
