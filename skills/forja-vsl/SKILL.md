---
name: forja-vsl
description: "Use when the user wants to write a complete long-form VSL (video sales letter) script in PT-BR for direct-response, starting from a full briefing or One Pager. Writes all 9 blocks (lead, background, emotional, discovery, mecanismo do problema, mecanismo da solução, product build up, oferta, close) in middle-out order: mechanisms first, lead last. Triggers in Portuguese: criar vsl, escrever vsl, roteiro de vsl, montar vsl completa, vsl longa de venda, forja-vsl. Triggers in English: write a vsl, vsl script, long-form video sales letter. Consumes a bundled swipe of 35 cataloged VSLs as a structural donor and 9 per-block craft references. Never mentions the product before the offer."
user-invocable: true
---

# forja-vsl

Skill que escreve uma VSL completa de resposta direta, bloco a bloco, em PT-BR. Recebe um briefing grande (One Pager) e dele extrai tudo o que precisa.

Usa o banco swipe-vsl (35 VSLs catalogadas, bundlado em `swipe/`) como **doadora de forma** (estrutura, ritmo, tom) e os 9 craft references (`reference/blocos/`) como guia de **como escrever cada bloco**.

Princípio central inviolável: **a substância (única crença, mecanismos, oferta) vem do briefing; o banco empresta só a forma.** Estrutura migra entre nichos, vocabulário não.

## Restrições absolutas (invioláveis)

Valem em toda invocação. Se você se pegar prestes a violar uma, pare e reescreva.

1. **Os 9 blocos são a espinha.** Nunca pule um bloco sem registrar (ausente ou fundido) e explicar.
2. **Vender a ideia antes do produto.** Cerca de 80% do tempo (blocos 1 a 7) sem citar o produto. O nome do produto aparece pela primeira vez só no Product Build Up, no fim, como gatilho de virada para a oferta. Vale também para o MECANISMO: na Lead e em todo future pacing, pinte o RESULTADO e a existência de uma saída, nunca o mecanismo da solução nem o produto (nem a ferramenta, nem o "como"). Se o lead pensa "ah, já sei o que é", a curiosidade murcha e ele desliga antes da tese.
3. **Ordem de escrita middle-out.** Mecanismos primeiro, lead por último. Nunca escreva a lead antes da tese (ver "Ordem de escrita").
4. **Zero em-dash (—).** Use vírgula, ponto, dois-pontos, parênteses, ponto e vírgula, reticências, ou "a" em intervalos.
5. **Zero "Não é X, é Y"** como fórmula de oposição. Afirmação direta.
6. **Acentuação PT-BR 100% norma culta.**
7. **Mecanismo NUNCA é sigla inventada.** Sempre nome chiclete sensorial de 2 a 4 palavras concretas.
8. **Prova SEMPRE específica:** nome + idade ou situação + número quebrado. Zero "muitos alunos", "estudos mostram" sem fonte.
9. **Pontos lógicos no mecanismo:** afirmação seguida de reason why, sempre. Calibre a prova: muita onde é inacreditável, nenhuma onde é óbvio.
10. **Não citar nomes de copywriters nem de autores de métodos.** Material conceitual e limpo.
11. **A VSL é um roteiro falado**, não uma página de vendas. A prova final de qualidade é a leitura em voz alta (fase de fluidez).
12. **Não inventar provas** (testemunhos, números). Se o briefing não forneceu, use placeholders explícitos ([NOME], [IDADE], [NÚMERO_QUEBRADO]) ou peça.
13. **Não condense. Cada bloco é desenvolvido por inteiro.** VSL boa é longa. Escreva primeiro, corte depois. Cada bloco cumpre o seu orçamento de tempo e desenvolve TODOS os seus movimentos: agite a dor, empilhe a prova, demore na emoção, explique o mecanismo passo a passo, abra e feche cada loop, esgote o briefing. O instinto de resumir é o maior inimigo da conversão. Um bloco que corre rápido é um bloco incompleto. Proporção entre blocos (GUIA de equilíbrio, nunca um teto, não trave nisso): os mecanismos são o maior pedaço (em torno de 35 a 50% do tempo), seguidos por oferta, lead, histórias, close e build up. Serve só para o mecanismo não ser espremido nem a oferta comer o vídeo inteiro. Se um bloco pedir mais, dá mais. O que manda é desenvolver cada bloco por inteiro e o alvo total de roteiro longo: de 25 a 45 minutos falados, raramente menos. Se a VSL inteira couber em poucos minutos, ela está incompleta: volte e desenvolva cada bloco.
14. **A copy final SEMPRE vai para um arquivo .md.** Nunca entregue a VSL só no chat. Escreva o roteiro completo em um arquivo; no chat vão só o caminho, os metadados e um resumo.

