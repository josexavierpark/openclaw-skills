# Audit (scans binários anti-AI-slop)

5 scans. Cada um é passa/falha. Um falha = reescreve antes de entregar. Consulte [dna/ai-tells.md](../dna/ai-tells.md) Anexo A para a blocklist completa.

## Scan 1: Léxico (Tier-1 e Tier-2)

Procure no copy, palavra por palavra: em-dash (—, --), outrossim, vale ressaltar, é importante destacar, em suma, dessa forma, consequentemente, ademais, jornada, mergulhar, alavancar, empoderar, fomentar, transformador, holístico, robusto, ecossistema, sinergia, catalisador, potencializar, capacitar, revolucionar.
PASSA se zero ocorrências.

## Scan 2: Estruturas-cacoete

Procure: "Não é X, é Y"; "Esse [X] tem nome:"; bullets "**Termo:** descrição"; 2+ frases seguidas começando com "Não"; invalidação em lista / negação em série ("não é [causa 1], não é [causa 2], nem [causa 3]"); pergunta retórica genérica de abertura ("Você já se sentiu...?"); "Você sabia que..." abrindo; "Imagine..." abrindo.
PASSA se zero. A transferência de culpa é permitida só na forma positiva (nomear o culpado real direto, sem empilhar negativas: ver estilo.md marcador 11).

## Scan 3: Conectores e CTAs

Conectores acadêmicos (Furthermore, Além disso, Portanto, No entanto, Posteriormente). CTAs nuas sem valor/motivo/urgência ("Clique aqui", "Saiba mais" seco, "Comece sua jornada", "Garanta seu acesso", "Transforme sua vida"). Atenção: "toca no botão de saiba mais aqui embaixo" dentro de CTA com valor é PERMITIDO (mecânica da plataforma, regra de ouro 3).
PASSA se zero violações.

## Scan 4: Tom e tipografia

Title Case em títulos PT-BR (exceto nome chiclete do mecanismo). CAPS em substantivo comum (permitido só em palavra-chave emocional). Bold estrutural "Termo: descrição". Acentuação fora da norma culta (inclusive tá/pra/tô).
PASSA se zero.

## Scan 5: Red zones do formato

- Preço do PRODUTO mencionado (âncora de valor da apresentação é permitida).
- Destino chamado de curso, treinamento, programa ou produto.
- Prova genérica ("muitos alunos", "estudos mostram") sem placeholder.
- Dado, nome, estudo ou número INVENTADO que não veio do original, do brief ou de placeholder declarado.
- Mecanismo como sigla inventada, ou sem nome ("esse método" 2+ vezes).
- Bullets antes do primeiro CTA.
- Sagrados do original alterados numa reescrita (mecanismo renomeado, número de prova mudado).
PASSA se zero.

## Veredito

```
AUDIT
Scan 1 Léxico: PASSA/FALHA [ocorrências]
Scan 2 Estruturas: PASSA/FALHA
Scan 3 Conectores/CTA: PASSA/FALHA
Scan 4 Tom/tipografia: PASSA/FALHA
Scan 5 Red zones: PASSA/FALHA
VEREDITO: PASSA (todos) / REPROVA (reescrever os que falharam)
```

Não falsifique. Se um scan falha, declare e reescreva a seção. No METADATA final aparece só o veredito; a tabela completa só se houve falha e correção, ou se o usuário pedir.
