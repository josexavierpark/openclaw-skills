---
name: raio-x-ad
description: "Use when the user wants a complete teardown of a video ad: watches the video (extracts smart frames + transcribes audio via Groq Whisper), then writes one full report with visual observations, the 7 macro layers + persuasive blueprint, the verbatim transcription, a timestamped block map, and a PT-BR translation. Delivers everything at once to a markdown file. Trigger words in Portuguese: raio-x do anúncio, analisar anúncio completo, teardown de ad, dissecar anúncio em vídeo, análise visual do ad, 7 camadas do anúncio. Trigger words in English: ad teardown, analyze this ad video, full ad breakdown."
user-invocable: true
---

# raio-x-ad

Skill de análise profunda. Você aponta um vídeo de anúncio (arquivo local ou URL) e ela devolve o raio-x completo num único arquivo markdown, tudo de uma vez.

É a irmã de análise da `swipe-builder`: a swipe cataloga e grava no Notion/Drive; a raio-x-ad disseca fundo e entrega um relatório. Não grava em banco, não julga qualidade, não sugere melhorias. Extrai e rotula.

Diferente do fluxo em etapas com gate (que é do Gem do Gemini), aqui é **tudo de uma vez**: as 5 seções saem juntas num único arquivo nomeado por nicho e data (ver Passo 6).

## O que a skill entrega (5 seções)

1. **Relatório visual:** dados básicos (duração, orientação, formato, produção), tabela de personagens com reconhecimento facial de celebridade local, hook em 4 camadas, provas visuais cronológicas, texto na tela, símbolos carregados, produto/oferta, pacote do editor, sensação geral.
2. **7 camadas + blueprint:** classificação base + as 7 camadas macro + os movimentos persuasivos numerados.
3. **Transcrição:** verbatim no idioma original, com timestamps (via Groq Whisper).
4. **Mapa de blocos:** 13 nomes canônicos, com primeira e última fala de cada bloco, ancorado nos timestamps reais.
5. **Tradução PT-BR:** fiel, espelhando os timestamps (quando a fonte não é português).

## Como ela assiste o vídeo

O `scripts/extract.py` monta o workspace: baixa (yt-dlp, se URL), tira frames inteligentes (troca de cena + hook denso + intervalo + fim), extrai o áudio e transcreve no Groq Whisper (`whisper-large-v3`, com timestamps por segmento), e escreve o `manifest.json`. Depois o Claude lê os frames como imagens e a transcrição, e escreve o relatório.

## Gates de preflight

Antes de rodar, declare:

```
RAIOX_PREFLIGHT: input=received deps=checked frames=pending transcript=pending refs=loaded
```

| Gate | Verificação |
|---|---|
| `input` | Caminho de arquivo ou URL fornecido |
| `deps` | `bash scripts/check-deps.sh` passou (ffmpeg, ffprobe, python3; yt-dlp se URL; chave Groq se for transcrever) |
| `refs` | `reference/7-camadas.md`, `reference/classificacao-base.md`, `reference/movimentos-e-blocos.md`, `reference/pistas-visuais.md`, `reference/reconhecimento-facial.md`, `reference/estilo-e-regras.md` carregados |

Se faltar a chave Groq, rode com `--no-transcribe`: as seções 1 e 2 (visual + 7 camadas) ainda saem; 3, 4 e 5 ficam "não disponível (sem transcrição)".

## Workflow obrigatório

### Passo 1: Intake

Receba o caminho/URL. Capture país-alvo e nicho se o usuário informar (`país: Brasil`, `nicho: diabetes`). Se não informar, o país vai ser inferido no Passo 4.

### Passo 2: Checar dependências

```bash
bash ~/.claude/skills/raio-x-ad/scripts/check-deps.sh
```

Se faltar algo, informe o usuário e pare (ou siga com `--no-transcribe` se só faltar a chave Groq).

### Passo 3: Extrair (assistir o vídeo)

Crie um workspace e rode o extrator. Use o scratchpad da sessão ou uma subpasta do destino final:

```bash
python3 ~/.claude/skills/raio-x-ad/scripts/extract.py "<arquivo-ou-URL>" "<workdir>" [--country Brasil] [--niche emagrecimento]
```

Flags úteis: `--no-transcribe` (sem áudio ou sem chave), `--max-frames N` (padrão 55), `--resolution 1080` (pra ler texto miúdo), `--scene-threshold 0.2` (pega mais cenas em ads muito cortados).

**Flags de transcrição (usar sempre que souber o idioma):**

