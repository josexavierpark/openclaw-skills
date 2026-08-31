# Template: fase audit da skill gerada

Cole como `reference/audit.md` na skill gerada. Scans binários contra a DNA. Diferente do critique (qualitativo, nota): o audit é passa/falha por padrão detectável. Fonte: [dna/ai-tells.md](../dna/ai-tells.md) Anexo A.

```markdown
# Audit (scans binários anti-AI-slop)

5 scans. Cada um é passa/falha. Um falha = reescreve antes de entregar. Consulte [dna/ai-tells.md](../dna/ai-tells.md) Anexo A para a blocklist completa.

## Scan 1: Léxico (Tier-1 e Tier-2)
Procure no copy, palavra por palavra: em-dash (—, --), outrossim, vale ressaltar, é importante destacar, em suma, dessa forma, consequentemente, ademais, jornada, mergulhar, alavancar, empoderar, fomentar, transformador, holístico, robusto, ecossistema, sinergia, catalisador, potencializar, capacitar, revolucionar.
PASSA se zero ocorrências.

## Scan 2: Estruturas-cacoete
Procure: "Não é X, é Y"; "Esse [X] tem nome:"; bullets "**Termo:** descrição"; 2+ frases seguidas com "Não"; pergunta retórica genérica de abertura.
PASSA se zero.

## Scan 3: Conectores e CTAs
Conectores acadêmicos (Furthermore, Além disso, Portanto, No entanto, Posteriormente). CTAs fracas ("Clique aqui", "Saiba mais", "Comece sua jornada", "Garanta seu acesso").
PASSA se zero.

## Scan 4: Tom e tipografia
Title Case em títulos PT-BR. CAPS em substantivo comum. Bold em "Termo: descrição". Acentuação fora da norma culta.
PASSA se zero.

## Scan 5: Red zones de conteúdo
Prova genérica ("muitos alunos", "estudos mostram"). Mecanismo como sigla inventada. Mecanismo sem nome ("esse método" 2x). <red zone específica do formato>.
PASSA se zero.

## Veredito
\```
AUDIT
Scan 1 Léxico: PASSA/FALHA [ocorrências]
Scan 2 Estruturas: PASSA/FALHA
Scan 3 Conectores/CTA: PASSA/FALHA
Scan 4 Tom/tipografia: PASSA/FALHA
Scan 5 Red zones: PASSA/FALHA
VEREDITO: PASSA (todos) / REPROVA (reescrever os que falharam)
\```

Não falsifique. Se um scan falha, declare e reescreva a seção.
```

## Red zone específica por peça (scan 5)
- Anúncio: menção a preço; destino chamado de "curso/produto".
- VSL: hook travado no corpo; preço sem escada narrada.
- E-mail: assunto clickbait vazio; mais de 1 CTA forte.
- Sales page: bloco isolado "Depoimentos" em vez de prova integrada.

## Nota sobre automação
Hoje os scans são lidos pelo modelo. Para virar determinístico (como o `npx impeccable`), dá pra escrever um script de regex que recebe o copy e retorna os hits por scan. Oportunidade futura, não bloqueia o uso.
