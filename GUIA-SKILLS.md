# Guia das 19 skills

O que cada skill faz e tudo que precisa estar no lugar para ela funcionar: programa
instalado, servidor MCP, conta, chave de API, arquivo de configuração e outras skills.

Dois repositórios:

- **[openclaw-skills](https://github.com/josexavierpark/openclaw-skills)**: 13 skills de copy. Escrevem texto.
- **[openclaw-skills-ops](https://github.com/josexavierpark/openclaw-skills-ops)**: 6 skills de operação. Fazem trabalho de campo.

## Leitura rápida

| Nível | O que significa | Quantas |
|---|---|---|
| Zero | funciona assim que instalar, sem nada a mais | 8 |
| Só python3 | precisa do `python3` para o validador rodar | 5 |
| Médio | um ou dois programas, sem conta externa | 3 |
| Alto | programas, conta em serviço e chave de API | 3 |

---

# Repositório 1: skills de copy

## Zero dependência

Estas oito escrevem texto e nada mais. Instalou, funciona.

### master-hooks
**O que faz.** Biblioteca master de hooks para resposta direta: 9 elementos, 8 pilares,
7 fórmulas, 10 tipos e mais de 955 templates. Serve para criar hook do zero, modelar um
que já roda, bater controle ou desconstruir por que um gancho funciona.
**Precisa de.** Nada.

### hooks-nativos
**O que faz.** Hooks de vídeo curto (Reels, TikTok, Shorts) pelo método do hook nativo:
4 componentes, 7 estruturas e psicologia do contraste. Entrega 3 variações por estrutura,
com hook falado de 1 a 4 linhas e texto na tela de 3 a 7 palavras.
**Precisa de.** Nada. Faz handoff para a `master-hooks` quando o pedido cresce.

### copy-email
**O que faz.** E-mail de resposta direta que manda para VSL ou página de oferta, em
broadcast único ou sequência. O e-mail ganha a abertura no assunto e na primeira linha,
e cada linha entrega a próxima.
**Precisa de.** Nada.

### forja-ads
**O que faz.** Modelagem e criação de anúncios para tráfego frio em 16 modos, entre
diagnóstico, cirurgia e criação: bater controle, revelar a estrutura invisível de um ad,
reescrever com outro ângulo, gerar variações, adaptar para outro nicho.
**Precisa de.** Nada. Lê o banco de anúncios da `copy-ads`, então instale as duas juntas.

### forja-skill
**O que faz.** Meta-skill que cria skills de copy. Toda skill gerada nasce com a
arquitetura padrão (roteador, gates, fases, critique, audit, polish) e a DNA anti-slop
em duas camadas. Não escreve copy: escreve a skill que escreve copy.
**Precisa de.** Nada.

### premium-pwa-builder
**O que faz.** PWA instalável e offline em HTML, CSS e JS puros, sem build e sem
framework, com acabamento de estúdio caro: tokens de design, tipografia embutida, ícones
em SVG, movimento discreto, acessibilidade levada a sério.
**Precisa de.** Nada. (Esta mora no repositório 2, mas é a mais leve de todas.)

---

## Só python3

Estas cinco escrevem copy e passam o texto por um validador métrico antes de entregar.
O script usa apenas biblioteca padrão: nenhum `pip install`.

### copy-ads
**O que faz.** Anúncios de resposta direta para tráfego frio, em qualquer nicho, sempre
mandando para VSL ou quiz. O anúncio nunca pode parecer anúncio. Usa banco de 39
exemplares anotados como referência estrutural, nunca de vocabulário. Nunca menciona preço.
**Precisa de.** `python3` para o `scripts/slop_copy.py`, que mede o texto contra um
baseline de copy humana e devolve o Slop Score.

### forja-vsl
**O que faz.** VSL longa completa em PT-BR, os 9 blocos escritos middle-out: mecanismos
primeiro, lead por último. A substância vem do briefing; o banco de 35 VSLs catalogadas
empresta só a forma. Nunca menciona o produto antes do bloco de oferta.
**Precisa de.** `python3` (mesmo validador).

### forja-oferta
**O que faz.** Co-piloto que conduz a fase de pesquisa e os 13 playbooks teóricos até um
Big Briefing completo de oferta ou VSL. Nome chiclete, mecanismo, USP, prova. Tem modo
completo e modo cirúrgico, para ativar só um pedaço.
**Precisa de.** `python3` (mesmo validador).

### forja-mini-vsl
**O que faz.** Mini-VSL de 3 a 6 minutos para vender baixo ticket por impulso logo depois
de um quiz, pela fórmula de 5 blocos: Lead, Agitar, Ação Acreditável, Solução Acreditável,
Oferta.
**Precisa de.** `python3` (mesmo validador). Aceita o pacote de handoff da `forja-quiz-nhb`.

### forja-quiz-nhb
**O que faz.** Funil de quiz pela arquitetura oculta NHB: o quiz não procura um problema,
ele cria um, leva pelo arco Positiva, Neutra, Negativa até a posse do problema na
identidade, e entrega resultado que pré-vende.
**Precisa de.** `python3` (mesmo validador). Passa handoff para a `forja-mini-vsl`.

### fala-simples
**O que faz.** Escreve, adapta e audita roteiro falado de vídeo. O diferencial é que o
estilo tem número, não adjetivo: os alvos foram medidos num corpus de 26 roteiros reais e
são conferidos por script.
**Precisa de.** `python3` para o `scripts/validar.py`. Traz léxicos prontos de fitness,
emagrecimento feminino, postural, renda extra e sono de bebê, mais um template para
destilar o seu.

---

## Com dependência real

### raio-x-ad
**O que faz.** Teardown completo de anúncio em vídeo. Assiste o vídeo de verdade: extrai
frames inteligentes na troca de cena, transcreve o áudio, e entrega num arquivo só as
observações visuais, as 7 camadas macro com blueprint persuasivo, a transcrição verbatim
com timestamps, o mapa de blocos e a tradução PT-BR.

**Precisa de.**

| Item | Como instalar | Obrigatório |
|---|---|---|
| `python3` | `brew install python` | sim |
| `ffmpeg` e `ffprobe` | `brew install ffmpeg` | sim |
| `yt-dlp` | `python3 -m pip install --user yt-dlp` | só para vídeo por URL |
| Chave Groq (Whisper) | grátis em console.groq.com/keys | para transcrever |

A chave vai em arquivo, nunca dentro da skill:

```bash
mkdir -p ~/.config/raio-x-ad
printf 'GROQ_API_KEY=%s\n' "SUA_CHAVE" > ~/.config/raio-x-ad/.env
chmod 600 ~/.config/raio-x-ad/.env
```

Aceita `OPENAI_API_KEY` como alternativa. Sem chave nenhuma, rode com `--no-transcribe`:
as seções visual e de 7 camadas saem inteiras, as outras três ficam vazias.

Confira com `bash scripts/check-deps.sh`.

### lowticket-content
**O que faz.** Produz o conteúdo entregável de um produto low ticket (curso, ebook,
mini-curso, app), ancorado em pesquisa real de YouTube e web, auditado contra as fontes e
escrito passo a passo na língua do público. A pesquisa vira um notebook no NotebookLM, que
passa a ser a fonte da verdade.

**Precisa de.**

| Item | Como instalar | Obrigatório |
|---|---|---|
| CLI `notebooklm` | `pipx install notebooklm` e depois `notebooklm login` | sim |
| `python3` | `brew install python` | sim |
| Skill `yt-search` | não vem nos repositórios, instale à parte | sim, na fase de pesquisa |
| Google Chrome | google.com/chrome | só no modo de material imprimível |
| MCP de imagem (Magnific ou equivalente) | conforme o servidor | opcional, para mockups |

```bash
notebooklm login                     # OAuth pelo navegador, uma vez
notebooklm auth check --test --json  # exige status:ok e checks.token_fetch:true
notebooklm language set pt_BR
```

**Atenção.** É a única do repositório 1 que depende de skill de fora. A fase de descoberta
de fontes chama a `yt-search`, que não está em nenhum dos dois repositórios. Sem ela, faça
a busca de vídeos na mão e alimente o notebook com as URLs.

---

# Repositório 2: skills de operação

### garimpo-oferta
**O que faz.** Varre a Meta Ad Library por palavra-chave e devolve os anunciantes que já
validaram a oferta. Não lê a tela: intercepta as respostas GraphQL que o Facebook já
busca, o que entrega dois campos escondidos na interface. O `page_id`, sem o qual não se
abre a biblioteca completa do anunciante, e o `collation_count`, que diz quantos criativos
rodam a mesma copy. Grupo de 1 é aposta, grupo de 18 é copy que já ganhou.

**Precisa de.**

| Item | Como instalar |
|---|---|
| `node` e `npm` | `brew install node` |
| `playwright-core` | o `scripts/setup.sh` instala no diretório de trabalho |
| `python3` | `brew install python` |

Sem conta, sem chave, sem login: a Ad Library é pública. Se a página pedir login, a URL
está errada. Não use o perfil de navegador do MCP nestes scripts, sempre perfil isolado.

### forja-pagina-maxima
**O que faz.** Página de vendas low ticket pelo método dos 14 blocos, do briefing ao ar,
em 10 fases. Pergunta sempre se a oferta roda em plano único ou em escada de dois planos,
e se você quer variantes de estrutura.

**Precisa de.**

| Item | Como instalar | Para quê |
|---|---|---|
| `node` e `npm` | `brew install node` | o `verificar.mjs` roda Playwright por `npx` |
| Hospedagem com Apache | cPanel ou equivalente | publicar |

Não vem com banco de páginas doadoras: você monta o seu com a `swipe-page`.

### forja-quiz-live
**O que faz.** Pega um roteiro de quiz e publica como página estática hospedada, com
analytics próprio no PostHog, no lugar de Inlead ou XQuiz. Entrega a URL do quiz no ar e o
painel com os indicadores da Inlead mais métricas de diagnóstico. Um subdomínio por quiz,
inclusive nas variantes de teste A/B.

**Precisa de.**

| Item | Como instalar | Obrigatório |
|---|---|---|
| `python3` | `brew install python` | sim |
| `node` e `npm` | `brew install node` | sim |
| Conta no PostHog | posthog.com | sim |
| `wrangler` | `npx wrangler login` | se publicar na Cloudflare |
| Conta cPanel | sua hospedagem | se publicar em cPanel |

```bash
# PostHog: na raiz dos quizzes (~/Quizzes por padrao, ou QUIZZES_RAIZ)
mkdir -p ~/Quizzes
cat > ~/Quizzes/.env <<'CONF'
POSTHOG_API_KEY=
POSTHOG_HOST=https://us.posthog.com
POSTHOG_PROJECT_ID=
CONF
chmod 600 ~/Quizzes/.env

# cPanel, se for o caso
cat > ~/.config/cpanel-quiz.conf <<'CONF'
CPANEL_USER=
CPANEL_ROOT_DOMAIN=
CPANEL_BASE_DIR=quizzes
CONF
chmod 600 ~/.config/cpanel-quiz.conf
```

A `POSTHOG_API_KEY` é a chave pessoal de API, não a chave pública do projeto (`phc_...`),
que o script busca sozinho.

**Atenção.** Em cPanel, o quiz mora fora do `public_html`. Dentro, o `.htaccess` do
WordPress do domínio principal captura as rotas e quebra o proxy do PostHog.

### swipe-quiz
**O que faz.** Percorre um funil de quiz ou uma VSL inteira e devolve a transcrição
organizada em Markdown e DOCX com as imagens embutidas, tela por tela. Arquiva os vídeos
de credibilidade e a mini-VSL no Drive, e cria a linha na sua database do Notion. Conteúdo
em outra língua sai também traduzido para PT-BR.

**Precisa de.**

| Item | Como instalar | Para quê |
|---|---|---|
| `node` e `npm` | `brew install node` | pacote `docx`, gera o DOCX |
| `python3` | `brew install python` | orquestra a captura |
| `faster-whisper` | `pip install --user faster-whisper` | transcreve local |
| `ffmpeg` e `ffprobe` | `brew install ffmpeg` | corta e converte áudio |
| `yt-dlp` | `pip install --user yt-dlp` | baixa vídeo sem `.m3u8` |
| `curl`, `file`, `unzip` | já vêm no sistema | download e inspeção |
| **MCP do Playwright** | configurado no Claude Code | navega o funil |
| Google Chrome | google.com/chrome | alternativa ao MCP |
| `rclone` com remote `gdrive` | `brew install rclone` e `rclone config` | arquiva no Drive |
| CLI `ntn` autenticada | `ntn login` | grava no Notion |

A database do Notion é sua: crie com o schema de `reference/notion-swipe-quiz.md` e guarde
os IDs em `~/.config/swipe-notion.conf`. Vídeo arquivado entre 480p e 720p.

`bash scripts/check-deps.sh --install` instala o que der sozinho.

### swipe-page
**O que faz.** Captura uma página de vendas inteira: print de página completa, clone
offline autossuficiente com as imagens, a copy verbatim bloco a bloco e um template
editável que reconstrói o layout exato. Arquiva no Drive e cria a linha no Notion, com
Relation de mão dupla para os anúncios que mandam tráfego. Destrava conteúdo escondido
antes de capturar.

**Precisa de.**

| Item | Como instalar | Para quê |
|---|---|---|
| **Google Chrome instalado** | google.com/chrome | o `single-file` depende dele |
| `node` e `npm` | `brew install node` | `playwright` e `single-file-cli` |
| `python3` | `brew install python` | recorte e montagem |
| Pillow | `pip install --user Pillow` | trata as imagens |
| OCR | Vision do macOS, ou `brew install tesseract tesseract-lang` | lê texto de imagem |
| **MCP do Playwright** | configurado no Claude Code | navega e destrava a página |
| `rclone` com remote `gdrive` | `brew install rclone` e `rclone config` | arquiva no Drive |
| CLI `ntn` autenticada | `ntn login` | grava no Notion |

No macOS, o OCR nativo:

```bash
python3 -m pip install --user pyobjc-framework-Vision pyobjc-framework-Quartz
```

`bash scripts/check-deps.sh --install` resolve a maior parte.

---

# Resumo por dependência

| Dependência | Quem precisa |
|---|---|
| Nada | master-hooks, hooks-nativos, copy-email, forja-ads, forja-skill, premium-pwa-builder |
| `python3` | copy-ads, forja-vsl, forja-oferta, forja-mini-vsl, forja-quiz-nhb, fala-simples, raio-x-ad, lowticket-content, garimpo-oferta, forja-quiz-live, swipe-quiz, swipe-page |
| `node` e `npm` | garimpo-oferta, forja-pagina-maxima, forja-quiz-live, swipe-quiz, swipe-page |
| `ffmpeg` e `ffprobe` | raio-x-ad, swipe-quiz |
| `yt-dlp` | raio-x-ad, swipe-quiz |
| Google Chrome instalado | swipe-page, lowticket-content (modo imprimível) |
| MCP do Playwright | swipe-quiz, swipe-page |
| `rclone` com remote `gdrive` | swipe-quiz, swipe-page |
| CLI `ntn` (Notion) | swipe-quiz, swipe-page |
| CLI `notebooklm` | lowticket-content |
| Pillow | swipe-page |
| OCR (Vision ou tesseract) | swipe-page |
| `faster-whisper` | swipe-quiz |
| `wrangler` | forja-quiz-live |

# Contas e chaves

| Serviço | Quem usa | Custo | Onde guardar |
|---|---|---|---|
| Groq (Whisper) | raio-x-ad | grátis | `~/.config/raio-x-ad/.env` |
| PostHog | forja-quiz-live | grátis até o limite | `<raiz-dos-quizzes>/.env` |
| Notion | swipe-quiz, swipe-page | grátis | CLI `ntn`, via `ntn login` |
| Google Drive | swipe-quiz, swipe-page | grátis | `rclone config` |
| Google (NotebookLM) | lowticket-content | grátis | `notebooklm login` |
| Cloudflare | forja-quiz-live | grátis | `npx wrangler login` |
| Hospedagem cPanel | forja-quiz-live, forja-pagina-maxima | pago | `~/.config/cpanel-quiz.conf` |

Nenhuma chave fica dentro da skill. Todas moram em arquivo de configuração fora do
repositório, com permissão `600`.

# Servidores MCP

Só duas skills exigem MCP: `swipe-quiz` e `swipe-page`, ambas pelo **Playwright**, para
navegar o funil ou a página e destravar conteúdo escondido antes da captura. As duas
aceitam Google Chrome instalado como alternativa quando o MCP não estiver disponível.

A `lowticket-content` usa um MCP de geração de imagem (Magnific ou equivalente) só para
mockup no modo de material imprimível, e é opcional.

A `garimpo-oferta` funciona sem MCP de propósito: ela abre um Chromium próprio com perfil
isolado, porque Chrome de marca a partir da versão 137 ignora `--load-extension`.

# Instalação base, tudo de uma vez

```bash
# macOS
brew install node python ffmpeg rclone
python3 -m pip install --user Pillow faster-whisper yt-dlp

# Debian/Ubuntu
sudo apt update && sudo apt install -y nodejs npm python3 python3-pip ffmpeg rclone tesseract-ocr tesseract-ocr-por
python3 -m pip install --user Pillow faster-whisper yt-dlp
```

Se o pip reclamar de ambiente gerenciado, acrescente `--break-system-packages`.

# Nota de plataforma

Tudo foi feito e testado em macOS. O que assume macOS de verdade: o OCR por Vision na
`swipe-page` (com `tesseract` como alternativa), o caminho do Google Chrome em
`/Applications/`, e os `brew install` dentro dos verificadores. Em Linux, troque pelo
gerenciador da distribuição e o resto funciona.
