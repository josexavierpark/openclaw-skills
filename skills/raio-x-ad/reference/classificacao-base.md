# Classificação base: nicho, subnicho, hook, mídia e CTA

Referência para o bloco "Classificação base" da seção 2 do relatório. É o que vem antes das 7 camadas, e o que dá nome ao arquivo final (`<AAAA-MM-DD>_<subnicho>_<slug-do-ad>.md`).

Nenhum campo aqui vira linha de banco de dados. A raio-x-ad só descreve.

---

## 1. Nicho (primeiro nível)

Duas famílias apenas.

**Saúde** inclui: emagrecimento, fitness, sono, energia, diabetes, hipertensão, libido, articulações, memória/cognição, saúde feminina, saúde masculina, longevidade, ansiedade física, dor crônica, suplementação, alimentação, queda capilar por causa interna, pele por causa dérmica.

**Diversos** inclui tudo que não cabe em saúde:

- Renda extra, negócio online, IA aplicada a negócios, dropshipping, marketing digital
- Investimentos, day trade, ações, criptomoedas, fundos
- Relacionamentos, reconquista, sedução
- Autoconhecimento, espiritualidade, manifestação, energia espiritual
- Educação, inglês rápido, concurso público, estudos
- Imóveis, financiamento, score de crédito, dívidas
- Carreira, produtividade, gestão do tempo
- Beleza (foco estético externo)
- Maternidade e infância, pet, culinária e confeitaria, artesanato

Quando ambíguo (ex: emagrecimento via método espiritual), decida pela **oferta**: o produto resolve um problema de saúde física? Saúde. Resolve um problema financeiro, espiritual, relacional ou de rotina? Diversos.

---

## 2. Subnicho (segundo nível)

Tag descritiva curta, em minúsculas, com hífen se composta. É ela que entra no nome do arquivo.

### Subnichos comuns em saúde

`emagrecimento` (genérico, sem segmentação por sexo), `emagrecimento-feminino`, `emagrecimento-masculino`, `sono`, `energia-disposicao`, `diabetes`, `hipertensao`, `libido-feminina`, `libido-masculina`, `articulacoes-dores`, `memoria-cognicao`, `alzheimer-demencia`, `longevidade`, `ansiedade-estresse`, `cabelo-queda`, `pele-rugas`, `suplementacao-geral`, `intestino-digestao`, `prostata`, `zumbido`, `visao`, `neuropatia`.

### Subnichos comuns em diversos

`renda-extra-ia`, `renda-extra-generica`, `negocio-online`, `dropshipping`, `marketing-digital`, `day-trade`, `acoes-fundos`, `criptomoedas`, `score-credito`, `imoveis-financiamento`, `reconquista`, `seducao-relacionamento`, `manifestacao`, `espiritualidade-geral`, `ingles-rapido`, `concurso-publico`, `produtividade`, `sono-infantil`, `confeitaria-lucrativa`, `pet`.

Se o anúncio não cabe em nenhum subnicho listado, **crie um novo** descritivo, na mesma convenção (minúsculas, hífen, duas palavras no máximo). Não force um subnicho aproximado só pra usar a lista: o nome do arquivo precisa dizer a verdade sobre o ad.

---

## 3. Hook exato

A **frase literal de abertura**: os primeiros 3 a 5 segundos, verbatim, entre aspas. É o que para o scroll, palavra por palavra. Não classificamos "tipo" de hook aqui, só a frase real. A anatomia visual do hook (text overlay, som, visual, vibe) fica na seção 1 do relatório.

- A frase falada ou escrita nos primeiros ~5s. Se a legenda na tela abrir diferente da fala, registre a que aparece primeiro e anote a outra.
- Verbatim. Se a transcrição tiver artefato óbvio do Whisper (ex: grafa "bombom" no lugar de "bumbum"), registre a frase corrigida e anote o artefato.
- Se o ad abre sem fala, registre o texto na tela como hook e marque `(sem áudio nos primeiros segundos)`.

Exemplos: `"Eu sou a elevação pélvica..."`, `"Bumbum de Monjaro, né?..."`.

---

## 4. Mídia: anúncio ou orgânico

Marca se o criativo é **anúncio pago** ou **conteúdo orgânico**. Muda como o exemplar se lê: anúncio tem CTA duro com link rastreável; orgânico empurra pra bio/engajamento.

| Valor | Como reconhece |
|---|---|
| Anúncio | Veio de biblioteca de anúncios (Meta Ads Library, TikTok Creative Center); rótulo "Patrocinado"/"Sponsored"; botão de CTA de plataforma (Saiba mais, Comprar, Cadastre-se, Enviar mensagem); copy de conversão direta com link |
| Orgânico | Postado no feed/Reels sem promoção paga; sem botão de anúncio; CTA tipo "link na bio", "comenta X", "salva", "me segue"; objetivo é alcance/seguidores |
| não-determinável | Sem como saber a origem |

