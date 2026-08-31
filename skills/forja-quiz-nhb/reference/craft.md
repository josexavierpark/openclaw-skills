# Fase 3: Craft (montar o quiz)

Monta o quiz inteiro a partir do `QUIZ_BRIEF` confirmado, do método ([metodo-nhb.md](metodo-nhb.md)) e de 2 a 4 swipes do banco. Modele a ESTRUTURA dos swipes, nunca o vocabulário. Consulte o card da DNA antes de cada bloco.

Ordem de montagem: arco de perguntas primeiro, depois resultado, depois abertura, e a headline do anúncio por último (o hook se decide depois do corpo, regra da DNA).

## Bloco A: o arco de perguntas

Escolha o comprimento pelo brief (curto 5 a 9, médio 10 a 16, longo 20+). Distribua sempre em três fases nesta ordem. Nunca pule do positivo direto ao negativo.

### Positivas (2 a 3, "verde")
Dão algo, leves, externas. Linguagem dissociada: fala do que a pessoa FAZ, não de quem ela é.

Moldes:
- "Qual é o seu principal objetivo com [tema]?" (declara a meta, que o resultado vai espelhar)
- "O que mais você espera alcançar?" (múltipla, abre várias portas de dor)
- "Você já tentou [categoria de solução] antes?" (segmenta experiência, acolhe quem diz "não")
- Prova social como tela de reforço entre as positivas: "Mais de [número] pessoas já [resultado]."

### Neutras (3 a 4, "laranja")
Situação, comportamento, contexto. É o diagnóstico. Transição para o negativo.

Moldes:
- "Como você descreveria [seu corpo / sua situação / sua rotina] hoje?" (com imagens, se aplicável)
- "Há quanto tempo isso acontece?" (ativa a sensação de declínio)
- "Você tem dificuldade com algum destes?" (múltipla; cada item é uma alavanca)
- Dados objetivos quando fizer sentido (idade exata, peso/altura com IMC dinâmico, frequência). O dado técnico entrega a má notícia de forma impessoal ("seu IMC é 26.8, sobrepeso").

### Negativas (2 a 3, "vermelho")
Forçam a admissão do problema na identidade. Aqui mora a conversão.

Moldes (use "eu sou" / "eu tenho" / sondagem na primeira pessoa):
- "Eu tenho dificuldade com ___ e não importa o que eu faça, não consigo superar." (sim / não)
- "A coisa que mais me assusta sobre [tema] é ___." (future pace de medo, futuro próximo)
- "O que te levou a [estado atual]?" (externaliza a causa: hormônio, vida, biologia, parasita: tira a culpa da pessoa)
- "Qual o seu maior motivo para mudar isso agora?" (ancora a motivação emocional profunda)

Em cada negativa, empilhe o **micro-compromisso triplo**: enunciado + resposta + botão de compliance ("É exatamente o que eu sinto, quero ver a saída"). Dê sempre uma saída ("Outro", campo livre, ou pular): só de ler a opção, o problema já acende.

### Ramificação
A primeira negativa pode abrir uma árvore: a resposta aprofunda aquela linha. Muitos caminhos, mesmo destino (o problema reconhecido). Marque os ramos como `[RAMO: resposta → tela/pergunta seguinte]`.

### Técnicas obrigatórias no arco
- **Motivo para perguntar** nas sensíveis: "A razão de perguntarmos é para montar seu plano sob medida."
- **Telas de reforço** entre fases ("Isso é ótimo!", prova social, "Nós cuidamos de você").
- **Emoji e cor** para suavizar as negativas (a não ser tom clínico no brief).

## Bloco B: a página de resultado (estrutura fixa)

1. **Conforto:** agradece + "você não está sozinha, milhares passaram por isso e acharam a saída".
2. **Má notícia primeiro:** agrupe a pessoa num "tipo" e dê um rótulo negativo ao tipo. Use 2 a 3 respostas dela para provar que você entende o caso (autoridade por personalização).
3. **Mecanismo do problema:** explique por que nada funcionou, ligando às respostas. É aqui que o problema criado no brief ganha corpo.
4. **Virada:** "Aqui está a boa notícia..." → apresenta o mecanismo da solução (nome chiclete) como a resposta exata ao mecanismo do problema.
5. **Dimensione a medida:** um número de impacto que materializa a perda ("você passou 1.825 dias tentando do jeito errado").

## Bloco C: a captura de lead

No FIM, depois da inércia, como pedágio para "desbloquear o plano". Nunca no começo. Molde: "Digite seu [e-mail/WhatsApp] para liberar o seu [plano/protocolo] personalizado." Se o destino for checkout direto, a identificação pode migrar para lá (caso de alguns swipes).

## Bloco D: a abertura do quiz (decidida depois do arco)

Desliza direto para a primeira pergunta. Sem pedir dados. Headline + selo de baixo atrito ("Teste de 1 minuto"). Inverte o tom: do problema do anúncio para a esperança da personalização.

## Bloco E: a headline do anúncio (por último)

Assuntiva, de marketing diagnóstico. Presume o problema. Moldes:
- "Descubra o que está te impedindo de [resultado]."
- "Que tipo de [perfil] você é? Faça o teste."
- "Quão [risco] você está? Teste em 1 minuto."

## Ponte para o próximo passo

Se o destino é mini-VSL, feche o craft entregando o **pacote de handoff** para a `forja-mini-vsl`:

```
HANDOFF_PARA_MINI_VSL:
  avatar: [...]
  problema_criado + mecanismo_problema: [...]
  mecanismo_solucao (nome chiclete): [...]
  promessa do resultado do quiz: [a frase exata da virada]
  rótulo/tipo diagnosticado: [...]
  oferta + ticket: [...]
  prova disponível: [...]
  Única Crença sugerida: Fazer [ação] é a chave para [desejo], e a melhor forma é com [solução].
```

## Production bar (exit gate do craft)

Antes de seguir para critique, confirme cada item:

1. Arco em 3 fases, sem salto positivo→negativo?
2. 2 a 3 negativas usando "eu sou / eu tenho" (posse negativa)?
3. Micro-compromisso triplo + saída em cada negativa?
4. Problema CRIADO (não só identificado) e nomeado?
5. Mecanismo da solução com nome chiclete em aspas?
6. Resultado segue conforto → má notícia → mecanismo → virada?
7. Captura no fim, não no começo?
8. Headline do anúncio decidida só agora, no fim?
9. Prova específica ou placeholder explícito (zero "muitos alunos")?
10. Zero em-dash, zero tells do card da DNA?

Falhou um, reescreve a seção antes de avançar.
