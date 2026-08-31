# Fase 1: Intake

5 perguntas com opções numeradas, uma por vez, espera resposta. Output: `BRIEF_LOCK`.

## Pergunta 1: Produto e promessa
```
Qual o produto e o que ele entrega em UMA frase?
E o nicho (saúde/nutra, renda extra, relacionamento, outro)?
```

## Pergunta 2: Temperatura da lista
```
Pra quem vai esse e-mail?
1. Lista fria (nunca comprou, pouco engajada)
2. Lista morna (já abriu/clicou, conhece você)
3. Lista quente (já comprou algo antes)
4. Carrinho abandonado / lead que não converteu
```

## Pergunta 3: Destino do clique
```
O e-mail manda pra onde?
1. VSL
2. Página de oferta direta
3. Quiz / diagnóstico
4. Conteúdo (artigo, vídeo) antes da oferta
```

## Pergunta 4: Objetivo deste e-mail
```
Qual o trabalho único deste e-mail?
1. Apresentar a oferta
2. Reabrir/criar desejo (sem vender ainda)
3. Quebrar uma objeção específica
4. Urgência / fechamento (último dia)
5. Reengajar quem sumiu
```

## Pergunta 5: Único ou sequência
```
1. E-mail único (broadcast)
2. Sequência de N e-mails (me diz quantos e o intervalo)
```

## Output: BRIEF_LOCK
```
BRIEF_LOCK:
  produto: [...]
  nicho: [...]
  temperatura: [...]
  destino: [tipo + como chamar no copy]
  objetivo: [...]
  formato: [único / sequência de N]

Confirma antes de eu escolher o ângulo?
```

## Calibragem
- Lista fria pede mais história e quebra de ceticismo. Lista quente pode ir direto à oferta.
- Sequência: cada e-mail tem UM objetivo. Não empilhe tudo no primeiro.
- Não peça avatar demográfico. A temperatura + objetivo já guiam o tom.
