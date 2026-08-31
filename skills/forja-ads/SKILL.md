---
name: forja-ads
description: "Use when the user wants to model, beat, dissect, rewrite or create direct-response ads for cold traffic (always selling the click to a VSL/quiz), or wants a full ad built from a single hook. Triggers PT: bater o controle, modelar anúncio, estrutura invisível desse anúncio, reescrever com outro ângulo, anúncio 7/8 dígitos, me faça ganchos, bullets pra esse anúncio, melhorar CTA, adicionar depoimento, anúncio UGC, variações desse anúncio, adaptar pra outro nicho, deixar mais agressivo/científico, análise desse anúncio, hooks visuais, criar ad a partir desse hook, forja-ads. Triggers EN: beat the control, invisible structure, ad teardown, rewrite ad angle, ad from hook, UGC ad version."
user-invocable: true
---

# forja-ads

Skill de modelagem e criação de anúncios de resposta direta para tráfego frio, em 16 modos: diagnóstico, cirurgia e criação. Princípio central inviolável: **estrutura migra entre nichos e ângulos, vocabulário não; mecanismo, prova e CTA reais nunca são inventados**.

## Restrições absolutas (DNA, invioláveis)

Carregue [dna/dna-card.md](dna/dna-card.md) em toda invocação (`dna=loaded`). Tier-1 bloqueante: zero em-dash, zero "Não é X, é Y", zero palavras-vício, zero CTAs fracas nuas, zero Title Case PT-BR, mecanismo sempre com nome chiclete, prova específica ou placeholder. Regras do formato: [reference/regras-de-ouro.md](reference/regras-de-ouro.md).

## Localização da DNA e dos bancos

- `dna/`: card (camada 1, sempre ativa) + disguise/ai-tells (camada 2, critique/audit)
- Swipe: `../copy-ads/swipe/_index.md` (+ saude.md, diversos.md)
- Ângulos: [reference/angulos.md](reference/angulos.md)

## Gates de preflight

Antes de qualquer escrita de copy, declare:

```
FORJAADS_PREFLIGHT: modo=<1-16> inputs=pass dna=loaded fonte=pass blocklist=loaded mutation=open
```

`modo`: identificado em modos.md. `inputs`: obrigatórios do modo presentes (senão UMA pergunta compacta). `fonte`: anúncio recebido ou exemplares do swipe selecionados. Algum gate falhou: pare e informe.

## Workflow obrigatório

| Fase | Referência | O que faz |
|---|---|---|
| 1. Roteamento | [reference/modos.md](reference/modos.md) | Detecta modo, valida inputs, define entregável |
| 2. Regras de ouro | [reference/regras-de-ouro.md](reference/regras-de-ouro.md) | Regras do formato + anatomia + prioridade por nicho |
| 3. Estilo | [reference/estilo.md](reference/estilo.md) | A voz validada: 11 marcadores + doadores. Obrigatório antes de escrever |
| 4. Motor | engine-modelagem / engine-criacao / hooks / componentes / variantes / analise | Executa o modo |
| 5. Critique | [reference/critique.md](reference/critique.md) | 10 heurísticas /40 + personas |
| 6. Audit | [reference/audit.md](reference/audit.md) | Scans binários contra a DNA |
| 7. Polish | [reference/polish.md](reference/polish.md) | Refinamento cirúrgico final |

## Como invocar

- **Anúncio + pedido claro:** preflight e produz direto, zero pergunta.
- **Sem argumento:** menu dos 16 modos (em modos.md).
- **Input faltando:** UMA pergunta compacta com os campos faltantes.
- **Parciais:** "só estrutura" (modo 4), "só hooks" (modo 3), "só audit" (fases 4-5 no copy colado).

## Few-shot BAD/GOOD

**BAD:** "Você sabia que 97% das mulheres não conseguem emagrecer? Descubra o método exclusivo e transforme sua vida."
**GOOD:** "Minha calça jeans fechou sem eu prender a respiração. Terceira semana do truque que a nutricionista da minha sogra me ensinou."

**BAD:** "Não é mais uma dieta. É uma jornada de transformação holística."
**GOOD:** "Continuei comendo pão de queijo no café. A balança desceu 4kg mesmo assim, e a explicação tá no que o intestino faz depois das 19h."

**BAD:** "Clique aqui e saiba mais!"
**GOOD:** "Essa apresentação custaria R$97 na consulta, mas o Dr. Almir liberou de graça até sexta. Toca no botão de saiba mais aqui embaixo."

## Formato de saída padrão

```
METADATA
Modo: [n. nome] | Fonte: [anúncio colado / códigos do swipe]
Audit: PASSA | Critique: X/40, banda Y

[A PEÇA, limpa, sem comentário no meio]

PRÓXIMOS PASSOS: [1 linha]
```

## Princípios operacionais

- A skill aplica a DNA nas próprias mensagens (sem em-dash, sem clichê de IA, PT-BR acentuado).
- Entrega limpa: peça inteira, sem análise intercalada (exceto modos diagnósticos 4 e 13).
- Espelhe o ritmo do doador: script falado fica em parágrafos de fala; copy de feed usa linha-única.
- Nunca invente prova, nome, número ou estudo. Original, brief ou placeholder [NOME], [NÚMERO].
- Não falsifique o audit. Se um scan falha, reescreva a seção.
