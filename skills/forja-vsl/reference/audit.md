# Fase 6: Audit (varredura binária: estrutura + DNA anti-AI-slop)

> Função: scan binário, passa ou falha. Não é review qualitativo (isso é a Fase 5, critique).
> Entrada: o roteiro completo da VSL (9 blocos) já escrito na ordem middle-out.
> Saída: veredito por scan + lista de trechos a reescrever com sugestão concreta.
> Princípio: ocorrência presente = falha do scan + reescrita do trecho. Sem cinza, sem nota.

## Como usar

Critique mede "o quanto está bom". Audit mede "passou ou não passou". O audit só pega o que está LITERAL no texto; o implícito vira critique. Duas partes: PARTE A audita estrutura (9 blocos, handoffs, ordem de produção, mecanismo e prova); PARTE B audita o DNA anti-AI-slop (em-dash, léxico, oposição binária, tom, indicadores). O audit só PASSA se as duas passarem inteiras. A blocklist está EMBUTIDA aqui; não dependa de fonte externa.

---

## PARTE A: scans estruturais (específicos de VSL)

### A1: Presença e ordem dos 9 blocos

Confira que os 9 blocos estão presentes e na ordem de leitura 1 a 9:

1. Lead, 2. Background Story, 3. Emotional Story, 4. Discovery Story, 5. Mecanismo do Problema, 6. Mecanismo da Solução, 7. Product Build Up, 8. Oferta, 9. Close.

- Bloco ausente sem registro: FALHA. Um bloco pode ser fundido ou cortado, mas só se a nota explicar por quê (ex.: "Background e Discovery fundidos: o porta-voz descobre o mecanismo na própria pele"). Fusão ou ausência sem explicação na seção NOTAS: FALHA.
- Blocos fora de ordem (ex.: Oferta antes do Product Build Up): FALHA.

### A2: Handoffs (as três fronteiras que não podem saltar)

Cada handoff é uma costura. Se o leitor sente um pulo, falha.

- **05 para 06:** a Ação Acreditável (a causa raiz, o que a pessoa faz de errado sem saber) vira a Solução Acreditável (a forma superior de agir). O mecanismo da solução nasce direto do mecanismo do problema, sem buraco lógico. Bloco 6 com ideia que não responde ao problema do bloco 5: FALHA.
- **07 para 08:** o nome do produto sai do Product Build Up e abre a oferta, aparecendo pela primeira vez no fim do bloco 7 como gatilho de virada. Oferta abrindo sem o nome ter sido revelado no build up, ou nome vazado antes do bloco 7: FALHA.
- **08 para 09:** o primeiro CTA é a fronteira. O bloco 8 termina no primeiro chamado para ação (preço ancorado mais comando); o Close empilha garantia, escassez e FAQ a partir dele. Sem CTA marcando a passagem, ou Close que repete a oferta em vez de fechar: FALHA.

### A3: Produto não citado antes do Product Build Up

Regra dura: o nome do produto aparece pela primeira vez no bloco 7. Os blocos 1 a 6 vendem a ideia, nunca o produto.

- Procure o nome do produto (e variações: marca, "o método", "o programa", "o app") nos blocos 1 a 6. Qualquer menção antes do Product Build Up: FALHA.
- A Lead (bloco 1) tem que estar 100% livre de menção a produto. Lead é trailer da ideia, não do produto. Menção de produto na Lead: FALHA crítica.

### A4: Ordem de produção middle-out

O audit não vê a ordem em que foi escrito, mas vê os sintomas de quando a ordem foi furada. A ordem correta é: mecanismos primeiro (05 e 06 juntos), depois oferta e close, depois histórias, lead por último.

- Sintoma de lead escrita cedo demais: a Lead promete uma virada que os mecanismos não entregam, ou usa um nome de mecanismo diferente do que aparece nos blocos 5 e 6. Incoerência entre a promessa da Lead e a tese: FALHA.
- Sintoma de histórias antes da tese: o porta-voz descobre algo que não é o mecanismo do bloco 6. Discovery Story que aponta para outra solução: FALHA.

### A5: Mecanismo com nome chiclete e prova específica

