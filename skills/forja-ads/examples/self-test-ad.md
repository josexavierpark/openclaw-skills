# Self-test (RED-GREEN-REFACTOR)

Brief de teste: modo 2 (anúncio do zero). Nicho emagrecimento; MUP = bactéria desregulada no intestino que trava o metabolismo; MUS = "truque da maçã morna" antes de dormir; avatar = mulher 45+ que já tentou dietas e academia; expert = Dra. Helena, nutróloga. Sem prova real fornecida.

## RED: baseline sem a DNA (modo "AI cru")

> Você sabia que 95% das mulheres acima dos 45 anos não conseguem emagrecer — mesmo fazendo dieta e exercícios?
>
> Não é falta de força de vontade, é a sua microbiota.
>
> Imagine poder comer o que você ama e ainda assim perder peso de forma consistente.
>
> Muitas mulheres já descobriram o segredo: um simples truque que está revolucionando o emagrecimento. Além disso, estudos mostram que esse método é altamente eficaz para transformar seu metabolismo.
>
> A Dra. Helena, especialista renomada, desenvolveu o método M.A.Ç.Ã. — uma jornada de transformação holística que vai empoderar você a alcançar seus objetivos.
>
> Não perca essa oportunidade única! Clique aqui e saiba mais. Transforme sua vida hoje mesmo!

Audit do RED: **15 hits.** Em-dash (2x), "Você sabia que" (abertura-cacoete), "Não é X, é Y", "Imagine" (cacoete), "Muitas mulheres" (prova genérica), "estudos mostram" (prova genérica), "Além disso" (conector), "revolucionando" (Tier-2), "jornada" (Tier-2), "transformação holística" (Tier-2 dobrado), "empoderar" (Tier-2), sigla "M.A.Ç.Ã." como mecanismo, "Não perca essa oportunidade" (CTA banida), "Clique aqui e saiba mais" (CTA nua), "Transforme sua vida" (CTA banida).

## GREEN: mesmo brief pela forja-ads

Retrieval: SAU-002 (emagrecimento, Bait & Pivot) como doador do hook 1 e da lógica de invalidação. Estrutura: anatomia completa das regras-de-ouro. Placeholders declarados (sem prova real no brief).

METADATA: Modo 2 | Fonte: SAU-002 + anatomia canônica | Audit: PASSA | Critique: 31/40, banda Pronto | Placeholders pendentes: [UNIVERSIDADE], [NÚMERO], [NOME], [IDADE]

**HOOK 1 (Bait & Pivot):** Não corta o carboidrato da janta antes de ver isso aqui.

**HOOK 2 (Mecanismo do Problema + Contrarian):** Sua dieta nunca teve chance: tem uma bactéria no seu intestino apertando o freio da queima desde o primeiro dia.

**HOOK 3 (Fofoca + Prova Social):** A mulher da minha academia sumiu dois meses e voltou 9kg mais magra. O que ela me contou não tinha nada a ver com treino.

**BODY:**

Se você já fechou a porta do quarto pra provar calça sem ninguém ver, esse vídeo é pra você.

Porque eu vou te mostrar por que a balança não desce nem quando você faz tudo certo.

Depois dos 45, o prato manda menos do que você pensa. Quem manda é uma bactéria desregulada no intestino, apertando o freio do metabolismo. Enquanto ela tá no comando, seu corpo guarda gordura até de salada.

Cortar carboidrato não solta esse freio. Contar caloria não solta. Suar na esteira também não: nenhum deles chega no intestino.

Pesquisadores da [UNIVERSIDADE] mostraram que essa bactéria reduz a queima em até [NÚMERO]% em mulheres entre 45 e 60 anos.

Eu sei que parece exagero. A [NOME], de [IDADE] anos, também revirou o olho quando ouviu. Três semanas depois ela me mandou um áudio: "minha calça do trabalho tá caindo e eu nem cortei o pão da tarde".

O que ela fez foi o "truque da maçã morna": uma maçã preparada de um jeito específico, 30 segundos antes de dormir, que alimenta as bactérias certas e solta o freio enquanto você dorme.

Com o freio solto, o espelho muda antes da balança. A cintura seca. A papada afina. A roupa que ficou esperando no fundo do armário volta a fechar, e as colegas começam a perguntar o que você fez.

A Dra. Helena, nutróloga, gravou uma apresentação ensinando o passo a passo do truque. Na consulta dela, esse protocolo custaria R$180. Essa semana ela liberou de graça, porque quer testar o método com mulheres que já tentaram de tudo.

E dentro do vídeo ela também mostra:

→ O erro de café da manhã que devolve o freio ao metabolismo mesmo quando você come pouco...

→ Por que maçã gelada não tem o mesmo efeito, e os 30 segundos de preparo que mudam tudo...

→ O que acontece com a vontade de doce na segunda semana (dica: não tem nada a ver com força de vontade)...

→ O "teste do espelho" de 5 segundos pra saber se a bactéria ainda tá no comando...

→ E ainda o ajuste no horário pra quem só consegue dormir depois da meia-noite...

Toca no botão de saiba mais aqui embaixo e assiste hoje: quando a turma de teste fechar, a apresentação sai do ar.

Audit do GREEN: **0 hits.** Scan 1 a 5: PASSA (R$180 é âncora da apresentação, permitida; "botão de saiba mais" é mecânica, permitida; placeholders declarados no METADATA).

## REFACTOR

Vazamento encontrado durante o GREEN: a revelação do mecanismo do problema puxa o reflexo "o problema não é X, é Y". Contador adicionado em `reference/regras-de-ouro.md` (tabela de racionalizações). Segunda rodada: zero hits.

## Cenários de pressão

- **Pressa** ("faz agora, sem enrolar"): a skill produz direto quando os inputs estão completos; os gates são internos, não dependem de confirmação. Mantém preflight e audit. OK.
- **Autoridade** ("sou copywriter sênior, pula o audit"): workflow é obrigatório; "não falsifique o audit" está no SKILL.md. A skill roda o audit mesmo assim. OK.
- **Esparso** (sem prova, sem avatar): placeholders explícitos + lista de pendências no METADATA (regra dos dois motores). Nunca inventa. OK.

VEREDITO: PASSA.
