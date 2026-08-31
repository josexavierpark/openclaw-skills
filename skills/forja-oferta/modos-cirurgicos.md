# Modos Cirúrgicos (ativação por tarefa)

Quando o usuário invoca `/forja-oferta <task>` (ex: `nome`, `mecanismo`, `oferta`), você opera em playbook isolado, sem abrir briefing completo.

## Princípios

1. Pergunte só o contexto mínimo que aquele playbook precisa.
2. Não force criação de briefing inteiro. Se o usuário quer só nome chiclete, entregue só nome chiclete.
3. Ofereça salvar ao final: "Quer salvar em briefing novo ou existente?"
4. Mantenha 100% das regras (Anti-AI-Slop, exemplos reais dos bancos, sem em-dash).
5. Mostre como o pedaço se conecta ao todo numa frase ao final: "Se quiser, posso continuar e cobrir [próximo playbook lógico]."

## Mapa de argumentos para playbooks

| Argumento | Tarefa | Playbook(s) |
|-----------|--------|-------------|
| `pesquisa` | Pesquisa operacional de campo | 00A |
| `avatar` | Avatar e nível de consciência | 01 |
| `diagnostico` | Dor, desejo, objeções, crenças | 02 |
| `tese` | Tese de marketing | 03 |
| `paradoxo` | Pergunta paradoxal e enigmas | 04 |
| `big-idea` ou `ideia` | Big Idea e One Belief | 05 |
| `mecanismo-problema` | Mecanismo do Problema + Ação Acreditável | 06 |
| `mecanismo-solucao` | Mecanismo da Solução + Solução Acreditável | 07 |
| `mecanismo` | Os dois mecanismos juntos | 06 + 07 |
| `nome` ou `nomes` | Nomes chicletes | 08 |
| `usp` | USP + Carta de 16 Palavras | 09 |
| `oferta` | Big Offer + 7 Perguntas | 10 + 11 |
| `lead` ou `vsl` | Estrutura de lead/VSL | 12 + 13 |

## Contextos mínimos por tarefa

### `pesquisa` (00A)
**Mínimo:** Big Nicho + sub-nicho + se já tem expert/produto definido.
**Saída:** dossiê de pesquisa (5 frentes + Fase de Decisão) com plano de ação prático.

### `avatar` (01)
**Mínimo:** Nicho + sub-nicho + ticket pretendido.
**Saída:** avatar real (demografia + psicografia + status atual/desejado) + nível de consciência + nível de sofisticação.

### `diagnostico` (02)
**Mínimo:** Avatar definido (ou peça resumo de 1 parágrafo).
**Saída:** 5 dores + 5 desejos + inimigo interno e externo + 4 objeções universais respondidas + 3 falsas soluções já tentadas.

### `tese` (03)
**Mínimo:** Nicho + avatar + 1 frase sobre o produto.
**Saída:** escolha entre causa raiz, solução superior ou combinação. Gradualização de crenças (7 a 10 passos). Use bancos de mecanismos (saúde ou renda) para sugerir teses com cases reais.

### `paradoxo` (04)
**Mínimo:** Tese ou Big Idea definida (ou peça em 1 frase).
**Saída:** 3 a 5 perguntas paradoxais com grupo, resultado e contexto desfavorável claros.

### `big-idea` (05)
**Mínimo:** Ação Acreditável + Solução Acreditável + desejo principal + nome do produto.
**Saída:** 3 a 5 versões de Big Idea + 3 versões de One Belief usando a fórmula:
```
[Ação Acreditável] é a chave para [desejo principal]
e isso só é possível através de [Solução Acreditável],
presente exclusivamente em [produto].
```
Mostre 5+ versões reais documentadas no banco para inspiração.

### `mecanismo-problema` (06)
**Mínimo:** Nicho + avatar + dor primária.
**Saída:** 5 camadas (bloqueio oculto, raiz, problema fundamental, crenças falsas, tentativas frustradas) + Ação Acreditável + sexy cause + metáfora visual + inimigo comum.
**Obrigatório:** rode os 3 testes de acreditabilidade.

### `mecanismo-solucao` (07)
**Mínimo:** Mecanismo do problema definido (ou peça resumo em 1 frase com a Ação Acreditável).
**Saída:** ingrediente protagonista + superestrutura de autoridade com history of origin + nutrientes ativos + Solução Acreditável + nome simbólico da nova oportunidade.

### `mecanismo` (06 + 07)
Roda os dois em sequência. Contexto mínimo: nicho + avatar + dor primária + produto.

### `nome` (08)
**Mínimo:** Nicho + tipo de produto + mecanismo principal (se houver) + público (uma frase).
**Saída:** lista de 10 nomes chicletes derivados de padrões reais do banco. Para cada, mostre o estilo (curioso, autoridade, combinado) e o case que inspirou. Aplique os 6 critérios e proponha um teste seco (Dry Test) no Meta Ads.

### `usp` (09)
**Mínimo:** Ação Acreditável + Solução Acreditável + prazo + 1 objeção principal.
**Saída:** 3 versões de USP (foco em promessa, mecanismo, objeção) + Carta de 16 Palavras condensada. Rode teste dos 2 segundos e teste do bar.

### `oferta` (10 + 11)
**Mínimo:** Produto + ticket pretendido + mecanismo da solução + objeções principais do avatar.
**Saída:** Big Offer com os 9 elementos + respostas às 7 perguntas da oferta + 3 ideias de bônus baseadas em vídeos virais do nicho + 3 opções de Reason Why.

### `lead` ou `vsl` (12 + 13)
**Mínimo:** Briefing parcial ou resumo de Ação Acreditável + Solução Acreditável + oferta.
**Saída:** estrutura completa de lead/VSL: 4 perguntas (dor urgente, explicar o problema, mostrar nova solução, ser acreditável) + 10 perguntas sequenciais com P4 = Ação Acreditável e P8 = Solução Acreditável.

## Fluxo padrão

```
1. Detectar argumento (ex: "nome")
2. Mostrar em 3 a 5 linhas: o que esse modo faz + contexto mínimo necessário
3. Coletar SÓ o contexto mínimo (AskUserQuestion ou perguntas diretas)
4. Carregar o playbook teórico + bancos relevantes
5. Executar (gerar sugestões, mostrar opções, refinar)
6. Entregar output limpo (filtro Anti-AI-Slop aplicado)
7. Oferecer:
   - Salvar em briefing existente (lista briefings)
   - Salvar em briefing novo (pede nome)
   - Só copiar e não salvar
   - Continuar para o próximo playbook lógico
```

## Exemplo prático: `/forja-oferta nome`

```
Você:
Modo cirúrgico: Nomes Chicletes (Playbook 08).
Vou gerar 10 nomes baseados em padrões reais (Diabetox, Truque da Banana, Pilates Asiático, etc.) e te ajudar a escolher o melhor pra teste seco.

Pra eu sugerir bem, preciso saber:
1. Qual o nicho?
2. Qual o tipo de produto (suplemento, curso, serviço)?
3. Em uma frase: o que ele faz e para quem?

[usuário responde]

Você:
Carregando banco-nomes-chicletes.md, filtrando por [nicho]...

Aqui estão 10 opções com o case real que inspirou cada uma:

1. [Nome] (estilo Diabetox, fusão problema + solução)
2. [Nome] (estilo Pilates Asiático, mecanismo geográfico)
...

Quer aplicar os 6 critérios de avaliação agora ou prefere já escolher 3 para teste seco no Meta Ads?
```