- **Nome chiclete:** o mecanismo (problema e solução) tem nome sensorial concreto de 2 a 4 palavras (ex.: "gatilho da gordura noturna", "porta dos fundos do metabolismo"). Sigla inventada ("ative o QH3X", "o fator ZX-7") ou nome abstrato sem ancoragem física: FALHA.
- **Prova específica:** toda prova tem nome mais idade ou situação mais número quebrado (ex.: "Cláudia, 47, professora em Belo Horizonte, 6,8 kg em 9 semanas"). Prova genérica ("muitos alunos", "estudos mostram", "vários relatos") sem nome e número: FALHA.
- **Calibragem:** muita prova onde a afirmação é inacreditável, nenhuma onde é óbvia. Prova empilhada sobre obviedade, ou afirmação inacreditável sem lastro: FALHA.

---

## PARTE B: scans de DNA anti-AI-slop (blocklist embutida e autossuficiente)

### B1: Em-dash (tolerância zero)

Regex: `—`. Meta: 0 (zero), em qualquer posição. Substitua por vírgula, ponto, dois-pontos, parênteses, ponto e vírgula, reticências, ou "a" em intervalos. Qualquer ocorrência: FALHA.

### B2: Léxico banido

Procure palavra por palavra. Cada ocorrência é uma falha e exige reescrita.

**Verbos banidos:** mergulhar (figurado), alavancar, fomentar, desbloquear, desvendar, desnudar, revelar (teatral), elevar, otimizar, maximizar, capacitar, empoderar, potencializar, transformar (vago), revolucionar, navegar (figurado), embarcar, abraçar (figurado), propelir, impulsionar (vago), prosperar (CTA), florescer (CTA), agilizar, enxugar (jargão), aprimorar, ressoar, ecoar, alinhar, garantir (burocrático), enfatizar, reverberar, destrinchar, explorar (abertura "vamos explorar"), descobrir (CTA "descubra como").

**Adjetivos banidos:** robusto, abrangente, completo (vazio), integral, fluido (sem atrito), multifacetado, holístico, sistêmico, vibrante, pulsante, intrincado, pivotal, primordial, paramount, matizado, dinâmico (vago), inovador (vago), disruptivo, de ponta, vanguardista, estado da arte, transformador (vago), inestimável, imprescindível (vago), incrível (vago), fantástico (vago), revolucionário (vago), extraordinário (vago), grandioso, impressionante, espetacular, comendável, louvável, profundo (vago), sem precedentes, inigualável, incomparável, exclusivo (vazio), único (vazio), premium (vazio), excelente, essencial (vazio), vital (vazio).

**Substantivos banidos:** tapeçaria, mosaico (figurado), panorama (figurado), cenário (figurado "no cenário atual"), jornada, trajetória (figurado), ecossistema, paradigma, sinergia, catalisador, propulsor (figurado), divisor de águas, virada de chave (clichê), testemunho (figurado), atestado (figurado), plêtora, infinidade, vislumbre, interação (elevada), alma (do negócio), labirinto (figurado), enigma, metamorfose, cadinho, símbolo (figurado), tecido (figurado), farol (figurado), sinfonia (figurada), mapa do caminho (overuse), gabarito (só se virar muleta), pedra angular, alicerce (figurado).

**Conectivos banidos (smoking gun):** outrossim, ademais, vale ressaltar, vale lembrar, vale notar, é importante destacar, cabe destacar, é importante notar, é importante observar, em essência, no fundo (conclusivo), em última análise, no fim do dia, ao fim e ao cabo, em conclusão, concluindo, em suma, pra finalizar (de redação), dito isso, posto isso, nesse sentido, dessa forma, diante disso, sob essa ótica, naturalmente (doutoral), efetivamente, consequentemente, por conseguinte, posteriormente, subsequentemente, no que tange a, entretanto, todavia, contudo (formal), portanto (escolar), além disso (emenda), certamente, com certeza (politeness), de fato (enchimento), essencialmente.

**Jargão marketing/negócios:** escalável, disruptivo, ágil (jargão), sem atrito, capacidade ociosa, ponto de contato, granular, alinhamento, geração de ideias (jargão), parte interessada, framework (vago), liderança de pensamento, fruta no chão (low-hanging fruit), análise profunda (deep dive), gerar resultado (move the needle), vitória rápida, ponto de dor (pain point), insights acionáveis, entregáveis, investimento (substituindo "preço").

Registre cada ocorrência (ex.: `"outrossim" no bloco 4, frase "..."`). Se X > 0: FALHA. Reescreva cada uma.

