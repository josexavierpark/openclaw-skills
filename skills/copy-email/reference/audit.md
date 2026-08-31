# Fase 6: Audit (scans binários anti-AI-slop)

5 scans, cada um passa/falha. Um falha = reescreve antes de entregar. Consulte [dna/ai-tells.md](../dna/ai-tells.md) Anexo A.

## Scan 1: Léxico
em-dash (—, --), outrossim, vale ressaltar, é importante destacar, em suma, dessa forma, consequentemente, ademais, jornada, mergulhar, alavancar, empoderar, fomentar, transformador, holístico, robusto, ecossistema, sinergia, catalisador, potencializar, capacitar, revolucionar.
PASSA se zero.

## Scan 2: Estruturas-cacoete
"Não é X, é Y"; "Esse [X] tem nome:"; bullets "**Termo:** descrição"; 2+ frases seguidas com "Não"; abertura "Você sabia que" / "Imagine" / "Olá, tudo bem".
PASSA se zero.

## Scan 3: Conectores e CTAs
Furthermore, Além disso, Portanto, No entanto, Posteriormente. CTAs fracas: "Clique aqui", "Saiba mais", "Garanta seu acesso", "Não perca essa oportunidade".
PASSA se zero.

## Scan 4: Tom e tipografia
Title Case PT-BR. CAPS em substantivo comum. Bold "Termo: descrição". Assunto com "!" ou clickbait vazio. Acentuação fora da norma culta.
PASSA se zero.

## Scan 5: Red zones de e-mail
Prova genérica ("muitos clientes"). Mecanismo como sigla. Mais de 1 CTA forte competindo. Assunto que promete o que o corpo não entrega.
PASSA se zero.

## Veredito
```
AUDIT
Scan 1 Léxico: PASSA/FALHA [ocorrências]
Scan 2 Estruturas: PASSA/FALHA
Scan 3 Conectores/CTA: PASSA/FALHA
Scan 4 Tom/tipografia: PASSA/FALHA
Scan 5 Red zones: PASSA/FALHA
VEREDITO: PASSA / REPROVA
```

Não falsifique. Se um scan falha, declare e reescreva.
