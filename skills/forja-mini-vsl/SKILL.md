---
name: forja-mini-vsl
description: "Use when the user wants to write a short video sales letter (3 to 6 min) to sell a low-ticket offer right after a quiz, or to convert a quiz result into a sale. Triggers PT: criar mini-vsl, mini vsl, vsl curta, roteiro de vsl de quiz, vsl pós-quiz, vender low ticket por vídeo. Triggers EN: mini-vsl, short vsl, quiz vsl script, low ticket video script. Produces a 5-block annotated mini-VSL script (Lead, agitate, believable action, believable solution, offer) built on the Única Crença."
user-invocable: true
---

# forja-mini-vsl

Escreve mini-VSLs (vídeo curto de 3 a 6 minutos, ~1000 palavras) para vender baixo ticket por impulso logo depois de um quiz. Roteiriza pela fórmula de 5 blocos (Lead, Agitar, Ação Acreditável, Solução Acreditável, Oferta), toda apoiada numa Única Crença que dispara duas Transferências de Desejo. Princípio inviolável: não é preciso vídeo longo para vender produto barato, e tudo no roteiro empurra a pessoa a aceitar a Única Crença.

A skill separa FORMA de SUBSTÂNCIA. A forma (arco, ritmo, tom) vem de uma mini-VSL doadora do banco de swipes. A substância (avatar, Única Crença, mecanismo, oferta, vocabulário) vem inteira do briefing. A escrita de cada bloco não imita a doadora: vem dos guias de craft em [reference/blocos/](reference/blocos/), destilados dos 9 swipes reais mais o método. Estrutura migra entre nichos, vocabulário não.

Skill irmã da [forja-quiz-nhb](../forja-quiz-nhb/SKILL.md): aceita o pacote `HANDOFF_PARA_MINI_VSL` dela e continua o funil sem perder congruência. As duas compartilham o banco de swipes e devem ser exportadas sempre como par.

## Regras invioláveis

1. Os 5 blocos são a espinha, na ordem de leitura: Lead, Agitar, Ação Acreditável, Solução Acreditável, Oferta.
2. Vender a Única Crença antes do produto. As duas Transferências de Desejo (benefício para ação, ação para solução) acontecem antes da oferta.
3. Ordem de produção middle-out: miolo primeiro (Ação + Solução sobre o trilho), depois Oferta, depois Agitar, e a Lead por último. A Lead é trailer.
4. O trilho de pontos lógicos é montado ANTES de escrever os blocos 3 e 4. A tese é o preenchimento do trilho, não invenção no escuro.
5. A Lead pinta o resultado e a existência de uma saída, e nunca entrega o COMO: a explicação do mecanismo, os passos, a prova e o protocolo ficam nos blocos 3, 4 e 5. Em funil pós-quiz, a Lead pode (e por congruência costuma) nomear o mecanismo ou o produto que o quiz já revelou; o que ela não faz é explicá-lo. Se o quiz não revelou o mecanismo, a Lead o mantém oculto. O mesmo vale para qualquer projeção de futuro: pinta o resultado, não ensina o caminho.
6. Prova calibrada pela inacreditabilidade: muita prova onde é inacreditável, nenhuma onde é óbvio. Nunca provar o que a pessoa já acredita.
7. Prova SEMPRE específica (nome + idade + situação + número) ou placeholder explícito. Zero "muitos clientes".
8. Mecanismo e solução SEMPRE com nome chiclete sensorial (2 a 4 palavras concretas), nunca sigla inventada.
9. Congruência com o quiz: a Promessa da Lead continua a promessa do quiz, e a recompensa prometida no início é a que a oferta entrega no fim.
10. Não condense. O alvo de tamanho é guia para não inflar, não teto para apressar. Bloco que corre rápido e esvazia o argumento está incompleto.
11. Zero em-dash (use vírgula, ponto, dois-pontos, parênteses, ponto e vírgula, reticências). Sem a fórmula "não é X, é Y". PT-BR norma culta. Sem nome de copywriter ou de autor de método.
12. A copy final SEMPRE num arquivo .md, nunca só no chat.

## Restrições absolutas (DNA, camada sempre-ativa)

Carregue [dna/dna-card.md](dna/dna-card.md) em toda invocação (`dna=loaded`). Tier-1 bloqueante: zero em-dash, zero "Não é X, é Y", zero palavras-vício, zero CTAs fracas, zero Title Case PT-BR, zero abertura-cacoete. Lista completa e as 7 alavancas no card. `dna/disguise.md` e `dna/ai-tells.md` (camada 2) são lidas em critique e audit.

## Localização do banco

Banco compartilhado com a forja-quiz-nhb: [../forja-quiz-nhb/swipe/INDEX.md](../forja-quiz-nhb/swipe/INDEX.md). Use a PARTE 2 de cada arquivo (a mini-VSL anotada nos 5 blocos) e o "Índice de aderência à fórmula de 5 blocos" para a seleção da doadora.

## Gates de preflight

Antes de qualquer escrita, declare:

```
FORJAMINIVSL_PREFLIGHT: intake=pass dna=loaded retrieval=pass trilho=pass blocklist=loaded mutation=open
```

| Gate | Verificação |
|---|---|
| `intake` | `MINIVSL_BRIEF` declarado e confirmado (via handoff do quiz ou brief fresco) |
| `dna` | `dna/dna-card.md` lido nesta sessão |
| `retrieval` | doadora confirmada e blueprint adaptado declarado |
| `trilho` | Única Crença travada e pontos lógicos montados (Fase 3) |
| `blocklist` | Restrições absolutas da DNA ativas |
| `mutation` | Todos os gates acima passaram |

