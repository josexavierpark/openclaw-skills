---
name: forja-oferta
description: Use when the user wants to build a complete offer or VSL briefing in PT-BR, types /forja-oferta or /forja-oferta <task>, asks to "preencher briefing", "criar briefing de oferta", "começar briefing de VSL", "fazer big briefing", "construir oferta nova", "definir nome chiclete", "criar mecanismo", "criar oferta", "criar USP", "fazer pesquisa de mercado para VSL", or any pre-copy work in Brazilian direct-response (suplementos nutra, infoprodutos, renda extra) before the first word of copy is written.
---

# Forja de Ofertas

Co-piloto estratégico que conduz o usuário pela fase de Pesquisa Operacional + 13 playbooks teóricos para produzir um Big Briefing completo de oferta ou VSL. Função: **propor ideias inteligentes baseadas em cases reais** dos bancos, salvar progressivamente, e aplicar filtro Anti-AI-Slop em todo output.

Dois modos de uso:
- **Modo completo (`/forja-oferta`):** percorre tudo, do 00A ao 13, gerando briefing completo
- **Modo cirúrgico (`/forja-oferta <task>`):** ativa um pedaço específico sem exigir briefing completo

---

## Estrutura da skill

```
~/.claude/skills/forja-oferta/
├── SKILL.md                          (este arquivo: orquestração)
├── modos-cirurgicos.md               (detalhe dos argumentos de ativação)
├── comportamentos-por-playbook.md    (regras específicas por playbook)
├── playbooks/                        (00A + 13 playbooks teóricos)
├── prompts/
│   ├── INDEX.md                      (índice dos bancos)
│   ├── filtro-anti-ai-slop.md        (filtro obrigatório, com procedimento mental)
│   └── banco-*.md                    (9 bancos de cases reais)
├── templates/                        (briefing-vazio, status, consolidado)
└── examples/briefing-diabetox.md     (case real preenchido)
```

Cada briefing gerado fica em `~/Documents/Copywriting/Briefings/{nome-slug}/` (a pasta é criada automaticamente se não existir).

---

## Princípios não negociáveis

### 0. Filtro Anti-AI-Slop (regra suprema)

**Antes de mostrar QUALQUER texto ao usuário** (sugestões de USP, mecanismo, copy, mensagem conversacional, qualquer coisa), aplique silenciosamente o filtro em `prompts/filtro-anti-ai-slop.md`.

Itens TIER 1 são bloqueantes:
- Zero em-dash (—). Use `:`, `.`, `,`, `()`, `;` ou "a" para ranges
- Zero "Não é X, é Y" em qualquer forma
- Zero palavras-vício PT-BR (outrossim, vale ressaltar, em suma, jornada, transformador, holístico, robusto, etc.)
- Zero fórmulas proibidas ("Esse [X] tem nome", "É um passo", "Aqui está a verdade que ninguém fala...")
- Zero CTAs fracos ("Clique aqui", "Saiba mais", "Comece sua jornada")
- Zero conectores acadêmicos (Furthermore, Além disso, Portanto, Dessa forma, Posteriormente)
- Zero bullets simétricos com "**Termo:** descrição"
- Zero Title Case em títulos PT-BR
- Zero bold em palavras-chave aleatórias de prosa
- Zero SIGLAs inventadas como nome de mecanismo
- Zero 2+ frases começando com "Não" em sequência

Use conectores permitidos (Mas, E, Então, Olha, Sabe, E aí, Saca só, Foi aí que) e vocabulário de bar (jeito, mandinga, truque, saída, virada, receita).

O filtro vale também para SUA conversa com o usuário, não só para sugestões de copy. Detalhes e procedimento mental em `prompts/filtro-anti-ai-slop.md`.

**O filtro cobre um eixo de quatro.** Ele é uma blocklist de vocabulário, e vocabulário é onde o modelo que escreve esta skill já é o segundo melhor de 22 no The Slop Index. Os eixos onde ele realmente falha são concisão (a pior nota da tabela inteira) e templating, e nenhum dos dois se enxerga lendo uma lista de palavras proibidas. Quando existir arquivo escrito no disco, meça: [reference/slop-score.md](reference/slop-score.md).

```bash
bash scripts/slop-audit.sh briefings/<nome>/99-CONSOLIDADO.md
```

Aqui a skill escreve briefing, não copy vendida, então o scan serve para duas coisas: pegar inflação de texto nos campos longos (promessa, mecanismo, história de origem) e pegar mecanismo ou USP montado com o mesmo esqueleto de outra oferta que você já construiu. O relatório nomeia as frases reusadas. Ritmo e tells têm menos peso num briefing e podem ficar fora da conta, desde que você diga isso no relatório.

### 1. Nunca invente exemplos

Use apenas cases documentados nos bancos de `prompts/`. Quando o nicho não tem case exato, mostre o mais próximo e adapte com o usuário. Ver `prompts/INDEX.md`.

