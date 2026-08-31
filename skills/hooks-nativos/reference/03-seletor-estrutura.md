# Fase 3: Selecionador de Estrutura

## Objetivo

Escolher 1-2 das 7 estruturas do método hook nativo que melhor se encaixam ao contraste, nicho e avatar. Justificar a escolha. Respeitar preferência declarada pelo usuário na Fase 1.

## Inputs

- Brief da Fase 1 (tema, nicho, avatar, estrutura preferida opcional)
- Diagnóstico de contraste da Fase 2 (expectativa, realidade, distância, tipo)
- Consulta obrigatória a `references/metodo-7-estruturas.md`

## As 7 estruturas + 1 combinável

Síntese (consulte `metodo-7-estruturas.md` para definições completas e exemplos verbatim):

| Estrutura | Encaixe ideal | Tipo de contraste |
|---|---|---|
| Vidente | Apresenta o tema como futuro inevitável, presente vs futuro | Implícito |
| Experimentação | Mostra resultado de experimento prático ao vivo | Implícito |
| Educacional/Tutorial | Promete método nomeado pra resolver problema | Declarado |
| Revelação de Segredo | Expõe verdade escondida, marca/método pouco conhecido | Declarado |
| Contrário/Negativo | Inverte crença comum em primeira linha | Declarado (forte) |
| Comparação | Compara opções e questiona qual é a melhor | Implícito |
| Pergunta | Postula questão cuja resposta o avatar quer | Implícito ou Declarado |
| Choque Direto (combinável) | Para o scroll com palavra/objeto físico | Qualquer (modifica outra) |

## Regra de seleção

### Se o usuário escolheu estrutura na Fase 1
- Respeite a escolha. Use essa estrutura como #1.
- Se quiser, ofereça uma segunda complementar.

### Se nenhuma estrutura foi pedida
- Combine os filtros abaixo nesta ordem:

**Filtro 1: tipo de contraste da Fase 2**
- Se contraste **declarado** → priorize Contrário/Negativo, Revelação de Segredo, Educacional/Tutorial
- Se contraste **implícito** → priorize Vidente, Experimentação, Comparação, Pergunta

**Filtro 2: nicho**
- Tech, inovação, produto físico → Vidente, Experimentação
- Saúde, finanças, relacionamento (conselho contra-intuitivo) → Contrário/Negativo, Revelação de Segredo
- How-to, método, sistema → Educacional/Tutorial
- Beleza, moda, lifestyle (descoberta) → Revelação de Segredo, Comparação
- Curiosidade pura, ciência, fato chocante → Pergunta, Revelação de Segredo

**Filtro 3: avatar**
- Avatar cético, já tentou várias soluções → Contrário/Negativo (precisa quebrar crença antes de propor)
- Avatar iniciante, quer roteiro → Educacional/Tutorial
- Avatar tomador de decisão racional → Comparação
- Avatar movido por curiosidade → Pergunta, Revelação de Segredo
- Avatar quer ver provas, não promessas → Experimentação

**Filtro 4: cota máxima**
- Selecione no máximo 2 estruturas
- Se selecionar 2, prefira uma "Declarada" + uma "Implícita" para gerar variedade que o usuário pode testar em A/B

### Choque Direto como modificador

Choque Direto não é estrutura sozinha. É modificador combinável. Use quando:
- Avatar tem TDAH de feed (cota de atenção curta)
- Tema permite mostrar objeto físico ou gesto chamativo no início
- Você quer hyper-curto, palavra-chave seguida da estrutura principal

Exemplo: "Olha essa caixa de remédio aqui" (Choque Direto) + "essa pílula azul não fez nada, mas a verde mudou tudo" (Contrário).

## Output esperado

Imprima:

```
**Estruturas selecionadas:**

1. **<Nome da estrutura 1>**: <1 linha de justificativa: por que encaixa no contraste + nicho + avatar>
2. **<Nome da estrutura 2>** (opcional): <1 linha de justificativa>

Combinável: <Choque Direto sim/não, com qual estrutura>

Posso seguir pra Fase 4 (Escritor de Hook Falado) com essas estruturas? Se quiser trocar, é só falar.
```

## Checkpoint

Esta fase **pausa** para confirmação leve do usuário. Se ele não responder em até uma rodada, considere aprovado e siga.

## Edge cases

| Situação | Como tratar |
|---|---|
| Distância de contraste foi "baixa" e usuário insistiu em seguir | Use Educacional/Tutorial. É a estrutura mais segura quando o contraste não é forte. |
| Usuário pediu estrutura que não combina com o contraste | Aceite, mas alerte: "essa estrutura encaixa melhor em <tipo de contraste oposto>; vou adaptar mas pode sair menos afiado". |
| 3+ estruturas parecem boas | Escolha 2. Não passe de 2. Mais variações por estrutura > mais estruturas. |
