---
name: copy-ads
description: "Use when the user wants to create direct-response ads for cold traffic targeting any niche, always sending to VSL/quiz/test (never to a paid product page). The ad must never look like an ad. Triggers in Portuguese: criar anúncio cold, copy de anúncio frio, anúncio para VSL, anúncio que parece orgânico, anúncio disfarçado, copy-ads. Triggers in English: cold traffic ad, organic-looking ad, VSL ad copy, disguised ad. Inputs collected via 5 questions with numbered options. Workflow in 9 phases (intake, disguise, retrieval, craft, hook, variants optional, critique, audit, polish). Uses a swipe of 39+ annotated exemplars as structural reference. Never mentions price."
user-invocable: true
---

# copy-ads

Skill especializada em anúncios de resposta direta para tráfego frio. Cobre QUALQUER nicho. Sempre direciona para VSL ou quiz/teste (referido no copy como aula, vídeo, conteúdo, apresentação, demonstração). Princípio central inviolável: **o anúncio nunca pode parecer anúncio**.

Usa um banco de 39+ exemplares anotados (script verbatim + blueprint persuasivo extraído) como referência ESTRUTURAL. Nunca copia vocabulário de superfície.

## Restrições absolutas (invioláveis)

Estas regras valem em toda invocação. Se você se pegar prestes a violar uma, pare e reescreva.

1. **Sempre cold traffic → VSL/quiz.** Nunca anúncio direto para venda. O destino é referido como aula, vídeo, conteúdo, apresentação, demonstração, passo a passo, teste, diagnóstico, avaliação. Nunca: curso, treinamento, programa, produto pago.
2. **Zero menção a valor monetário.** Nada de preço, desconto, ROI absoluto em reais, faturamento como prova de venda. A oferta no anúncio é gratuita do ponto de vista do leitor.
3. **Nunca parecer anúncio.** Imitar formato orgânico (confissão, conselho, alerta, descoberta acidental, post de bastidor, comentário em grupo).
4. **Zero em-dash (—).** Use vírgula, ponto, dois-pontos, parênteses.
5. **Zero "Não é X, é Y"** em qualquer variante.
6. **Blocklist Tier-1** (zero): outrossim, vale ressaltar, é importante destacar, em suma, dessa forma, naturalmente, efetivamente, consequentemente, em conclusão, ademais.
7. **Blocklist Tier-2** (zero): jornada, mergulhar, alavancar, empoderar, fomentar, transformador, holístico, robusto, abrangente, exclusivo (vazio), único (vazio), ecossistema, paradigma, sinergia, catalisador.
8. **CTAs proibidas:** "Clique aqui", "Saiba mais", "Comece sua jornada", "Garanta seu acesso", "Adquira agora", "Descubra agora", "Transforme sua vida".
9. **Aberturas-cacoete proibidas:** "Você sabia que…", "E se eu te dissesse…", "Imagine…", "Nos dias de hoje…", "Você já se perguntou…", "Olá, tudo bem".
10. **Fórmulas proibidas:** "Esse [X] tem nome:", "Esse [X] existe. Funciona.", "Não X. Não Y. É Z.", "Você nunca ouviu falar nisso. E é exatamente…", "A verdade que ninguém te conta", "É um passo".
11. **6 construções retóricas proibidas:** Elliptical Setup, Revelation Hook, Big Contrast, Great Reframe, Philosophical Reduction, Repetição paralela seca.
12. **Acentuação PT-BR 100% norma culta.**
13. **Mecanismo NUNCA é sigla inventada** ("QH3X"). Sempre nome chiclete sensorial 2-4 palavras concretas.
14. **Prova SEMPRE específica:** nome + idade + situação + número quebrado. Zero "muitos alunos", "estudos mostram".
15. **Hook é feito DEPOIS do script.** Não trave a abertura no craft.

## Localização dos arquivos do swipe

Banco de exemplares dentro desta skill:

- `swipe/_index.md` — índice leve (39 entradas)
- `swipe/saude.md` — 26 exemplares de saúde
- `swipe/diversos.md` — 13 exemplares de outros nichos

Outras skills podem consumir esses arquivos por path absoluto.

## Gates de preflight

Antes de qualquer mutação, declare:

```
COPADS_PREFLIGHT: intake=pass disguise=loaded retrieval=pass blocklist=loaded mutation=open
```

| Gate | Verificação |
|---|---|
| `intake` | BRIEF_LOCK declarado e confirmado pelo usuário |
| `disguise` | `reference/disguise.md` carregado |
| `retrieval` | 2-3 exemplares do swipe selecionados, blueprint adaptado declarado |
| `blocklist` | Restrições absolutas acima ativas |
| `mutation` | Todos os gates passaram |

Se algum gate falhar, pare e informe o que falta.

## Workflow obrigatório (9 fases + scan de slop)