## Os 9 blocos (a espinha)

| # | Bloco | Função | Reference |
|---|-------|--------|-----------|
| 1 | Lead | Trailer. Captura atenção, vende os melhores momentos. | `reference/blocos/01 - Lead.md` |
| 2 | Background Story | "Por que confiar em você?". Porta-voz, credenciais. | `reference/blocos/02 - Background Story.md` |
| 3 | Emotional Story | "Você me entende?". Dor, fundo do poço. | `reference/blocos/03 - Emotional Story.md` |
| 4 | Discovery Story | "Como você descobriu isso?". A busca, a revelação. | `reference/blocos/04 - Discovery Story.md` |
| 5 | Mecanismo do Problema | A causa raiz oculta. A Ação Acreditável. | `reference/blocos/05 - Mecanismo do Problema.md` |
| 6 | Mecanismo da Solução | A forma superior. A Solução Acreditável. | `reference/blocos/06 - Mecanismo da Solução.md` |
| 7 | Product Build Up | Como a solução virou produto. Revela o nome. | `reference/blocos/07 - Product Build Up.md` |
| 8 | Oferta | Produto, bônus, ancoragem, preço. | `reference/blocos/08 - Oferta.md` |
| 9 | Close | Garantia, escassez, empilhamento, FAQ de conversão. | `reference/blocos/09 - Close.md` |

Os blocos 5 e 6 juntos formam a **tese de marketing** (o coração argumentativo). São escritos juntos, primeiro.

## Ordem de escrita (middle-out, obrigatória)

A ordem de leitura é 1 a 9. A ordem de PRODUÇÃO é outra:

1. Mecanismo do Problema + Mecanismo da Solução (a tese, sobre o trilho de pontos lógicos)
2. Product Build Up + Oferta + Close
3. Histórias (Background, Emotional, Discovery)
4. **Lead (por último)**
5. Revisão (critique, audit, fluidez, polish)

Por quê: a lead é trailer, só dá para montar depois do filme pronto; e o mecanismo é o mais caro de refazer, então vem primeiro. Cada bloco é escrito vendo o texto já escrito dos anteriores, para a coerência e a crença se sustentarem.

## Workflow obrigatório (9 fases + scan de slop)

| Fase | Arquivo | O que faz |
|---|---|---|
| 1. Intake | [reference/intake.md](reference/intake.md) | Extrai os campos do One Pager do briefing grande. Pausa se faltar campo crítico. |
| 2. Retrieval | [reference/retrieval.md](reference/retrieval.md) | Filtra o índice do banco, propõe 1 a 3 doadoras, você confirma. Declara o blueprint adaptado. |
| 3. Pontos Lógicos | [reference/pontos-logicos.md](reference/pontos-logicos.md) | Monta o trilho da tese (única crença, pontos da Ação e da Solução Acreditável, prova calibrada). Motor dos mecanismos. |
| 4. Craft | [reference/blocos/](reference/blocos/) | Escreve os 9 blocos na ordem middle-out, cada um consultando seu reference e o seletor dele. |
| 5. Critique | [reference/critique.md](reference/critique.md) | Rubrica de 3 níveis: 4 perguntas, 10 perguntas por bloco, 9 vendas, proporção 40/25/35. |
| 6. Audit | [reference/audit.md](reference/audit.md) | Scans binários: presença e ordem dos 9 blocos, handoffs, e DNA anti-AI-slop (em-dash, blocklist, tom). |
| 6b. Slop Score | [reference/slop-score.md](reference/slop-score.md) | Medida mecânica contra 49.347 palavras de copy humana que vendeu: concisão, templating, ritmo, tells. Roda `bash scripts/slop-audit.sh <arquivo>`. Reprova em 30 ou mais, e qualquer eixo em 50+ é conserto obrigatório. |
| 7. Fluidez | [reference/fluidez.md](reference/fluidez.md) | Alavancas de voz e leitura em voz alta, caçando os 3 vilões: inacreditável, confuso, entediante. |
| 8. Prova dos 9 | [reference/prova-dos-9.md](reference/prova-dos-9.md) | Leitura corrida final, holística: linearidade, mecanismo simples, dimensionalização, costura, e espelho do doador (lê como uma VSL vencedora?). |
| 9. Polish | (inline) | Refinamento cirúrgico final, transições, corta o excesso (tira, não adiciona). |

