# Fase 1: Intake (entrevistar para montar o quiz)

Coleta o brief do quiz que vamos construir. Mesmo quando o usuário cola um briefing pronto, você LÊ o briefing, preenche o que dá, e PERGUNTA só os buracos que faltam para o quiz vender. Um quiz fraco quase sempre nasce de um intake preguiçoso.

## Princípio

Perguntas com opções numeradas, uma por vez, espera resposta. Use o modo 3-vias: **sugiro** (proponho a resposta a partir do nicho e dos swipes) / **você responde** / **pula** (uso um placeholder explícito e sigo). Nunca despeje o quiz inteiro sem fechar o brief.

Aplique a DNA nas próprias perguntas: sem em-dash, sem clichê de IA, PT-BR acentuado.

## As 8 perguntas (adapte a ordem ao que o briefing já cobre)

### 1. Avatar e nicho
Quem é a pessoa que entra no quiz? Me dá idade, gênero, e o momento de vida em uma frase (ex: mulher 40+ que já tentou toda dieta e nada gruda). Se você não souber fechar o avatar, eu proponho a partir do nicho.

### 2. O resultado desejado (o que ela já quer e ninguém entregou)
Qual é o resultado que essa pessoa deseja e que as soluções atuais não deram? É o estado-fim que o quiz vai prometer revelar como alcançar.

### 3. O PROBLEMA que o quiz vai CRIAR
Esta é a pergunta central do método. O quiz não procura um problema, ele instala um. Qual a limitação invisível que vamos fazer a pessoa descobrir respondendo? (ex: "suas fibras profundas adormeceram", "parasitas roubando seus nutrientes", "seu metabolismo entrou em modo de resistência"). Se você não tem, eu proponho 2 a 3 mecanismos de problema a partir do nicho e dos swipes.

### 4. O mecanismo da solução (nome chiclete)
Como o seu produto resolve esse problema, e com que nome? Mecanismo nunca é sigla. É nome chiclete sensorial de 2 a 4 palavras (primeira concreta + segunda emocional). Se não tiver, eu crio 3 opções.

### 5. A oferta e o ticket
O que está sendo vendido no fim, por quanto, e em que plataforma (Hotmart, Kiwify, LastLink, Payt)? Tem order bump, garantia, bônus? Se o preço ainda não está definido, eu marco como [TICKET] e sigo.

### 6. A prova que você tem
Que prova real existe? Depoimento com nome e número, antes/depois, autoridade (médica, anos de prática), estudo, demonstração visual. Liste o que for verdadeiro. Sem prova inventada: o que faltar vira placeholder [PROVA: ...] para você preencher.

### 7. O destino depois do quiz
A página de resultado entrega para onde?
1. Mini-VSL (vídeo curto de 3 a 6 min) e depois página ou checkout. Posso já encadear a `forja-mini-vsl`.
2. VSL longa existente.
3. Página de vendas direta.
4. Agendamento de call / WhatsApp.

### 8. Tamanho e tom do quiz
1. Curto (5 a 9 perguntas), compra por impulso, ticket baixo.
2. Médio (10 a 16), o padrão para saúde/emagrecimento.
3. Longo (20+, com dados corporais e muita personalização), tipo Noom.
E o tom: leve com emoji, ou sóbrio e clínico (autoridade)?

## Perguntas-faca (faça mesmo com briefing completo)

Sempre cace estes buracos, porque são onde o quiz vaza:

- **A causa é a real?** O sintoma que o público enxerga costuma não ser a causa. Confirme que o problema que vamos criar é o que de fato trava a pessoa.
- **A promessa conflita com o histórico de fracasso?** Se o público já tentou e falhou mil vezes, "perder peso" soa furado. Vale mais "destravar o que te impede".
- **Onde está a posse negativa?** Quais 2 a 3 perguntas vão forçar o "eu sou / eu tenho"? Sem isso, o quiz vira pesquisa, não funil.
- **A medida (o filtro) está nomeada?** Por que a solução genérica não serve para ela ("só funciona se for personalizado para o seu caso")?

## Output: QUIZ_BRIEF

```
QUIZ_BRIEF:
  avatar: [idade, gênero, momento de vida]
  resultado_desejado: [...]
  problema_criado: [a limitação invisível]
  mecanismo_solucao: [nome chiclete em aspas]
  oferta: [produto + ticket + plataforma + bumps/garantia]
  prova: [lista real ou placeholders]
  destino: [mini-vsl / vsl / página / call]
  tamanho_tom: [curto/médio/longo + leve/clínico]
  swipes_referencia: [códigos QZ-XXX do mesmo nicho/mecânica]
  buracos_marcados: [placeholders que o usuário ainda vai preencher]

Confere antes de eu montar o quiz?
```

Espere a confirmação explícita. O gate `intake=pass` só vale depois dela. Se o usuário mandar "pode fazer", ainda assim mostre o QUIZ_BRIEF preenchido e os placeholders, para ele ver o que foi assumido.