### B3: Construção de oposição binária "X / Y" e parentes

Meta: 0. Procure por padrão (a estrutura de opor o que não é ao que é):

- "Não é X, é Y" e qualquer variação ("não é só X, é Y", "isso não é X, é Y").
- Paralelismo triplo negativo: "Não X. Não Y. É Z." (ex.: "Não é academia. Não é suplemento. É um protocolo.")
- Antítese micro: "Isso não é X. É Y." (ex.: "Isso não é azar. É estrutura.")
- "Esse [substantivo] tem nome:" usado como fórmula de revelação.
- "Esse [X] existe. Funciona."
- "Você nunca ouviu falar nisso. E é exatamente por isso que..."
- "É um passo." / "É só um passo." como fechamento.
- "E aí vem aquela conclusão que dói:".
- "A verdade que ninguém te conta." / "Você não vai acreditar...".

Qualquer uma destas: FALHA. Reescreva como afirmação direta do que a coisa É.

### B4: Estruturas e formatação banidas

- Pergunta retórica genérica de abertura ("Você já se sentiu...", "Você sabia que..."). Numa Lead, abrir In Media Res no problema, não com pergunta vazia.
- Tríade paralela forçada (3 adjetivos ou 3 itens só pela cadência). Listas de 2, 4, 5 e 1 são humanas.
- Modificadores em gerúndio empilhados no fim da frase ("...oferecendo energia, dando foco, criando disposição").
- Meta-comentário de abertura ("Neste vídeo, vou te mostrar..."). Framing de abertura pode; anúncio acadêmico do que vai fazer, não.
- Frase final que reafirma a tese ("e é por isso que isso importa"). Sandwich (afirmar, ressalvar, reafirmar).
- Falsa agência (objeto inanimado como sujeito humano: "o protocolo percebeu", "esse método pega você pela mão").
- Substituição de cópula ("serve como", "representa", "marca" em vez de "é"). Variação elegante (trocar o sinônimo do sujeito a cada menção).
- Ponto e vírgula ligando cláusulas simples (use ponto ou conjunção).
- Bold em palavras soltas na prosa do roteiro (roteiro falado não tem ênfase tipográfica; a ênfase é a palavra certa).
- Title Case em título PT-BR (use sentence case). Vírgula antes do "e" (Oxford comma). Aspas curvas em vez de retas.

Registre cada ocorrência (bloco + frase). Se X > 0: FALHA.

### B5: Tom (tells com threshold, calibrado para roteiro falado longo)

Uma VSL longa respira: o threshold é por densidade, não por frase isolada.

- **Hedging crônico:** "pode ser", "talvez", "em geral", "muitas vezes", "geralmente", "frequentemente", "alguns dizem", "muitos especialistas dizem". Threshold: no máximo 1 a cada 250 palavras. Acima: FALHA. (Um roteiro afirma. A dúvida só entra como objeção que o porta-voz já trata.)
- **Neutralidade compulsória:** "ambos os lados", "depende do contexto", "por um lado X, por outro Y", "há diferentes perspectivas". Threshold: 0. Acima: FALHA.
- **Politeness excessivo:** "excelente pergunta", "com certeza", "certamente", "fico feliz em", "espero ter ajudado". Threshold: 0. Acima: FALHA.
- **Otimismo de catálogo (adjetivo hype sem dado):** adjetivo superlativo seguido de promessa sem âncora numérica ("resultado incrível", "método revolucionário", "transformação extraordinária"). Threshold: 0. Cada adjetivo hype solto sem número ou cena: FALHA.
- **Postura forte:** o roteiro toma partido em algum momento? Confronta a crença velha da audiência (o que ela acha que é o problema)? Threshold: SIM em pelo menos 1 ponto (tipicamente no mecanismo do problema). Roteiro neutro de ponta a ponta: FALHA (vira aula, não venda).

### B6: Indicadores quantitativos (calibrados para roteiro falado longo)

Não force frase média curta como em copy de anúncio. Uma VSL alterna frases longas que constroem com frases curtas que batem. O que se mede é variação e ausência de tells, não brevidade.

