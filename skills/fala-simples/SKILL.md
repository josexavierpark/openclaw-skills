---
name: fala-simples
description: "Use when the user wants to rewrite, adapt or write a video script (ad, short VSL, Reels) in a plain spoken register, or to audit how simple an existing script really is. Triggers in Portuguese: deixar o texto mais simples, escrever falado, adaptar pro tom simples, transformar em roteiro de vídeo, tirar o jeito de IA do texto, deixar mais conversado, medir a simplicidade do meu roteiro, fala-simples. Triggers in English: make this sound spoken, simplify this script, rewrite in plain talk, adapt to video script, audit script simplicity."
user-invocable: true
---

# fala-simples

Escreve e reescreve **roteiro de vídeo de resposta direta** no registro falado. O princípio inviolável: o estilo aqui tem número, não adjetivo, e nenhum roteiro sai sem passar pelo validador métrico.

Não escreve página de vendas, e-mail nem post. Só roteiro para ser falado em vídeo.

## O que a torna diferente de um prompt de estilo

Os alvos foram medidos num corpus real de 26 roteiros falados (6.310 palavras) e são verificados por script, não por impressão. "Escreva simples" é infalsificável; "desvio do tamanho da frase >= 5,5" não é.

A skill tem duas camadas: a **mecânica**, que é fixa e vale para qualquer nicho, e o **léxico**, que é trocável por nicho. Copiar as duas produz copy de finanças escrita como personal trainer.

## Restrições absolutas

Herdadas da DNA (`dna/dna-card.md`, carregada em toda invocação):

- Zero em-dash (—) e zero `--`. Use `:` `.` `,` `()` `;` ou "a" em ranges.
- Zero "não é X, é Y" em qualquer variante.
- Zero Tier-1 e Tier-2 (vale ressaltar, além disso, portanto, jornada, alavancar, transformador, clique aqui, comece sua jornada, você já se perguntou).
- Acentuação PT-BR norma culta, inclusive em contrações (tá, pra, tô).
- Prova sempre com nome, número ou prazo vindos do usuário. Nunca inventada.

Específicas desta skill:

- **Futuro sintético é proibido.** "Você vai receber", nunca "você receberá".
- **Abstração motivacional é proibida.** Jornada, mentalidade, disciplina, propósito, mindset, superação. Troque por coisa que se vê, se toca ou se mede.
- **Muleta de fala é proibida.** Zero "né?", "sabe?", "viu?", "tá?", "entendeu?" colados no fim da oração, e zero "ó" solto. Eles simulam oralidade sem obrigar a frase a mudar. Oralidade se ganha com interjeição (pô, cara, mano), chamada de atenção (olha, se liga, chega aí) e conectivo de fala (aí, então).
- **O hook é escrito por último**, depois do corpo pronto.
- **O hook não nomeia o produto nem cita preço**, salvo pedido explícito.

## Localização

- Spec e mecânica: `reference/`
- DNA completa: `dna/`
- Léxicos: `lexicos/*.json` (`fitness` destilado de corpus real, `generico` como piso, `_template` para clonar)
- Validador: `scripts/validar.py`
- Corpus de origem e a análise que gerou o spec: `~/Documents/Copywriting/Analises-Ads/VictorPareto-Swipe/`

## Gates de preflight

Antes de escrever, declare:

```
FALASIMPLES_PREFLIGHT: brief=pass modo=adaptar|criar|auditar lexico=<nome> spec=loaded mecanica=loaded dna=loaded validador=ok mutation=open
```

| Gate | Verificação |
|---|---|
| `brief` | `FALA_BRIEF` confirmado ([01-intake.md](reference/01-intake.md)). No modo `auditar`, basta o nicho |
| `modo` | Um dos três, declarado |
| `lexico` | Arquivo existe em `lexicos/`. Se caiu no `generico`, avise o usuário |
| `spec` | [02-spec.md](reference/02-spec.md) carregado |
| `mecanica` | [03-mecanica.md](reference/03-mecanica.md) carregado |
| `dna` | `dna/dna-card.md` lido |
| `validador` | `python3 scripts/validar.py --help` roda sem erro |
| `mutation` | Todos acima passaram |

## Workflow obrigatório

