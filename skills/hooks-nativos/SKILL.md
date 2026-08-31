---
name: hooks-nativos
description: Use sempre que o usuário quiser criar hooks de vídeo curto (Reels, TikTok, Shorts) baseados no método hook nativo. Aciona em PT-BR e EN com: "hook de reels", "hook de tiktok", "hook de vídeo curto", "abertura de vídeo", "hook nativo", "criar hook", "primeiros 3 segundos do vídeo", "parar o scroll", "gancho de short". Gera 3 variações de hook falado + texto na tela por estrutura escolhida, com revisão anti-AI-slop obrigatória. Ideal para Trial Reels e teste rápido de variações.
metadata:
  version: 1.0
---

# hooks-nativos

Skill de geração de hooks para vídeos curtos baseada no material de referência (4 componentes + 7 estruturas + psicologia do contraste) com revisão anti-AI-slop integrada usando blocklist PT-BR, 25 smoking guns e 5 construções retóricas proibidas.

Output: hook falado (1-4 linhas) + texto na tela (3-7 palavras, sentence case). Sem direção visual ou áudio.

## Localização dos arquivos da skill

- Lógica das 7 fases: `~/.claude/skills/hooks-nativos/reference/`
- Dados consultáveis: `~/.claude/skills/hooks-nativos/references/`

## Como invocar

Usuário tipa `/hooks-nativos <tema>` ou pede em linguagem natural ("cria 3 hooks pra um vídeo sobre X", "preciso de abertura de reels sobre Y"). A skill executa as 7 fases sequencialmente, pausando para confirmação do usuário em checkpoints estratégicos (Fase 1 brief, Fase 3 estrutura escolhida).

## Princípios operacionais

- **Idioma fixo:** PT-BR. Acentuação norma culta obrigatória (sempre que "tá" usar acento, "pra" sem til, "é" com acento agudo, "cê" só quando o avatar fala assim).
- **Sem em-dash em hipótese alguma.** Substituir por vírgula, ponto, dois-pontos ou parênteses.
- **Sem "Não é X, é Y"** ou qualquer variante (Não é A, é B / Não X, mas Y / It's not X, it's Y). Use afirmação direta.
- **Sem as 5 construções retóricas proibidas** (Elliptical Setup, Revelation Hook, Big Contrast, Great Reframe, Philosophical Reduction). Ver `references/antislop-5-construcoes.md`.
- **"você/seu/sua" sempre que possível**, não "eu/meu/minha". Princípio do método de "Identificação Direta".
- **Contexto na primeira frase.** O avatar precisa saber em 2 segundos se o vídeo é pra ele.
- **Destilação.** Menos palavras é melhor, mas nunca sacrifique clareza.

## Workflow obrigatório (7 fases sequenciais)

Execute uma fase por vez. Leia o documento da fase em `reference/<arquivo>.md`, produza o output esperado, mostre ao usuário se for checkpoint, e só depois passe pra próxima.

### Fase 1: Briefer

- **Documento:** `reference/01-briefer.md`
- **Objetivo:** extrair `tema`, `nicho` e `avatar` da mensagem do usuário. Se algum estiver vago ou ausente, pedir antes de seguir.
- **Checkpoint:** mostrar o brief consolidado ao usuário e esperar confirmação antes da Fase 2.

### Fase 2: Cartógrafo de Contraste

- **Documento:** `reference/02-cartografo-contraste.md`
- **Apoio:** `references/metodo-psicologia.md`
- **Objetivo:** identificar expectativa do avatar (crença comum no nicho) vs realidade do conteúdo (verdade que será entregue). Decidir tipo de contraste: declarado ou implícito.
- **Output:** par expectativa/realidade + tipo de contraste recomendado + justificativa de 1-2 linhas.

### Fase 3: Selecionador de Estrutura

- **Documento:** `reference/03-seletor-estrutura.md`
- **Apoio:** `references/metodo-7-estruturas.md` + bancos de hooks em `references/banco-*.md`
- **Objetivo:** entre as 7 estruturas do método hook nativo (Vidente, Experimentação, Educacional/Tutorial, Revelação de Segredo, Contrário/Negativo, Comparação, Pergunta) + Choque Direto combinável, selecionar 1-2 mais adequadas.
- **Checkpoint:** mostrar estrutura(s) selecionada(s) + justificativa. Se usuário pediu estrutura específica na Fase 1, respeitar.

