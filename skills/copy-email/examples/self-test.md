# Self-test: copy-email

Loop RED-GREEN-REFACTOR rodado na entrega da skill. A versão RED contém de propósito os tells banidos (exemplo negativo).

## Brief de teste
```
BRIEF_LOCK (teste):
  produto: método de renda extra no automático
  nicho: renda extra / negócio online
  temperatura: lista morna
  destino: VSL
  objetivo: apresentar a oferta
  formato: e-mail único
```

## RED: e-mail sem a DNA

> **Assunto:** Transforme sua vida financeira hoje mesmo!
>
> Olá, tudo bem?
>
> Você já se perguntou por que algumas pessoas conseguem uma renda extra e outras não? No cenário atual, ter uma renda alternativa não é um luxo, é uma necessidade.
>
> Nosso método inovador foi cuidadosamente desenvolvido para empoderar você a alavancar seus resultados. Além disso, a estratégia é exclusiva e robusta.
>
> Milhares de alunos já transformaram suas jornadas — os resultados são extraordinários.
>
> Não perca essa oportunidade única, clique aqui e comece sua jornada agora!

### Audit do RED

| Scan | Resultado | Hits |
|---|---|---|
| 1. Léxico | FALHA | transforme, transformaram, empoderar, alavancar, exclusiva, robusta, jornada(s), em-dash (—) |
| 2. Estruturas | FALHA | "não é um luxo, é uma necessidade"; "Você já se perguntou"; "Olá, tudo bem" |
| 3. Conectores/CTA | FALHA | "Além disso"; "clique aqui"; "Não perca essa oportunidade única"; "comece sua jornada" |
| 4. Tom | FALHA | assunto com "!" e "Transforme sua vida" |
| 5. Red zones | FALHA | "Milhares de alunos" (prova genérica); sem mecanismo nomeado |

**Baseline: ~17 hits. REPROVA.**

## GREEN: e-mail pela copy-email (DNA ativa)

> **Assunto:** o print que eu não consigo parar de olhar (R$ 412 num sábado)
>
> Sábado de manhã. Eu ainda de pijama.
> O celular vibrou. R$ 412 tinham caído na conta enquanto eu dormia.
>
> E não foi sorte. Foi uma coisa que eu montei e batizei de "Caixa Silencioso".
> É um jeito de deixar uma engrenagem rodando no automático, que continua trabalhando mesmo quando você fecha o notebook.
>
> [PROVA: inserir nome + número quando tiver. Ex: "O Rodrigo, 38, motorista, fez os primeiros R$ 300 em 11 dias, mexendo nisso 40 minutos por noite."]
>
> Eu gravei um vídeo curto mostrando o Caixa Silencioso por dentro, passo a passo.
> Aperta no botão aqui embaixo pra assistir. São 9 minutos. Vou deixar no ar até domingo à noite, porque depois eu fecho a turma.

### Audit do GREEN

| Scan | Resultado |
|---|---|
| 1. Léxico | PASSA (zero) |
| 2. Estruturas | PASSA ("E não foi sorte" é uma frase, não antítese) |
| 3. Conectores/CTA | PASSA (1 CTA com comando + razão) |
| 4. Tom | PASSA (assunto minúsculo, sem "!") |
| 5. Red zones | PASSA (mecanismo nomeado; prova em placeholder) |

## REFACTOR (brecha fechada)

O primeiro rascunho do GREEN apresentava o mecanismo com "isso tem nome: Caixa Silencioso". O scan 2 pegou: é a fórmula-muleta proibida "Esse [X] tem nome:". Troquei por "batizei de 'Caixa Silencioso'", que nomeia sem a muleta. Brecha registrada.

## Veredito

```
TEST_HARNESS (copy-email, brief renda extra):
  RED (sem DNA): ~17 hits
  GREEN (com skill): 0 hits
  REFACTOR: 1 brecha ("isso tem nome:" -> "batizei de")
  veredito: PASSA
```