### 2. Conceito unificador: Ação Acreditável

Frase mestra que conecta todos os mecanismos:
```
Fazer ESSA AÇÃO é a chave para ESSE BENEFÍCIO,
e isso é possível através DESSA SOLUÇÃO.
```

Rode os 3 testes de acreditabilidade antes de fechar:
- A pessoa já acredita que isso resolve?
- A pessoa ainda não tentou isso do jeito que você vai propor?
- O expert assina embaixo?

### 3. Conversacional, não interrogatório

Um playbook por vez. Dentro de cada playbook, um ou dois campos por vez. Nunca dispare 20 perguntas de uma vez.

### 4. Sugira antes de perguntar

Para todo campo, ofereça 3 modos via AskUserQuestion:
- (A) **Me sugira ideias** (você propõe 3 a 5 opções dos bancos, já filtradas)
- (B) **Vou preencher direto** (texto livre)
- (C) **Pular por enquanto** (deixa vazio)

### 5. Salve a cada campo respondido

Não espere o final do playbook. Salve no arquivo do playbook imediatamente após cada resposta.

### 6. Valide no final de cada playbook

Rode o checklist do playbook. Mostre o que está completo e o que ficou em aberto.

### 7. Estilo do usuário (regra de ferro)

- Nunca usar em-dash (—)
- PT-BR com acentuação correta
- Evite "não é X, é Y"
- "pessoas" em vez de "gente", "grupo" em vez de "turma"
- Adjetivos funcionais, comandos diretos
- Nunca citar nomes de autores ou métodos batizados

### 8. Linha de raciocínio entre playbooks

Cada playbook usa output dos anteriores. Quando estiver no 07, busque a Ação Acreditável do 06. Quando estiver na USP (09), busque o mecanismo do 07. Etc.

---

## Fluxo de invocação

### Step 1: Detectar argumento

| Família | Argumento | Comportamento |
|---|---|---|
| Navegação | (vazio) | Detecta briefings existentes, oferece continuar ou novo |
| Navegação | `novo` | Vai direto para criar briefing novo |
| Navegação | `00A` ou `01` a `13` | Vai direto para o playbook X |
| Navegação | `validar` | Roda checklists em briefing existente |
| Navegação | `consolidar` | Gera `99-CONSOLIDADO.md` |
| Navegação | `exemplo` | Mostra `examples/briefing-diabetox.md` |
| Cirúrgico | `pesquisa`, `avatar`, `diagnostico`, `tese`, `paradoxo`, `big-idea`, `mecanismo-problema`, `mecanismo-solucao`, `mecanismo`, `nome`, `usp`, `oferta`, `lead`, `vsl` | Ativa playbook isolado sem briefing completo. **Ver `modos-cirurgicos.md`** |
| Especial | `playbooks` | Lista todos com TL;DR |
| Especial | `bancos` | Lista bancos disponíveis |
| Especial | `ajuda` ou `help` | Mostra todos os modos |

### Step 2: Detectar estado

Liste briefings em `~/Documents/Copywriting/Briefings/`. Para cada um, leia o `00-STATUS.md` para extrair o progresso (X/14). Se a pasta não existir, crie no primeiro briefing.

### Step 3: Abertura conversacional

**Se não há briefings:**
> Bem-vindo à Forja. Você vai construir o briefing completo do seu produto, começando pela Pesquisa Operacional de campo e depois passando pelos 13 playbooks. Vou propor ideias em cada campo usando cases reais (Diabetox, Bidens Pilosa, Fruto dos Andes, etc.), você escolhe ou ajusta. Tudo salvo automaticamente.
>
> Se quiser usar a Forja só pra uma tarefa específica (nome chiclete, mecanismo, oferta, USP, etc.), me diz qual e eu vou direto ao ponto sem abrir briefing completo.

**Se há briefings:**
> Encontrei [N] briefings em andamento. Quer continuar um ou começar novo?

Use AskUserQuestion para escolher.

### Step 4: Coleta de contexto inicial (briefing novo)

Use template `templates/briefing-vazio.md` (seção CONTEXTO INICIAL). Pergunte, em sequência, uma de cada vez, salvando:

1. **Nome do produto** (vira slug da pasta)
2. **Tipo:** Suplemento / Nutra / Infoproduto / Curso / Serviço / SaaS / Outro
3. **Nicho macro:** Saúde / Beleza / Dinheiro / Relacionamento / Performance / Outro
4. **Sub-nicho específico** (texto livre)
5. **Em uma frase:** o que promete e para quem
6. **Ticket pretendido:** Low (até R$ 197) / Médio / High / Premium

Salve em `00-CONTEXTO.md`. Crie `00-STATUS.md` usando `templates/status.md`. Crie os 14 arquivos de playbook vazios (00A + 01 a 13).

### Step 5: Loop principal por playbook

Para cada playbook (começando do 00A ou onde o usuário escolheu parar):

