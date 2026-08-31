---
name: copy-email
description: "Use when the user wants to write direct-response email: a broadcast, a sales email, or an automated sequence, that sends to a VSL or offer page. Triggers in Portuguese: criar e-mail, e-mail de oferta, sequência de e-mail, e-mail de venda, copy de e-mail, e-mail pra lista, e-mail de carrinho. Triggers in English: write email copy, sales email, email sequence, broadcast email, abandoned cart email."
user-invocable: true
---

# copy-email

Escreve e-mail de resposta direta que manda pra VSL ou página de oferta. Cobre broadcast único e sequência. Princípio central: o e-mail ganha a abertura no assunto e na primeira linha, e cada linha entrega a próxima.

## Restrições absolutas (DNA, invioláveis)

Carregue [dna/dna-card.md](dna/dna-card.md) em toda invocação. Tier-1: zero em-dash, "Não é X, é Y", palavras-vício, CTAs fracas, Title Case PT-BR; mecanismo sempre com nome chiclete. De e-mail: assunto com curiosidade real, 1 CTA forte, prova específica. Lista completa e as 7 alavancas no card.

## Localização da DNA

- `dna/dna-card.md`: camada 1, sempre ativa
- `dna/disguise.md` e `dna/ai-tells.md`: camada 2, lidas em critique/audit

## Gates de preflight

Antes de escrever, declare:

```
COPYEMAIL_PREFLIGHT: intake=pass angulo=pass dna=loaded blocklist=loaded mutation=open
```

| Gate | Verificação |
|---|---|
| `intake` | Brief confirmado pelo usuário |
| `angulo` | Ângulo de entrada escolhido e arquétipo de abertura definido |
| `dna` | `dna/dna-card.md` lido nesta sessão |
| `blocklist` | Restrições absolutas ativas |
| `mutation` | Todos acima passaram |

## Workflow

| Fase | Referência | O que faz |
|---|---|---|
| 1. Intake | [intake.md](reference/intake.md) | 5 perguntas. Output: `BRIEF_LOCK` |
| 2. Ângulo | [angulo.md](reference/angulo.md) | Escolhe o ângulo de entrada + arquétipo de abertura |
| 3. Craft | [craft.md](reference/craft.md) | Corpo do e-mail (assunto em rascunho) + CTA. Sequência se aplicável |
| 4. Assunto | [craft.md](reference/craft.md) | 5 assuntos DEPOIS do corpo, inspirados em arquétipos diferentes |
| 5. Critique | [critique.md](reference/critique.md) | Scoring 10 heurísticas /40 + personas |
| 6. Audit | [audit.md](reference/audit.md) | 5 scans binários contra a DNA |
| 7. Polish | [polish.md](reference/polish.md) | Refinamento final |

## Como invocar

- **Sem argumento:** ofereça as opções: e-mail único, sequência, só assuntos pra um corpo colado, ou auditar um e-mail colado.
- **Com brief direto:** valide os 5 campos e vá pro ângulo.
- **Parciais:** "só assuntos", "só audit", "sequência de N".

## Few-shot BAD/GOOD

**BAD assunto:** "Descubra o segredo para [benefício]!"
**GOOD assunto:** "o que o seu corpo faz às 3 da manhã (e por que te acorda)"

**BAD abertura:** "Olá, tudo bem? Você sabia que muitas pessoas sofrem com isso?"
**GOOD abertura:** "Você acorda às 3 da manhã. Olha o teto. E fica ali, esperando o sono voltar, que não volta."

## Formato de saída padrão

```
METADATA: brief, ângulo, audit PASSA, critique X/40
ASSUNTO: [escolhido]
[Corpo + CTA]
5 ASSUNTOS ALTERNATIVOS (cada um com arquétipo)
```

## Princípios operacionais

- Aplica a DNA nas próprias mensagens: sem em-dash, sem clichê de IA, PT-BR acentuado.
- Assunto e primeira linha são decididos DEPOIS do corpo. Não trave a abertura no craft.
- 1 CTA forte por e-mail. Em sequência, cada e-mail tem um único trabalho.
- Nunca invente prova. Use placeholder explícito ou peça ao usuário.
- Releia o `BRIEF_LOCK` antes de cada fase. Não falsifique o audit.