Falhou um, pare e informe o que falta.

## Workflow obrigatório (8 fases + scan de slop)

| Fase | Referência | O que faz |
|---|---|---|
| 1. Intake | [reference/intake.md](reference/intake.md) | Lê o handoff do quiz OU entrevista do zero. Fecha o `MINIVSL_BRIEF` e a Única Crença |
| 2. Retrieval | [reference/retrieval.md](reference/retrieval.md) | Seleciona a mini-VSL doadora pela aderência, confirma com o usuário e declara o blueprint adaptado |
| 3. Pontos Lógicos | [reference/pontos-logicos.md](reference/pontos-logicos.md) | Trava a Única Crença e monta o trilho das duas Transferências de Desejo, com prova calibrada |
| 4. Craft | [reference/craft.md](reference/craft.md) + [reference/blocos/](reference/blocos/) | Roteiriza os 5 blocos middle-out, cada um pelo seu guia de craft. Junta e edita |
| 5. Critique | [reference/critique.md](reference/critique.md) | Rubrica por bloco (4 baldes + micro-venda + armadilha) e placar 0 a 40 |
| 6. Audit | [reference/audit.md](reference/audit.md) | 6 scans binários contra a DNA |
| 6b. Slop Score | [reference/slop-score.md](reference/slop-score.md) | Medida mecânica contra 49.347 palavras de copy humana que vendeu: concisão, templating, ritmo, tells. Roda `bash scripts/slop-audit.sh <arquivo>`. Reprova em 30 ou mais, e qualquer eixo em 50+ é conserto obrigatório. |
| 7. Prova Real | [reference/prova-real.md](reference/prova-real.md) | Leitura corrida holística: linearidade, mecanismo simples, transferências, costura, espelho da doadora |
| 8. Polish | [reference/polish.md](reference/polish.md) | Refino falado, corte de gordura, checklist DNA |

Referência de domínio consultada na Fase 2 e na Fase 4: [reference/metodo-mini-vsl.md](reference/metodo-mini-vsl.md) (a fórmula). Ordem das fases fixa. Dentro do craft, a escrita é fora de ordem (miolo, depois Lead, Agitar, Oferta, junta).

## Como invocar

- **Sem argumento:** ofereça (1) roteiro do zero, (2) continuar de um handoff do quiz, (3) só a Lead, (4) só a oferta, (5) auditar uma mini-VSL existente.
- **Com handoff ou brief:** se vier `HANDOFF_PARA_MINI_VSL`, preencha o `MINIVSL_BRIEF` dele e confirme só Única Crença, destino e prova. Brief solto: leia, preencha e pergunte os buracos. Nunca pule o intake.
- **Parciais:** "só a Lead", "só a oferta", "auditar [vsl]", "continuar do quiz". Em parciais, ainda assim consulte o guia de craft do bloco pedido.

## Few-shot BAD/GOOD

**BAD 1 (Lead):** "Olá! Você sabia que existe um método revolucionário para emagrecer?"
**GOOD 1:** "Oi, obrigado por responder o teste. No fim deste vídeo você recebe seu plano personalizado pra destravar o que te segura. Assiste até o fim, que foi feito pra você."

**BAD 2 (pula a transferência):** "Compre o Protocolo X e emagreça."
**GOOD 2:** "Pra secar de novo, você precisa reativar as fibras profundas. E o único jeito de acordar elas em casa é com [solução nomeada]." (ação, depois solução, depois produto)

**BAD 3 (prova do óbvio):** "Estudos provam que comer demais engorda."
**GOOD 3:** "Acredite ou não, o que te trava não é comer demais. É o acúmulo de toxinas. Deixa eu te mostrar." (pattern interrupt + prova onde importa)

**BAD 4 (oferta):** "Garanta seu acesso agora, clique no botão!"
**GOOD 4:** "Na clínica isso sai por 397. Como você fez o teste online e não precisou ir até lá, hoje sai por 37,90. Clica abaixo e pega o seu, com 30 dias de garantia."

## Formato de saída padrão

A copy final vai sempre num arquivo .md (regra inviolável 12).

```
METADATA
Brief: [resumo 1 linha]
Única Crença: [frase]
Doadora: [QZ-XXX] + aderência
Destino: [página / checkout] => variante [A / B]
Audit: PASSA
Critique: X/40, banda Y
Prova Real: PASSA
Slop Score: X/100 (concisão x · templating x · ritmo x · tells x), veredito
Palavras / minutos: [N] / [~min]

[ROTEIRO: Bloco 1 Lead => Bloco 2 Agitar => Bloco 3 Ação Acreditável => Bloco 4 Solução Acreditável => Bloco 5 Oferta]
```

## Princípios operacionais

- A skill aplica a DNA nas próprias mensagens (sem em-dash, sem clichê de IA, PT-BR acentuado) e relê o `MINIVSL_BRIEF` e a Única Crença antes de cada bloco.
- Relê o briefing mais de uma vez. Se ele já traz uma gradualização pronta, usa a escada inteira no trilho.
- Nunca invente prova: placeholder explícito ou peça ao usuário. Não prove o óbvio nem sub-prove o inacreditável.
- Mantenha a congruência com o quiz: a Promessa da Lead continua a promessa do quiz.
- Não falsifique o audit nem a Prova Real. Modele a estrutura da doadora, nunca o vocabulário.
