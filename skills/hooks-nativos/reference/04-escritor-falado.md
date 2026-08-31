# Fase 4: Escritor de Hook Falado

## Objetivo

Gerar exatamente **3 variações de hook falado** por estrutura selecionada na Fase 3. Cada variação tem 1 a 4 linhas. Aplica princípios "Bem Direcionado" do método + alavancas de fluidez do disguise.

## Inputs

- Estrutura(s) selecionada(s) na Fase 3
- Diagnóstico de contraste da Fase 2 (expectativa, realidade, tipo)
- Brief da Fase 1 (tema, nicho, avatar)
- Consulta obrigatória a `references/metodo-7-estruturas.md` (templates verbatim por estrutura)
- Consulta a `references/disguise-alavancas.md` (alavancas de fluidez)
- Consulta a `references/exemplos-few-shot.md` (pares BAD/GOOD)
- Opcional: `references/banco-hooks-por-nicho.md`, `banco-hooks-vulnerabilidade.md`, `banco-hooks-virais.md` para inspiração

## Princípios obrigatórios (Bem Direcionado)

1. **Contexto na primeira frase.** O avatar precisa saber em 2 segundos se o vídeo é pra ele.
2. **Identificação direta com "você/seu/sua".** Não "eu/meu/minha" (a não ser que a estrutura seja vulnerabilidade declarada e o contraste exija).
3. **Destilação.** Use o mínimo de palavras possível. Cada palavra que não puxa o leitor pra próxima, corta.
4. **Clareza inequívoca.** Se a primeira frase pode ser interpretada de 2 jeitos, reescreva.

## Alavancas de fluidez (disguise: adaptadas pra hook curto)

- **Ritmo linha-única.** Cada frase ocupa uma linha. Quebra entre frases. Vide `disguise-alavancas.md` Alavanca 1.
- **Conectores conversacionais.** "Olha", "Sabe", "E aí", "Mas", "Saca só". Nunca "Outrossim", "Vale ressaltar", "Em conclusão".
- **Mecanismo nomeado quando aplicável.** Se a estrutura é Revelação de Segredo, Educacional ou Vidente e cabe um nome chiclete (2-4 palavras, primeira concreta + segunda emocional/identitária), use aspas + Title Case **só no nome do mecanismo**. Exemplos: "Janela Metabólica das 14h", "Truque do Aperto", "Brecha do MEI Silencioso".
- **Detalhe sensorial > adjetivo abstrato.** "Acordou 3 minutos antes do despertador" > "estava ansioso".
- **CAPS estratégico em 1-2 palavras emocionais.** Não em substantivos comuns nem em frases inteiras. Use com parcimônia.

## Templates por estrutura

Cada template é só um esqueleto. Adapte ao tema/avatar específico. Consulte os exemplos verbatim em `references/metodo-7-estruturas.md`.

### Vidente
> "Esse(a) <tema/objeto> vai mudar a forma como <avatar pluralizado> faz(em) <atividade> no futuro."

Adapte: substitua "vai mudar" por verbo sensorial se possível ("vai virar de cabeça pra baixo a forma como...").

### Experimentação
> "<Avatar singular> consegue <resultado contrário ao esperado> se fizer(em) só isso..."

Adapte: nomeie o que ele "consegue" de forma concreta.

### Educacional/Tutorial
> "Se você quer <resolver problema X>, usa o <Método Nomeado>."

Adapte: o método precisa ter nome chiclete entre aspas. Se não tem nome ainda, crie um na hora.

### Revelação de Segredo
> "Existe <coisa pouco conhecida> que <prova social de elite> usa(m), mas ninguém comenta."

Adapte: a prova social precisa ser específica e crível pro nicho.

### Contrário/Negativo
> "<Avatar pluralizado> perde(m) tempo demais com <crença comum>."
> ou
> "Você tá fazendo <coisa X> errado a vida toda."

Adapte: declare a crença oposta com convicção. Não suavize.

### Comparação
> "Esses são os <N> <opções> que <avatar plural> usa(m). Mas qual realmente entrega <resultado>?"

Adapte: mantenha 3-7 opções no máximo no escopo do hook.

### Pergunta
> "Por que <observação específica do nicho>?"

Adapte: a pergunta precisa ter resposta que o avatar quer saber. Pergunta vazia ("vocês já se perguntaram...") não conta.

### Choque Direto (modificador)
> "Olha isso aqui..." (antes de outra estrutura)
> "Vê esse <objeto>..."
> "Para tudo."

Use como primeira linha curta. Linha 2 entra com a estrutura principal.

## Aplicação por contraste

### Contraste declarado
- Nomeie a crença na primeira frase
- Inverta na segunda
- Pode usar "Se você acha que <crença>, espera..." como ponte

### Contraste implícito
- Vá direto na realidade
- Deixe o avatar inferir a crença oposta
- Funciona quando a realidade já é forte sozinha

## Output esperado

Imprima:

```
**Hooks falados gerados:**

### Estrutura 1: <nome>

**Variação 1:**
<1-4 linhas de hook>

**Variação 2:**
<1-4 linhas de hook>

**Variação 3:**
<1-4 linhas de hook>

### Estrutura 2: <nome> (se houver)

**Variação 1:**
...

[seguindo o mesmo padrão]

Seguindo pra Fase 5 (Escritor de Texto na Tela).
```

## Checkpoint

Esta fase **não pausa**. Avance direto pra Fase 5 com os hooks gerados.

## Restrições absolutas (replicadas do SKILL.md)

- Sem em-dash (—). Use vírgula, ponto, dois-pontos, parênteses.
- Sem "Não é X, é Y" nem variantes. Use afirmação direta.
- Sem as 5 construções retóricas proibidas (ver `references/antislop-5-construcoes.md`).
- Sem palavras da blocklist (ver `references/antislop-blocklist.md`). Em particular: "jornada", "mergulhar", "alavancar", "empoderar", "transformador", "outrossim".
- Acentuação correta em 100% dos outputs.

## Heurística de qualidade durante geração

Antes de soltar cada variação, pergunte-se:

1. Em 2 segundos lendo essa frase, o avatar sabe que o vídeo é pra ele? Se não, reescreva.
2. Existe pergunta sem resposta criada na cabeça do avatar? Se não, reescreva.
3. A primeira linha tem contraste (declarado ou implícito) ou só descreve algo? Se só descreve, reescreva.
4. As palavras são curtas e diretas? Se tem 3 sílabas onde cabe 2, simplifique.
5. Algum cacoete de IA escapou? Se sim, troque. (A Fase 6 vai pegar de qualquer jeito, mas auto-revisão aqui economiza ciclos.)

## Edge cases

| Situação | Como tratar |
|---|---|
| Estrutura é Contrário e o avatar está psicologicamente fechado | Comece com Choque Direto pra abrir o ouvido antes da inversão |
| Variação 2 saiu parecida demais com Variação 1 | Mude o ângulo: troque o sujeito, o tempo verbal, ou o gancho emocional |
| Tema técnico que exige termo jargão | Mantenha o jargão mas explique em 1 linha imediatamente depois |
| Avatar já é avançado no nicho | Suba o nível: use jargão sem explicar, foco no detalhe que diferencia avançado de iniciante |
