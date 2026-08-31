# Fase 6: Audit (scans binários anti-AI-slop)

6 scans. Cada um é passa/falha. Um falha = reescreve antes de entregar. Consulte [dna/ai-tells.md](../dna/ai-tells.md) Anexo A. Detecção binária, não nota.

## Scan 1: Léxico (Tier-1 e Tier-2)
Procure palavra por palavra: em-dash (—, --), outrossim, vale ressaltar, é importante destacar, em suma, dessa forma, consequentemente, ademais, jornada, mergulhar, alavancar, empoderar, fomentar, transformador, holístico, robusto, ecossistema, sinergia, catalisador, potencializar, capacitar, revolucionar.
PASSA se zero.

## Scan 2: Estruturas-cacoete
Procure: "Não é X, é Y"; "Esse [X] tem nome:"; bullets "**Termo:** descrição"; 2+ frases seguidas com "Não"; abertura-cacoete ("Você sabia que...", "E se eu te dissesse...", "Imagine...").
PASSA se zero.

## Scan 3: Conectores e CTAs
Conectores acadêmicos (Furthermore, Além disso, Portanto, No entanto, Posteriormente). CTAs fracas ("Clique aqui", "Saiba mais", "Garanta seu acesso", "Descubra agora", "Transforme sua vida").
PASSA se zero.

## Scan 4: Tom e tipografia
Title Case em títulos PT-BR. CAPS em substantivo comum ou no nome do produto. Bold em "Termo: descrição". Acentuação fora da norma culta. Mecanismo como sigla inventada.
PASSA se zero.

## Scan 5: Red zones do método (específico de mini-VSL)
- Sem Única Crença explícita.
- Pula do benefício direto para o produto (sem Transferência de Desejo).
- Afirmação forte sem prova proporcional, OU prova do óbvio (que a pessoa já acredita).
- Lead que não reconhece o quiz / quebra a congruência.
- Sem pattern interrupt de virada.
- VSL longa demais para ticket baixo (passou muito de ~1000 palavras sem motivo).
PASSA se zero.

## Scan 6: Oferta e prova
Prova genérica ("muitos clientes", "estudos comprovam" sem fonte). Escassez inventada sem lastro. Ancoragem sem justificativa do desconto. Garantia ausente na variante de checkout. Promessa sem âncora.
PASSA se zero.

## Veredito
```
AUDIT MINI-VSL
Scan 1 Léxico: PASSA/FALHA [ocorrências]
Scan 2 Estruturas: PASSA/FALHA
Scan 3 Conectores/CTA: PASSA/FALHA
Scan 4 Tom/tipografia: PASSA/FALHA
Scan 5 Red zones do método: PASSA/FALHA
Scan 6 Oferta/prova: PASSA/FALHA
VEREDITO: PASSA (todos) / REPROVA (reescrever os que falharam)
```

Não falsifique. Scan que falha, declare e reescreve a seção. Audit reprovado bloqueia a entrega.