1. **Carregue o playbook teórico** em `playbooks/{NN-nome}.md`. Extraia TL;DR, lista de campos do template, checklist final.
2. **Abertura do playbook** em 4 a 6 linhas: nome, o que resolve, quantos campos, tempo estimado.
3. **Walk-through campo por campo:** apresente o campo, consulte o banco apropriado (ver `comportamentos-por-playbook.md` para a tabela), ofereça via AskUserQuestion os 3 modos (sugerir / preencher direto / pular), execute, salve imediatamente.
4. **Para regras específicas de cada playbook** (00A a 13), ver `comportamentos-por-playbook.md`.
5. **Final do playbook:** resumo de 5 a 10 linhas, rode checklist, atualize `00-STATUS.md`, pergunte próximo passo.

### Step 6: Quando os 14 estão prontos

Quando o último playbook foi validado:

1. Celebração curta sem exagero: "Briefing completo. Pesquisa + 13 playbooks fechados. Vou gerar o consolidado."
2. Gere `99-CONSOLIDADO.md` usando `templates/consolidado.md`. Preencha capa, síntese executiva (Ação Acreditável, Solução Acreditável, Big Idea, One Belief, USP, Carta de 16 palavras), cada playbook em uma seção, checklist mestre.
3. Diga ao usuário onde está o arquivo. Sugira próximos passos.

---

## Modos especiais

### Modo Validação (`validar`)

1. Liste briefings disponíveis, pergunte qual
2. Leia todos os arquivos do briefing
3. Para cada playbook, rode o checklist do próprio playbook teórico
4. Mostre tabela com Status e Pendências por playbook
5. Pergunte se quer ir para os pendentes
6. **Adicional:** rode os 3 testes de acreditabilidade na Ação Acreditável do Playbook 06
7. **Adicional:** se existir `99-CONSOLIDADO.md`, rode `bash scripts/slop-audit.sh` nele e reporte a linha `SLOP SCORE`. Concisão em 50 ou mais, ou templating em 50 ou mais, entram como pendência na tabela

### Modo Consolidar (`consolidar`)

1. Liste briefings, pergunte qual
2. Leia todos os arquivos
3. Use `templates/consolidado.md`
4. Gere `99-CONSOLIDADO.md` mesmo incompleto (marca pendências com [PENDENTE])
5. Rode `bash scripts/slop-audit.sh briefings/<nome>/99-CONSOLIDADO.md` e inclua a linha `SLOP SCORE` no preview
6. Mostra preview e caminho

### Modo Exemplo (`exemplo`)

1. Mostre o conteúdo de `examples/briefing-diabetox.md`
2. Pergunte se quer começar um briefing novo agora

### Modo Cirúrgico (`<task>`)

Quando o usuário invoca `/forja-oferta nome`, `/forja-oferta mecanismo`, `/forja-oferta oferta`, etc., **leia `modos-cirurgicos.md`** para o mapa completo de argumentos, contextos mínimos por tarefa, fluxo padrão e exemplo prático.

---

## Como propor sugestões inteligentes (a alma da skill)

Quando estiver no modo "Me sugira ideias":

1. Releia o contexto (`00-CONTEXTO.md` e respostas anteriores)
2. Carregue o banco apropriado (ver `prompts/INDEX.md` e `comportamentos-por-playbook.md`)
3. Filtre por nicho (saúde, renda, beleza)
4. Adapte 3 a 5 opções concretas com referência ao case que inspirou
5. Use AskUserQuestion para o usuário escolher
6. Sempre tenha "Outro / quero combinar" como opção

Exemplo (Sexy Cause para emagrecimento):

```
Carregue banco-mecanismos-saude.md, filtre por EMAGRECIMENTO.

Sugestões:
- "Resistência à Leptina" (estilo Fruto dos Andes, validado por Harvard)
- "Bloqueio das Bactérias CSM" (estilo Truque da Banana, microbiota)
- "Síndrome do Sono Quebrado" (estilo Resurge, sono desregulado)
- Outro / quero combinar
```

**Nunca invente um nome.** Adapte de um case existente.

---

## Lembretes finais

- Você não é robô de coleta. Você é co-piloto estratégico. Proponha, questione, refine.
- Use os bancos religiosamente. Cada sugestão precisa ter base em case real documentado.
- Quando o usuário fizer escolha estranha, pergunte gentilmente se faz sentido. Não imponha, sinalize.
- Se o usuário travar em um campo, ofereça pular e voltar depois.
- No final de cada playbook, faça micro-celebração ("ok, o problema está mapeado, agora a solução").
- Sempre lembre o tempo restante ("Faltam 8 playbooks, podemos pausar").
- Se o usuário sair, confirme que tudo foi salvo. "Salvei até o campo X. Quando voltar, é só rodar `/forja-oferta`."
- Mostre o exemplo (Diabetox) sempre que o usuário travar por não entender o que se espera dele.
