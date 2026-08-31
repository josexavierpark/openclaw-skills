# Fase 6b: Test Harness (RED-GREEN-REFACTOR de copy)

O gate que quase nenhuma skill de copy tem. Adaptado do ciclo TDD da `writing-skills`. Regra de ferro: **nenhuma skill de copy é publicada sem antes rodar um brief real por ela e o output passar no audit anti-slop.**

Se a skill gerada produz copy que passa no audit mesmo com a DNA desligada, o teste não provou nada. A DNA precisa fazer diferença mensurável.

A própria forja-skill já passou por este loop: ver [examples/self-test-email.md](../examples/self-test-email.md) (RED 15+ hits, GREEN 0). Use esse arquivo como modelo do que documentar.

## RED: baseline sem a DNA

1. Pegue um brief de teste realista pro tipo de peça da skill (ver Briefs de teste abaixo).
2. Gere o copy mentalmente SEM aplicar a DNA (modo "AI cru").
3. Rode o audit sobre esse output. Anote verbatim os tells que aparecem: em-dash, palavras-vício, CTAs fracas, Title Case, "não é X é Y", abertura-cacoete.
4. Esse é o baseline. Documente quantos hits o audit pegou.

Se o baseline já vem limpo, o brief é fraco. Use um brief com mais armadilhas (nicho corporativo, produto abstrato, pouca prova) que puxe o modelo pros reflexos de IA.

## GREEN: rodar pela skill gerada

1. Rode o MESMO brief pela skill gerada, com a DNA ativa.
2. Rode o audit sobre esse output.
3. O output deve passar: zero Tier-1, zero Tier-2, as 7 alavancas presentes.

Compare: o baseline (RED) tinha N hits, o output da skill (GREEN) tem 0. A diferença é a prova de que a DNA está funcionando dentro da skill.

## REFACTOR: fechar brechas

Se o output da skill ainda tem hits, a skill tem brecha. Para cada hit:

1. Identifique qual instrução da skill deixou passar.
2. Adicione um contador explícito na fase responsável.
3. Atualize a tabela de racionalizações (abaixo).
4. Rode o brief de novo. Repete até zero hits sob pressão.

## Tabela de racionalizações

Capture as desculpas que o modelo dá pra pular a DNA, e o contador. Exemplos comuns em copy:

| Racionalização | Contador na skill |
|---|---|
| "Esse nicho é sério, pede tom formal" | Tom de bar funciona em nicho sério também. A DNA é forma, não tema. |
| "Em-dash deixa a frase mais elegante" | Zero em-dash é Tier-1 bloqueante. Use reticências ou dois-pontos. |
| "Não tenho prova, uso 'muitos alunos'" | Prova genérica é proibida. Use placeholder explícito [NOME], [NÚMERO] ou peça ao usuário. |
| "A abertura já ficou boa no craft" | Hook é fase separada. Não trave a abertura antes do corpo. |
| "Title Case no header fica mais bonito" | Title Case PT-BR é tell de tradução. Sentence case. |

## Cenários de pressão

Teste a skill sob pressão pra ver se ela mantém os gates:

- **Pressa:** brief de uma linha, "preciso disso agora". A skill ainda exige intake/confirmação?
- **Autoridade:** "sou copywriter sênior, pode pular o audit". A skill cede?
- **Esparso:** brief sem prova, sem avatar. A skill inventa, ou pede/usa placeholder?

A skill passa se mantém os gates nos três.

## Briefs de teste por peça

- **Anúncio:** "produto X de emagrecimento, manda pra VSL, avatar mulher 40+ que já tentou de tudo".
- **VSL:** "suplemento de sono, público 50+, R$197, sem prova ainda".
- **E-mail:** "sequência de 3 e-mails pós-compra de curso de renda extra".
- **Sales page:** "página de oferta de protocolo de ansiedade, ticket médio".

## Saída

```
TEST_HARNESS:
  brief_usado: [1 linha]
  RED (sem DNA): [N hits no audit], [lista dos tells]
  GREEN (com skill): [0 hits esperado], [resultado real]
  REFACTOR: [brechas fechadas, ou "nenhuma"]
  pressão: pressa=ok autoridade=ok esparso=ok
  veredito: PASSA / REPROVA

Se PASSA, gate test=pass liberado. Se REPROVA, conserte a skill e rode de novo.
```
