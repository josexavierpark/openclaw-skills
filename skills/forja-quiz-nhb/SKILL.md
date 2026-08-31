---
name: forja-quiz-nhb
description: "Use when the user wants to build a quiz funnel that creates a problem and pre-sells an offer, using the NHB hidden-architecture method. Triggers PT: criar quiz, funil de quiz, montar quiz de venda, quiz que cria problema, quiz NHB, quiz pré-venda, arquitetura de quiz. Triggers EN: build a quiz funnel, NHB quiz, problem-creating quiz, quiz to pre-sell offer. Produces a full annotated quiz (ad headline, question arc, result page, lead capture, bridge) plus a handoff for forja-mini-vsl."
user-invocable: true
---

# forja-quiz-nhb

Constrói funis de quiz pela arquitetura oculta NHB: o quiz não procura um problema, ele CRIA um, leva a pessoa pelo arco Positiva → Neutra → Negativa até a posse do problema na identidade, e entrega um resultado que pré-vende a oferta. Princípio inviolável: quem controla o problema controla a venda, e a pessoa precisa descobrir a limitação respondendo, nunca por imposição.

Skill irmã da [forja-mini-vsl](../forja-mini-vsl/SKILL.md): ao fim do quiz, ela passa um pacote de handoff para a mini-VSL que vende no destino.

## Restrições absolutas (DNA, invioláveis)

Carregue [dna/dna-card.md](dna/dna-card.md) em toda invocação (`dna=loaded`). Tier-1 bloqueante: zero em-dash, zero "Não é X, é Y", zero palavras-vício, zero CTAs fracas, zero Title Case PT-BR, zero abertura-cacoete. Mecanismo SEMPRE com nome chiclete sensorial (2 a 4 palavras concretas), nunca sigla. Prova SEMPRE específica (nome + idade + situação + número) ou placeholder explícito. Específico do formato: captura de lead no FIM, nunca no começo; o quiz CRIA o problema, não só identifica. Lista completa e as 7 alavancas no card.

## Localização da DNA e do banco

- `dna/dna-card.md`: camada 1, sempre ativa.
- `dna/disguise.md` e `dna/ai-tells.md`: camada 2, lidas em critique/audit.
- `swipe/INDEX.md`: banco de 9 funis reais (quiz + mini-VSL anotados), compartilhado com a forja-mini-vsl.

## Gates de preflight

Antes de qualquer escrita, declare:

```
FORJAQUIZ_PREFLIGHT: intake=pass dna=loaded retrieval=pass blocklist=loaded mutation=open
```

| Gate | Verificação |
|---|---|
| `intake` | `QUIZ_BRIEF` declarado e confirmado pelo usuário |
| `dna` | `dna/dna-card.md` lido nesta sessão |
| `retrieval` | 2 a 4 swipes do banco selecionados (mesmo nicho/mecânica) |
| `blocklist` | Restrições absolutas da DNA ativas |
| `mutation` | Todos os gates acima passaram |

Falhou um, pare e informe o que falta.

## Workflow obrigatório

| Fase | Referência | O que faz |
|---|---|---|
| 1. Intake | [reference/intake.md](reference/intake.md) | Entrevista o usuário e fecha o `QUIZ_BRIEF`. Pergunta mesmo com briefing pronto |
| 2. Retrieval | [reference/metodo-nhb.md](reference/metodo-nhb.md) + [swipe/INDEX.md](swipe/INDEX.md) | Carrega o método NHB e seleciona swipes do mesmo nicho/mecânica |
| 3. Craft | [reference/craft.md](reference/craft.md) | Monta arco, resultado, captura, abertura, headline + `HANDOFF_PARA_MINI_VSL` |
| 4. Critique | [reference/critique.md](reference/critique.md) | Scoring 10 heurísticas /40 + personas |
| 5. Audit | [reference/audit.md](reference/audit.md) | 6 scans binários contra a DNA |
| 5b. Slop Score | [reference/slop-score.md](reference/slop-score.md) | Medida mecânica contra 49.347 palavras de copy humana que vendeu: concisão, templating, ritmo, tells. Roda `bash scripts/slop-audit.sh <arquivo>`. Reprova em 30 ou mais, e qualquer eixo em 50+ é conserto obrigatório. |
| 6. Polish | [reference/polish.md](reference/polish.md) | Refinamento final + checklist DNA |

Ordem fixa. O hook (headline + abertura) se decide DEPOIS do arco, no craft.

## Como invocar

- **Sem argumento:** ofereça (1) quiz do zero, (2) só o arco de perguntas, (3) só a página de resultado, (4) auditar um quiz existente, (5) encadear a forja-mini-vsl.
- **Com brief direto:** leia o briefing, preencha o `QUIZ_BRIEF` e PERGUNTE só os buracos (avatar, problema a criar, mecanismo, prova, destino). Nunca pule o intake: mostre o que foi assumido.
- **Parciais:** "só o arco", "só o resultado", "auditar [quiz]", "handoff pra mini-vsl".

## Few-shot BAD/GOOD

**BAD 1 (pergunta):** "Você já se perguntou por que não consegue emagrecer? Descubra agora!"
**GOOD 1:** "Há quanto tempo você está na sua melhor forma? 1-2 anos / 3-5 / mais de 5 / nunca." (neutra que ativa declínio)

**BAD 2 (negativa fraca):** "Você tem dificuldade para perder peso?"
**GOOD 2:** "Eu faço tudo certo e o resultado não vem, e isso me assusta. ( ) é exatamente o que eu sinto ( ) ainda não, mas tenho medo" (posse negativa + future pace + saída)

**BAD 3 (resultado):** "Parabéns! Seu resultado está pronto. Clique para ver a oferta."
**GOOD 3:** "Seu perfil ficou pronto. E tem uma notícia difícil: seu metabolismo entrou em modo de resistência. Foi por isso que nada funcionou. A boa notícia é que dá pra reativar com [mecanismo]."

**BAD 4 (captura):** Pede e-mail na primeira tela.
**GOOD 4:** Captura no fim: "Digite seu WhatsApp pra desbloquear o seu protocolo personalizado."

## Formato de saída padrão

```
METADATA
Brief: [resumo 1 linha]
Swipes-base: [códigos QZ-XXX]
Audit: PASSA
Critique: X/40, banda Y
Slop Score: X/100 (concisão x · templating x · ritmo x · tells x), veredito

[QUIZ COMPLETO: headline do anúncio → abertura → arco anotado por fase → captura → página de resultado → ponte]

HANDOFF_PARA_MINI_VSL: [pacote pra skill irmã]
```

## Princípios operacionais

- A skill aplica a DNA nas próprias mensagens (sem em-dash, sem clichê de IA, PT-BR acentuado) e relê o `QUIZ_BRIEF` antes de cada fase.
- Nunca invente prova: placeholder explícito ou peça ao usuário.
- O quiz CRIA o problema. Se o rascunho só pergunta sem instalar uma limitação, reescreve.
- Não falsifique o audit. Modele a estrutura dos swipes, nunca o vocabulário.
