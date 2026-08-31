# Fase 5: Audit (scans binários anti-AI-slop)

6 scans. Cada um é passa/falha. Um falha = reescreve antes de entregar. Consulte [dna/ai-tells.md](../dna/ai-tells.md) Anexo A para a blocklist completa. Diferente do critique (nota): aqui é detecção binária.

## Scan 1: Léxico (Tier-1 e Tier-2)
Procure palavra por palavra: em-dash (—, --), outrossim, vale ressaltar, é importante destacar, em suma, dessa forma, consequentemente, ademais, jornada, mergulhar, alavancar, empoderar, fomentar, transformador, holístico, robusto, ecossistema, sinergia, catalisador, potencializar, capacitar, revolucionar.
PASSA se zero ocorrências.

## Scan 2: Estruturas-cacoete
Procure: "Não é X, é Y"; "Esse [X] tem nome:"; bullets "**Termo:** descrição"; 2+ frases seguidas com "Não"; pergunta retórica genérica de abertura ("Você sabia que...", "E se eu te dissesse...", "Imagine...").
PASSA se zero.

## Scan 3: Conectores e CTAs
Conectores acadêmicos (Furthermore, Além disso, Portanto, No entanto, Posteriormente). CTAs fracas ("Clique aqui", "Saiba mais", "Comece sua jornada", "Garanta seu acesso", "Descubra agora").
PASSA se zero.

## Scan 4: Tom e tipografia
Title Case em títulos PT-BR. CAPS em substantivo comum. Bold em "Termo: descrição". Acentuação fora da norma culta. Nome do mecanismo como sigla inventada (ex: "QH3X").
PASSA se zero.

## Scan 5: Red zones do método (específico de quiz)
- Pede nome/e-mail ANTES das perguntas (deve ser no fim).
- Quiz que só identifica a pessoa, sem CRIAR o problema.
- Salto do positivo direto para o negativo, sem o meio neutro.
- Nenhuma pergunta de posse negativa ("eu sou / eu tenho") nas últimas.
- Página de resultado sem a estrutura conforto → má notícia → mecanismo → virada.
- Negativa sem saída (força a pessoa).
PASSA se zero.

## Scan 6: Prova e personalização
Prova genérica ("muitos alunos", "estudos mostram" sem fonte). Mecanismo sem nome ("esse método" 2x). Resultado idêntico para todos fora de teste seco declarado. Promessa sem âncora.
PASSA se zero.

## Veredito
```
AUDIT QUIZ
Scan 1 Léxico: PASSA/FALHA [ocorrências]
Scan 2 Estruturas: PASSA/FALHA
Scan 3 Conectores/CTA: PASSA/FALHA
Scan 4 Tom/tipografia: PASSA/FALHA
Scan 5 Red zones do método: PASSA/FALHA
Scan 6 Prova/personalização: PASSA/FALHA
VEREDITO: PASSA (todos) / REPROVA (reescrever os que falharam)
```

Não falsifique. Se um scan falha, declare e reescreva a seção. Audit reprovado bloqueia a entrega.
