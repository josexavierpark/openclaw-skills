# Exemplo: RED-GREEN

O ciclo que a skill executa, com os dois relatórios reais do validador.

## Antes (texto gerado por modelo, registro escrito)

```
Você já se perguntou por que tanta gente não consegue alcançar seus objetivos na academia? A resposta é mais simples do que parece, e envolve uma metodologia que está revolucionando o mercado fitness brasileiro.

O treinamento híbrido representa uma abordagem inovadora que combina exercícios de resistência cardiovascular com treinamento de força, proporcionando resultados extraordinários para quem busca uma transformação completa. Essa metodologia holística considera que o desenvolvimento muscular e a queima calórica podem ocorrer simultaneamente, desde que haja uma periodização adequada.

Além disso, é importante destacar que a personalização do treinamento é fundamental. Cada indivíduo possui características fisiológicas específicas, e um programa genérico dificilmente proporcionará os resultados desejados. Portanto, uma avaliação criteriosa do seu nível atual, dos seus objetivos e da sua disponibilidade semanal será determinante para o sucesso da sua jornada.

Nossa equipe de profissionais especializados desenvolverá um plano totalmente customizado, considerando suas particularidades e potencializando seu desempenho. Você receberá orientações detalhadas sobre cada exercício, além de acompanhamento contínuo para garantir sua evolução constante.

Não perca essa oportunidade de transformar sua vida e alcançar a sua melhor versão. Clique aqui e comece sua jornada rumo ao corpo que você sempre desejou.
```

**Validação: REPROVADO.** 5 alvos bloqueantes (palavras curtas 44%, palavras longas 8,3%, futuro sintético 3x, concreto por abstração 0,6:1, desvio 4,3) e 7 itens de blocklist (você já se perguntou, é importante destacar, além disso, portanto, clique aqui, comece sua jornada, jornada 2x).

## Primeira tentativa de adaptação

Passou em 14 de 16, mas reprovou no tamanho médio da frase: 10,6 palavras contra o alvo de 13 a 20, com 62% das frases abaixo de 10 palavras.

O erro foi over-correção. Ao fugir do registro escrito eu piquei tudo, e ritmo uniformemente curto é tão artificial quanto ritmo uniformemente longo. É a armadilha descrita na passada 4 de `reference/06-craft.md`.

Correção: juntar frases curtas consecutivas em blocos de entrega mais longos, preservando as viradas curtas nos pontos de mudança de direção.

## Depois (aprovado)

```
Você treina há meses e continua igual no espelho.
Você faz cardio, faz musculação, e continua igual no espelho.
Você já tentou de tudo, e continua igual no espelho.
Pois é. E o problema não é você.
Deixa eu te falar o que tá acontecendo aí: você faz corrida e musculação, só que soltos, cada um por conta, sem um conversar com o outro.
Ah, mas se eu faço os dois, então tá certo.
Calma.
Se você errar a dose, a corrida come o músculo que você levantou na academia, e o teu corpo fica murcho em vez de ficar definido.
É por isso que tem gente que corre todo dia, treina pesado, e continua sem definição nenhuma.
O treino híbrido resolve isso.
Resumidamente: você faz corrida e musculação numa ordem e numa carga em que uma puxa a outra, no lugar de uma comer a outra.
Aí o teu corpo para de escolher e passa a queimar gordura e ganhar músculo ao mesmo tempo.
Mas a dose muda de pessoa pra pessoa, e depende do teu nível, do teu objetivo e da rotina que você aguenta cumprir.
Por isso eu monto o teu plano na mão.
Você responde umas perguntas rápidas, eu olho o que cabe na tua semana, e em menos de 24 horas o teu treino chega no teu WhatsApp com vídeo de cada exercício.
Sem dieta maluca, sem remédio e sem morar na academia.
Toca no botão aqui embaixo e responde as perguntas que hoje mesmo o teu treino já sai.
Bora!
```

**Validação: APROVADO, 15 de 16.** Único aviso: 58% de frases com até 10 palavras contra a faixa de 20% a 50%. Aviso e não falha porque o corpus de origem varia de 0% a 70% nessa métrica.

## O que este exemplo prova

1. O validador reprova texto de modelo com diagnóstico específico, não com "está genérico".
2. Ele reprova também o rascunho de quem está usando a skill, inclusive quando o erro é o oposto do esperado.
3. O ciclo é rascunho, validação, correção dirigida pelo relatório, revalidação.

## Sinalizado nesta peça

O roteiro adaptado não tem prova. O texto de origem também não tinha, e a skill não inventa nome, número nem prazo. Numa entrega real, isso vira uma linha de SINALIZADO pedindo o caso de aluno com nome e número.