| Indicador | Meta (VSL longa) | Como medir |
|---|---|---|
| Em-dash | 0 | Regex `—` |
| Densidade de "você"/"te"/"seu" | no mínimo 1 a cada 40 palavras | Contagem total (VSL conversa direto com 1 pessoa) |
| Burstiness (desvio padrão de palavras por frase) | no mínimo 8 | Roteiro falado oscila mais que copy escrita |
| Tamanho médio de frase | sem teto rígido; alerta só acima de 28 | Frase de respiro longa é normal na VSL; o que mata é tudo igual |
| Densidade de hedges | no máximo 1 a cada 250 palavras | Já medido em B5 |
| Adjetivos hype sem dado | 0 | Já medido em B5 |
| Conectivos acadêmicos | no máximo 1 a cada 600 palavras | Contagem de B2 |
| Bold em prosa do roteiro | 0 | Conta `**...**` no corpo falado |
| Frases iniciando com "Não" em sequência | no máximo 2 seguidas | Análise sequencial |
| Mecanismo nomeado (nome chiclete) | no mínimo 1 | Já medido em A5 |
| Provas nominais (nome + número quebrado) | no mínimo 1 (calibrado) | Já medido em A5 |
| Primeiro CTA com verbo + valor + comando físico | no mínimo 1 (fronteira 08 para 09) | Análise do CTA |

```
B6 Indicadores: [PASSA / FALHA]
- Em-dash: 0
- Densidade "você": 1/34 (meta 1/40)
- Burstiness: 9.1 (meta 8)
- Frase média: 17.2 (sem teto; pico isolado de 31 ok)
- Bold em prosa: 0
- Conectivos acadêmicos: 1 em 3.200 palavras
- Mecanismo nomeado: 1 ("porta dos fundos do metabolismo")
- Provas nominais: 3
- Primeiro CTA físico na fronteira 08/09: 1
```

---

## Veredito final

```
═══════════════════════════════════════
AUDIT VSL. VEREDITO: [PASSA / FALHA]

PARTE A (estrutura)
A1 Blocos presentes e em ordem: [PASSA / FALHA]
A2 Handoffs (05>06, 07>08, 08>09): [PASSA / FALHA]
A3 Produto só a partir do build up: [PASSA / FALHA]
A4 Ordem de produção middle-out: [PASSA / FALHA]
A5 Mecanismo chiclete e prova específica: [PASSA / FALHA]

PARTE B (DNA anti-AI-slop)
B1 Em-dash (zero): [PASSA / FALHA]
B2 Léxico banido: [PASSA / FALHA] (X ocorrências)
B3 Oposição binária X/Y: [PASSA / FALHA] (X ocorrências)
B4 Estruturas e formatação: [PASSA / FALHA] (X ocorrências)
B5 Tom: [PASSA / FALHA]
B6 Indicadores: [PASSA / FALHA]

═══════════════════════════════════════
TRECHOS QUE PRECISAM REESCRITA:

1. [Bloco, trecho atual com o problema]
   > Sugestão: [trecho reescrito]

2. [Bloco, trecho atual]
   > Sugestão: [trecho reescrito]

[...]
═══════════════════════════════════════
```

## Regra de output

- Passou nas duas partes inteiras: roteiro liberado para a Fase 7 (fluidez).
- Falhou em qualquer scan: liste cada ocorrência com bloco e frase específica mais a sugestão de substituição. Reescreva os trechos. Rode o audit de novo após a reescrita.
- O audit não opina sobre qualidade subjetiva (isso é critique). Só passa ou falha o que é detectável LITERALMENTE no texto.

## Anti-padrões no próprio audit

- **Suave demais.** Errado: "Tem uns em-dashes mas tá ok." Certo: "2 em-dashes nos blocos 3 e 6. FALHA. Trocar por vírgula ou parênteses."
- **Detectar o implícito.** O audit só pega o que está escrito. "A ideia de jornada está ali" é critique, não audit.
- **Recomendar sem reescrever.** Errado: "3 itens de blocklist, refaz." Certo: cada ocorrência com a substituição concreta.
- **Ignorar threshold.** Errado: "Hedging tá ok, só tem 5." Certo: "Hedging: 5 em 900 palavras = 1/180. Excede o limite 1/250. FALHA."
- **Tratar a VSL como anúncio.** Errado: marcar frase de 26 palavras como falha. Certo: a VSL respira; o que falha é a monotonia (burstiness baixa), não a frase longa isolada.