| Fase | Arquivo de referência | O que faz |
|---|---|---|
| 1. Intake | [reference/intake.md](reference/intake.md) | 5 perguntas com opções numeradas, uma por vez. Output: BRIEF_LOCK |
| 2. Disguise | [reference/disguise.md](reference/disguise.md) | Princípios pré-geração. 5 sinais que denunciam anúncio. 5 construções retóricas IA a evitar. Carregado antes de craft |
| 3. Retrieval | [reference/retrieval.md](reference/retrieval.md) | Busca 2-3 exemplares no swipe. Extrai estrutura prioritariamente, tom secundário, palavras pontuais terciário. Declara blueprint adaptado |
| 4. Craft | [reference/craft.md](reference/craft.md) | Voice Lock Sentence + corpo do script (com abertura em rascunho). Production bar |
| 5. Hook | [reference/hook.md](reference/hook.md) | DEPOIS do script. 5 hooks, cada um inspirado em exemplar diferente. Testes Blob/Bar/Memória. Regra 1-5-1 e DIAL BACK opcionais |
| 6. Variants | [reference/variants.md](reference/variants.md) | (Opcional) 3 versões estrutural-mente diferentes, cada uma puxando exemplar distinto |
| 7. Critique | [reference/critique.md](reference/critique.md) | Scoring 10 heurísticas (0-4 cada, total 0-40). Red flags por 3 personas |
| 8. Audit | [reference/audit.md](reference/audit.md) | 5 scans binários: léxico, estruturas, tom, indicadores quantitativos, red zones |
| 8b. Slop Score | [reference/slop-score.md](reference/slop-score.md) | Medida mecânica contra 49.347 palavras de copy humana que vendeu: concisão, templating, ritmo, tells. Roda `bash scripts/slop-audit.sh <arquivo>`. Reprova em 30 ou mais, e qualquer eixo em 50+ é conserto obrigatório. |
| 9. Polish | [reference/polish.md](reference/polish.md) | Refinamento cirúrgico final |

## Ordem natural de uso

```
intake → disguise → retrieval → craft → hook → critique → audit → slop score → polish
                                                ↓
                                          (opcional: variants)
```

## Como invocar

### Sem argumento

Mostre o menu e pergunte o que o usuário quer:

```
Posso ajudar com:
- Anúncio completo do zero (vou começar pelo intake)
- 3 variantes estrutural-mente diferentes (se já tem brief)
- Auditar copy existente (cole o copy)
- Gerar só hooks pra script existente (cole o script)

Qual?
```

### Com brief direto

Se o usuário já mandou um brief completo, vá direto para retrieval e pule intake (mas valide os 5 campos: nicho, produto/entrega VSL, destino, avatar comportamento, formato, mecanismo opcional).

### Comandos sub-orquestrados

O usuário pode pedir invocações parciais. Aceite:

- "Só intake" — roda só fase 1
- "Só hooks pra esse script" — pula fases 1-4 e vai direto pra 5 (precisa do script colado)
- "Só audit" — roda só fase 8 sobre o copy colado
- "Critique + audit" — roda 7+8 sobre copy colado
- "3 variantes" — roda fase 6 (precisa de brief ou copy de referência)

## Few-shot BAD/GOOD (calibração de voz)

**BAD 1:** "Você sabia que 97% das pessoas não conseguem emagrecer? Descubra o método exclusivo que transformou a vida de milhares."

**GOOD 1:** "Comecei a derreter 4kg por mês depois que descobri o que acontece com o pâncreas depois das 19h. A nutricionista da minha mãe (75 anos) explicou isso num jantar."

**BAD 2:** "Não é mais um curso. É uma jornada de transformação que vai revolucionar seu negócio."

**GOOD 2:** "Apaguei meu funil ontem. Tive que reconstruir do zero quando vi o que o algoritmo do Meta fez com 3 dos meus alunos na última semana."

**BAD 3:** "Clique aqui agora e garanta sua vaga antes que acabe! Investimento exclusivo só hoje."

**GOOD 3:** "Aperta no botão azul aqui embaixo e te mando o vídeo agora. Vou tirar do ar amanhã porque a janela do método fecha quando o Banco Central muda a Selic."

## Formato de saída padrão

```
═══════════════════════════════════════
METADATA

Brief utilizado: [resumo BRIEF_LOCK em 1 linha]
Exemplares de referência: [CÓDIGOS do swipe usados]
Voice Lock: [frase da fase 04]
Audit veredito: PASSA
Slop Score: X/100 (concisão x · templating x · ritmo x · tells x), veredito
Critique score: X/40 — banda Y

═══════════════════════════════════════
SCRIPT — [NICHO/PRODUTO]
[Hook escolhido pelo usuário OU placeholder se ainda não escolheu]

[Corpo do anúncio]

[CTA]

═══════════════════════════════════════
5 HOOKS ALTERNATIVOS
1. [Hook] (inspirado em [CÓDIGO]) — tipo: [In Media Res/Confissão/etc]
2. [...]
3. [...]
4. [...]
5. [...]

═══════════════════════════════════════
NOTAS TÉCNICAS
Formato: [...]
Plataforma sugerida: [Meta/TikTok/YouTube/Reels]
A/B: testar hooks 1+3 vs 2+4

═══════════════════════════════════════
PRÓXIMOS PASSOS
- Quer 3 variantes estrutural-mente diferentes?
- Mais hooks?
- Ajuste em algum bloco?
═══════════════════════════════════════
```

## Princípios operacionais

- A skill é especializada em UM formato (anúncio cold → VSL/quiz). Para outros formatos (sales page, e-mail, VSL completa, headline isolada), o usuário precisa de outra skill.
- O swipe é referência estrutural, nunca template a copiar.
- Hook sempre depois do script. Não trave abertura no craft.
- Pause após intake (Fase 1) e após retrieval/blueprint (Fase 3) para confirmação do usuário antes de prosseguir.
- Após entregar o pacote final, ofereça próximos passos (variantes, mais hooks, ajustes em bloco específico).
- Trabalhe em PT-BR por padrão (a não ser que o usuário peça outro idioma).

## Comportamento esperado

- Aplique os gates de preflight antes de mutação.
- Carregue `reference/disguise.md` ANTES de qualquer escrita de copy.
- Releia o BRIEF_LOCK antes de cada nova fase.
- Cite os códigos dos exemplares do swipe que inspiraram cada decisão estrutural.
- Não falsifique auditoria. Se algum scan falha, declare e reescreva.
- Não invente provas (testemunhos, números). Se o usuário não forneceu, use placeholders explícitos ([NOME], [IDADE], [NÚMERO_QUEBRADO]) ou peça.
