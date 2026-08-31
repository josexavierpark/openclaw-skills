# Fase 1: Intake (entrevistar para montar a mini-VSL)

Coleta o brief da mini-VSL. Dois caminhos de entrada: o **handoff da forja-quiz-nhb** (a skill irmã entrega um pacote pronto) ou um **brief fresco** do usuário. Em ambos, pergunte os buracos antes de roteirizar. Mesmo com handoff, valide a Única Crença e a prova.

## Caminho A: veio handoff do quiz

Se o usuário colou um `HANDOFF_PARA_MINI_VSL`, leia e preencha o `MINIVSL_BRIEF` direto dele. Confirme só 3 coisas:
1. A **Única Crença** sugerida está afiada? (ação + desejo + solução)
2. O **destino**: página de vendas (oferta de ponte) ou checkout direto (oferta completa)?
3. A **prova** que entra no corpo: o que é real, o que vira placeholder?

## Caminho B: brief fresco

Perguntas com opções numeradas, uma por vez, modo 3-vias (sugiro / você responde / pula com placeholder). Aplique a DNA nas próprias perguntas.

### 1. Avatar e a promessa do quiz
Quem assiste, e o que o quiz/etapa anterior prometeu a essa pessoa? A Lead precisa ser congruente com isso. Se não houve quiz antes, qual a promessa de entrada?

### 2. O desejo final
Qual é o resultado que a pessoa quer? (o "[Alcançar o Desejo]" da Única Crença)

### 3. A Ação Acreditável
Qual ação a pessoa precisa fazer para chegar ao desejo? É "resolver um problema" (você tem X, precisa fazer Y) ou "agarrar uma oportunidade" (faça Y para conseguir Z)? Se não souber, eu proponho a partir do nicho.

### 4. A Solução Acreditável (o produto como mecanismo)
Como executar a ação, e qual o nome chiclete da solução/produto? A solução é a materialização do produto. Sem nome chiclete, eu crio 3.

### 5. A oferta e o ticket
Produto, preço, plataforma. Tem ancoragem (preço cheio de referência)? Garantia? Bônus? Order bump? Se for ponte para página, a oferta na VSL é curta; se for checkout, é completa.

### 6. A prova disponível
Depoimento com nome/idade/número, demonstração visual, estudo, autoridade, antes/depois. Lista o que é real. Regra de ouro: grandes afirmações precisam de grandes provas, e não se prova o que a pessoa já acredita. O que faltar vira [PROVA: ...].

### 7. Destino e duração
1. Página de vendas (oferta de ponte, ~3 a 4 min).
2. Checkout direto (oferta completa, ~5 a 6 min).
E o nível de inacreditabilidade do mecanismo (define quanta prova carregar).

## Output: MINIVSL_BRIEF

```
MINIVSL_BRIEF:
  avatar + promessa_do_quiz: [...]
  desejo_final: [...]
  acao_acreditavel: [...] (tipo: problema / oportunidade)
  solucao_acreditavel + nome_chiclete: [...]
  unica_crenca: Fazer [ação] é a chave para [desejo], e a melhor forma é com [solução].
  oferta: [produto + ticket + ancoragem + garantia + bumps]
  prova: [real + placeholders]
  destino: [página / checkout] + duração-alvo
  swipes_referencia: [códigos QZ-XXX do mesmo nicho/mecânica]

Confere antes de eu roteirizar?
```

Espere a confirmação. O gate `intake=pass` só vale depois dela. Se o usuário mandar "pode fazer", mostre o `MINIVSL_BRIEF` preenchido e os placeholders antes de roteirizar.
