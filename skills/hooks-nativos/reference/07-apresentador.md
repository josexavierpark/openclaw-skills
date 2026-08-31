# Fase 7: Apresentador Final

## Objetivo

Organizar todos os pares aprovados/reescritos da Fase 6 em formato legível e copiável. Adicionar nota de uso curta com sugestão de gravação ou A/B test.

## Inputs

- Pares finais (falado + texto na tela) da Fase 6 com status APROVADO ou REESCRITO
- Brief da Fase 1 (pra contextualizar)
- Diagnóstico de contraste da Fase 2 (pra exibir no topo de cada bloco)

## Formato de saída obrigatório

```
# Hooks: <tema do brief>

**Nicho:** <nicho>
**Avatar:** <avatar>
**Tipo de contraste:** <declarado | implícito>

---

## Estrutura: <Nome da estrutura 1>

**Contraste:**
- Expectativa do avatar: <da Fase 2>
- Realidade entregue: <da Fase 2>

### Variação 1

**Falado:**
<texto 1-4 linhas, quebrando linha entre frases conforme Alavanca 1 do disguise>

**Texto na tela:** <3-7 palavras sentence case>

### Variação 2

**Falado:**
<texto>

**Texto na tela:** <texto>

### Variação 3

**Falado:**
<texto>

**Texto na tela:** <texto>

---

## Estrutura: <Nome da estrutura 2> (se houver)

[mesmo padrão]

---

## Nota de uso

<1-2 linhas com sugestão prática>
```

## Regras de formatação

### Quebra de linha no falado
- Cada frase em sua própria linha (Alavanca 1 disguise)
- Espaço em branco visual entre frases
- Não compactar 2-3 frases numa linha só

Exemplo:

```
Ele tá mentindo pra você.

Quando ele fala que precisa de um tempo, ele tá mentindo.

Olha o que tá acontecendo de verdade.
```

### Texto na tela
- Sempre em uma linha
- Sentence case
- 3-7 palavras
- Nome de mecanismo nomeado entre aspas mantém Title Case próprio

### Headers
- H1 só pro título "Hooks: <tema>"
- H2 pras estruturas
- H3 pras variações
- Sentence case em todos (exceto nomes próprios e mecanismos nomeados)

## Nota de uso (gerar 1-2 linhas)

Escolha uma das pegadas abaixo conforme o contexto:

### Pegada A: A/B test
> "Posta a Variação 1 da Estrutura <X> e a Variação 1 da Estrutura <Y> no mesmo dia. Se uma performar 2x mais que a outra, dobra a aposta nessa estrutura na semana seguinte."

### Pegada B: gravação
> "Grava 3 takes de cada variação. Na edição, escolhe o take onde teu olhar bate na câmera no segundo 1 e o ritmo de fala tá mais alto."

### Pegada C: visual sugerido
> "Pra Variação <X>, considera começar com um movimento físico (apontar pra objeto, levantar da cadeira) antes da primeira palavra. Isso ativa o Choque Direto modificador."

### Pegada D: timing
> "Variação <X> funciona melhor em vídeo de até 30s. Variação <Y> aguenta vídeo de 45-60s pelo ritmo mais lento."

Escolha a pegada mais útil dado o brief. Não cole as 4. **Uma nota só.**

## Checkpoint

Esta é a fase final. Após imprimir o output formatado, pergunte:

> Quer que eu gere mais variações de alguma estrutura? Quer testar uma estrutura do método diferente? Ou tá pronto pra gravar?

Espera resposta. Se "tá pronto", encerra. Se quer mais, volta pra Fase 3 (selecionar nova estrutura) ou Fase 4 (mais variações da mesma estrutura).

## Edge cases

| Situação | Como tratar |
|---|---|
| Fase 6 reescreveu vários hooks | Mostre só a versão final no Apresentador. Não exiba o diff aqui (isso já foi mostrado na Fase 6). |
| Usuário pediu só 1 estrutura | Apresente as 3 variações da única estrutura. Mantenha o mesmo formato sem o segundo bloco. |
| Hook ficou estranho mesmo depois da Fase 6 | Sinalize na nota de uso: "Variação <X> tá no limite do natural. Se você ler em voz alta e travar, volta e me pede pra reescrever." |
| Usuário quer copy de descrição/legenda do post | Não é escopo desta skill. Sugere a skill `copywriting` ou pede pra ele me passar o brief de descrição depois. |