## Gates de preflight

Antes de escrever qualquer bloco, declare:

```
FORJAVSL_PREFLIGHT: intake=pass retrieval=pass trilho=pass blocklist=loaded mutation=open
```

| Gate | Verificação |
|---|---|
| `intake` | One Pager extraído do briefing e campos críticos confirmados pelo usuário |
| `retrieval` | Doadora selecionada e aprovada; blueprint adaptado declarado |
| `trilho` | Pontos lógicos da tese montados (única crença + pontos + prova calibrada) |
| `blocklist` | DNA card (audit + fluidez) ativa |
| `mutation` | Todos os gates passaram |

Se algum gate falhar, pare e informe o que falta.

## Como invocar

### Sem argumento

Mostre o menu:

```
Posso ajudar com:
- VSL completa do zero (me manda o briefing/One Pager; começo pelo intake)
- Só a tese (mecanismo do problema + solução) a partir do briefing
- Reescrever um bloco específico (cole o bloco + o briefing)
- Auditar uma VSL existente (cole o roteiro: rodo critique + audit + fluidez)

Qual?
```

### Com briefing direto

Se o usuário já mandou um briefing completo, vá para o intake (valide os campos), depois retrieval.

### Comandos parciais

- "Só intake" / "Só retrieval" / "Só o trilho de pontos lógicos"
- "Reescreve o bloco da oferta" (precisa do briefing e do que já existe)
- "Critique + audit + fluidez nessa VSL" (cole o roteiro)

## Formato de saída

**A VSL completa é SEMPRE escrita em um arquivo `.md`, nunca só no chat.** Salve em `VSLs-Forja/[nome-do-produto]-vN.md` na pasta de trabalho do usuário (crie a pasta se não existir). No chat, entregue só o caminho do arquivo, os metadados e um resumo curto dos passes de qualidade. O roteiro inteiro, desenvolvido por completo, vive no arquivo.

Estrutura do arquivo `.md`:

```
═══════════════════════════════════════
METADADOS
Briefing: [resumo em 1 linha]
Única crença: [frase]
Doadora de forma: [CÓDIGO do swipe] (aderência: ...)
Critique: [veredito] · Audit: [PASSA/FALHA] · Fluidez: [PASSA/FALHA]
Slop Score: [X/100] · concisão [x] templating [x] ritmo [x] tells [x] · [veredito]
═══════════════════════════════════════
ROTEIRO DA VSL

[BLOCO 1: LEAD]
...
[BLOCO 9: CLOSE]
═══════════════════════════════════════
NOTAS
Blocos ausentes ou fundidos: [...]
Proporção por terço: [40/25/35 conferido]
Próximos passos: [variações de lead, ajuste de bloco, etc.]
═══════════════════════════════════════
```

## Princípios operacionais

- Trabalhe em PT-BR por padrão.
- Escreva a VSL completa em um arquivo `.md`. O chat recebe só o caminho e o resumo.
- Não condense: desenvolva cada bloco por inteiro, conforme o orçamento de tempo. VSL é longa. Esgote o briefing antes de cortar.
- A substância vem do briefing. A doadora dá só a forma. Cite o código da doadora.
- Hook (lead) sempre por último. Mecanismos primeiro, sobre o trilho de pontos lógicos.
- Pause após intake e após retrieval para confirmação do usuário antes de escrever.
- Releia o briefing mais de uma vez antes e durante a escrita, e minere os dados específicos que ele já traz: gradualização pronta, números, provas, depoimentos, exemplos. Não escreva de memória nem invente uma versão mais rasa do que o briefing entregou.
- Se o briefing já traz uma escada de pontos lógicos pronta, use-a INTEIRA como o trilho da tese, degrau por degrau, começando pelo óbvio. Não pule os primeiros degraus que aquecem o lead.
- Não falsifique critique, audit nem fluidez. Se algo falha, declare e reescreva o trecho.
- A textura (ritmo, revelação gradual, emenda entre histórias) é carregada em três lugares: o exemplo anotado de cada reference, a doadora viva imitada, e a fase de fluidez. Nunca reduza textura a regra seca.