| Flag | Quando usar |
|---|---|
| `--language pt` | Quando você sabe o idioma do áudio. Pula a autodetecção, que erra em áudio curto ou barulhento. **Omita em lote multi-idioma**, senão força o idioma errado e a transcrição sai traduzida ou corrompida. |
| `--vocab "..."` | Nomes próprios, marca, produto, jargão e regionalismo do ad. É onde o Whisper mais erra. |

```bash
python3 ~/.claude/skills/raio-x-ad/scripts/extract.py video.mp4 workdir \
  --country Brasil --niche "sono infantil" \
  --language pt \
  --vocab "Anúncio de sono infantil, com a especialista. Termos: técnica da vaquinha, método semente, desmame noturno. Sotaque mineiro: uai sô."
```

**Regra do `--vocab` (importante):** o Whisper copia o *estilo* do prompt, não só o vocabulário. Escreva o vocabulário como uma frase real, com maiúsculas e pontuação. Uma lista solta em caixa baixa faz a transcrição inteira voltar sem maiúscula e sem pontuação.

- Certo: `"Anúncio de renda extra, com o mentor. Termos: Mercedes G63, Porsche 911, Hotmart, comissão."`
- Errado: `"renda extra, mentor, g63, hotmart"`

Validado em 2026-08-01: sem as flags, um ad em PT-BR transcreveu "Uai, sua"; com `--language pt` e vocabulário bem escrito, saiu "Uai sô" com a pontuação preservada.

O script imprime um resumo e grava `manifest.json`, `frames/`, `transcript.json` e `transcript.txt` no workdir.

### Passo 4: Ler o material

1. Leia (Read) os frames de `frames/` como imagens. Os nomes trazem o timestamp (`frame_007_00m19s.jpg`), use isso pra citar tempos.
2. Leia `transcript.txt` e `transcript.json`. **Confirme o idioma pelo conteúdo real**, não confie cego no campo `language` (o Whisper erra em áudio curto).
3. Infira o país-alvo se não foi informado (idioma, sotaque, marcas, cenário, moeda na tela) e declare a suposição no topo do relatório.

### Passo 5: Escrever o relatório

Escreva as 5 seções no formato de `output-template.md`, consultando:

- `reference/pistas-visuais.md` para Formato, Avatar, símbolos carregados e tells de IA (seção 1).
- `reference/reconhecimento-facial.md` para celebridade/âncora local não nomeada (seção 1 e Camada 5).
- `reference/classificacao-base.md` para nicho, subnicho, hook exato, mídia, CTA exato e as regras de inferência das camadas (seção 2, bloco "Classificação base").
- `reference/7-camadas.md` para as 7 camadas e exemplos de tema por nicho (seção 2).
- `reference/movimentos-e-blocos.md` para o blueprint (seção 2) e os blocos canônicos (seção 4).
- `reference/estilo-e-regras.md` para as regras de escrita e precisão.
- `reference/exemplos/exemplo-saude.md` e `exemplo-renda.md` como âncora de formato e profundidade.

O mapa de blocos (seção 4) usa os timestamps reais de `transcript.json`. A tradução (seção 5) só quando a fonte não é PT-BR.

### Passo 6: Salvar e resumir

Salve o relatório numa pasta `~/Documents/Copywriting/Analises-Ads/<AAAA-MM-DD>_<slug-do-ad>/` e copie a pasta `frames/` e o `transcript.txt` pra lá (ou aponte o workdir direto pra esse destino no Passo 3).

**Nome do arquivo principal (obrigatório):** o relatório NÃO se chama `relatorio.md`. Nomeie sempre com característica do ad: `<AAAA-MM-DD>_<subnicho>_<slug-do-ad>.md`. Use a data da extração, o subnicho classificado na seção 2 e um slug curto do tema (minúsculas, hífen). Ex: `2026-07-08_confeitaria-lucrativa_brigadeiros-florais.md`, `2026-07-08_diabetes_cha-que-baixa-glicose.md`. O arquivo tem que se identificar sozinho mesmo fora da pasta.

Mostre ao usuário o caminho do relatório e um resumo de 3 linhas: nicho/subnicho, formato, e o gancho.

## Princípios

- Tudo de uma vez, num arquivo. Sem gate entre seções (isso é do Gem, não da skill).
- Não julga qualidade, não sugere melhoria, não diz se pararia de scrollar.
- Verbatim na transcrição. Campo ausente = "NÃO IDENTIFICADO". Camada indecidível = "não-determinável".
- Sem em-dash, sem cifrão de fórmula, PT-BR acentuado, sem "não é X é Y".

## Roteamento sem argumento

Se o usuário invocar sem apontar um vídeo, mostre:

```
Aponte o vídeo do anúncio (caminho do arquivo ou URL).
Opcional: país-alvo e nicho (ex: "país: Brasil, nicho: diabetes").
```

E aguarde.
