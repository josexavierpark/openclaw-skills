# Fase 03: Retrieval (busca e uso de exemplares do swipe)

Como encontrar e usar exemplares do banco como referência estrutural. Roda DEPOIS do intake.

## Princípio

O banco de exemplares (`swipe/*.md`) é referência viva. Outras skills/assistentes vão crescer com novos ads. Cada anúncio tem:
- Script verbatim (preservado, pode conter qualquer coisa, inclusive preço)
- Blueprint anotado (estrutura persuasiva extraída, abstrato e reutilizável)

Você usa prioritariamente o **blueprint**. Secundariamente o **tom**. Pontualmente **palavras específicas** quando servem ao argumento.

## Sequência obrigatória

### Passo 1: Leia o BRIEF_LOCK

Confirme em uma frase qual nicho/subnicho/formato você está buscando. Exemplo:

> Buscando exemplares: nicho saúde, subnicho emagrecimento, formato copy longa feed, avatar comportamento 3 (já tentou e falhou).

### Passo 2: Abra swipe/_index.md

O índice tem 39 entradas leves. Cada uma com:
- Código único (SAU-NNN ou DIV-NNN)
- Nicho
- Subnicho
- Hook
- Arquivo correspondente

### Passo 3: Filtre em ordem de prioridade

1. **Nicho** (exato): saúde vai pra `swipe/saude.md`, qualquer outro vai pra `swipe/diversos.md`
2. **Subnicho** (exato se existir): emagrecimento, sono, energia, audição, etc.
3. **Tipo de hook** (apenas como PISTA de estrutura, NÃO trave seleção aqui — o hook real é decidido depois na fase 05)
4. **Formato** (se houver correspondência)

### Passo 4: Selecione 2-3 exemplares mais próximos

Critério de seleção:
- **Match perfeito** (mesmo nicho, mesmo subnicho, mesmo formato): pega 2-3 desses
- **Match parcial** (mesmo nicho, subnicho diferente mas estrutura compatível): pega 1-2
- **Match estrutural** (nicho diferente mas blueprint aplicável): pega 1 se houver poucos matches no nicho

**Importante:** se o aluno está em renda extra com IA (DIV-003 já existe), mas você tem que escrever um copy de saúde, você ainda pode pegar DIV-003 se a ESTRUTURA é a melhor disponível. Estrutura migra entre nichos. Vocabulário NÃO.

### Passo 5: Abra o arquivo correspondente

- Se selecionou códigos SAU-* → `swipe/saude.md`
- Se selecionou códigos DIV-* → `swipe/diversos.md`
- Se selecionou mistura → abra os dois

Leia APENAS os IDs selecionados, não o arquivo inteiro. Cada exemplar tem 3 blocos:
- Metadados
- Script completo
- Estrutura persuasiva (blueprint)

### Passo 6: Extraia (priorizando estrutura)

#### Prioridade 1: Estrutura persuasiva
Identifique os MOVIMENTOS persuasivos do blueprint. Cada movimento tem:
- Nome funcional (ex: "Nomeação de adversário externo")
- Descrição da função
- Padrão abstrato com placeholders

**Use o padrão abstrato.** É reutilizável.

#### Prioridade 2: Tom
Observe:
- Tempo verbal (passado recente, presente, narrativo)
- Pessoa (1ª pessoa, 2ª direta, narrador externo)
- Registro (bar, conversa, palco, conselho)
- Ritmo (curto-curto-curto vs longo-curto-curto)

#### Prioridade 3: Palavras pontuais
Pode reusar palavras específicas quando:
- Servem ao argumento do brief atual
- Pertencem ao vocabulário do nicho/avatar (gírias, termos técnicos comuns)
- Não são frases-fórmula nem clichês do nicho original

**NÃO copie:**
- Frases inteiras do exemplar
- Estrutura de sentença literal
- Jargão de catálogo (mesmo presente no exemplar)
- Frases-fórmula da blocklist (mesmo se aparecem no exemplar — alguns exemplares preservam tics IA)

### Passo 7: Declare o blueprint adaptado

Antes de craft, declare assim:

