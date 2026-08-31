# Fase 08: Audit (varredura técnica binária)

Não é review qualitativo (isso é o critique). É **scan binário** contra padrões detectáveis.

## Princípio

Critique = "o quanto está bom". Audit = "passou ou não passou". Sem cinza. Sem nota. Ocorrência presente = falha + reescrita do trecho.

## Procedimento

### Passo 1: Pegue o copy gerado (corpo + hook escolhido)

### Passo 2: Rode os 5 scans

#### Scan 1: Léxico (palavras banidas)
Procure palavra por palavra:

**Verbos banidos:**
mergulhar, alavancar, fomentar, desbloquear, desvendar, elevar, otimizar, capacitar, transformar (vago), revolucionar, enhar, navegar (figurativo), embarcar, abraçar, propelir, prosperar (CTA), florescer (CTA), maximizar, agilizar

**Adjetivos banidos:**
robusto, abrangente, fluido, multifacetado, holístico, vibrante, intrincado, pivotal, primordial, matizado, dinâmico (vago), inovador (vago), de ponta, vanguardista, transformador (vago), inestimável, incrível (vago), fantástico (vago), revolucionário (vago), extraordinário (vago), grandioso, impressionante, comendável, paramount, sem precedentes, exclusivo (vazio), único (vazio), premium (vazio), excelente

**Substantivos banidos:**
tapeçaria, panorama (figurado), jornada, ecossistema, paradigma, sinergia, catalisador, divisor de águas, mosaico (figurado), testemunho (figurado), plêtora, infinidade, alma (do negócio), labirinto (figurado), enigma, metamorfose, cadinho, símbolo, fabric (tecido figurado)

**Conectivos banidos (Tier-1, smoking gun):**
outrossim, ademais, vale ressaltar, é importante destacar, cabe destacar, é importante notar, é importante observar, em essência, em última análise, em conclusão, em suma, dito isso, nesse sentido, dessa forma, naturalmente, efetivamente, consequentemente, posteriormente, ao fim e ao cabo, no fim do dia

**Jargão marketing/negócios:**
scalable, disruptive, agile, frictionless, bandwidth, touchpoint, granular, alignment, ideation, stakeholder, framework (vago), thought leadership, low-hanging fruit, deep dive, move the needle, quick win, pain point, actionable insights, deliverables, investimento (substituindo "preço")

**Resultado do scan 1:**
```
Léxico — [X ocorrências]:
- "outrossim" em movimento 2, frase "Outrossim, vale destacar..."
- "jornada" em movimento 5, frase "comece sua jornada..."
- [...]
```

Se X > 0: **AUDIT FALHA**. Reescreva cada ocorrência.

#### Scan 2: Estruturas banidas

Procure por padrão:

**Construções proibidas:**
- "Não é X, é Y" (qualquer variação)
- "Não X. Não Y. É Z." (paralelismo triplo negativo)
- "Isso não é X. É Y." (antítese micro)
- "Esse [substantivo] tem nome:"
- "Esse [X] existe. Funciona."
- "Você nunca ouviu falar nisso. E é exatamente..."
- "A verdade que ninguém te conta"
- "Você não vai acreditar..."
- "É um passo" / "É só um passo"
- "E aí vem aquela conclusão que dói:"
- "Não é teoria."
- "A notícia é simples:"

**Estruturas retóricas IA:**
- Pergunta retórica genérica de abertura ("Você já se sentiu...", "Você sabia que...")
- Tríade paralela forçada (3 adjetivos)
- Bullets simétricos com bold + dois pontos como padrão
- Meta-comentário de abertura ("Neste anúncio, vou te mostrar...")
- Frase final de reafirmação ("E é por isso que X importa")
- Sandwich (afirmar + ressalvar + reafirmar)
- Repetição paralela seca ("Não é sorte. Não é herança. Não é família rica.")

