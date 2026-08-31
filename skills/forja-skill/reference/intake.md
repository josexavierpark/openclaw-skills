# Fase 1: Intake (escopar a skill nova)

Coleta o brief mínimo da skill que vamos criar. 6 perguntas com opções numeradas, uma por vez, espera resposta. Output: `SKILL_BRIEF` declarado e confirmado.

## Princípio

A skill nova é definida por DUAS coisas: que copy ela produz, e como ela trabalha. As perguntas filtram as duas. Use o padrão 3-modos da forja-oferta quando fizer sentido: sugira / o usuário responde / pula.

Aplique a DNA nas suas próprias perguntas. Sem clichê de IA na conversa.

## As 6 perguntas

### Pergunta 1: Que tipo de copy a skill vai produzir?

```
Que peça a skill nova escreve? Escolhe uma:

1. Anúncio de tráfego frio (já existe a copy-ads, posso clonar o padrão)
2. VSL (roteiro de vídeo de vendas, curto ou longo)
3. E-mail (sequência, broadcast, automação)
4. Sales page / página de vendas longa
5. Headline / lead isolado
6. Upsell / downsell / order bump
7. Outro: descreve em uma frase
```

### Pergunta 2: Nicho e amplitude

```
A skill é pra um nicho só ou ampla?

1. Um nicho específico (ex: só emagrecimento feminino)
2. Uma família de nichos (ex: saúde em geral)
3. Qualquer nicho (genérica)
```

### Pergunta 3: Destino e formato da peça

```
A peça final vai pra onde e em que formato?
(ex: VSL longa em texto corrido; e-mail HTML; sales page com blocos; roteiro 60s)

Me descreve em uma frase o destino e o tamanho típico.
```

### Pergunta 4: De onde vem a matéria-prima

```
A skill vai puxar referência de onde?

1. Do banco de swipe existente (swipe-builder)
2. De um briefing da forja-oferta
3. De documentos pra eu analisar (curso, método, swipe, transcrição, pesquisa)
4. De um banco novo, específico dessa skill (eu ajudo a estruturar)
5. Só do brief que o usuário colar na hora
```

**Roteamento:** se a resposta é 3 (documentos), peça os paths ou o texto e marque que a Fase 2 (Destilar fontes) vai rodar. Senão, a Fase 2 é `n/a`.

### Pergunta 5: Modo de uso

```
Como o usuário vai usar a skill?

1. Fluxo completo do zero (entrevista → peça pronta)
2. Cirúrgico (pedaços isolados: só hook, só CTA, só auditar)
3. Os dois (fluxo completo + sub-comandos parciais)
```

### Pergunta 6: Nome e gatilhos

```
Qual nome pra skill (o que você digita: /nome)?
E quais palavras devem disparar ela em PT e EN?
(se não souber, eu proponho a partir do tipo de peça)
```

## Output: SKILL_BRIEF

```
SKILL_BRIEF:
  nome: [slug com hífen]
  peca: [tipo de copy]
  nicho: [específico / família / genérica]
  destino_formato: [1 frase]
  materia_prima: [swipe / forja / banco novo / brief colado]
  modo_uso: [completo / cirúrgico / ambos]
  gatilhos_pt: [lista]
  gatilhos_en: [lista]
  fases_provaveis: [intake, retrieval, craft, hook, critique, audit, polish... adaptado à peça]

Confirma se está certo antes de eu montar a estrutura?
```

Espere a confirmação explícita do usuário. O gate `brief=pass` só vale depois dela.

## Regras de calibragem

- Se o usuário responder vago ("é pra vender"), peça a peça concreta. Anúncio ≠ VSL ≠ e-mail.
- Se o usuário escolher "1. Anúncio de tráfego frio" na Pergunta 1, avise que a copy-ads já cobre isso e ofereça: clonar o padrão pra outro nicho, ou seguir só se ele quer mesmo uma skill separada.
- Se ele já mandar tudo num bloco, valide cada campo e declare `SKILL_BRIEF` direto.
- Nunca invente os gatilhos sem mostrar pro usuário. Proponha, ele confirma.
