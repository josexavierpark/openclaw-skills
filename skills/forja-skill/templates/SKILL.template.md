# Template: SKILL.md da skill gerada

Andaime do SKILL.md. Substitua os `<...>`. Mantenha a ordem das 9 partes. Veja [authoring-rules.md](../reference/authoring-rules.md) antes de finalizar.

````markdown
---
name: <nome-com-hifen>
description: "Use when <gatilho principal em inglês, 3ª pessoa>. Triggers PT: <lista>. Triggers EN: <lista>. <1 linha do que produz, sem resumir o workflow>."
user-invocable: true
---

# <nome-com-hifen>

<Parágrafo de identidade: 2-3 frases. Que peça produz. Princípio central inviolável.>

## Restrições absolutas (DNA, invioláveis)

Carregue [dna/dna-card.md](dna/dna-card.md) em toda invocação. Tier-1 bloqueante: zero em-dash, zero "Não é X, é Y", zero palavras-vício, zero CTAs fracas, zero Title Case PT-BR, mecanismo sempre com nome chiclete sensorial. Lista completa e as 7 alavancas no card.

## Localização da DNA e do banco

- `dna/dna-card.md`: camada 1, sempre ativa
- `dna/disguise.md` e `dna/ai-tells.md`: camada 2, lidas em critique/audit
- <path do swipe/banco, se houver>

## Gates de preflight

<cole o bloco de preflight.template.md, adaptado>

## Workflow obrigatório

| Fase | Referência | O que faz |
|---|---|---|
| 1. <fase> | [reference/<fase>.md](reference/<fase>.md) | <função> |
| ... | ... | ... |
| N. critique | [reference/critique.md](reference/critique.md) | Scoring 10 heurísticas /40 + personas |
| N. audit | [reference/audit.md](reference/audit.md) | Scans binários contra a DNA |
| N. polish | [reference/polish.md](reference/polish.md) | Refinamento final |

## Como invocar

### Sem argumento
<menu de opções>

### Com brief direto
<o que fazer se o usuário já mandou brief>

### Comandos parciais
<lista de sub-invocações>

## Few-shot BAD/GOOD

**BAD 1:** <copy com tells de IA>
**GOOD 1:** <copy modelado na DNA>

<3 a 7 pares>

## Formato de saída padrão

\```
METADATA
Brief: [resumo 1 linha]
Exemplares: [códigos do swipe]
Audit: PASSA
Critique: X/40, banda Y

[PEÇA]
...
\```

## Princípios operacionais

- A skill aplica a DNA nas próprias mensagens (sem em-dash, sem clichê de IA, PT-BR acentuado).
- Releia o brief antes de cada fase.
- Nunca invente prova. Use placeholder explícito ou peça ao usuário.
- Não falsifique o audit. Se um scan falha, reescreva.
````

## Lembretes

- Corpo do SKILL.md alvo < 500 palavras. Detalhe vai pras referências.
- `description` só com gatilhos. Nunca resume as fases.
- Toda skill tem critique, audit e polish. Não são opcionais.
