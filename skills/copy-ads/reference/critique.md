# Fase 07: Critique (scoring quantitativo)

Avalia o copy gerado contra 10 heurísticas, 0-4 cada, total 0-40. Não é review qualitativo solto. É tabela com nota.

## Princípio

A diferença entre copy mediano e copy que converte é mensurável. Esta fase quantifica. Scores reais ficam entre 18 e 34. Score abaixo de 22 = reescrita obrigatória. Score 35+ = excepcional.

## As 10 heurísticas

| # | Heurística | O que mede | Como pontuar |
|---|---|---|---|
| 1 | Disguise Score | Parece orgânico, não publicidade? | 0 = grita anúncio, 4 = passa por orgânico real |
| 2 | Hook | Passa nos 3 testes (Blob, Bar, Memória)? | 0 = falha nos 3, 4 = passa nos 3 com folga |
| 3 | Especificidade | Número quebrado, nome chiclete, situação concreta? | 0 = tudo abstrato, 4 = 3+ specifics ancorados |
| 4 | Adversário externo (quando usado) | Nomeado e específico? Se peça não usa adversário, pontua N/A e não conta no total | 0 = "o mercado", 4 = nome+sistema+mecanismo |
| 5 | Protagonismo do leitor | Leitor como herói, não vendedor? | 0 = "nós oferecemos", 4 = "você" direto em cada frase de valor |
| 6 | Ritmo | Varia frase curta/longa? Burstiness alta? | 0 = todas frases iguais, 4 = std dev >7 |
| 7 | Antecipação de objeção | Tem objeção tratada antes de virar barreira? | 0 = nenhuma objeção tratada, 4 = 2+ objeções neutralizadas naturalmente |
| 8 | CTA | Comando específico, razão pra agir agora, sem ser publicitário? | 0 = "clique aqui", 4 = comando + razão real + nomeação indireta |
| 9 | Ausência de menção a valor | Zero referência a preço/desconto? | 0 = menciona preço explícito, 4 = zero |
| 10 | Ausência de reflexos IA | Passou na blocklist? | 0 = 5+ itens, 4 = zero blocklist hits |

**Heurística 4** é condicional. Se a peça não usa adversário externo, marque "N/A" e calcule o total dividindo pelo número de heurísticas aplicáveis × 4 (proporcional).

## Procedimento

### Passo 1: Leia o copy gerado (corpo + hook escolhido)

### Passo 2: Pontue cada heurística

Use a tabela acima como guia. Justifique cada nota em 1 linha:

```
1. Disguise Score: 3/4 — passa em 3 dos 4 critérios (vocabulário OK, estrutura OK, CTA tarde, mas leitor reconhece "anúncio" no segundo parágrafo)
2. Hook: 4/4 — passa nos 3 testes com folga
3. Especificidade: 3/4 — 2 números quebrados (R$2.347, 29 dias), nome chiclete presente, falta 1 situação concreta no movimento 4
4. Adversário externo: N/A — peça não usa adversário
5. Protagonismo do leitor: 4/4 — "você" em todas as frases de valor
6. Ritmo: 3/4 — std dev em torno de 6, alguns parágrafos com frases muito uniformes no meio
7. Antecipação de objeção: 2/4 — só 1 objeção tratada (preço implícito), falta tratar "será que funciona pra mim?"
8. CTA: 4/4 — "aperta no botão verde aqui embaixo, te mando o vídeo agora, vou tirar do ar quinta" — comando + razão + nomeação indireta
9. Ausência de valor: 4/4 — zero menção a preço
10. Ausência de reflexos: 4/4 — zero blocklist
```

### Passo 3: Some o total

Heurísticas aplicáveis × 4 = máximo. Soma das notas = total.

Se heurística 4 está N/A: máximo = 36 (9 × 4). Calcule pontuação proporcional pra base 40 pra comparação justa.

### Passo 4: Bandas de qualidade