Se o usuário informar a origem ("tirei da Ads Library"), use direto. Vídeo solto num arquivo local, sem contexto e sem CTA de plataforma, costuma ser `não-determinável`.

---

## 5. CTA exato

Captura o CTA **verbatim** mais o destino e o objetivo. Serve pra saber **como foi feito** (as palavras exatas, o botão, a urgência) e **pra quê** (o que pede e pra onde leva).

Convenção (uma linha):

`"<frase verbatim do CTA>" → <destino> (<objetivo>)`

- **frase verbatim:** o texto exato, sem reescrever.
- **destino:** VSL/página de vídeo, quiz, checkout, WhatsApp, app, link na bio, formulário de lead.
- **objetivo:** gerar venda, capturar lead, agendar call, instalar app, ganhar seguidor, levar pro grupo.

Exemplos:

- `"Clique no botão abaixo e garanta seu desconto" → checkout (gerar venda)`
- `"Faça o quiz gratuito e descubra seu tipo" → quiz (capturar lead)`
- `"Chama no WhatsApp que eu te explico" → WhatsApp (vender 1-a-1)`
- `"Link na bio pra ver o passo a passo" → link na bio (engajamento/tráfego)`

Se houver mais de um CTA, registre o principal e anote os secundários. Esta linha é o resumo; o detalhamento em 4 dimensões (destino nomeado, ação pedida, gatilho de urgência, onde aparece) fica no blueprint, em `movimentos-e-blocos.md`.

---

## 6. Regras de inferência das 7 camadas

Valem na hora de preencher a lista das 7 camadas na seção 2. Bancos de opções em `7-camadas.md`.

- **Estrutura Invisível (C1)** nunca é só uma tag. Registre `Nome | Hook → ... → CTA` com a sequência real observada.
- **Formato (C2)** e **Avatar (C5)** são visuais e a transcrição não entrega. Leia os frames e use `pistas-visuais.md`. Sem material visual, marque `não-determinável` em vez de chutar.
- **Ângulo (C3)** aceita combinação (`Contrarian + Mecanismo`). Liste todos os que operam.
- **Fatia (C4)** costuma ser indireta. Deduza pela situação de rotina retratada, não por declaração explícita.
- **Tema (C6)** vai em duas partes: Tipo de Tema (categoria) + tema concreto (com as palavras do ad).
- **Nível de Consciência (C7)** se lê pelo hook: curiosidade pura = 1-2; dor direta = 2-3; mecanismo ou contrarian = 3-4; oferta e preço = 4-5.
- Qualquer camada que o material não permita inferir vai como `não-determinável`. Havendo dúvida entre duas opções, registre a escolhida e anote a segunda entre parênteses.

### Não confundir Estrutura Invisível × Ângulo × Tema (erro comum)

Vários rótulos aparecem em MAIS DE UMA camada (Lista, Erro Comum, História Pessoal, The One Thing, Alerta Urgente, Conspiração, Mecanismo). Antes de marcar, pergunte qual camada o rótulo descreve:

- **Estrutura Invisível (C1) = a SEQUÊNCIA de blocos (o roteiro).** Pergunta: "qual a ordem dos blocos, do Hook ao CTA?". Ex: Estrutura "Lista" = Hook → opção fraca → opção fraca → opção forte → CTA.
- **Ângulo (C3) = o PONTO DE VISTA / enquadramento persuasivo.** Pergunta: "de que ângulo o argumento é vendido?". Ex: Ângulo "Lista" = enquadramento numerado ("5 erros", "3 ferramentas").
- **Tema (C6) = o ASSUNTO.** Pergunta: "sobre o quê é o anúncio?". Ex: Tema "Lista" = o assunto é uma lista de itens (lista de alimentos, lista de exercícios).

Teste: descrevendo a ORDEM dos blocos → Estrutura. O ENQUADRAMENTO → Ângulo. O ASSUNTO → Tema. O mesmo nome ("Lista") quase nunca é a mesma camada nas três.

Caso real (ad de glúteo): Estrutura = **The One Thing** (revela a única solução, a Sequência Ativadora), Tema = **Lista** (o assunto é uma lista de exercícios), Ângulo = **Mecanismo da Solução**. Não marque Estrutura = Lista só porque o ad menciona uma lista.

| Camada | O que decidir | Tipo |
|---|---|---|
| 1. Estrutura Invisível | Qual roteiro macro conduz do hook ao clique | uma opção + sequência |
| 2. Formato | Embalagem visual do criativo | uma opção (+ secundário) |
| 3. Ângulo | Ponto(s) de vista, podem ser combinados | uma ou mais |
| 4. Fatia de Público | Segmento específico que o ad mira | uma opção |
| 5. Avatar | Quem aparece na tela | uma opção |
| 6. Tema | Tipo de Tema + tema concreto | categoria + texto |
| 7. Nível de Consciência | Estágio Schwartz (1 a 5) | uma opção |