| Fase | Referência | O que faz |
|---|---|---|
| 1. Intake | [01-intake.md](reference/01-intake.md) | Define modo, nicho, duração e o que não pode sair. Output: `FALA_BRIEF` |
| 2. Spec | [02-spec.md](reference/02-spec.md) | Carrega os alvos e a lógica de calibração |
| 3. Mecânica | [03-mecanica.md](reference/03-mecanica.md) | As 12 regras que produzem os números |
| 4. Léxico | [04-lexico.md](reference/04-lexico.md) | Escolhe ou destila o vocabulário do nicho |
| 5. Arquitetura | [05-arquitetura.md](reference/05-arquitetura.md) | Hook, arco, dois mecanismos, CTA, fechamento |
| 6. Craft | [06-craft.md](reference/06-craft.md) | As 5 passadas. Hook por último |
| 7. Audit | [07-audit.md](reference/07-audit.md) | Validador + 14 scans de julgamento |
| 8. Diretrizes | [08-diretrizes.md](reference/08-diretrizes.md) | As 12 Diretrizes: o que virou alvo, o que virou scanner, o que foi rejeitado |

Ordem fixa. No modo `auditar`, pule 5 e 6.

## Como invocar

- **Sem argumento:** ofereça os três modos: `adaptar` (tenho um texto), `criar` (tenho um briefing), `auditar` (só medir).
- **Com texto colado:** modo `adaptar`. Pergunte só nicho, duração e invioláveis.
- **Com arquivo:** rode o validador primeiro e mostre o diagnóstico antes de propor a reescrita.
- **Parciais:** "só validar", "destilar léxico de [nicho]", "só o hook", "só o fechamento".

## Calibração de voz (BAD → GOOD)

**Futuro e registro**
- BAD: "Você receberá seu plano personalizado em até 24 horas."
- GOOD: "Em menos de 24 horas você vai receber o teu plano."

**Subordinação**
- BAD: "Como o treino é montado de acordo com o seu nível, você consegue evoluir sem se machucar."
- GOOD: "O treino é montado pro teu nível. Aí você evolui sem se machucar."

**Abstração**
- BAD: "Essa metodologia vai transformar sua jornada e destravar seu potencial."
- GOOD: "Em 60 dias você tira a camisa no rolê sem pensar duas vezes."

**Ritmo plano**
- BAD: "O treino combina corrida e musculação. Os dois trabalham juntos. O resultado aparece rápido."
- GOOD: "O treino junta corrida e musculação de um jeito que uma puxa a outra, em vez de uma comer a outra. Quer ver?"

**Objeção**
- BAD: "Muitas pessoas se perguntam se o método funciona para mulheres."
- GOOD: "Ah, mas isso só funciona pra homem? Claro que não, pô. Se liga na Morgana."

**Muleta x marcador de verdade**
- BAD: "Eu tinha umas gordurinhas nas costas, sabe?"
- GOOD: "E eu tinha umas gordurinhas nas costas."
- BAD: "Tá aí a resposta daquela pergunta do começo, né?"
- GOOD: "Então chega aí que eu vou te dar a resposta daquela pergunta do começo."

**Explicação**
- BAD: "O protocolo utiliza periodização não linear com foco em adaptação metabólica."
- GOOD: "Resumidamente: você faz corrida e musculação numa dose certa, pra uma complementar a outra."

**Fechamento**
- BAD: "Clique no link abaixo e comece sua transformação hoje mesmo!"
- GOOD: "Toca no botão aqui embaixo e responde umas perguntas rápidas que hoje o teu treino já chega. Bora!"

## Formato de saída

```
ROTEIRO
<uma frase por linha>

---
VALIDAÇÃO
<tabela do validar.py>

EXCEÇÕES
<alvo, motivo> ou "nenhuma"

SINALIZADO
<claims a conferir, provas a pedir> ou "nada"
```

## Princípios operacionais

- **Nunca entregue sem a validação anexa.** É ela que separa esta skill de um prompt.
- **Corrija o texto, nunca o alvo.** Afrouxar número para o rascunho passar destrói o único mecanismo honesto que a skill tem.
- **Marcador oral é tempero, não métrica.** O validador mede o piso. Passar do ponto vira paródia, e só o scan 13 do audit pega isso.
- **Nicho errado, léxico errado.** Antes de escrever fora de fitness, cheque se existe `lexicos/<nicho>.json`. Se não existe, ofereça destilar ([04-lexico.md](reference/04-lexico.md)) em vez de rodar no `generico` e entregar razão concreto/abstração apertada.
- Este registro é o oposto do estilo sóbrio de lead de VSL. Não aplique a skill em Lead sem o usuário pedir.
- A skill aplica a DNA nas próprias mensagens: sem em-dash, sem clichê de IA, PT-BR acentuado.
