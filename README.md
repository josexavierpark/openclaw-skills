# Skills de copy (Claude Code + OpenClaw)

13 skills de copywriting de resposta direta em PT-BR. Mesmo formato `SKILL.md` nos dois lados,
entao o conteudo roda igual no Claude Code e no OpenClaw, sem alteracao.

> Repositorio privado. Contem swipes proprietarios e frameworks autorais.

## O que tem aqui

| Skill | Para que serve |
|---|---|
| `copy-ads` | anuncios cold que nao parecem anuncio, sempre pro clique (VSL/quiz) |
| `forja-ads` | modelagem, cirurgia e criacao de ads em 16 modos |
| `master-hooks` | biblioteca master de hooks: 9 elementos, 8 pilares, 7 formulas, 955 templates |
| `hooks-nativos` | hooks de video curto (Reels, TikTok, Shorts) no metodo hook nativo |
| `copy-email` | sequencias e e-mails de resposta direta |
| `fala-simples` | escreve e audita roteiro falado, com validador metrico por nicho |
| `forja-oferta` | briefing completo de oferta e VSL antes da primeira linha de copy |
| `forja-vsl` | VSL longa de 9 blocos, escrita middle-out, com swipe de 35 VSLs |
| `forja-mini-vsl` | mini-VSL pos-quiz de 5 blocos para low ticket |
| `forja-quiz-nhb` | funil de quiz que cria o problema e pre-vende a oferta |
| `lowticket-content` | conteudo e estrutura de produto low ticket |
| `forja-skill` | meta-skill: gera novas skills de copy no padrao da casa |
| `raio-x-ad` | teardown completo de anuncio em video: frames, transcricao, 7 camadas |

## Dependencias

Doze das treze rodam so com `python3` (os scripts usam apenas biblioteca padrao).

A excecao e a `raio-x-ad`, que precisa de:

- `ffmpeg` e `ffprobe`
- `yt-dlp` (so para analisar video por URL)
- uma chave Whisper em `~/.config/raio-x-ad/.env`:

```bash
mkdir -p ~/.config/raio-x-ad
printf 'GROQ_API_KEY=%s\n' "SUA_CHAVE" > ~/.config/raio-x-ad/.env
```

Chave gratuita em https://console.groq.com/keys. Sem chave, rode com `--no-transcribe`:
as secoes visual e de 7 camadas ainda saem.

Confira tudo com `bash skills/raio-x-ad/scripts/check-deps.sh`.

## Instalar no OpenClaw

Escolha um dos tres caminhos.

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

**C. Copiar pro workspace.** Mais simples, porem manual:

```bash
cp -R skills/* ~/.openclaw/workspace/skills/
```

Depois de qualquer um dos tres, reinicie o gateway e valide:

```bash
openclaw skills list
openclaw agent --agent main --message "/skill master-hooks" --model claude-cli/claude-sonnet-5
```

Com o backend `claude-cli`, o OpenClaw materializa estas skills como plugin temporario do
Claude Code e passa via `--plugin-dir`, entao elas entram no Claude Code de verdade.

## Instalar no Claude Code

```bash
bash install.sh              # copia para ~/.claude/skills/
bash install.sh --link       # cria symlink, para editar direto no repo
```

## Manutencao

```bash
git pull                     # nas maquinas que clonaram
openclaw skills update --all # nas que instalaram pelo modo A
```

## O que foi retirado antes de publicar

Nenhuma chave de API, token ou credencial entra aqui. Tambem foram removidos os caminhos
absolutos da maquina de origem, os nomes de clientes usados como exemplo e a lista de
arquivos do corpus humano dentro dos `baseline.json` (so as estatisticas importam para o score).
O corpus bruto de origem nao esta no repositorio.