**Pontuação banida:**
- Em-dash (—) em qualquer posição (use vírgula, ponto, dois-pontos, parênteses)
- Semicolons conectando cláusulas simples (use ponto ou conjunção)
- Pontuação metronômica em frases-bumbas ("X. Y. Z. W." 4+ vezes seguidas)

**Formatação banida em copy:**
- Title Case em headlines PT-BR (use sentence case)
- Vírgula antes do "e" (Oxford comma)
- Bold em palavras-chave aleatórias dentro de prosa
- Headers H2/H3 em copy curta (<800 palavras)

**Anatomia banida:**
- Falsa Agência (objetos como sujeitos humanos: "A estratégia percebeu uma nova tendência")
- Variação elegante (troca de sinônimos toda vez que sujeito aparece)
- Substituição de cópula ("serves as", "marks", "represents" em vez de "é")
- Modificadores -ing/gerúndio empilhados no final da frase

**Resultado do scan 2:**
```
Estruturas — [X ocorrências]:
- Em-dash no movimento 3, parágrafo "Esta estratégia — quando bem aplicada — é decisiva"
- "Não é X, é Y" no hook, "Não é só ferramenta, é transformação"
- [...]
```

Se X > 0: **AUDIT FALHA**.

#### Scan 3: Tom (tells quantificáveis)

**Hedging crônico:**
Conte ocorrências de: "pode ser", "talvez", "em geral", "muitas vezes", "muitos especialistas dizem", "alguns afirmam", "geralmente", "frequentemente", "pode acontecer".

Threshold: ≤1 a cada 200 palavras. Se exceder, falha.

**Neutralidade compulsória:**
Procure: "ambos os lados", "depende do contexto", "por um lado X, por outro Y", "há diferentes perspectivas".

Threshold: zero ocorrências em copy DR. Se >0, falha.

**Politeness excessivo:**
Procure: "Excelente pergunta", "Adorei a ideia", "Que ótimo briefing", "Que ideia maravilhosa", "Com certeza", "Certamente".

Threshold: zero. Se >0, falha.

**Otimismo de catálogo (adjetivos hype sem dado):**
Procure adjetivos superlativos sem âncora numérica: "incrível", "fantástico", "extraordinário", "revolucionário", "transformador", "impressionante", "espetacular".

Threshold: zero adjetivo hype sem dado. Se aparece adjetivo seguido de promessa não-quantificada, falha.

**Ausência de opinião forte:**
Lê o copy de ponta a ponta. Pergunta: ele toma partido? Tem postura? Confronta alguma crença?

Threshold: SIM em pelo menos 1 momento. Se NÃO em nenhum: falha (copy DR sem posição = artigo educacional).

**Resultado do scan 3:**
```
Tom — [PASSA / FALHA]:
- Hedging: X ocorrências em Y palavras (limit Z). [PASSA/FALHA]
- Neutralidade: X. [PASSA/FALHA]
- Politeness: X. [PASSA/FALHA]
- Otimismo de catálogo: X. [PASSA/FALHA]
- Opinião forte: [SIM/NÃO]. [PASSA/FALHA]
```

#### Scan 4: Indicadores quantitativos (thresholds)

Mensure objetivamente:

| Indicador | Meta | Como medir |
|---|---|---|
| Em-dash count | 0 (zero) | Regex `—` |
| Densidade de "você"/"te"/"seu" | ≥1 a cada 30 palavras | Contagem total |
| Burstiness (std dev em palavras/frase) | ≥7 | Calcular std dev |
| Tamanho médio de frase | ≤15 palavras | Contagem |
| Densidade de hedges | ≤1 a cada 200 palavras | Já feito no scan 3 |
| Densidade de adjetivos hype | 0 | Já feito no scan 3 |
| Densidade de conectivos acadêmicos | ≤1 por 500 palavras | Contagem |
| Bold em prosa | 0 (só em CTA button se houver) | Conta `**...**` |
| Headers em copy curta (<800 palavras) | 0 | Conta `^#` |
| Frases iniciando com "Não" em sequência | ≤2 | Análise sequencial |
| Mecanismo único nomeado | ≥1 (se aplicável) | Detecção de aspas + nome chiclete |
| Provas nominais (nome + número/situação) | ≥1 (se aplicável) | Contagem |
| CTAs com VVU (Verbo + Valor + Urgência) | ≥1 (no fim) | Análise da CTA |

