# Fase 1: Briefer

## Objetivo

Extrair da mensagem do usuário os 3 inputs obrigatórios para gerar hooks: `tema`, `nicho` e `avatar`. Se algum estiver ausente ou vago demais, pedir antes de avançar pra Fase 2.

## Inputs aceitos

- Mensagem em texto livre ("cria hooks pra um vídeo sobre jejum intermitente, pro nicho de mulher que quer emagrecer, avatar é mulher 35-50 que já tentou várias dietas")
- Brief estruturado (com labels explícitas)
- Ambos os formatos são válidos. A skill normaliza pra estrutura única.

## Extração

Identifique os campos abaixo na mensagem do usuário:

### Tema (obrigatório)
- O que o vídeo vai entregar como conteúdo central
- Pergunta-guia: "Do que é o vídeo? Qual é a informação, dica, revelação ou cena que o vídeo entrega?"
- Aceitar: tema único e específico ("jejum intermitente de 16h"), tema com ângulo ("brecha tributária pro MEI") ou tema com revelação ("o erro que a maioria comete ao fazer jejum")

### Nicho (obrigatório)
- O mercado, vertical ou comunidade em que o conteúdo se encaixa
- Pergunta-guia: "Em que mercado tu atua? Quem segue tua conta?"
- Aceitar exemplos: emagrecimento feminino 35-50, finanças autônomos MEI, relacionamento masculino, fitness levantadores naturais, beleza pele madura
- Se o usuário disser apenas "saúde" ou "marketing", pedir refinamento. Nicho amplo demais quebra a Fase 2.

### Avatar (obrigatório)
- Quem é o espectador alvo. Idade, situação, dor principal, contexto de vida
- Pergunta-guia: "Quem é a pessoa específica que tu quer fisgar nos primeiros 3 segundos?"
- Aceitar exemplos: "mulher 35-50, casada, já tentou Dukan, Low Carb e jejum sem sucesso, frustrada com a balança"; "homem 28-40, autônomo, ganha R$8k-15k, paga DAS mas sente que tá entregando dinheiro pro governo"
- Avatar vago ("mulheres em geral", "pessoas que querem emagrecer") força perguntas de refinamento

### Estrutura preferida (opcional)
- Se o usuário citar uma das 7 estruturas do método hook nativo (Vidente, Experimentação, Educacional, Revelação de Segredo, Contrário, Comparação, Pergunta) ou Choque Direto, capturar. Respeitar essa escolha na Fase 3.

## Output esperado

Imprima exatamente este bloco antes de pedir confirmação:

```
**Brief consolidado:**

- Tema: <tema extraído>
- Nicho: <nicho extraído>
- Avatar: <avatar extraído>
- Estrutura preferida: <nome da estrutura | "nenhuma, vou escolher na Fase 3">

Confirma esse brief pra eu seguir pra Fase 2 (Cartógrafo de Contraste)?
```

## Quando pedir mais informação

Se faltar qualquer um dos 3 campos obrigatórios, escreva:

```
Pra criar hooks que funcionam preciso de mais detalhe em [campo faltante]. Me passa:

- [pergunta-guia específica do campo faltante]

Pode mandar curto, 1-2 frases já resolvem.
```

Não tente "completar" campos vagos com chute. Avatar é o componente que mais define o contraste; sem ele claro, a Fase 2 produz hook genérico.

## Checkpoint

A Fase 1 SEMPRE termina pedindo confirmação. Não avance pra Fase 2 sem o usuário responder "sim", "confirma", "pode seguir" ou equivalente. Se o usuário pedir ajuste no brief, ajuste e peça confirmação de novo.

## Edge cases

| Situação | Como tratar |
|---|---|
| Usuário pede vários temas no mesmo pedido | Pergunte: "Qual é o vídeo prioritário? Faço esse primeiro e depois você pede o próximo." |
| Usuário não sabe o avatar | Pergunte 3 coisas: faixa etária, situação principal, dor que tira o sono. Suficiente. |
| Usuário pede VSL/anúncio pago | Sugira a skill `master-hooks` e pergunte se ele quer seguir mesmo assim no formato vídeo curto. |
| Usuário pede em inglês | Confirme se ele quer output em PT-BR ou EN. Esta skill é PT-BR por padrão. |
