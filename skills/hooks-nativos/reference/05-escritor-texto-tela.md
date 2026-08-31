# Fase 5: Escritor de Texto na Tela

## Objetivo

Para cada hook falado da Fase 4, gerar o **texto que aparece na tela** durante a fala. O texto na tela reforça, sintetiza ou complementa o falado. Cria o segundo canal de informação (princípio do alinhamento entre os 4 componentes).

## Inputs

- Todos os pares falado da Fase 4 (3 por estrutura)
- Diagnóstico de contraste da Fase 2 (pra saber qual elemento destacar)

## Regras de execução

### 1. Sentence case obrigatório

PT-BR usa sentence case nativo (só a primeira palavra em maiúscula, mais nomes próprios). Title Case ("Como Melhorar Seu Treino") é assinatura de tradução de IA do inglês.

✔️ Certo: "Como acelerar seu treino em 7 dias"
❌ Errado: "Como Acelerar Seu Treino em 7 Dias"

Exceção: o nome do mecanismo nomeado entre aspas mantém Title Case próprio. Exemplo: "Aprende o Truque do Aperto" (só "Truque do Aperto" em Title Case, o resto em sentence case).

### 2. Comprimento: 3 a 7 palavras

- Mais curto facilita leitura no scroll
- Mais longo perde no ritmo do vídeo
- Se realmente precisar de 8-9 palavras pra capturar a ideia, ok. Mas raro.

### 3. Acentuação correta

Sem exceção. Todos os acentos onde a norma culta pede. "Câmara", "está", "é", "também", "vídeo". Cf. memória `feedback_acentuacao_pt_br.md`.

### 4. Quatro funções possíveis

Escolha **uma** função por hook falado. Não misture:

**A. Legenda (repetição da fala-chave)**
- Pega a frase mais forte do hook falado e repete na tela
- Funciona quando o falado já tem uma linha matadora isolada
- Exemplo: falado "Ele tá mentindo pra você. Quando ele fala que precisa de um tempo, ele tá mentindo." → tela: "Ele tá mentindo pra você"

**B. Título-pergunta**
- Quando a estrutura é Pergunta, repete ou reformula como subhead
- Exemplo: falado "Por que algumas pessoas agacham assim, e outras assim?" → tela: "Qual agachamento tá certo?"

**C. Tag descritiva (tema + ângulo)**
- Categoriza o vídeo pra audiência saber do que é
- Funciona em Educacional/Tutorial e Comparação
- Exemplo: falado "Se você quer economizar imposto, usa essa brecha do MEI" → tela: "Brecha do MEI silencioso"

**D. Reforço emocional**
- 1-3 palavras em CAPS pra marcar emoção dominante
- Funciona em Contrário/Negativo e Revelação de Segredo
- Exemplo: falado "Você tá fazendo jejum errado a vida toda" → tela: "VOCÊ FOI ENGANADA"

### 5. Sem repetir o falado inteiro

Texto na tela não é legenda automática. É **decisão editorial**. Pegue a palavra-chave, não a frase toda.

### 6. Sem em-dash (—), sem vírgula oxford ("X, Y, e Z")

Use vírgula simples ou ponto. Cf. memória `feedback_no_em_dash.md`.

### 7. Sem palavras da blocklist

Não escreva "jornada", "transformação", "mergulhe", "alavanque", "descubra agora", "garanta sua vaga", etc. Cf. `references/antislop-blocklist.md`.

## Output esperado

Imprima cada hook falado pareado com seu texto na tela:

```
### Estrutura 1: <nome>

**Variação 1:**
- Falado: <texto da Fase 4>
- Texto na tela: <3-7 palavras sentence case>

**Variação 2:**
- Falado: ...
- Texto na tela: ...

**Variação 3:**
- Falado: ...
- Texto na tela: ...

### Estrutura 2: <nome> (se houver)
...

Seguindo pra Fase 6 (Revisor Anti-AI-Slop).
```

## Checkpoint

Esta fase **não pausa**. Avance direto pra Fase 6.

## Edge cases

| Situação | Como tratar |
|---|---|
| Falado já é curto (1-2 frases) | Texto na tela pode ser ainda mais reduzido, 2-4 palavras só |
| Falado tem dois ganchos fortes | Escolha o gancho que aparece **primeiro** na fala. Texto na tela aparece no início do vídeo. |
| Texto na tela ficou idêntico ao falado | Repensa: você fez legenda preguiçosa. Pegue só a palavra-chave. |
| Mecanismo nomeado tem 5+ palavras | Encurte ou use só a parte mais memorável. "Janela das 14h" funciona melhor que "Janela Metabólica das 14h da Tarde" na tela. |

## Heurística de qualidade

Antes de soltar cada texto na tela:
1. Cabe na tela vertical do celular em fonte grande? (5-7 palavras max)
2. É legível em 0.5 segundo? (sem palavras técnicas longas)
3. Reforça o falado sem repetir literal?
4. Sentence case correto?
5. Sem em-dash, sem blocklist, sem Title Case?