**Resultado do scan 4:**
```
Indicadores — [PASSA / FALHA]:
- Em-dash: 0 ✓
- Densidade "você": 1/22 palavras (meta 1/30) ✓ acima da meta
- Burstiness: 8.2 (meta ≥7) ✓
- Frase média: 12.4 palavras (meta ≤15) ✓
- Bold em prosa: 0 ✓
- Mecanismo nomeado: 1 ("Protocolo das 5 Janelas") ✓
- Provas nominais: 2 ("Carlos 47 mecânico SP", "Ana 38 SP 4kg em 21 dias") ✓
- CTA VVU: 1 (no fim) ✓
```

#### Scan 5: Flags de alta confiança (red zones)

Qualquer flag presente = reescrever IMEDIATAMENTE:

- [ ] 3+ itens da blocklist em <400 palavras
- [ ] 2+ em-dashes por 250 palavras
- [ ] Qualquer "não é X, é Y" ou variação
- [ ] Hook sem específico nominal (sem número, sem nome, sem cena)
- [ ] Prova com "estudos mostram", "muitos clientes", "experts dizem" sem nome+número
- [ ] 2+ triplets paralelos em <500 palavras
- [ ] CTA que poderia servir pra outro produto qualquer
- [ ] Nenhuma objeção antecipada
- [ ] Texto parece artigo neutro (sem postura/opinião)
- [ ] Menção a valor monetário (preço, desconto, ROI absoluto)

**Resultado do scan 5:**
```
Red zones — [PASSA / FALHA]:
[Lista cada flag e marca ✓ ou ✗]
```

### Passo 3: Veredito final

```
═══════════════════════════════════════
AUDIT — VEREDITO: [PASSA / FALHA]

Scan 1 Léxico: [PASSA/FALHA] (X ocorrências)
Scan 2 Estruturas: [PASSA/FALHA] (Y ocorrências)
Scan 3 Tom: [PASSA/FALHA]
Scan 4 Indicadores: [PASSA/FALHA]
Scan 5 Red zones: [PASSA/FALHA]

═══════════════════════════════════════
TRECHOS QUE PRECISAM REESCRITA:

1. [Trecho atual com problema]
   → Sugestão: [trecho reescrito]

2. [Trecho atual]
   → Sugestão: [trecho reescrito]

[...]

═══════════════════════════════════════
```

## Regra de output

- Se PASSA em todos 5 scans: copy aprovado, liberar pro polish.
- Se FALHA em qualquer scan: lista cada ocorrência com linha/frase específica + sugestão de substituição. Reescreva os trechos. Rode audit de novo após reescrita.
- Audit não opina sobre qualidade subjetiva. Só passa/falha objetivamente detectável.

## Anti-padrões no próprio audit

### Audit suave demais
RUIM: "Tem alguns em-dashes mas tá ok."
BOM: "2 em-dashes detectados nos movimentos 3 e 6. AUDIT FALHA. Substitua por vírgula ou parênteses."

### Audit não detecta porque trecho está "implícito"
RUIM: "Não tem 'jornada' explícita mas a copy tem essa ideia."
BOM: audit só pega o que está LITERAL no texto. Implícito é critique, não audit.

### Audit recomenda sem reescrever
RUIM: "Tem 3 ocorrências de blocklist, refaça."
BOM: cada ocorrência com sugestão concreta de substituição.

### Audit ignora threshold
RUIM: "Hedging tá ok, só tem 4."
BOM: "Hedging: 4 ocorrências em 350 palavras = densidade 1/87. Excede meta de 1/200. FALHA."
