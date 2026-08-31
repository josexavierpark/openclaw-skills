# Fase 01: Intake (coleta do brief mínimo)

Coleta o brief em **5 perguntas com opções numeradas**, uma por vez, sequencial, espera resposta antes da próxima. Output final: `BRIEF_LOCK` declarado.

## Princípio

Input mínimo + opções comportamentais (não dados demográficos genéricos). Cada pergunta filtra o caminho da geração.

## As 5 perguntas

### Pergunta 1: Nicho e produto

Apresente assim:

```
Pra começar, em qual nicho o anúncio vai rodar? Escolhe uma:

1. Saúde (emagrecimento, sono, energia, dor, micose, audição, ronco, saúde feminina, etc.)
2. Renda extra / negócio online / IA / dropshipping
3. Investimentos / day trade / criptomoedas / score de crédito
4. Relacionamentos / reconquista / sedução / autoconhecimento
5. Espiritualidade / manifestação
6. Educação (inglês, concurso, estudos)
7. Outro: descreve em uma frase

Depois me passa: nome do produto + o que o VSL/aula entrega em UMA frase.
```

### Pergunta 2: Destino do clique

```
Pra onde o anúncio vai mandar?

1. VSL longa (mais de 5 min)
2. VSL curta (até 5 min, mini-VSL)
3. Quiz (3-5 perguntas, página de resultado)
4. Teste de avaliação / diagnóstico
5. Página de captura simples (lead magnet pra e-mail)
6. Outro: descreve
```

**Nota interna:** essa resposta define como o copy vai REFERIR ao destino:
- VSL longa → "essa apresentação", "esse vídeo", "essa explicação completa"
- VSL curta → "esse vídeo rápido", "essa demonstração"
- Quiz → "esse teste", "essa avaliação rápida", "esse diagnóstico"
- Captura → "esse material", "esse passo a passo"

NUNCA: "esse curso", "esse treinamento", "esse programa", "essa aula paga".

### Pergunta 3: Onde o avatar está agora

```
Descreve o avatar pelo COMPORTAMENTO dele agora, não dados demográficos. Escolhe a opção mais próxima:

1. Nunca tentou nada nesse nicho, mas o problema apareceu recentemente
2. Tentou 1-2 soluções óbvias e desistiu rápido
3. Já tentou muita coisa e nada funcionou, está cético com promessas
4. É especialista no nicho mas frustrado com plateau / falta de resultado
5. Já é cliente de algum concorrente, não está satisfeito
6. Outro: descreve em uma frase comportamental

Depois me passa idade aproximada + gênero (homem/mulher/misto).
```

### Pergunta 4: Formato do anúncio

```
Qual formato vai rodar?

1. Copy longa de feed (Facebook/Instagram, texto corrido, 400+ palavras)
2. Copy curta de feed (até 3 parágrafos, até 200 palavras)
3. Roteiro de vídeo curto (15-30 segundos, Reels/Stories/TikTok)
4. Roteiro de vídeo médio (60-90 segundos)
5. Roteiro de vídeo longo (3-5 minutos, mini-VSL como anúncio)
6. Carrossel (copy por card)
7. Outro: descreve
```

### Pergunta 5: Mecanismo único / nome chiclete (opcional)

```
Por último: o produto já tem um nome próprio pro método? Tipo "Truque do Arroz", "Protocolo das 5 Janelas", "Hack de 7 Segundos"?

1. Sim: [me passa o nome]
2. Ainda não tem (vou sugerir 3 nomes na hora de escrever, se fizer sentido pra peça)
3. Não quero usar nome chiclete nessa peça
```

## Por que NÃO perguntamos adversário externo no intake

Forçar adversário em todo brief gera copy repetitiva (sempre abrindo nomeando vilão). O adversário é recurso opcional. Quando o brief pede ou o exemplar do swipe sugere, aparece naturalmente. Está descrito em `disguise.md` como vocabulário interno, não como pergunta obrigatória.

## Output: BRIEF_LOCK

Ao final, declare assim:

```
BRIEF_LOCK:
  nicho: [valor]
  subnicho: [se identificável]
  produto: [valor]
  entrega_vsl: [o que o destino entrega em 1 frase]
  destino: [tipo + como chamar no copy]
  avatar_comportamento: [opção escolhida + idade + gênero]
  formato: [valor]
  mecanismo: [nome se existe / "sugerir 3" / "sem nome"]
  
Confirma se está certo antes de eu seguir pra busca no swipe?
```

## Regras de calibragem

- Se o aluno responder vago ("é pra saúde"), peça mais especificidade. Saúde tem subnichos muito diferentes (emagrecimento ≠ ronco ≠ audição ≠ micose).
- Se o aluno der opção 7/outro, transforme a resposta livre em tag descritiva (minúsculas, hífen).
- Se ele já mandar todas as respostas em um único bloco, valide cada uma e declare BRIEF_LOCK direto.
- Se ele pedir pra você sugerir o avatar, NÃO chute. Peça os comportamentos primeiro. Avatar genérico = copy genérica.

## Anti-padrões no intake

- Não peça avatar por "idade, gênero, renda" como dados demográficos. Peça por comportamento atual.
- Não peça "dor e sonho" do avatar. Isso vem do exemplar do swipe + nicho.
- Não peça tom. Tom vem do exemplar selecionado.
- Não peça oferta detalhada. A oferta no copy é gratuita (VSL/quiz).
- Não peça depoimentos. Não vamos usar nomes específicos a não ser que o aluno mande.