| Score (base 40) | Banda | Ação |
|---|---|---|
| 35-40 | Excepcional | Liberar pro aluno. Apenas refinamento opcional. |
| 30-34 | Pronto pra rodar | Liberar. Sugerir 1-2 melhorias específicas pra teste futuro. |
| 25-29 | OK mas pode melhorar | Liberar mas detalhar 3-4 melhorias prioritárias. |
| 20-24 | Marginal | Reescreva 1-2 movimentos antes de liberar. |
| <20 | Crítico | Reescreva do zero antes de liberar. |

## Red flags por persona

Além do scoring numérico, analise contra 3 personas:

### Persona 1: Cético com filtro ligado
Avatar que já comprou curso ruim antes. Lê copy procurando razão pra sair.

Red flags pra avaliar:
- Promessa sem âncora temporal? ("rapidamente", "em breve")
- Adversário ausente quando deveria estar?
- Abertura genérica?
- Prova sem nome próprio?

Se 2+ red flags presentes: marca como problemático pra essa persona.

### Persona 2: Primeiro contato com o produto
Não conhece o vendedor, sem contexto.

Red flags:
- Copy assume familiaridade ("como vocês já sabem")?
- Usa jargão interno sem explicar?
- CTA pressupõe confiança já estabelecida ("garante o seu como sempre")?

### Persona 3: Mobile em scroll rápido
Vê os primeiros 2-3 segundos. Provavelmente vê só a parte de cima do feed.

Red flags:
- Primeira frase fraca?
- Não quebra padrão visual/cinético?
- Benefício principal enterrado no terceiro parágrafo?
- Hook tem dependência da próxima frase pra fazer sentido?

## Saída do critique

```
═══════════════════════════════════════
SCORING (X/40)

[Tabela das 10 heurísticas com nota + justificativa de 1 linha cada]

Banda: [Excepcional / Pronto / OK / Marginal / Crítico]

═══════════════════════════════════════
RED FLAGS POR PERSONA

Cético com filtro: [lista de red flags ou "nenhum"]
Primeiro contato: [lista ou "nenhum"]
Mobile scroll rápido: [lista ou "nenhum"]

═══════════════════════════════════════
3 MELHORIAS PRIORITÁRIAS (em ordem de impacto)

1. [Melhoria específica com referência ao parágrafo/frase]
2. [Melhoria específica]
3. [Melhoria específica]

═══════════════════════════════════════
```

## Como calibrar pontuação

### Não inflar
A tendência é dar 4 em tudo pra agradar o aluno. Resista. Copy real de mercado tira média 28-32. Score 38+ é raro.

### Não punir excessivamente
Se um movimento está bom mas não impecável, é 3. Não é 2. Score 2 = problema real que prejudica conversão.

### Justifique cada nota
1 linha por nota mínimo. Sem justificativa, a nota não é confiável.

### Compare com referência
Quando em dúvida, compare o trecho com o exemplar do swipe que originou o blueprint. Se o exemplar entregue melhor naquela dimensão, é 4. Se entrega pior, é menor.

## Anti-padrões no critique

### Vagar nas justificativas
RUIM: "Hook bom, passa nos testes."
BOM: "Hook 4/4 — primeira frase tem cena específica + número quebrado (4kg em 21 dias). Passa nos 3 testes com folga."

### Esquecer de pontuar heurísticas N/A
RUIM: ignorar heurística 4 quando peça não usa adversário.
BOM: marcar "N/A" explicitamente + recalcular base.

### Não traduzir score em ação
RUIM: "Score 24/40."
BOM: "Score 24/40 — banda Marginal. Reescreva os movimentos 4 e 6 antes de liberar. Movimento 4 falta prova nominal específica, movimento 6 tem CTA publicitária."

### Pular red flags por persona
RUIM: só fazer scoring numérico.
BOM: red flags por 3 personas + scoring + 3 melhorias = pacote completo.