### Fase 4: Escritor de Hook Falado

- **Documento:** `reference/04-escritor-falado.md`
- **Apoio:** `references/disguise-alavancas.md` + `references/exemplos-few-shot.md`
- **Objetivo:** gerar 3 variações de hook falado por estrutura selecionada (1-4 linhas cada). Aplicar princípios de "Bem Direcionado" + alavancas de disguise.

### Fase 5: Escritor de Texto na Tela

- **Documento:** `reference/05-escritor-texto-tela.md`
- **Objetivo:** para cada hook falado, gerar o texto que aparece na tela durante a fala. Sentence case PT-BR, 3-7 palavras, acentuação correta.

### Fase 6: Revisor Anti-AI-Slop

- **Documento:** `reference/06-revisor-anti-slop.md`
- **Apoio:** `references/antislop-blocklist.md` + `references/antislop-smoking-guns.md` + `references/antislop-5-construcoes.md` + `references/antislop-checklist.md`
- **Objetivo:** rodar checklist quantitativo em cada par. Em-dash, blocklist, fórmulas-fórmula, 5 construções, acentuação, hedging. Se flagar, reescrever com correção mínima. Se não flagar, APROVAR.

### Fase 7: Apresentador Final

- **Documento:** `reference/07-apresentador.md`
- **Objetivo:** organizar saída em formato legível e copiável agrupado por estrutura, com contraste declarado no topo de cada bloco. Adicionar nota de uso curta.

## Gates de preflight

Antes de iniciar a Fase 1, verificar:

| Gate | O que verifica | Ação se falhar |
|---|---|---|
| Input recebido | Usuário enviou tema/pedido | Pedir tema |
| Idioma PT-BR | Usuário escreveu em português | Confirmar idioma antes de seguir |
| Tipo de conteúdo | Vídeo curto (Reels/TikTok/Shorts), não VSL/anúncio | Se for VSL/anúncio de tráfego pago, sugerir `master-hooks` no lugar |

## Output format esperado

A Fase 7 entrega no formato:

```
## Estrutura: <nome da estrutura>
**Contraste:** <declarado|implícito>. <expectativa do avatar> vs <realidade entregue>

### Variação 1
**Falado:** <1-4 linhas>
**Texto na tela:** <3-7 palavras, sentence case>

### Variação 2
**Falado:** ...
**Texto na tela:** ...

### Variação 3
**Falado:** ...
**Texto na tela:** ...

---

[se houver 2ª estrutura, repetir bloco]

**Nota de uso:** <1-2 linhas curtas com sugestão de gravação ou A/B test>
```

## Restrições absolutas

- Nunca usar em-dash (—) em nenhuma fase, em nenhum output. Memória: `feedback_no_em_dash.md`.
- Nunca usar "Não é X, é Y" ou variantes. Memória: `feedback_evitar_nao_e_x_e_y.md`.
- Nunca usar Title Case em PT-BR (nem em texto na tela, nem em headers de output).
- Nunca usar palavras da blocklist: jornada, mergulhar, alavancar, empoderar, transformador, outrossim, vale ressaltar, em suma, etc. Lista completa em `references/antislop-blocklist.md`.
- Acentuação correta em 100% dos outputs. Memória: `feedback_acentuacao_pt_br.md`.

## Roteamento sem argumento

Se o usuário acionar a skill sem tema (apenas `/hooks-nativos`), entrar diretamente na Fase 1 e pedir:

> Beleza, vou te ajudar a criar hooks pro teu vídeo curto. Me passa:
> 1. **Tema** do vídeo (do que é o conteúdo?)
> 2. **Nicho** (em que mercado tu atua?)
> 3. **Avatar** (quem é o espectador? idade, situação, dor principal)
>
> Pode mandar tudo junto em uma mensagem só.

## Related skills

- `master-hooks`: hooks de VSL/anúncio de tráfego pago, copy longa de DR. Use quando o output for anúncio pago de produto, não vídeo curto orgânico.
- `swipe-builder`: catalogar anúncios em swipe file. Use quando o usuário quiser **salvar** um hook existente, não criar novo.
- `copywriting`: copy de página/lead/CTA. Use quando o output for texto de página, não vídeo.