```
BLUEPRINT ADAPTADO (referenciando [CÓDIGO 1] + [CÓDIGO 2] + [CÓDIGO 3])

Movimentos:
1. [Nome funcional] — adaptação: [como aplicar pro brief atual]
2. [Nome funcional] — adaptação: [...]
3. [Nome funcional] — adaptação: [...]
4. [Nome funcional] — adaptação: [...]
5. CTA — adaptação: [como nomear o destino, ação, gatilho]

Tom: [descrição em uma frase]
Palavras-âncora do nicho que vou reutilizar: [lista pequena se aplicável]
```

Espere confirmação do aluno antes de craft.

## Regra crítica

A **estrutura persuasiva** é o que mais importa. Tom é segundo. Vocabulário pontual entra quando ajuda. O que evitar é **pattern-matching cego na superfície**: frases-fórmula do exemplar, jargão de catálogo, estrutura de sentença literal.

Estrutura migra entre nichos. Vocabulário não.

## Quando não há match exato

Se nenhum exemplar é match perfeito, use o de **estrutura persuasiva mais próxima**, mesmo de outro nicho. Casos típicos:

- Brief de saúde feminina pélvica sem match em SAU → use SAU-020 (Vagina Coach) que é o único, OU use um exemplar de saúde feminina com estrutura compatível
- Brief de criptomoedas sem match em DIV → use DIV-002 (renda extra) que tem estrutura de "milionário aos 22" compatível, OU use DIV-003 (renda extra com IA) que confronta o leitor
- Brief de espiritualidade → use os exemplares de saúde com narrativa de descoberta (SAU-001 memória, SAU-009 grounding) por estrutura de "ritual com mecanismo único"

## Como navegar o swipe rapidamente

O `swipe/saude.md` tem "Navegação rápida" no topo agrupando por subnicho. O `swipe/diversos.md` também. Use isso pra localizar IDs sem ler tudo.

Exemplo de busca:
- Brief = emagrecimento feminino → vê em saude.md: "Emagrecimento feminino → SAU-004"
- Brief = emagrecimento misto → vê: "Emagrecimento → SAU-002, SAU-003, SAU-012"
- Brief = audição → vê: "Audição → SAU-018, SAU-021, SAU-025"

## Mapa de exemplares por hook type

Quando o brief sugere um hook específico, esses são os go-to:

**In Media Res:** SAU-022 (MMA Story), SAU-026 (Apex Labs)
**Confissão Vulnerável:** SAU-021 (Nebroo whiteboard), SAU-025 (100 reasons), DIV-008 (Eskin founder)
**Bait & Pivot:** SAU-002 (vinagre→azeite), SAU-005 (No Blue Glasses), SAU-024 (Quiet Lab), DIV-012 (Dr Marty)
**Authority Hijacking:** SAU-020 (Vagina Coach), DIV-004 (Farmer's Dog)
**Apagou o Trabalho:** raro no swipe atual, use DIV-003 como aproximação (renda extra com IA)
**Vilão Externo Nomeado:** SAU-006 (iliacus), SAU-007 (travesseiros), SAU-014 (Luna parasita)
**Sensorial:** SAU-015 (mushroom coffee curto), SAU-016 (Grons), SAU-017 (Wixson), DIV-007 (Status Audio)
**Contradição-Impossibilidade:** SAU-001 (100 anos memória), SAU-011 (pai 79 anos), SAU-018 (78 hearing like 27), DIV-005 (Briza AC), DIV-006 (Glacier Breeze)
**Myth-Busting:** SAU-008 (Luna Via), SAU-009 (Grounding Well), SAU-012 (Gundry), SAU-019 (Honx), SAU-023 (Earthing System), DIV-001 (Credit Score), DIV-010 (Procrastination)
**Entrevista-Revelação:** SAU-004 (entrevista 42 anos), SAU-013 (Elder Bruno tea), DIV-002 (milionário 22), DIV-009 (JumpSpeak)
**Confronto Direto:** SAU-010 (Spartan hair), DIV-003 (renda extra IA), DIV-011 (Flicky), DIV-013 (Bare Skin)
**Pergunta-Descoberta:** SAU-003 (Noom GLP-1)

Use esse mapa para acelerar busca quando o brief é claro sobre o tipo de hook desejado.
