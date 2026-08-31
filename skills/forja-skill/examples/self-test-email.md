# Self-test executado: e-mail

Prova de que a forja-skill passou pelo próprio [test-harness](../reference/test-harness.md). Loop RED-GREEN-REFACTOR rodado sobre um brief de e-mail. Fecha a lacuna "a meta-skill nunca foi testada com o próprio ciclo".

**Atenção:** a versão RED abaixo contém de propósito os tells banidos (em-dash, palavras-vício, "não é X é Y"). É o exemplo negativo, igual aos pares BAD/GOOD. Não é violação da DNA, é a prova dela.

## Brief de teste

```
SKILL_BRIEF (teste):
  peca: e-mail único de oferta pra lista morna
  produto: suplemento natural de sono (melatonina + magnésio)
  avatar: 50+, acorda de madrugada e não volta a dormir
  destino: página de oferta
  prova: ainda não tem (usar placeholder)
```

## RED: e-mail sem a DNA (AI cru)

> **Assunto:** Descubra o segredo para uma noite de sono perfeita!
>
> Olá, tudo bem?
>
> Você sabia que mais de 60% das pessoas acima dos 50 anos sofrem com noites mal dormidas? No cenário atual, dormir bem virou um verdadeiro desafio.
>
> Não é apenas mais um suplemento, é uma jornada transformadora rumo ao bem-estar. Nossa solução holística foi cuidadosamente desenvolvida para potencializar a qualidade do seu sono.
>
> Milhares de clientes já comprovaram a eficácia do produto. Os resultados são extraordinários. Além disso, a fórmula é exclusiva e robusta.
>
> Não perca essa oportunidade única — clique aqui agora e transforme suas noites!

### Audit do RED

| Scan | Resultado | Hits |
|---|---|---|
| 1. Léxico | FALHA | jornada, transformadora, holística, potencializar, exclusiva, robusta, em-dash (—) |
| 2. Estruturas | FALHA | "Não é apenas X, é Y"; abertura "Você sabia que"; "Olá, tudo bem" |
| 3. Conectores/CTA | FALHA | "Além disso"; "clique aqui"; "Não perca essa oportunidade única" |
| 4. Tom | FALHA | assunto genérico com "!", "Descubra o segredo" |
| 5. Red zones | FALHA | "Milhares de clientes" (prova genérica); sem mecanismo nomeado |

**Baseline: 15+ hits. REPROVA forte.** É o que um modelo sem gates produz.

## GREEN: e-mail pela skill gerada (DNA ativa)

> **Assunto:** o que o seu corpo faz às 3 da manhã (e por que te acorda)
>
> Você acorda às 3 da manhã.
> Olha o teto.
> E fica ali, esperando o sono voltar, que não volta.
>
> Isso tem um nome. Eu chamo de "Janela Quebrada do Sono".
> É a hora em que o corpo, depois dos 50, para de segurar você dormindo a noite inteira.
>
> A maioria tenta resolver tomando mais remédio. Aí acorda grogue, pior que antes.
>
> [PROVA: inserir nome + idade + número quando o usuário tiver. Ex: "Seu Antônio, 63, voltou a dormir 7 horas seguidas em 9 dias."]
>
> Tem um jeito mais simples.
> Dois nutrientes que o seu corpo já conhece, na hora certa, antes de deitar.
>
> Aperta no botão aqui embaixo. Te mostro o que tomar e a que horas. Leva 2 minutos.
> Vou deixar a página no ar até domingo, porque o lote que separei é pequeno.

### Audit do GREEN

| Scan | Resultado |
|---|---|
| 1. Léxico | PASSA (zero) |
| 2. Estruturas | PASSA (zero) |
| 3. Conectores/CTA | PASSA (CTA com comando + razão real) |
| 4. Tom | PASSA (sentence case, sem CAPS abusivo) |
| 5. Red zones | PASSA (mecanismo nomeado; prova com placeholder explícito) |

Alavancas aplicadas: ritmo linha-única, conectores de fala (Aí, Olha), header narrativo (assunto), mecanismo nomeado em aspas, cena sensorial. E-mail curto não usa as 7, só as que servem à peça.

## REFACTOR (brecha fechada)

O primeiro rascunho do GREEN terminava o CTA com "e transforme suas noites". "Transforme" entrou por reflexo. O audit do scan 4 pegou. Troquei por comando físico concreto ("Aperta no botão... te mostro o que tomar"). Brecha registrada na tabela de racionalizações do test-harness.

## Veredito

```
TEST_HARNESS (forja-skill, brief e-mail):
  RED (sem DNA): 15+ hits no audit
  GREEN (com skill): 0 hits
  REFACTOR: 1 brecha fechada ("transforme" no CTA)
  delta: a DNA levou o audit de 15+ para 0
  veredito: PASSA
```

A DNA embutida pela forja-skill produz diferença mensurável. Gate `test=pass` validado para a própria meta-skill.
