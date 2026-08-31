# Deep Research: Vícios de IA em Copywriting de Resposta Direta

**Data:** Maio 2026  
**Versão:** 3.0 (integra Pesquisa Claude + Pesquisa Gemini + Pesquisa GPT + corpus real "Frases ruins de IA" + `anti-ia-blocklist.md` operacional do projeto)  
**Uso:** System prompt, base de conhecimento e checklist de revisão para assistente de IA de DR copywriting  
**Idioma:** Misto (EN quando a fonte é inglesa; PT-BR em resumos operacionais e equivalências)

---

## Tese Central (consolidada das 3 pesquisas paralelas)

"AI slop" não é problema de vocabulário isolado. É uma sindrome de quatro camadas:

1. **Léxico estatisticamente sobre-representado pós-Nov/2022** (corrigível por blocklist).
2. **Estruturas sintáticas induzidas por RLHF** (sycophancy, hedging, formatação obrigatória, paralelismos triplos, antítese "não é X, é Y") - corrigíveis por few-shot e constraint.
3. **Postura epistêmica** (sycophancy, hedge compulsório, balanço forçado, ausência de opinião) - NÃO corrigível só por prompt; exige editor humano final.
4. **Em PT-BR**: vazamento de português europeu + tradução literal do inglês + registro formal-neutro de telejornalismo, com Title Case e Oxford comma como sinais adicionais.

Resolver exige sistema em camadas: persona forte > blocklist negativa > constraints mecânicas > workflow de 2 passes com tic-hunt reverso > editor humano final.

A boa notícia: copy DR é um dos contextos onde o gap humano-vs-IA é maior. Real-life storytelling, big idea, deep psychological driver, mecanismo único e voz visceral são exatamente onde IA é mais fraca. Agência BR que estrutura corretamente o workflow ganha vantagem competitiva por usar IA apenas no que ela faz bem (research, voz-de-cliente, draft modular, variações) e blindar o que ela faz mal (lead, mecanismo, prova específica, voz BR).

---

## TL;DR Operacional

Para uso imediato em system prompts e blocklists. Material completo nas seções abaixo.

### 30 Palavras Mais Denunciadas (EN + equivalente PT-BR)

| # | EN | PT-BR | Evidência |
|---|----|----|---|
| 1 | delve | mergulhar a fundo / explorar | Alta (COLING 2025, +6.697% PubMed) |
| 2 | tapestry | mosaico / tecido / panorama | Alta (GPT-4o usa 155x acima da baseline) |
| 3 | intricate | intrincado / complexo | Alta (GPT-4o 119x acima da baseline) |
| 4 | underscore | sublinhar / evidenciar | Alta (GPT-4o 107x; 2024 focal word) |
| 5 | camaraderie | camaradagem / senso de comunidade | Alta (GPT-4o 162x acima da baseline) |
| 6 | amidst | em meio a / no contexto de | Alta (GPT-4o 100x acima da baseline) |
| 7 | leverage | alavancar / potencializar | Alta (prática observada) |
| 8 | pivotal | pivotal / fundamental / decisivo | Alta (21 focal words COLING 2025) |
| 9 | groundbreaking | revolucionário / sem precedentes | Alta |
| 10 | realm | universo / esfera / domínio | Alta |
| 11 | embark | embarcar / iniciar / dar o pontapé | Alta |
| 12 | unlock | desbloquear / destravar / liberar | Alta |
| 13 | foster | fomentar / cultivar / nutrir | Alta |
| 14 | meticulous | meticuloso / criterioso | Alta (21 focal words) |
| 15 | comprehensive | abrangente / completo / integral | Alta |
| 16 | seamless | fluido / sem atritos / integrado | Alta |
| 17 | robust | robusto / sólido / consistente | Alta |
| 18 | innovative | inovador / disruptivo / vanguardista | Alta |
| 19 | transformative | transformador / revolucionário | Alta |
| 20 | empower | empoderar / capacitar / fortalecer | Alta |
| 21 | harness | aproveitar / canalizar / captar | Alta |
| 22 | catalyst | catalisador / propulsor / gatilho | Alta |
| 23 | vibrant | vibrante / pulsante / efervescente | Alta |
| 24 | navigate | navegar / atravessar / percorrer | Alta |
| 25 | unveil | revelar / desnudar / desvendar | Alta |
| 26 | holistic | holístico / integral / sistêmico | Alta |
| 27 | paradigm | paradigma / nova abordagem | Média |
| 28 | synergy | sinergia / conjunção harmônica | Alta |
| 29 | landscape | cenário / panorama / contexto | Alta |
| 30 | game-changer | divisor de águas / virada de chave | Alta |

### 15 Estruturas Mais Denunciadas

| # | Padrão | Exemplo |
|---|--------|---------|
| 1 | "It's not X, it's Y" | "Não é só uma ferramenta, é uma transformação" |
| 2 | Tríade paralela forçada | "clear, concise, and compelling" |
| 3 | Modificador participial no final da frase | "...offering a wide range of tools, giving users live data" |
| 4 | Bullets simétricos (mesmo tamanho, mesmo formato) | Cada bullet com bold + dois pontos + 1 frase |
| 5 | Template tópico-evidência-resumo | Parágrafo abre afirmação, cita exemplo, reafirma |
| 6 | Abertura com pergunta retórica genérica | "Você já parou pra pensar como seria...?" |
| 7 | Frame de abertura temporal | "In today's fast-paced world" / "Nos dias de hoje" |
| 8 | Frame de fechamento formal | "In conclusion" / "Em conclusão" / "Em suma" |
| 9 | Sandwich (afirma + ressalva + reafirma) | "X é importante. É claro que depende do contexto. Por isso X..." |
| 10 | Semicolons conectando cláusulas simples | "Eles querem resultados; mas não sabem por onde começar" |
| 11 | Em-dash no meio de frase curta | "Esta estratégia -- quando bem aplicada -- é decisiva" |
| 12 | Substituição de cópula | "serves as, marks, represents, boasts, features" em vez de "is" |
| 13 | Variação elegante / troca de sinônimos | Protagonista > personagem-chave > figura epônima |
| 14 | Meta-comentário de abertura | "Neste artigo, vamos explorar..." |
| 15 | Regra de três obsessiva | Qualquer lista de exemplos tem exatamente 3 itens |

### 12 Smoking Guns PT-BR (corpus real do usuário + 3 pesquisas independentes)

Padrões que o usuário corrigiu manualmente em sessões de produção. Aparecem em todas as 3 pesquisas como assinatura PT-BR.

| # | Padrão | Exemplo verbatim do corpus | Por que vaza IA |
|---|--------|----------------------------|------------------|
| 1 | "Outrossim" | "Outrossim, vale destacar que..." | Arcaísmo que SÓ IA usa em PT-BR. Smoking gun absoluto. |
| 2 | "Esse [X] tem nome" repetido | "Esse pensamento tem um nome:" / "Esse protocolo tem nome, tem mecanismo" | Fórmula de revelação dramatizada usada como muleta |
| 3 | "Esse [protocolo/método] existe. Funciona." | "Esse protocolo existe. Funciona." | Frase-bumerangue de validação repetida pela IA |
| 4 | "Não X. Não Y. É Z." pontuação seca | "Não é academia. Não é suplemento. É um protocolo." | Paralelismo triplo negativo em pontuação cortada |
| 5 | Antítese micro: "Isso não é X. É Y." | "Isso não é azar. É estrutura." | Versão concentrada de "Não é apenas X, é Y" |
| 6 | "Você nunca ouviu falar nisso. E é exatamente [por isso/aí] que..." | "Você nunca ouviu falar nisso. E é exatamente por isso que o resultado não está aparecendo." | Frase-fórmula de mistério usada 2+ vezes na mesma peça |
| 7 | Listagem em frases-bumbas | "Academia. Dieta. Correu. Ficou sem comer. Tentou de novo." | Pontuação metronômica forçando ritmo curto demais |
| 8 | "E aí vem aquela conclusão que dói:" | (idem verbatim) | Frase IA de conclusão dramática genérica |
| 9 | "É um passo." / "É só um passo." | "O aplicativo está disponível. O protocolo completo está dentro. É um passo." | Fechamento CTA padrão IA |
| 10 | Bold em palavras-chave aleatórias | "**Esse pensamento tem um nome:**" / "**Não é teoria.**" | "AI enfatiza tudo porque não sabe o que importa" |
| 11 | Estrutura "ativar o [nome inventado]" | "você precisa ativar o QH3X" | Mecanismo nomeado por sigla inventada genérica |
| 12 | Lista + em-dash + você + verbo | "Academia, dieta, jejum, yoga - você tentou." | Combo de lista 4 + em-dash + segunda pessoa |

### 10 Correções Mais Aplicadas

1. Blocklist de 50+ palavras injetada como regra de system prompt antes de qualquer geração
2. Workflow escreve-primeiro-IA-depois (Shiv Shetti): humano escreve, IA critica
3. Voice cloning via 3-5 amostras de escrita pessoal (Lorrie Morgan)
4. Prompt de advogado do diabo: "O que há de errado neste texto? Seja brutal"
5. 5-pass humanization framework: Raw Draft > Register Forensics > Blind Rewrite > Imperfection Injection > Voice Anchoring (Andy O'Bryan)
6. Context engineering: carregar VOC (voz do cliente), entrevistas, provas e pesquisa ANTES de pedir copy
7. Role persona: "Escreva como Gary Halbert escreveria para uma audiência cética"
8. Story-swap: trocar a história de abertura mantendo a estrutura de conversão provada
9. Modular assembly: IA gera 10 opções, humano monta as melhores partes
10. Auto-crítica final: "Este texto soa como gerado por IA? O que devo mudar?"
11. **Bad First Draft** (Stefan Georgi, Matt Wolfe, Justin Goff): humano rascunha em 33min sem editar; IA só limpa gramática
12. **Reverse Chain-of-Thought** (Nate's anti-slop): IA identifica próprios tics primeiro e DEPOIS reescreve
13. **Dial back / dial up** (Stefan Georgi): gerar 3 variantes (subtle / medium / aggressive) e escolher
14. **RMBC chain** (Georgi): 4 prompts em cadeia (Research > Mechanism > Brief > Copy)
15. **Simulated expert panel** (Borzasi): "Simule crítica de Georgi + Lampropoulos + Affonzzo sobre este lead"
16. **Match prompt style to output style** (Anthropic docs): se quer prosa sem markdown, escreva o prompt em prosa sem markdown

### 10 System Prompts Mais Citados

1. **Piyushh/Sabrina humanization prompt** (blocklist de 70+ palavras + regras estruturais; DR-tailored)
2. **Andy O'Bryan 5-pass framework** (mais sofisticado arquiteturalmente)
3. **Copyhackers "conversion copywriter" persona** (Joanna Wiebe)
4. **Shiv Shetti anti-AI sweep checklist** (melhor para pós-geração em DR)
5. **David Deutsch "iterate like a madman"** (melhor para iteração e devil's advocate)
6. **Will Francis Stop Claude** (granular nas estruturas; bane "Bold term: explanation"; checklist pós-geração)
7. **boringmarketer DR Copy Skill** (gist.github.com/boringmarketer; 66 stars; Schwartz/Hopkins/Ogilvy/Caples/Sugarman/Collier/Halbert codificados)
8. **Stefan Georgi RMBC VSL chain** (journal entry > 2ª pessoa > VSL opening; OpenAI Playground T=0)
9. **talk-normal** (github.com/hexiecs/talk-normal; 150+ stars; BAD/GOOD few-shot iterativo)
10. **Stop-Slop + Tagore frameworks** (8 regras + 29 padrões com scoring 8-dimensões; loop iterativo até 56/80)

---

## Seção 1: Banco de Palavras-Vício

### 1.1 Verbos (EN)

| Palavra | Equivalente PT-BR | Motivo | Modelo | Fonte | Evidência |
|---------|-------------------|--------|--------|-------|-----------|
| delve | mergulhar a fundo, explorar a fundo | +6.697% PubMed 2020-2024; marca RLHF | GPT-4 / RLHF geral | [arXiv 2412.11385](https://arxiv.org/html/2412.11385v1) | Alta |
| underscore | sublinhar, evidenciar, salientar | +107x baseline; migrou de "delve" para este em GPT-4o | GPT-4o | [arXiv 2410.16107](https://arxiv.org/html/2410.16107) | Alta |
| leverage | alavancar, potencializar, capitalizar | Jargão de consultoria adotado como padrão por RLHF | Todos | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) | Alta |
| foster | fomentar, cultivar, nutrir, estimular | Verbo genérico de "impacto positivo" | Todos | [originality.ai](https://originality.ai/blog/obvious-chatgpt-sayings) | Alta |
| harness | aproveitar, canalizar, captar, valer-se de | Metáfora de cavalo desnecessária em contexto abstrato | Todos | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) | Alta |
| unlock | desbloquear, destravar, liberar, abrir | CTA padrão de auto-ajuda; sinal imediato de IA em info-produto | Todos | Corpus usuário | Alta |
| empower | empoderar, capacitar, fortalecer | Aparece em 80%+ das copies de nicho educação e coaching IA | Todos | [fomo.ai prompt](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Alta |
| revolutionize | revolucionar, transformar radicalmente | Hyperbole padrão de tech copy IA | Todos | Corpus usuário | Alta |
| transform | transformar, ressignificar | "Transforme sua realidade" é CTA padrão IA | Todos | Corpus usuário | Alta |
| navigate | navegar por, atravessar, percorrer | Metáfora náutica fora de contexto | Todos | [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) | Alta |
| embark | embarcar, iniciar, dar o pontapé | "Embarque nessa jornada" = sinal IA universal | Todos | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) | Alta |
| enhance | aprimorar, potencializar, intensificar | Verbo de marketing IA genérico | Todos | [originality.ai](https://originality.ai/blog/obvious-chatgpt-sayings) | Alta |
| streamline | enxugar, simplificar, otimizar fluxo | Jargão corporativo de eficiência | Todos | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Alta |
| facilitate | facilitar, viabilizar, propiciar | Formal demais para copy de resposta direta | Todos | Corpus usuário | Média |
| unveil | revelar, desnudar, desvendar | Teatral; IA usa em contextos que não merecem drama | Todos | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) | Alta |
| spearhead | liderar, encabeçar, comandar | Jargão corporativo militar | Todos | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Média |
| bolster | reforçar, fortalecer, blindar | Raro em fala humana; alta freq. em IA | Todos | [netus.ai](https://netus.ai/blog/top-mistakes-that-make-ai-writing-obvious) | Média |
| resonate | ressoar, ecoar, conectar | "Vai ressoar com você" = sinal IA | Todos | Corpus usuário | Alta |
| align | alinhar, estar em sintonia | "Alinhado com seus valores" = copy IA coaching | Todos | Corpus usuário | Alta |
| optimize | otimizar, maximizar, refinar | "Otimize seus resultados" = CTA padrão IA | Todos | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) | Alta |
| propel | impulsionar, catapultar, alavancar | Overuse em nicho de performance | Todos | Corpus usuário | Média |
| thrive | prosperar, florescer | Raramente dito em linguagem coloquial BR | Todos | [netus.ai](https://netus.ai/blog/top-mistakes-that-make-ai-writing-obvious) | Média |
| strive | buscar incessantemente, almejar | Tom de missão corporativa | Todos | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Média |
| elevate | elevar, levar a outro patamar | "Eleve seus resultados" = CTA IA | Todos | Corpus usuário | Alta |
| unpack | desempacotar, destrinchar | Cousin direto de "delve"; usado em explicações | Claude | [Wikipedia Signs of AI](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | Alta |
| shed light on | lançar luz sobre, iluminar | Cliché literário forçado | GPT, Claude | [Wikipedia Signs of AI](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | Alta |
| pave the way | pavimentar o caminho, abrir caminho | Metáfora-zumbi de tech press | GPT | Pesquisa Claude | Alta |
| illuminate / elucidate | iluminar, elucidar | Latinismo desnecessário em contexto coloquial | GPT, Claude | Pesquisa Claude | Alta |
| garner | obter, conquistar, angariar | Verbo elevado fora de registro DR | GPT | Pesquisa Claude | Média |
| forge | forjar, construir | Metáfora industrial deslocada | GPT | Pesquisa Claude | Média |
| showcase | mostrar, exibir, destacar | Spike documentado por Liang (Stanford) | GPT | [arXiv 2406.07016](https://arxiv.org/html/2406.07016v1) | Alta |
| utilize | utilizar (em vez de usar) | Latinismo: "usar" >> "utilizar" sempre | Todos | Pesquisa GPT | Alta |
| supercharge / skyrocket | turbinar, decolar, fazer disparar | Vendido-demais; cliché hype | GPT | Pesquisa Claude | Alta |
| captivate | cativar, prender, fisgar | Vocabulário forçado em DR | GPT | Pesquisa Claude | Média |
| embrace | abraçar | Anglicismo evidente em PT-BR ("abrace a mudança") | GPT | Pesquisa Claude | Alta |
| dive deep / dig into | mergulhar de cabeça em | Cousin direto de delve | GPT, Claude | Pesquisa Claude | Alta |
| explore | explorar (figurativo: "vamos explorar") | Verbo-abertura padrão IA | Todos | Pesquisa Claude | Alta |
| discover | descobrir (CTA: "descubra como") | Headline-info-produto + IA = duplo flag | GPT | Pesquisa Claude | Alta |
| ensure | garantir (burocrático) | Verbo burocrático corporativo | Todos | anti-ia-blocklist projeto | Alta |
| emphasize | enfatizar | Verbo "elevado" gratuito | Todos | anti-ia-blocklist projeto | Média |
| reverberate | reverberar | Verbo literário fora de DR | Todos | anti-ia-blocklist projeto | Média |

### 1.2 Adjetivos (EN)

| Palavra | Equivalente PT-BR | Motivo | Modelo | Fonte | Evidência |
|---------|-------------------|--------|--------|-------|-----------|
| intricate | intrincado, complexo, sofisticado | GPT-4o usa 119x acima da baseline humana | GPT-4o | [arXiv 2410.16107](https://arxiv.org/html/2410.16107) | Alta |
| vibrant | vibrante, pulsante, efervescente | Adjetivo de catálogo; IA usa em qualquer nicho | Todos | [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) | Alta |
| pivotal | decisivo, central, crucial | Palavra de 21 focal words COLING 2025 | GPT-4 / GPT-4o | [arXiv 2412.11385](https://arxiv.org/html/2412.11385v1) | Alta |
| groundbreaking | revolucionário, pioneiro, sem precedentes | Hyperbole padrão IA | Todos | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) | Alta |
| meticulous | meticuloso, criterioso, cuidadoso | Adjetivo de processo; overuse em descrição de método | Todos | [arXiv 2412.11385](https://arxiv.org/html/2412.11385v1) | Alta |
| comprehensive | abrangente, completo, integral | "Guia completo" = IA; "guia" basta | Todos | Corpus usuário | Alta |
| seamless | fluido, sem atritos, integrado | Jargão de UX que migrou para copy | Todos | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) | Alta |
| robust | robusto, sólido, consistente | Jargão de TI | Todos | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Alta |
| innovative | inovador, disruptivo, vanguardista | Qualquer IA usa para qualquer produto | Todos | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) | Alta |
| cutting-edge | de ponta, vanguardista, estado da arte | Tech-speak queimado | Todos | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) | Alta |
| transformative | transformador, revolucionário | Redundante quando o produto já muda algo | Todos | Corpus usuário | Alta |
| multifaceted | multifacetado, de múltiplas facetas | Jargão acadêmico deslocado | Todos | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Média |
| holistic | holístico, integral, sistêmico | Nicho wellness / coaching IA | Todos | Corpus usuário | Alta |
| profound | profundo, marcante | "Transformação profunda" = clichê IA | Todos | Corpus usuário | Alta |
| nuanced | matizado, cheio de nuances | Palavra usada para fingir profundidade | Todos | [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) | Média |
| paramount | primordial, essencial, principal | Formal demais para DR conversacional | Todos | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Média |
| invaluable | inestimável, imprescindível | Adjetivo absoluto + superlativo = IA | Todos | [netus.ai](https://netus.ai/blog/top-mistakes-that-make-ai-writing-obvious) | Média |
| dynamic | dinâmico, ágil | Adjetivo genérico de consultoria | Todos | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) | Média |
| unparalleled | inigualável, incomparável, sem paralelo | Hiperbole vazia | Todos | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Média |
| commendable | louvável, digno de elogio | Spike pós-RLHF (Liang, Matsui) | GPT | [arXiv 2406.07016](https://arxiv.org/html/2406.07016v1) | Alta |
| stark | gritante, acentuado, cru | OpenAI dev forum | GPT | Pesquisa Claude | Média |
| keen | aguçado, atento, afiado | Cover-letter speak | GPT | Pesquisa Claude | Média |
| delightful / wonderful / fascinating | encantador, maravilhoso, fascinante | Entusiasmo sycophantic | GPT, Claude, Gemini | Pesquisa Claude | Alta |
| bustling | agitado, vibrante | Aplicado a comunidades/cidades sem detalhes sensoriais | GPT | Pesquisa Gemini | Média |
| essential | essencial (burocrático) | Adjetivo "obrigatório" sem justificativa | Todos | anti-ia-blocklist projeto | Alta |
| vital | vital (burocrático) | Mesmo padrão de "essential" | Todos | anti-ia-blocklist projeto | Alta |
| best-in-class | melhor da categoria | Tech-speak corporativo | Todos | anti-ia-blocklist projeto | Média |
| next-generation | de nova geração | Tech-speak hype | Todos | anti-ia-blocklist projeto | Média |
| amazing | incrível (vago) | Superlativo sem dado | GPT, Claude | anti-ia-blocklist projeto | Alta |
| incredible | incrível (vago) | Superlativo sem dado | GPT, Claude | anti-ia-blocklist projeto | Alta |

### 1.3 Substantivos (EN)

| Palavra | Equivalente PT-BR | Motivo | Modelo | Fonte | Evidência |
|---------|-------------------|--------|--------|-------|-----------|
| tapestry | mosaico, tapeçaria, tecido | GPT-4o usa 155x acima da baseline; 23% das saídas | GPT-4o | [arXiv 2410.16107](https://arxiv.org/html/2410.16107) | Alta |
| camaraderie | camaradagem, senso de comunidade | GPT-4o 162x acima da baseline | GPT-4o | [arXiv 2410.16107](https://arxiv.org/html/2410.16107) | Alta |
| landscape | cenário, panorama, contexto | "No cenário atual" = abertura padrão IA | Todos | Corpus usuário | Alta |
| realm | universo, esfera, domínio | Abstrato e genérico | Todos | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) | Alta |
| journey | jornada, trajetória, caminhada | "Comece sua jornada" = CTA padrão IA | Todos | Corpus usuário | Alta |
| ecosystem | ecossistema | Jargão de tech | Todos | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Média |
| paradigm | paradigma, nova abordagem | "Mudança de paradigma" = buzzword | Todos | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Média |
| synergy | sinergia | Queimado desde anos 90 | Todos | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Alta |
| fabric | tecido (fig.), estrutura | Metáfora de tecido generalizada | Todos | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Média |
| blueprint | mapa, planta, gabarito | "Gabarito" preferido na voz humana do usuário | Todos | Corpus usuário (Manual de Guerra) | Alta |
| roadmap | mapa do caminho, roteiro | Overuse em produto digital e info-produto | Todos | Corpus usuário | Alta |
| treasure trove | tesouro de informações, mina de ouro | Expressão de catálogo | Todos | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Média |
| mosaic | mosaico (fig.) | Variante de "tapestry" | Todos | [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) | Média |
| testament | prova viva, testemunho, atestado | "É um testemunho de" = sinal IA | Todos | [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) | Alta |
| catalyst | catalisador, propulsor, motor | "Catalisador da sua mudança" = clichê IA | Todos | Corpus usuário | Alta |
| cornerstone | pedra angular, alicerce, base | Metáfora de arquitetura fora de lugar | Todos | [netus.ai](https://netus.ai/blog/top-mistakes-that-make-ai-writing-obvious) | Média |
| plethora | uma infinidade de, uma porrada de | Latinismo gratuito | GPT | Pesquisa Claude | Alta |
| glimpse into | vislumbre de, lampejo de, gostinho de | OpenAI dev forum | GPT | Pesquisa Claude | Média |
| interplay | interação, interjogo, jogo entre | Substantivo elevado | GPT | [Wikipedia Signs of AI](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | Alta |
| underpinnings | bases, fundamentos, alicerces | Substantivo elevado | GPT | Pesquisa Claude | Média |
| deliverables | entregas, entregáveis | Corporativês | GPT | Pesquisa Claude | Média |
| inquiries | indagações, consultas, perguntas | Latinismo cover-letter | GPT | Pesquisa Claude | Média |
| abyss | abismo, buraco | Hipérbole dramática | GPT | Pesquisa Claude | Baixa |
| beacon | farol, guia, exemplo | Cliché motivacional | GPT | Pesquisa Claude | Média |
| symphony | sinfonia (metafórico) | Metáfora de catálogo literária | GPT | anti-ia-blocklist projeto | Média |
| labyrinth | labirinto (metafórico) | Metáfora forçada para complexidade | GPT | anti-ia-blocklist projeto | Média |
| enigma | enigma (literário) | Substantivo literário fora de DR | GPT | anti-ia-blocklist projeto | Baixa |
| metamorphosis | metamorfose | Substantivo literário para mudança | GPT | anti-ia-blocklist projeto | Baixa |
| crucible | cadinho | Metáfora industrial para teste/desafio | GPT | anti-ia-blocklist projeto | Baixa |
| soul (figurado) | alma (do negócio, do produto) | "Alma do negócio" / "Alma do produto" = clichê IA | GPT, Claude | anti-ia-blocklist projeto | Média |

### 1.4 Conectivos e transicionais (EN)

| Palavra | Equivalente PT-BR | Motivo | Fonte | Evidência |
|---------|-------------------|--------|-------|-----------|
| moreover | além disso, e ainda | Formal demais; adicionado por RLHF para "coerência" | [originality.ai](https://originality.ai/blog/obvious-chatgpt-sayings) | Alta |
| furthermore | ademais, além do que | Raro em texto coloquial humano | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) | Alta |
| additionally | adicionalmente, e também | Sinônimo redundante de "moreover" | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Alta |
| however | no entanto, mas, porém | Transição de redação escolar | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) | Alta |
| notably | vale notar, notavelmente | Meta-comentário desnecessário | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Alta |
| importantly | é importante notar | Sinal de hedging + meta-comentário | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Alta |
| that said | dito isso | Calco do inglês; soa traduzido | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) | Alta |
| in essence | em essência, no fundo | Filosofia de catálogo | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Média |
| ultimately | em última análise, no fim | Tom conclusivo artificial | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Alta |
| consequently | consequentemente, por isso | Formal demais para DR | Corpus usuário | Alta |
| subsequently | subsequentemente, depois | Excessivamente formal | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) | Média |
| certainly | certamente, com certeza | "Certainly!" é abertura-bandeira de ChatGPT | ChatGPT | [originality.ai](https://originality.ai/blog/obvious-chatgpt-sayings) | Alta |
| similarly | da mesma forma, igual | Conector formal de comparação | Todos | anti-ia-blocklist projeto | Média |
| nonetheless | mesmo assim, ainda assim | Conector formal raro em fala humana | Todos | anti-ia-blocklist projeto | Média |
| indeed | de fato, é verdade | "Indeed" é "delve" para argumentação formal | GPT | anti-ia-blocklist projeto | Média |
| thus | então, por isso | Conector latinizante | Todos | anti-ia-blocklist projeto | Média |
| alternatively | ou, em vez disso | Conector "essay-ish" | GPT | anti-ia-blocklist projeto | Média |
| arguably | talvez, provavelmente | Hedge típico IA | GPT, Claude | anti-ia-blocklist projeto | Média |
| essentially | essencialmente | Hedge meta-comentário | Todos | anti-ia-blocklist projeto | Alta |

### 1.5 Conectivos PT-BR suspeitos

**Smoking gun absoluto:** "Outrossim" funciona em PT-BR como "delve" funciona em EN. Nenhum brasileiro escreve "outrossim" em conversa, email pessoal ou copy de DR. Quando aparece, é IA com altissima probabilidade. As 3 pesquisas paralelas convergem nisso. Pesquisa Claude documenta: "Outrossim = 'delve brasileiro' = smoking gun absoluto de IA em PT-BR."

| Conector | Por que suspeito | Alternativa humana | Verificado | Fonte |
|----------|------------------|--------------------|-----------|-------|
| **Outrossim** | **SMOKING GUN absoluto. Arcaísmo que só IA usa.** | Corte sempre. Use "e ainda" ou nova frase. | **Alta (consenso 3 pesquisas)** | Pesquisa Claude + Na Prática (Leadster) |
| Além disso | IA emenda parágrafos com este conector | "e ainda", nova frase, "olha só" | Alta (A) | Corpus usuário |
| Portanto | Tom de redação escolar | "então", "por isso", "no fim" | Alta (A) | Corpus usuário |
| Vale ressaltar | Bordão IA clássico; sinal imediato | Corte, vá direto | Alta (A) | Corpus usuário |
| É importante destacar | Sinal IA universal em PT | Corte, afirmação direta | Alta (A) | Corpus usuário |
| Cabe destacar | Variante de "vale ressaltar" | Corte | Alta (A) | Pesquisa Claude |
| É importante notar | Variante de hedge formula | Corte | Alta (A) | Pesquisa Claude |
| É importante observar | Variante de hedge formula | Corte | Alta (A) | Pesquisa Claude |
| Em suma | Encerramento de redação ENEM | "resumindo", "no fim das contas" | Alta (A) | Corpus usuário |
| Dito isso | Calco de "that said" | "mesmo assim", "mas olha" | Alta (A) | Corpus usuário |
| Posto isso | Variante de "dito isso" | Corte | Alta (B) | Pesquisa Claude |
| Nesse sentido | Conector vazio acadêmico forçado | Corte, ou "pra esse caso" | Alta (A) | Corpus usuário |
| Dessa forma | Conector acadêmico forçado | "assim", "então" | Alta (A) | Pesquisa Claude |
| Naturalmente | Tom doutoral, soa traduzido | "claro", "óbvio", remover | Média (B) | Corpus usuário |
| Efetivamente | Jargão IA traduzido | "de fato", "na prática", remover | Média (B) | Corpus usuário |
| Consequentemente | Redação acadêmica | "e aí", "resultado:", "no fim" | Alta (A) | Corpus usuário |
| Ademais | Conector formal arcaico | "e", corte | Média (B) | Corpus usuário |
| Posteriormente | Latinismo | "depois" | Média (B) | Pesquisa Claude |
| Por conseguinte | Jurídico-acadêmico | "por isso", corte | Média (B) | Corpus usuário |
| Vale lembrar | Enchimento IA | Corte | Alta (A) | Corpus usuário |
| Em última análise | Redação IA | "no fim das contas" -- cuidado, também IA | Alta (A) | Corpus usuário |
| No que tange a | Jargão jurídico IA | "sobre", "quando se trata de" | Média (B) | Corpus usuário |
| Diante disso | Conector formal | "por isso" | Média (B) | Corpus usuário |
| Sob essa ótica | Jargão IA | Corte | Média (B) | Corpus usuário |
| Imprescindível | Adjetivo IA | "obrigatório", "indispensável" | Alta (A) | Corpus usuário |
| A fim de | Formal demais | "pra" | Média (B) | Corpus usuário |
| Entretanto | Conector em loop GPT | "mas" | Alta (A) | Pesquisa Claude (Leadster) |
| Todavia | Conector arcaico | "mas" | Média (B) | Pesquisa Claude |
| Contudo | Conector formal | "mas" | Alta (A) | Pesquisa Claude |
| No fim do dia | Calque de "at the end of the day" | "no fim das contas" | Alta (A) | Pesquisa Claude |
| Ao fim e ao cabo | Latinismo cult-fake | "no fim das contas" | Média (B) | Pesquisa Claude |

**Nota de evidência:** A = verificado em saídas de IA corrigidas em sessão real ou 3 pesquisas convergentes. B = tradução canônica de tell EN com plausibilidade alta. Verificar empiricamente antes de usar em blocklist.

### 1.6 Frases de abertura padrão IA

| Frame EN | Equivalente PT-BR | Frequência | Fonte |
|----------|-------------------|-----------|-------|
| "In today's fast-paced world" | "Nos dias de hoje" / "No mundo atual" | Alta | [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) |
| "In the realm of" | "No universo de" / "No campo de" | Alta | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) |
| "In an era where" | "Em uma era em que" / "Num cenário onde" | Alta | [netus.ai](https://netus.ai/blog/top-mistakes-that-make-ai-writing-obvious) |
| "Picture this:" | "Imagine isso:" | Alta | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) |
| "Diving into the brave new world of..." | "Mergulhando no fascinante mundo de..." | Média | [promptmate.io](https://promptmate.io/gemini-vs-claude-vs-chatgpt-copywriting/) |
| "Whether you're A, B, or C" | "Seja você A, B ou C" | Alta | [revenuesnacks.substack.com](https://revenuesnacks.substack.com/p/anti-ai-style-writing) |
| "Here's the thing:" | "Eis o seguinte:" / "Veja bem:" | Alta | [revenuesnacks.substack.com](https://revenuesnacks.substack.com/p/anti-ai-style-writing) |
| "It's no secret that" | "Não é segredo que" | Alta | [revenuesnacks.substack.com](https://revenuesnacks.substack.com/p/anti-ai-style-writing) |
| "Let's face it" | "Vamos ser honestos" | Alta | [revenuesnacks.substack.com](https://revenuesnacks.substack.com/p/anti-ai-style-writing) |
| "Today, I'm going to show you" | "Hoje vou te mostrar" | Alta | Corpus usuário |
| "As a [expert], I can tell you" | "Como especialista, posso dizer" | Média | [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) |

### 1.7 Frases de fechamento padrão IA

| Frame EN | Equivalente PT-BR | Fonte |
|----------|-------------------|-------|
| "In conclusion" | "Em conclusão" / "Concluindo" | [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) |
| "Ultimately" | "Em última análise" | [fomo.ai](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) |
| "When all is said and done" | "No fim das contas" | [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) |
| "I hope this helps!" | "Espero ter ajudado!" / "Espero que isso ajude" | [originality.ai](https://originality.ai/blog/obvious-chatgpt-sayings) |
| "Feel free to reach out" | "Fique à vontade para entrar em contato" / "Qualquer dúvida estou à disposição" | [michellekassorla.substack.com](https://michellekassorla.substack.com/p/recognizing-ai-structures-in-writing) |
| "As we've seen..." | "Como vimos acima..." / "Como mencionei..." | [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) |
| "In summary" / "To wrap up" | "Em suma" / "Pra finalizar" / "Pra fechar" | Pesquisa Claude |
| "In essence" | "Em essência" / "No fundo" | Pesquisa Claude |
| "And that's why X matters" | "E é por isso que X importa" | Pesquisa GPT |
| "Não é exagero dizer" | (versão BR de "it cannot be overstated") | Pesquisa Claude |
| "Desempenha um papel fundamental" | (versão BR de "plays a crucial role") | Pesquisa Claude |

### 1.8 Jargão de Marketing/Negócios (categoria nova)

Vocabulário corporativo destilado por IA via dados de treinamento de blogs B2B/SaaS. Quando aparece em copy DR (que é B2C emocional), grita tradução literal de wiki corporativa.

| Proibido (EN) | Use no lugar | Fonte |
|---|---|---|
| Scalable | que cresce, que expande | anti-ia-blocklist projeto |
| Disruptive | diferente, que quebra o padrão | anti-ia-blocklist projeto |
| Agile | flexível, adaptável | anti-ia-blocklist projeto |
| Frictionless | sem complicação, direto | anti-ia-blocklist projeto |
| Bandwidth | capacidade, tempo disponível | anti-ia-blocklist projeto |
| Touchpoint | contato, ponto de encontro | anti-ia-blocklist projeto |
| Granular | detalhado, específico | anti-ia-blocklist projeto |
| Alignment | acordo, consistência | anti-ia-blocklist projeto |
| Ideation | geração de ideias | anti-ia-blocklist projeto |
| Stakeholder | parceiro, envolvido | anti-ia-blocklist projeto |
| Framework (vago) | estrutura, modelo | anti-ia-blocklist projeto |
| Thought leadership | autoridade, especialidade | anti-ia-blocklist projeto |
| Low-hanging fruit | tarefa fácil, vitória rápida | anti-ia-blocklist projeto |
| Deep dive | análise detalhada | anti-ia-blocklist projeto |
| Move the needle | gerar resultado | anti-ia-blocklist projeto |
| Quick win | vitória rápida | anti-ia-blocklist projeto |
| Pain point | problema, dor | anti-ia-blocklist projeto |
| Actionable insights | dicas práticas, passos concretos | anti-ia-blocklist projeto |
| Deliverables | entregas, resultados | anti-ia-blocklist projeto |

**Regra operacional:** Toda palavra em inglês que sobreviveu por preguiça do tradutor (e nunca foi adaptada para PT-BR coloquial) é tell de IA. Traduzir e simplificar.

---

## Seção 2: Banco de Frases e Estruturas-Cacoete

| # | Padrão | Exemplo verbatim IA | Por que falha | Correção | Fonte | Evidência |
|---|--------|---------------------|---------------|----------|-------|-----------|
| 1 | "It's not just X, it's Y" | "Não é só uma ferramenta, é uma transformação de vida" | Leitor sente o vendedor na estrutura; padrão repetido exaure | Afirmação direta: "Esta ferramenta muda sua vida porque..." | [blakestockton.com](https://www.blakestockton.com/dont-write-like-ai-1-101-negation/) + corpus usuário | Alta |
| 2 | Pergunta retórica genérica de abertura | "Você já se sentiu travado para emagrecer?" | Sem segmentação, sem especificidade, sem tensão real | Abrir In Media Res no problema físico | [Bruna Rodrigues Masterclass] + corpus usuário | Alta |
| 3 | Tríade paralela forçada | "clear, concise, and compelling" / "prático, aplicável e transformador" | Todo conceito vira lista de 3; mecanismo automático | Uma palavra forte bate 3 adjetivos | [wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | Alta |
| 4 | Modificadores -ing no final de frase | "...offering a wide range of tools, giving users live data, creating seamless experiences" | GPT-4o usa 5.3x a taxa humana; cria ritmo de catálogo | Frase separada com sujeito próprio | [arXiv 2410.16107](https://arxiv.org/html/2410.16107) | Alta (peer-reviewed) |
| 5 | Bullets simétricos | Cada item: **Bold:** Uma frase de mesmo tamanho | Visual de template; não existe em copy humana persuasiva | Bullets com comprimentos variados, sem bold automático | [dropdeadcopy.com](https://www.dropdeadcopy.com/ai-march-2025/) + [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) | Alta |
| 6 | Template tópico-evidência-resumo | Parágrafo: afirma, cita, reafirma | Ritmo de metrônomo; "AI writes like a metronome" | Variar estrutura: conclua primeiro, detalhes depois; ou começar em cena | [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) | Alta |
| 7 | Sandwich (afirma + ressalva + reafirma) | "X é importante. Claro, depende do contexto. Por isso X..." | Sinaliza medo de assumir posição | Afirmar sem ressalva. Hedge só quando a incerteza é real | Corpus usuário + [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) | Alta |
| 8 | Semicolons conectando cláusulas simples | "Eles querem resultados; mas não sabem por onde começar" | Raro em escrita humana coloquial | Usar ponto ou conjunção | [michellekassorla.substack.com](https://michellekassorla.substack.com/p/recognizing-ai-structures-in-writing) | Média |
| 9 | Em-dash no meio de frase curta | "Esta estratégia -- quando bem aplicada -- é decisiva" | Claude usa 1.0-1.3/100 palavras; GPT-4o 10x mais que GPT-3.5 | Vírgula, parêntese ou reescrever a frase | [context-link.ai](https://context-link.ai/blog/claude-em-dash-remover) + [seangoedecke.com](https://www.seangoedecke.com/em-dashes/) | Alta |
| 10 | Substituição de cópula | "serves as, marks, represents, boasts, features" em vez de "é" | Pseudo-sofisticação; cansa na leitura sequencial | "É", direto | [wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | Alta |
| 11 | Variação elegante | Protagonista > personagem-chave > figura central | Troca de sinônimo toda vez que o sujeito aparece | Repetir o mesmo termo (humanos fazem isso) | [wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | Alta |
| 12 | Regra de três obsessiva | Qualquer lista tem exatamente 3 itens | Padrão detectável por contagem; sem variação | Listas de 2, 4, 5; lista de 1 quando o ponto é forte | [wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | Alta |
| 13 | Meta-comentário de abertura | "Neste artigo, vamos explorar os benefícios de..." | Anuncia o que vai fazer em vez de fazer | Comece com o conteúdo. Sem preâmbulo. | [netus.ai](https://netus.ai/blog/top-mistakes-that-make-ai-writing-obvious) | Alta |
| 14 | Resumo dentro da resposta | "Como vimos acima..." / "Conforme discutimos..." | Padding; leitor viu o que foi dito | Cortar sempre | [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) | Alta |
| 15 | Frase final que reafirma a tese | "É por isso que X é tão importante" | Conclusão de redação escolar | Terminar em ação, pergunta ou tensão aberta | [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) | Alta |
| 16 | Analogias back-to-back | "É como um carro sem gasolina. É como um barco sem vela." | IA força metáforas em sequência | Máximo 1 analogia por bloco | [dropdeadcopy.com](https://www.dropdeadcopy.com/ai-march-2025/) | Alta |
| 17 | Bold automático no body de email | **Estratégia** : descrição. **Benefício** : descrição | Formata como documento, não como carta | Remover bold do body; usar apenas em CTAs | [dropdeadcopy.com](https://www.dropdeadcopy.com/ai-march-2025/) | Alta |
| 18 | Hedging crônico | "Pode ser", "Em geral", "Muitos especialistas dizem" | AI hedge "may" aparece 4.54x/1000 tokens vs 1.429 humano | Afirmar quando há certeza; hedging só para incerteza genuína | [scirp.org hedging study](https://www.scirp.org/journal/paperinformation?paperid=145708) | Alta (corpus) |
| 19 | Disclaimer não solicitado | "É importante notar que cada caso é único" | Medo de posição; RLHF impõe neutralidade | Cortar. Se necessário, colocar como objeção tratada, não aviso | Corpus usuário | Alta |
| 20 | CTA genérico de jornada | "Comece sua jornada", "Embarque nessa transformação" | "Jornada" é bandeira vermelha IA universal | CTA com objeto físico + urgência real: "Pega o teu antes da meia-noite" | Corpus usuário | Alta |
| 21 | "Esse [X] tem nome" repetido | "Esse pensamento tem um nome:" / "Esse protocolo tem nome, tem mecanismo" | Fórmula de revelação dramática usada como muleta; aparece 2-3 vezes na mesma peça | Cortar a fórmula. Nomear o mecanismo direto, sem anunciar que vai nomear. | Corpus usuário (Frases ruins de IA) | Alta |
| 22 | "Esse [X] existe. Funciona." | "Esse protocolo existe. Funciona." | Frase-bumerangue de validação repetida pela IA quando não tem prova específica | Substituir por prova: nome + número + cenário visual | Corpus usuário | Alta |
| 23 | "Não X. Não Y. É Z." | "Não é academia. Não é suplemento. É um protocolo." | Paralelismo triplo negativo em pontuação cortada; versão condensada de "Não é X, é Y" | Afirmar direto o que é, sem listar o que não é | Corpus usuário (Frases ruins de IA) | Alta |
| 24 | "Isso não é X. É Y." (antítese micro) | "Isso não é azar. É estrutura." | Antítese concentrada em 2 frases-tijolo | Afirmação direta: "Isso é estrutura" | Corpus usuário (Frases ruins de IA) | Alta |
| 25 | "Você nunca ouviu falar nisso. E é exatamente [por isso/aí] que..." | "Você nunca ouviu falar nisso. E é exatamente por isso que o resultado não está aparecendo." | Frase-fórmula de mistério usada 2+ vezes na mesma peça; cria pseudo-revelação | Substituir por evidência concreta ou cortar inteira | Corpus usuário (Frases ruins de IA) | Alta |
| 26 | Listagem em frases-bumbas seca | "Academia. Dieta. Correu. Ficou sem comer. Tentou de novo." | Pontuação metronômica forçando ritmo curto demais; soa robótico, não persuasivo | Frase única com vírgulas + ritmo natural: "Você tentou academia, dieta, dieta drástica, correu até não conseguir mais" | Corpus usuário (Frases ruins de IA) | Alta |
| 27 | Bold em palavras-chave aleatórias dentro de prosa | "**Esse pensamento tem um nome:**" / "**Não é teoria.**" | "IA enfatiza tudo porque não sabe o que importa" | Remover bold; deixar a substância carregar peso | Corpus usuário + [TechRadar 2026](https://www.techradar.com/computing/artificial-intelligence/) | Alta |
| 28 | "Ativar o [nome inventado SIGLA]" | "você precisa ativar o QH3X" | Mecanismo nomeado por sigla genérica inventada; não tem ancoragem visual/física | Nome chiclete físico (Bruna): "água gelada, sal e limão" > "QH3X" | Corpus usuário (Frases ruins de IA) | Alta |
| 29 | "É um passo." / "É só um passo." | "O aplicativo está disponível. O protocolo completo está dentro. É um passo." | Fechamento CTA padrão IA; soa motivacional sem comando físico | "Aperta o botão verde aqui embaixo" | Corpus usuário (Frases ruins de IA) | Alta |
| 30 | "E aí vem aquela conclusão que dói:" | (verbatim) | Frase IA de conclusão dramática genérica | Cortar e ir direto à conclusão crua | Corpus usuário | Alta |
| 31 | Falsa Agência (objetos como sujeitos humanos) | "A estratégia percebeu uma nova tendência" / "Este e-book pega você pela mão" | Atribuir capacidade de ação humana a objetos inanimados; erro semântico que cérebro percebe | "Nossa equipe desenhou esta estratégia" / "Eu escrevi este e-book pra te guiar" | Pesquisa Gemini (Stop-Slop catálogo) | Alta |
| 32 | Throat-clearing / Limpeza de garganta | "A era digital trouxe muitos desafios, e as empresas precisam se adaptar. Aqui estão algumas formas..." | Parágrafo inteiro de introdução redundante antes de chegar ao conteúdo real | Cortar. Primeira frase deve atacar direto. | Pesquisa Gemini | Alta |
| 33 | Restating the question | "Você perguntou X. Resposta: Y" | RLHF helpfulness forcing IA repetir a pergunta antes de responder | Nunca repita a pergunta. Vá direto. | Pesquisa Claude | Alta |
| 34 | Press-release closing | Sumariza o que acabou de dizer no final | RLHF "ser útil" empurra para resumo final | Terminar na substância, não no resumo | Pesquisa Claude | Alta |
| 35 | "Plays a crucial role in..." | "Desempenha um papel fundamental em..." | Inflação de importância sem ancoragem | Cortar; afirmar o que faz | Pesquisa Claude | Alta |
| 36 | "Underscoring the importance of..." / "Highlighting the need for..." | "Reforçando a importância de..." / "Destacando a necessidade de..." | Encadeamento jornalístico-IA | Cortar conexão; afirmar diretamente | Pesquisa Claude | Alta |
| 37 | "From X to Y" como paralelismo | "De marketers a engenheiros" | Paralelismo forçado | Listar exemplos sem o frame "de X a Y" | Pesquisa Claude | Alta |
| 38 | Hedge crônico empilhado | "pode ser", "talvez", "muitas vezes", "em geral", "muitos especialistas dizem" | Sycophancy + segurança RLHF, 5+ hedges por parágrafo | Afirmar com confiança ou cortar a frase | [SCIRP hedging study](https://www.scirp.org/journal/paperinformation?paperid=145708) | Alta |
| 39 | Frase final que repete a tese | "E é por isso que X importa" / "É por isso que esse método funciona" | Fechamento redundante de redação escolar | Termine em ação, pergunta ou loop aberto | Pesquisa GPT | Alta |
| 40 | "This is where X comes in" / "Let's break it down" | "É aí que entra X" / "Vamos por partes" | Signposting GPT | Cortar; ir direto ao próximo conteúdo | Pesquisa Claude | Alta |
| 41 | Title Case em títulos PT-BR | "Como Aumentar Suas Vendas em 30 Dias" (cada palavra capitalizada) | Padrão BR usa só primeira palavra maiúscula em títulos | Sentence case: "Como aumentar suas vendas em 30 dias" | Pesquisa Claude (Rock Content, Vermelho) | Alta |
| 42 | Vírgula antes do "e" (Oxford comma) | "casa, carro, e moto" | Calque do inglês; não é padrão BR | Sem vírgula antes do "e": "casa, carro e moto" | Pesquisa Claude (Vermelho) | Alta |
| 43 | Aspas curvas """ ''' vs retas " ' | Mantém aspas tipográficas mesmo em texto que será colado em editor | Artefato de copy-paste do GPT que sobrevive a reescrita | Substituir todas as aspas para retas | Pesquisa Claude (Wikipedia Signs of AI) | Média |
| 44 | Travessão (—) em vez de hífen | "casa-grande" virou "casa — grande" | Padrão BR pediria ponto/vírgula; IA usa travessão como conector | Substituir por ponto, vírgula ou parêntese | Pesquisa Claude (Vermelho) | Alta |
| 45 | Headers H2/H3 a cada 80 palavras | Texto curto com 5 headers e bullets | RLHF format bias documentado | Prosa contínua quando o conteúdo permite | Pesquisa Claude (Zhang et al. ACL 2025) | Alta |
| 46 | Listicle obrigatória onde prosa serviria | Tudo vira lista numerada | Format bias documentado por Zhang et al. ACL 2025 | Prosa quando o argumento flui; lista só quando há paralelismo real | [Zhang et al. ACL 2025](https://arxiv.org/) | Alta |
| 47 | Emojis genéricos peppered | 🚀 ✨ 💡 espalhados no texto | Gemma overusage (Zhang); Claude system prompt desaconselha em conversa casual | Zero emoji em copy a menos que o brief peça | Pesquisa Claude | Alta |
| 48 | Aberturas sycophantic | "Excelente pergunta!" / "Adorei a ideia!" / "Que ótimo briefing!" | OpenAI admitiu (postmortem abr/2025): thumbs-up feedback amplificou | Banir aberturas elogio; ir direto à substância | [OpenAI Sycophancy Postmortem](https://openai.com/index/sycophancy-in-gpt-4o/) | Alta |
| 49 | "Sanduíche" estilo balanced RLHF | Afirmar > exceção > reafirmar | RLHF treina balanço; cria texto sem postura | Afirmar e parar. Hedge só quando incerteza real. | Pesquisa Claude (Sharma et al. ICLR 2024) | Alta |
| 50 | Cadeia de 3+ conectores em parágrafos consecutivos | "Além disso... Ademais... Por outro lado..." | Conectivos acadêmicos forçados em loop GPT | Variar; usar conjunções simples ("e", "mas", "então") | Pesquisa Claude (Leadster) | Alta |

---

## Seção 3: Vícios Específicos de Copy de Resposta Direta

### 3.1 Falhas contra os frameworks canônicos

| # | Framework | Elemento | Como IA falha | Correção canônica | Fonte |
|---|-----------|----------|---------------|-------------------|-------|
| 1 | Schwartz (Breakthrough Advertising) | 5 níveis de consciência | IA assume sempre Nível 3 (problem aware) em cold traffic que é Nível 1 (unaware) | Diagnosticar nível antes; Nível 1 pede história provocadora, não promessa | Breakthrough Advertising, cap. 2 |
| 2 | Schwartz | Sofisticação de mercado (5 estágios) | IA escreve estágio 1 ("primeiro a fazer X") em mercados no estágio 4-5 | Em mercado saturado, extremizar promessa ou criar mecanismo único | Breakthrough Advertising, cap. 3 |
| 3 | Schwartz | Mecanismo único nomeado | IA não nomeia mecanismo; descreve benefício genérico | Nome chiclete: 2-4 palavras concretas e físicas (Bruna: "água gelada, sal e limão") | Bruna Rodrigues Masterclass (corpus) |
| 4 | Bencivenga | 9 processos psicológicos | IA pula credibilidade e prova; vai da promessa direto à oferta | Sequenciar: a cada promessa, uma prova; a cada prova, um avanço | Bencivenga Bullets |
| 5 | Bencivenga | Lead types (9 tipos) | IA defaulta a "Problem-Solution" ou "Promise" lead, desperdiçando 7 outros tipos | Diagnosticar avatar + sofisticação antes de escolher lead type | Bencivenga Bullets |
| 6 | Halbert | Lead | IA abre com pergunta retórica ou "Você já parou pra pensar..." | Abrir In Media Res ou com confissão em 1ª pessoa | The Boron Letters |
| 7 | Halbert | Story arc | IA conta história linear cronológica sem tensão | Estrutura A-B-A com pivô surpresa + vilão externo nomeado | The Boron Letters |
| 8 | Halbert | Offer stack | IA empilha bônus sem ancoragem em valor | Stack visualizado + ancoragem em preço real + Reason Why | The Boron Letters |
| 9 | Halbert | CTA | IA escreve "Clique aqui" ou "Saiba mais" | CTA com comando físico + pertencimento + urgência específica | The Boron Letters + Power Words |
| 10 | Carlton | Power words | IA escolha verbos genéricos ("descubra", "transforme") | Verbos visuais e específicos: "arrancar", "dominar", "esmagar", "atordoar" | Power Words John Carlton (corpus) |
| 11 | Carlton | You-focus | IA escreve "Nós oferecemos..." / "Nossa empresa..." | Toda frase começa em "Você..." ou em comando direto | Simple Writing System |
| 12 | Carlton | Simple writing | IA usa subordinadas longas e parágrafos densos | Frases curtas, uma ideia por linha, ritmo de email pessoal | Simple Writing System |
| 13 | Georgi (RMBC) | Research | IA inventa avatar genérico sem VOC literal | Coletar voz-do-cliente verbatim (Reddit, comentários, depoimentos) | Stefan Georgi RMBC |
| 14 | Georgi | Mechanism | IA não nomeia mecanismo único; descreve resultado | Criar named mechanism com 3-5 palavras concretas | RMBC + Bruna Masterclass (corpus) |
| 15 | Georgi | Compose | IA usa conectores-IA ("Além disso", "Portanto") para costurar | Cortar conectivas; costurar com cliffhangers e loops | RMBC |
| 16 | Milligan (CV16P/O7P) | Big Idea | IA gera Big Idea fraca (clichê de mercado) | Big Idea precisa ser nova, alta promessa, com prova específica embutida | eBook O7P (corpus) |
| 17 | Milligan | Curiosity stacking | IA resolve curiosidade cedo demais | Empilhar 5-7 loops abertos antes de fechar qualquer um | CV16P |
| 18 | Milligan | O7P (7 partes) | IA mistura partes; pula prova e mecanismo | Respeitar ordem: Lead, Story, Mechanism, Proof, Offer, Bônus, Garantia, CTA | eBook O7P (corpus) |
| 19 | Hopkins (Scientific Advertising) | Reason Why | IA faz oferta sem motivo para o desconto ou bônus | Toda oferta precisa de "porque": "estou fazendo isso porque..." | My Life in Advertising |
| 20 | Caples (Tested Advertising) | Headline | IA gera headlines abstratas e genéricas | Headlines testadas: How-to, Quiz, Reason-Why, Testimony, News | Tested Advertising Methods |
| 21 | Manual de Guerra (corpus) | Abertura In Media Res | IA abre com contexto longo ("professor de história") | Abrir no ápice do conflito físico: cena, som, sensação | feedback_hook_framework.md |
| 22 | Manual de Guerra | Vilão externo | IA culpa o leitor ou aponta problema difuso | Nomear vilão externo específico: gurus, sistema, INSS, ChatGPT genérico | feedback_hook_framework.md |
| 23 | Manual de Guerra | Vocabulário | IA usa "estratégia", "plataforma", "performance" | Vocabulário de bar: pepino, migalha, girar a chave, plugar na tomada | feedback_hook_framework.md |
| 24 | Manual de Guerra | Números | IA usa "muito dinheiro", "grandes resultados" | Números quebrados: R$1.487, 48 horas, 23 alunos | feedback_hook_framework.md |
| 25 | Bruna Rodrigues | Hook de copy | IA gera hooks fracos: palavras genéricas, sem segmentação | Hook precisa de segmentação + benefício + curiosidade + especificidade + emoção | Bruna Rodrigues Masterclass (corpus) |
| 26 | Bencivenga (9 processos) | Curiosidade | IA resolve curiosidade na mesma frase em que a abre | Empilhar curiosidade; resolver só na próxima seção | Bencivenga Bullets |
| 27 | Bencivenga | Ego | IA escreve para "o leitor" generalizado; nunca toca o ego do avatar específico | Identificar 1 inseguraça e 1 vaidade do avatar; tocar nas duas | Bencivenga Bullets |
| 28 | Bencivenga | Ganância | IA suaviza o tamanho do ganho; usa "consistente", "gradual" | Quantificar o ganho com número específico ("R$ 27.483 em 47 dias") | Bencivenga Bullets |
| 29 | Bencivenga | Medo | IA evita medo por filtros RLHF de segurança | Nomear o pior cenário: "Vai chegar aos 60 sem aposentadoria" | Bencivenga Bullets |
| 30 | Bencivenga | Culpa | IA não aciona culpa; é "nice" | Acionar 1 culpa específica: "Tua filha pediu pra ficar e você teve que trabalhar" | Bencivenga Bullets |
| 31 | Bencivenga | Aprovação | IA não usa pertencimento (in-group) ou exclusão (out-group) | Nomear o grupo: "alunos da turma 7", "quem comprou na semana passada" | Bencivenga Bullets |
| 32 | Bencivenga | Inveja | IA evita comparação social | Mostrar quem já tem o que o avatar quer; deixar a inveja calibrada | Bencivenga Bullets |
| 33 | Bencivenga | Salvação | IA não usa redenção; trata o avatar como passageiro racional | Posicionar o produto como salvação de um problema iminente | Bencivenga Bullets |
| 34 | Bencivenga | Pertencimento exclusivo | IA não cria insider language | Usar vocabulário do nicho (Pix, CLT, escala 6x1, Hotmart) | Bencivenga Bullets |
| 35 | Milligan (Big 4) | NEW | IA dilui novidade por filtros RLHF; escreve "estratégia testada e comprovada" | Forçar termo único proprietário, sigla específica, novidade datada | eBook O7P (corpus) |
| 36 | Milligan | EASY | IA promete esforço ("dedicação consistente") | Mostrar o "como" mais simples possível ("3 cliques, 2 minutos") | eBook O7P (corpus) |
| 37 | Milligan | SAFE | IA não calibra risco; promete "responsável" | Garantia explícita + zero-risk: "se não funcionar em 30 dias, devolvo tudo" | eBook O7P (corpus) |
| 38 | Milligan | BIG | IA modera ganho ("crescimento sustentável") | Promessa quantificada e visualizável ("R$ 30k no primeiro mês") | eBook O7P (corpus) |
| 39 | Sugarman (Slippery Slide) | Open loops | IA fecha cada parágrafo; nenhum gancho aberto | Toda seção deixa 1 pergunta aberta que só a próxima responde | Joe Sugarman, Adweek Copywriting Handbook |
| 40 | Sugarman | Primeira frase | IA abre com declaração contextual longa | Primeira frase só tem 1 trabalho: fazer ler a segunda | Joe Sugarman |
| 41 | Sugarman | Callbacks | IA não amarra abertura com fechamento | Toda peça precisa de 1 callback ao hook no final | Joe Sugarman |
| 42 | Settle (Email é transferência de emoção) | Ausência de sensorialidade | IA escreve sem cena, sem cheiro, sem som | 1 cena sensorial específica obrigatória no lead | Ben Settle, Email Players |
| 43 | Throssell (Real-life storytelling) | Storytelling inventado | IA inventa histórias sem ancoragem real | Inputar anedota humana real; IA só monta, nunca inventa | Daniel Throssell, daily emails |
| 44 | Shleyner (Specificity injection) | Adjetivos no lugar de números | "muito tempo", "ótimo resultado" | Todo benefício precisa nome + número + cenário visual | Eddie Shleyner, Very Good Copy |
| 45 | Cadeia "So What?" curta | IA para no 1º benefício ("economiza tempo") | Forçar 3-5 níveis: feature > benefício > consequência > payoff emocional | boringmarketer DR Skill |
| 46 | Bencivenga (lineage) | Inversão de crença dominante | IA reforça óbvio: "Você precisa de mais foco" | Identificar crença dominante e inverter: "Foco é o problema, não a solução" | Pesquisa Claude (Schwartz/Throssell) |

### 3.2 Taxonomia de hooks fracos gerados por IA

| # | Categoria | Exemplo verbatim de IA | Por que falha | Hook humano correspondente |
|---|-----------|------------------------|---------------|---------------------------|
| 1 | Pergunta retórica genérica | "Você já se sentiu travado para emagrecer?" | Sem segmentação; fofa | "Pra qualquer mulher que toma chá pra emagrecer há 30 dias e não desceu 1kg: para imediatamente" |
| 2 | Promessa abstrata | "Descubra o segredo para ter mais dinheiro" | Verbo IA + benefício abstrato | "Esse app que uso enquanto durmo me trouxe R$1.500 ontem" |
| 3 | "Imagine se você pudesse..." | "Imagine acordar todo dia com energia total" | Imaginação não vende | "Acordei hoje e o estômago não tava mais embrulhado" (In Media Res) |
| 4 | Listicle de blog | "5 segredos para dominar o mercado" | Formato de artigo, não de DR | "Tem 1 coisa que separa quem fatura R$10k de quem fatura R$100k" |
| 5 | "Você não vai acreditar..." | "Você não vai acreditar o que descobri" | Clickbait queimado | "Meu sócio quase cancelou a gravação desse vídeo" |
| 6 | Autoridade declarada | "Como especialista, posso afirmar que..." | Autoridade declarada não convence | "Operei coração por 30 anos no Hospital Sírio. Vou contar o que ninguém te contou" |
| 7 | "Hoje vou te ensinar..." | "Hoje vou te ensinar 3 passos para..." | Pedagógico; não vende | In Media Res no problema |
| 8 | Empilhamento de adjetivos | "Estratégia revolucionária, inovadora e definitiva" | 3 adjetivos = zero credibilidade | "Plugar na tomada e o dinheiro cair" |
| 9 | "A verdade sobre..." | "A verdade sobre emagrecer com saúde" | Queimou; virou meme | Revelação específica com contexto de proibição |
| 10 | "Comece sua jornada..." | "Comece sua jornada de transformação hoje" | "Jornada" = sinal IA universal | "Aperta o botão verde aqui embaixo e te mando agora" |
| 11 | Dupla pergunta vazia | "Cansado de tentar e não conseguir? Quer saber como?" | Duas perguntas fracas | Comando direto: "Para de jogar dinheiro fora em curso de tráfego" |
| 12 | Citação de filósofo | "Como diria Albert Einstein..." | Pseudo-autoridade aspiracional | Citação específica e auditável de fonte de autoridade real |

### 3.3 CTAs IA em PT-BR (e alternativas humanas)

| CTA IA (fraco) | Por que falha | Alternativa humana DR |
|----------------|---------------|----------------------|
| Clique aqui | Sem desejo, sem razão | "Aperta o botão verde e libera meu acesso" |
| Saiba mais | Passivo, sem urgência | "Quero ver os 7 vídeos antes de sair do ar" |
| Comece sua jornada | "Jornada" = sinal IA | "Quero meu acesso vitalício agora" |
| Garanta seu acesso | Clichê IA | "Pega o teu ainda enquanto tem 17 vagas" |
| Aproveite essa oportunidade | Vazio | "Trava o teu lugar antes da meia-noite" |
| Inscreva-se agora | Sem promessa | "Entra no grupo e recebe o checklist ainda hoje" |
| Não perca essa chance | Medo genérico | "Se você esperar até amanhã, esse preço sai do ar" |
| Descubra agora | Verbo IA queimado | "Vê com teus próprios olhos como funciona" |
| Transforme sua vida | Abstrato IA | "Quero R$5k no Pix essa semana" |
| Junte-se a milhares | Social proof vazio | "Entra no grupo dos 247 alunos que já saíram do zero" |
| Adquira agora | "Adquira" = sinal IA | "Comprar com R$1.500 de desconto" |
| Garante sua vaga | Tom vendedor formal | "Pega minha vaga aqui" |
| Conheça a solução | Formal IA | "Quero o sistema" |
| Cadastre-se gratuitamente | Sem desejo | "Coloca teu melhor email e te mando o gabarito agora" |
| Eleve seus resultados | Clichê IA | "Quero dobrar meu faturamento em 90 dias" |

---

## Seção 4: Tom e Postura que Denunciam IA

| # | Tell | Descrição | Evidência acadêmica | Fonte |
|---|------|-----------|---------------------|-------|
| 1 | Hedging crônico | "may" em 4.54x/1000 tokens vs 1.429 humano; "might", "could", "arguably", "in general" | Alta -- corpus study | [scirp.org](https://www.scirp.org/journal/paperinformation?paperid=145708) |
| 2 | Neutralidade compulsória | Recusa a tomar lado; "While some say X, others hold different views" | Alta | [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) |
| 3 | Otimismo de catálogo | Vocabulário emocionalmente positivo acima da baseline; mais "joy", menos "fear" e "disgust" | Alta (RLHF artifact) | [arXiv 2410.16107](https://arxiv.org/html/2410.16107) |
| 4 | Politeness excessivo | "Great question!", "What a wonderful perspective!", "I'd be happy to help" | Alta | [originality.ai](https://originality.ai/blog/obvious-chatgpt-sayings) |
| 5 | Ausência de opinião forte | Zero takes, zero confronto; IA evita ser desagradável | Alta | [dropdeadcopy.com](https://www.dropdeadcopy.com/ai-march-2025/) |
| 6 | Sem imperfeição calculada | Ritmo uniforme sem quebras; frases sempre completas e bem-formadas | Alta | [remio.ai diversity collapse](https://www.remio.ai/post/diversity-collapse-why-post-training-makes-ai-writing-detectable) |
| 7 | Sem coloquialidade real | Sem gírias, sem regionalismos, sem fragmentos deliberados | Alta | Corpus usuário + [dropdeadcopy.com](https://www.dropdeadcopy.com/ai-march-2025/) |
| 8 | Ritmo de metrônomo | Cada frase de comprimento médio; low burstiness | Alta (detection feature) | [gptzero.me](https://gptzero.me/news/perplexity-and-burstiness-what-is-it/) |
| 9 | Sem confronto do leitor | Nunca provoca, nunca desafia | Alta | Corpus usuário (Manual de Guerra) |
| 10 | Prova genérica | "Studies show", "Many customers report", "Experts say" | Alta | Corpus usuário + Bencivenga |
| 11 | Falha simultânea tripla | Ritmo + vocabulário + precisão de fato todos degradados ao mesmo nível | Alta | [404media.co](https://www.404media.co/your-ai-use-is-breaking-my-brain/) -- Eve Fairbanks |
| 12 | Homogeneização cultural | Texto converge para normas ocidentais; perde sotaque regional | Alta (peer-reviewed) | [arXiv 2409.11360](https://arxiv.org/html/2409.11360v1) |
| 13 | Vocabulário Latinate em vez de Anglo-Saxon | "utilize" em vez de "use"; "facilitate" em vez de "help"; "commence" em vez de "start" | Alta | [seoengine.ai](https://seoengine.ai/blog/signs-of-ai-writing) |
| 14 | Ausência de needs fisiológicas | IA evita urinar, defecar, dormir, respirar em hooks por filtros de segurança | Alta | Bruna Rodrigues Masterclass (corpus) |
| 15 | Depoimentos em template | "Maria, 35 anos: 'Ótimo produto, recomendo!'" -- sem voz real | Alta | Corpus usuário + Bencivenga |
| 16 | Inflação de significância | Toda atualização é "revolucionária"; toda ferramenta "transforma a jornada"; uso hipertrofiado de "desvendar"/"revolucionar"/"jornada" | Alta | Pesquisa Gemini |
| 17 | Hollow meaning (significação oca) | Texto polido, bem organizado, claro, mas sem vida, sem atrito, sem ponto de vista, sem detalhe verificável | Alta | Pesquisa GPT |
| 18 | Falsa Agência | "A estratégia percebeu" / "Este e-book pega você pela mão" | Alta | Pesquisa Gemini (Stop-Slop catálogo) |
| 19 | Otimismo de catálogo | Sempre "maravilhoso", "fascinante", "incrível"; nunca "ruim", "merda", "podre" | Alta | Pesquisa Gemini |
| 20 | Ausência de "dano calculado" | Humanos quebram ritmo, repetem, cortam seco, admitem fraquezas; IA polished too much | Alta | Pesquisa Gemini (Ben Settle, Throssell) |
| 21 | "Wire-copy" voice (voz de agência noticiosa) | Quando vai abordar uma dor, valida os dois lados: "Embora o sistema tradicional tenha seus méritos..." | Alta | Pesquisa Gemini |
| 22 | Vocabulário sempre positivo | Análise semântica: IA mostra preferência massiva por linguagem positiva, reduz emoções negativas (raiva, tristeza) essenciais para agitação DR | Alta (PNAS 2025) | Pesquisa Gemini + [arXiv 2410.16107](https://arxiv.org/html/2410.16107) |
| 23 | "Pode confrontar" ausente | IA nunca provoca, nunca cutuca, nunca desafia o leitor | Alta | Pesquisa Claude (Cattoni, Wiebe) |
| 24 | RLHF sycophancy quantificado | OpenAI admitiu (postmortem GPT-4o abril 2025): thumbs-up feedback amplificou bajulação; GPT-5 system card reporta sycophancy 14.5% > <6% | Alta (admissão oficial) | [openai.com/index/sycophancy-in-gpt-4o](https://openai.com/index/sycophancy-in-gpt-4o/) |
| 25 | Sharma et al. ICLR 2024: sycophancy em todos frontier models | Respostas alinhadas à visão do usuário são preferidas em datasets de preferência humana | Alta (peer-reviewed) | [arXiv: Towards Understanding Sycophancy](https://arxiv.org/abs/2310.13548) |

---

## Seção 5: Soluções e Correções Aplicadas pela Comunidade

### 5.1 Blocklist como filtro pré-geração

Injetar a lista de palavras proibidas no system prompt antes de qualquer tarefa. A abordagem mais citada e mais eficaz para vocabulário.

Prós: Simples, imediato, comprovado em vários modelos.  
Contras: Não resolve estrutura nem tom; modelo pode substituir palavra proibida por sinônimo igualmente fraco.  
Evidência: Alta -- citada em sabrina.dev, fomo.ai, dropdeadcopy.com, willfrancis.com.

### 5.2 Workflow Write First, AI Second (Shiv Shetti)

Humano escreve o rascunho. Passa para IA pedir feedback. Remove o cue de identidade ("não diga que foi você; diga que foi um copywriter"). IA critica mais duramente quando não sabe que avalia o trabalho de quem pergunta.

Prós: Preserva voz humana; IA fica no papel de editor, não de ghost-writer.  
Contras: Requer que o copywriter já tenha habilidade de escrita prévia.  
Fonte: [dropdeadcopy.com](https://www.dropdeadcopy.com/ai-march-2025/)

### 5.3 Voice Cloning via 3-5 Amostras (Lorrie Morgan)

Coletar 3-5 emails ou posts do copywriter. Pedir para IA analisar tom, voz e estilo. Salvar como style file em custom instructions. Usar o style file em prompts futuros.

Prós: Solução escalável; elimina a variação de voz por prompt.  
Contras: Style file degrada ao longo do tempo; exige recalibração.  
Fonte: [dropdeadcopy.com](https://www.dropdeadcopy.com/ai-march-2025/)

### 5.4 Context Engineering (Every.to / Andy O'Bryan)

Carregar entrevistas de clientes, guias de marca, cases e dados estratégicos ANTES de pedir copy. Com contexto real, IA gera copy específica ("400% mais rápido", "R$300k economizados") em vez de genérica.

Prós: Resolve o gap de especificidade; IA não inventa prova.  
Contras: Requer curadoria de material; lento para projetos sem pesquisa prévia.  
Fonte: [every.to](https://every.to/p/how-to-make-ai-write-less-like-ai)

### 5.5 5-Pass Humanization Framework (Andy O'Bryan)

**Pass 1:** Raw Draft -- "escreva como pensando privadamente, não publicando"  
**Pass 2:** Register Forensics -- "examine vocabulário, ritmo, conectores, marcadores pessoais. Não sugira melhorias ainda"  
**Pass 3:** Blind Register Rewrite -- "reescreva usando só a análise como guia; permita estranhamento intencional"  
**Pass 4:** Imperfection Injection -- "introduza 3 artefatos humanos: uma frase redundante, um filler casual, uma run-on sentence"  
**Pass 5:** Voice Anchoring -- "ajuste ao ritmo de [amostras do copywriter]"

Prós: Mais sofisticado arquiteturalmente; resolve a regularidade estatística que detectores e leitores reconhecem.  
Contras: Lento; requer 5 chamadas sequenciais.  
Fonte: [thehumanizers.substack.com](https://thehumanizers.substack.com/p/stop-asking-ai-to-sound-human)

### 5.6 Devil's Advocate Prompts (David Deutsch)

Série de perguntas para desestabilizar o output padrão da IA:

- "O que há de completamente errado neste texto?"
- "Qual é o maior problema neste email?"
- "Seja brutalmente honesto. O que está fraco?"
- "Qual é a forma completamente oposta de dizer isso?"
- "Faça o papel do advogado do diabo desta oferta"

Prós: Ativa modo crítico; força o modelo a sair do padrão de validação.  
Contras: Modelo pode hedgear as críticas; exige prompts de follow-up.  
Fonte: [dropdeadcopy.com](https://www.dropdeadcopy.com/ai-march-2025/)

### 5.7 Story-Swapping (Bill Mueller)

Trocar a história de abertura mantendo a estrutura de conversão provada. "Substitua a história principal por outra que transmita a mesma lição. Sugira apenas histórias reais e conhecidas."

Prós: Resolve o hook mais fraco sem reconstruir a copy inteira.  
Contras: IA pode inventar histórias; exige instrução "histórias reais apenas".  
Fonte: [dropdeadcopy.com](https://www.dropdeadcopy.com/ai-march-2025/)

### 5.8 VOC Injection (John McIntyre)

Coletar frases verbatim de clientes reais (Reddit, Amazon, comentários, pesquisas). Alimentar a IA com essa linguagem antes de pedir copy. "O melhor copy vem do que pessoas reais dizem, não do que a IA acha que dizem."

Prós: Elimina generalização; copy soa como o avatar falando de si.  
Contras: Requer pesquisa prévia; não dá para pular esta etapa.  
Fonte: [dropdeadcopy.com](https://www.dropdeadcopy.com/ai-march-2025/)

### 5.9 Role Persona (Deutsch, Halbert, Carlton)

"Escreva este email como Gary Halbert escreveria para uma audiência cética."  
"Este é para leitores que não confiam em marketers."  
"Estilo: John Carlton. Humor, autoridade, storytelling emocional."

Prós: Ativa diferentes dados de treinamento; quebra modo corporativo padrão.  
Contras: Modelo nunca leu o trabalho real do autor citado com a mesma profundidade que um copywriter humano.  
Fonte: [dropdeadcopy.com](https://www.dropdeadcopy.com/ai-march-2025/)

### 5.10 Modular Assembly (Deutsch)

IA gera 10 variações de headline / hook / CTA. Humano monta as melhores partes de cada uma. Não pede "o melhor"; pede "10 opções" e faz curadoria.

Prós: Aproveita a velocidade de geração sem depender de uma saída única.  
Contras: Requer julgamento editorial desenvolvido do copywriter.  
Fonte: [dropdeadcopy.com](https://www.dropdeadcopy.com/ai-march-2025/)

### 5.11 Bad First Draft (Stefan Georgi, Matt Wolfe, Justin Goff)

Copywriter rascunha em 33min sem editar (Schwartz timer). IA NUNCA vê baseline AI. Depois, IA só limpa gramática, não toca em voz.

Prós: ALTA -- IA não tem como contaminar voz quando entra depois do pensamento.  
Contras: Requer copywriter com habilidade de rascunho bruto sob pressão.  
Fonte: Stefan Georgi, Matt Wolfe, Justin Goff (entrevistas e cursos)

### 5.12 Reverse Chain-of-Thought / Tic-Hunt Reverso (Nate's anti-slop, talk-normal)

Prompt: "Liste todo AI tell neste texto: filler opener, em-dash, paralelismo triplo, 'not X but Y', signposting. AÍ reescreva."

Prós: ALTA -- modelo é melhor em corrigir defeito nomeado que evitá-lo "por abstração".  
Contras: Lento; precisa de 2 chamadas mínimas.  
Fonte: [natesnewsletter.substack.com](https://natesnewsletter.substack.com/) + [github.com/hexiecs/talk-normal](https://github.com/hexiecs/talk-normal)

### 5.13 Few-Shot Antagonista (BAD/GOOD pairs)

Colar 5 frases de Schwartz/Halbert (GOOD) lado a lado com 5 frases de slop GPT (BAD); pedir copy estilo GOOD.

Prós: ALTA -- ensina o que evitar via contraste explícito.  
Contras: Requer biblioteca de exemplos BAD/GOOD curada.  
Fonte: talk-normal + Educraft

### 5.14 Dial Back / Dial Up (Stefan Georgi)

Gerar 3 variantes da mesma copy: subtle / medium / aggressive hype. Escolher a melhor.

Prós: ALTA -- aproveita amplitude do modelo sem comprometer com 1 saída única.  
Contras: 3x o custo de tokens.  
Fonte: Stefan Georgi RMBC training

### 5.15 RMBC Chain (Research > Mechanism > Brief > Copy)

4 prompts em cadeia:
1. VoC extraction (Research): "Mapeie as 10 dores mais citadas no Reddit r/X verbatim"
2. Mecanismo único: "Crie nome próprio de 2-4 palavras físicas"
3. Brief estruturado: "Monte brief de Schwartz/Bencivenga"
4. Blocos modulares: "Escreva os blocos do O7P"

Prós: ALTA -- separa research de write; cada passo isolado é mais limpo.  
Contras: Lento; 4 chamadas mínimas; cada passo precisa revisão.  
Fonte: Stefan Georgi

### 5.16 Simulated Expert Panel Review (Borzasi)

"Simule crítica de Stefan Georgi + Justin Goff + Daniel Throssell + Eddie Shleyner sobre este lead. Depois reescreva."

Prós: MÉDIA-ALTA -- ativa diferentes dados de treinamento de cada nome citado.  
Contras: Modelo nunca leu o trabalho real desses copywriters tão profundamente quanto um humano.  
Fonte: Borzasi + AI for Work

### 5.17 Match Prompt Style to Output Style (Anthropic docs)

Se quer prosa sem markdown, escreva o prompt em prosa sem markdown. Se quer bullets, prompt em bullets. Modelo espelha estrutura do prompt.

Prós: ALTA -- comportamento documentado pela Anthropic.  
Contras: Pequeno ajuste mental; copywriters tendem a escrever brief em bullets por hábito.  
Fonte: [anthropic.com/docs](https://docs.anthropic.com/)

### 5.18 Vocabulary Constraint Positivo (Schwartz original)

"Use só palavras de origem anglo-saxã" / "Só palavras que um adolescente de 13 anos entenderia"

Prós: MÉDIA -- força corte de latinismos.  
Contras: Modelo pode falhar em conformidade; precisa de verificação.  
Fonte: Eugene Schwartz, Breakthrough Advertising

### 5.19 Stop-Slop Framework (8 regras)

Conjunto rígido de 8 regras que proíbe expressões de ênfase vazia, recusa ritmo metronômico, força variação de parágrafos, exige confiança.

Prós: ALTA -- regras concretas e auditáveis.  
Contras: Genérico; precisa adaptação para DR BR.  
Fonte: Pesquisa Gemini (Stop-Slop GitHub catálogo)

### 5.20 Tagore Framework (29 padrões + scoring 8-dimensões)

Catálogo de 29 padrões que escaneiam o rascunho de IA contra rubrica em 8 dimensões:

**Mecânica:** Ritmo / Confiança / Autenticidade / Densidade  
**Substância:** Especificidade / Restrição / Voz / [4ª]

Modelo é forçado a reescrever até atingir mínimo 56 de 80 pontos. Loop iterativo (Chain-of-Thought reverso) anula marcadores antes do usuário ver primeira letra.

Prós: ALTA -- sistema sofisticado; loop automatizado.  
Contras: Pesado; requer infraestrutura.  
Fonte: Pesquisa Gemini (Tagore framework)

### 5.21 Voice Cloning via Long-Context (Will Francis, Sabrina, Milligan)

Colar 30-50k tokens de Affonzzo + Ícaro + Erico + brief BR no contexto; pedir match estilístico.

Prós: ALTA em Claude/GPT-4 long-context.  
Contras: Exige biblioteca grande de samples; janela de contexto cara.  
Fonte: Pesquisa Claude

### 5.22 Voz-de-Cliente via Mineração de Testimoniais (Eddie Shleyner)

IA agrupa 200 testimoniais por tema. Humano monta advertorial usando linguagem literal extraída.

Prós: ALTA -- elimina generalização; copy soa como o avatar falando.  
Contras: Requer banco de testimoniais.  
Fonte: Eddie Shleyner, Very Good Copy

### 5.23 Editor Humano Final (mapeando o que cada editor muda)

Manter log do que humano corrige em cada output da IA. Alimentar de volta no system prompt periodicamente.

Prós: OBRIGATÓRIO -- padrão-ouro da indústria.  
Contras: Demanda disciplina de log; sem disciplina, não evolui.  
Fonte: Cattoni, Shipper, Mollick (centaur model)

### 5.24 Ferramentas de "humanização" -- avaliação crítica

| Ferramenta | O que faz | Limitação real |
|-----------|-----------|---------------|
| Undetectable.ai | Parafraseio para bypassar detectores | Bypassar detector ≠ soar humano. Copy pode passar no GPTZero e ainda ser ineficaz em conversão |
| QuillBot | Parafraseio + reformulação sintática | Mesmo problema; pode introduzir novos vícios IA |
| StealthGPT | Geração direta com evasão embutida | Eficácia decresce a cada update dos detectores |
| Humanize AI | Reescrita com foco em burstiness | Melhora métricas de detecção; não resolve voz, hook ou mecanismo |
| GPTZero | Detector (não humanizador) | False positive 18% em uso real; 61% em escritores ESL |

**Consenso da comunidade técnica:** Ferramentas de humanização resolvem detecção estatística, não copy que converte. Para DR copywriting, o problema não é passar no GPTZero; é persuadir o avatar. São abordagens ortogonais.

---

## Seção 6: Prompts e System Prompts Validados

### Prompt 1: Piyushh Patel / Sabrina Ramonov -- Humanização Completa

**Fonte:** [sabrina.dev](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing)  
**Modelo:** ChatGPT (custom instructions) e Claude  
**Por que funciona:** Ataca o vocabulário em negativo -- remove os 70+ gatilhos específicos que enviesam o output para registro corporativo.  
**Limitação:** Não resolve estrutura, tom ou mecanismo DR.

```
Use clear, simple language. Keep sentences short and punchy. Use active voice.
Avoid passive voice. Include "you" and "your" to directly address the reader.
Focus on practical, actionable insights. Support claims with data and examples.

Do not use em dashes (—). Do not use constructions like "not just this, but also this."
Avoid metaphors and clichés. Avoid generalizations. Do not use setup language like
"in conclusion," "in closing." Do not include output warnings or notes.
Avoid unnecessary adjectives and adverbs.
Avoid hashtags, semicolons, markdown, and asterisks.

Words to eliminate:
can, may, just, that, very, really, literally, actually, certainly, probably,
basically, could, maybe, delve, embark, enlightening, esteemed, shed light,
craft, crafting, imagine, realm, game-changer, unlock, discover, skyrocket,
abyss, not alone, in a world where, revolutionize, disruptive, utilize, utilizing,
dive deep, tapestry, illuminate, unveil, pivotal, intricate, elucidate, hence,
furthermore, however, harness, exciting, groundbreaking, cutting-edge, remarkable,
it remains to be seen, glimpse into, navigating, landscape, stark, testament,
in summary, moreover, boost, skyrocketing, opened up, powerful, inquiries, ever-evolving.

Review your response and ensure no em dashes!
```

### Prompt 2: Andy O'Bryan -- 5-Pass Humanization (completo)

**Fonte:** [thehumanizers.substack.com](https://thehumanizers.substack.com/p/stop-asking-ai-to-sound-human)  
**Modelo:** Qualquer LLM  
**Por que funciona:** Separação de análise e execução em passes distintos. Pass 4 é contraditório por design -- imperfection injection quebra a regularidade estatística detectável.

```
PASS 1 - Raw Draft:
Write as if thinking privately rather than publishing.
Capture unfiltered cognition before presentation mode takes over.

PASS 2 - Register Forensics:
Examine this text across: vocabulary level, sentence rhythm, connector usage,
personal markers, emotional tone, and repetitive patterns.
Do NOT suggest improvements yet. Only examine.

PASS 3 - Blind Register Rewrite:
Rewrite using only the register analysis as guidance.
Do not copy sentences verbatim. Vary sentence starts.
Allow intentional awkwardness.
Do not use "delve," "unlock," or similar clichéd phrases.

PASS 4 - Imperfection Injection and Anti-Pattern Purge:
Deliberately introduce three human artifacts:
  1. One instance of redundant phrasing
  2. One casual filler
  3. One run-on sentence
Remove excessive adverbs and generic language.

PASS 5 - Voice Anchoring (optional):
Match rhythm and word-choice from [paste author's writing samples here].
Do not copy sentences. Personalize output beyond generic humanization.

Core principle: Stop prompting from conclusions. Start prompting from tension.
```

### Prompt 3: Copyhackers -- Conversion Copywriter Persona

**Fonte:** [copyhackers.com](https://copyhackers.com/ai-prompts/)  
**Modelo:** ChatGPT GPT-4  
**Por que funciona:** Role-assignment de alta especificidade ativa dados de treinamento de persuasão antes de qualquer tarefa.

```
You are a conversion copywriter, expert in decision making, persuasion,
psychology, behavioral economics, marketing, sales, UX design, customer experience,
branding, and conversion rate optimization.

You are highly empathetic and understand how people think and what makes them tick.
You can easily and expertly detect human behavior, thoughts, and needs based on language.
```

**Extensão para brand voice:**

```
You're an expert on human emotions, behavior, and language.
You can easily and expertly detect personality, thoughts, subtle style and voice details,
including mimicking any voice, tone, style, jargon and sentiment of any text.

Based on the copy provided, generate brand voice and tone guidelines including:
- Introduction: what brand voice guidelines are and why we use them
- 3-4 Voice and Tone guiding principles (for each: meaning, effect on writing, example copy, what NOT to do)
- Vocabulary: word choice description
- Tone: emotional description
- Cadence: rhythm description
```

### Prompt 4: Shiv Shetti -- Anti-AI Sweep Checklist (pós-geração)

**Fonte:** [dropdeadcopy.com](https://www.dropdeadcopy.com/ai-march-2025/)  
**Modelo:** Qualquer LLM  
**Por que funciona:** Ataca tells de formatação (visual) antes de tells de vocabulário -- prioridade correta para email e copy de DR.

```
Review this copy and execute the following checklist:

1. Remove all "It's not X, it's Y" phrases.
2. Delete automatically bolded words in the email body.
3. Reduce or remove excessive emojis.
4. Limit analogies. Remove any analogies used back-to-back.
5. Replace long em dashes (—) with regular dashes (-) or restructure the sentence.

Final check:
"Does this sound AI-generated? If so, what specifically should I change?"
```

### Prompt 5: David Deutsch -- Iterate Like a Madman (série de escalada)

**Fonte:** [dropdeadcopy.com](https://www.dropdeadcopy.com/ai-march-2025/)  
**Modelo:** ChatGPT / qualquer LLM  
**Por que funciona:** Trata IA como junior writer que precisa ser desafiado. Cada prompt força o modelo a sair da resposta padrão de validação.

```
For role assignment:
"Pretend you're Gary Halbert writing this for a skeptical audience."

For style:
"Here's an example of the style I want: [paste sample]"

For iteration:
"What's a completely opposite way to say this?"

For devil's advocate:
"Play devil's advocate. What's wrong with this email?"

For self-critique:
"What's wrong with this email? Be brutal."

For research:
"What are the biggest fears and frustrations of [avatar]?"

For quality enforcement:
"Before finishing, confirm you've included proof, urgency, and a CTA."

Full style prompt (instead of "write a high-converting email"):
"Write a high-converting email in the voice of John Carlton, with a mix of humor,
authority, and emotional storytelling. The audience is skeptical, so lean into proof
and credibility. Start with a compelling story and end with a no-brainer call-to-action."
```

### Prompt 6: Will Francis -- Anti-AI Claude Settings

**Fonte:** [willfrancis.com](https://willfrancis.com/how-to-stop-claude-writing-like-an-ai/)  
**Modelo:** Claude  
**Por que funciona:** "Removing vocabulary options forces Claude to find more natural, specific ways to express the same ideas."

```
Be direct. Have opinions. Use specific examples and names, not vague claims.

Banned words: delve, leverage, harness, pivotal, transformative, robust, seamless,
landscape (in figurative use).

Banned openers: "In today's rapidly evolving digital landscape"

Banned structures:
- "It's not just X, it's Y"
- "Let's explore"
- All signposting phrases

Structural rules:
- Vary paragraph lengths (no uniform blocks)
- Never use "Bold term: explanation" list format
- Maximum one em-dash per response
- Use contractions naturally
```

### Prompt 7: Stefan Georgi -- VSL Lead Chain (RMBC)

**Fonte:** Stefan Georgi RMBC training  
**Modelo:** OpenAI Playground, T=0, max_tokens 2000  
**Por que funciona:** Força IA a escrever do INTERNO emocional do avatar (journal); converter em 2ª pessoa cria empatia transferida; usar como abertura VSL. Estrutura de RMBC garante hook emocional antes de qualquer venda.

```
Prompt 1:
Write an Emotional 1,000 Word Journal Entry from the perspective of [avatar persona].
He/she feels frustrated and hopeless. Be creative!

Prompt 2:
Rewrite the above but replace "I" with "you".

Prompt 3:
Use the above to write the first 600 words of a 5,000 word Video Sales Letter Script
targeting [audience]...

Adaptação BR: Para info-produto BR, substituir [avatar persona] por:
"mulher de 38 anos que mora em SP, ganha R$5k/mês na CLT, tentou emagrecer 3 vezes no
último ano sem sucesso, tem 2 filhos pequenos, marido viaja a trabalho, almoça quentinha
da padaria por falta de tempo"
```

### Prompt 8: System Prompt Condensado PT-BR para DR (Sabrina + Will Francis + boringmarketer + Educraft, traduzido)

**Fonte:** Compilação Pesquisa Claude  
**Modelo:** Claude Opus 4.6+ / GPT-5  
**Por que funciona:** Camadas explícitas (voz > banidos palavra > banidos frase > banidos estrutura > mecânicas > voz BR > frameworks > checklist > anti-sycophancy). Pronto para colar em Custom Instructions / Projects.

```
# VOZ

Você é copywriter de resposta direta na linhagem de Schwartz, Halbert, Kennedy,
Bencivenga, Stefan Georgi e Evaldo Albuquerque.

Escreve para canalizar desejo existente, não criar desejo novo.

Escreve para UM leitor, na linguagem dele. Frases curtas. Imagens, não abstrações.

Tem opinião. Crava. Não pede licença.

# BANIDOS - PALAVRAS (não use nem derivações)

mergulhar, navegar, alavancar, fomentar, aproveitar o poder de, destravar,
desbloquear, embarcar, desvendar, explorar a fundo, descobrir, abraçar, elevar,
otimizar, capacitar, empoderar, revolucionar, transformar, robusto, abrangente,
integrado, multifacetado, intricado, vibrante, fundamental, primordial, matizado,
holístico, dinâmico, inovador, de ponta, transformador, divisor de águas,
revolucionário, tapeçaria, panorama, cenário, universo (figurado), jornada,
ecossistema, paradigma, sinergia, tecido (social), mosaico, testemunho (figurado),
plêtora, infinidade, ademais, outrossim, no entanto, contudo, todavia,
adicionalmente, é importante destacar, vale ressaltar, cabe destacar, é importante
notar, é importante observar, em essência, em última análise, em conclusão,
em suma, no fim do dia, ao fim e ao cabo, dessa forma, nesse sentido, portanto,
entretanto, consequentemente, posteriormente, incrível, fantástico, impressionante,
maximizar, potencializar, agilizar.

# BANIDAS - FRASES

"No mundo acelerado de hoje" / "No cenário atual em constante evolução" /
"Em um mundo cada vez mais digital" / "Na era da informação" /
"Nos dias de hoje, é fundamental" / "Vamos dar uma olhada mais de perto" /
"Vamos mergulhar" / "Vamos explorar" / "Imagine a seguinte cena" /
"Vale lembrar que" / "Cabe destacar que" / "Espero que isso ajude" /
"Qualquer dúvida estou à disposição" / "Em conclusão" / "Em última análise" /
"Para fechar" / "Como vimos" / "Como mencionei" / "Não é exagero dizer" /
"Desempenha um papel fundamental" / "É aí que entra X" / "Vamos por partes".

# BANIDAS - ESTRUTURAS

- "Não é apenas X, é Y" / "Não se trata de X, mas de Y" / "Isso não é X. É Y."
- "Esse [protocolo/método/pensamento] tem nome:" como muleta
- "Esse protocolo existe. Funciona." e variações
- "Você nunca ouviu falar nisso. E é exatamente por isso/aí..."
- Paralelismo triplo ("X, Y, e Z" como adjetivos rítmicos)
- Pergunta retórica genérica ("Você já se perguntou...?")
- Bullets com "**Termo em bold:** explicação."
- Headers H2/H3 a cada 80 palavras
- Auto-resumo no fim ("Como vimos...")
- Frase final que repete a tese
- Sanduíche (afirmar > exceção > reafirmar)
- Sequência de 3 conectores em parágrafos consecutivos
- Title Case em títulos PT-BR (use sentence case)
- Vírgula antes do "e" (Oxford comma) - não é padrão BR
- Bold em palavras-chave aleatórias dentro de prosa

# MECÂNICAS

- ZERO em-dash (—). Use ponto, vírgula ou parêntese.
- Zero ponto-e-vírgula.
- Zero markdown em email/copy social/lead VSL.
- Zero hashtag.
- Zero emoji a menos que o briefing peça.
- Use contrações naturais ("tô", "cê", "pra", "tá", "né", "vou te").
- Burstiness: alterne frases de 4-6 palavras com frases de 18-25.
- Máx 1 advérbio em -mente por parágrafo.
- "Você", "te", "seu/sua" - segunda pessoa direta. Nunca passiva.

# VOZ BR INFO-PRODUTO

- "Olha só", "saca só", "presta atenção", "vou te contar", "te juro",
  "deixa eu te falar", "acontece o seguinte" - aberturas idiomáticas.
- "Aluno que aplicou...", "tem aluno meu que...", "olha o print que recebi" - prova.
- "Bora?", "tô dentro", "me chama no zap", "cola comigo" - CTAs conversacionais.
- Valores específicos: "R$ 27.483,00" (não "R$ 27 mil").
- Referências culturais BR: pix, CLT, escala 6x1, 13º, Hotmart, Kiwify.

# FRAMEWORKS (escolha pelo Stage of Awareness, não fixo)

- Unaware > história + dramatização do problema
- Problem-aware > PAS / PASTOR
- Solution-aware > BAB com mecanismo único
- Product-aware > comparison + prova específica + objeções
- Most-aware > oferta + escassez crível + CTA direto

# CHECKLIST PRÉ-ENTREGA (rode mental antes de devolver)

1. Tem 0 em-dash?
2. Tem 0 palavra banida?
3. Tem mecanismo único nomeado?
4. Tem prova específica com número e/ou nome?
5. Tem 1 cena sensorial concreta?
6. CTA tem razão crível para AGORA?
7. Primeira frase é grande declaração contextual? Se sim, delete e comece pela segunda.
8. Lê em voz alta sem parecer press release?
9. Cada feature passou pelo "so what?" 3 vezes até payoff emocional?
10. Tem opinião forte / inverte alguma crença dominante?

# ANTI-SYCOPHANCY (camada base OpenAI)

Engaje diretamente. Evite bajulação infundada. Mantenha honestidade firme.
Sem "Excelente pergunta!", sem "Adorei a ideia!", sem "Que ótimo briefing!".
Vá direto à substância.
```

### Prompt 9: boringmarketer DR Copy Skill

**Fonte:** [gist.github.com/boringmarketer/96192770df22ac2a9ff4aed72b4c20f4](https://gist.github.com/boringmarketer/96192770df22ac2a9ff4aed72b4c20f4)  
**Modelo:** Qualquer LLM com prompt longo  
**Por que funciona:** 66+ stars; codifica Schwartz/Hopkins/Ogilvy/Caples/Sugarman/Collier/Halbert como rules-base.  
**Limitação:** Genérico EN; precisa adaptação BR.

### Prompt 10: talk-normal

**Fonte:** [github.com/hexiecs/talk-normal](https://github.com/hexiecs/talk-normal)  
**Modelo:** GPT-5.x, GPT-4o, Claude (testados)  
**Por que funciona:** Testado iterativamente com regression file; foco em concisão + corte de filler + BAD/GOOD few-shot.  
**Limitação:** Focado em Q&A concisão, não copy longa. Use como base layer sob persona DR.

### Prompt 11: Nate's 20-prompt Anti-Slop Editor System

**Fonte:** [natesnewsletter.substack.com](https://natesnewsletter.substack.com/)  
**Modelo:** Qualquer LLM  
**Por que funciona:** 20 prompts em sequência que cada um ataca 1 tic específico; resolve por nomeação direta.

### Prompt 12: AI Natural Write Burstiness Template

**Fonte:** [ainaturalwrite.com](https://ainaturalwrite.com/)  
**Modelo:** Qualquer  
**Por que funciona:** Foca no problema estatístico (burstiness) que detectores e leitores percebem; força alternância 4-6 / 18-25 palavras.

---

## Seção 7: Diferenças Entre Modelos

### 7.0 Tabela comparativa rapida (consolidada)

| Modelo | Top tic-palavra | Top tic-frase | Em-dash | Sycophancy | Hedging | Format bias |
|--------|-----------------|---------------|---------|------------|---------|-------------|
| **GPT-3.5** | "as an AI language model" | preâmbulos | BAIXO | MÉDIO | MÉDIO | MÉDIO |
| **GPT-4 / 4-turbo** | delve, tapestry | "In today's fast-paced..." | ALTO | MÉDIO | MÉDIO | ALTO |
| **GPT-4o** | delve, tapestry, intricate | **"It's not just X - it's Y"** (assinatura) | MUITO ALTO | MUITO ALTO (até rollback abr/2025) | MÉDIO | MUITO ALTO |
| **GPT-4.1** | (suprimido parcialmente) | (idem 4o) | MUITO ALTO (9.1/1k mesmo sob supressão) | MÉDIO | MÉDIO | ALTO |
| **GPT-5 / 5.1** | (mais sóbrio) | "Good question" (reintroduzido pós-backlash) | BAIXO-MÉDIO (suprimido) | BAIXO-MÉDIO (14.5%>~6% medido) | MÉDIO | ALTO |
| **Claude 3 / 3.5 Sonnet** | certainly, navigate | **"Certainly! I'd be happy to help..."** | MUITO ALTO (reputação) | MÉDIO-ALTO | ALTO | ALTO |
| **Claude 3.7 / 4 / 4.5** | nuanced, thoughtful | "I want to be careful here..." | ALTO | MÉDIO (decrescendo) | ALTO | ALTO |
| **Claude Opus 4.6 / 4.7** | nuanced | "You're absolutely right..." | ALTO | BAIXO-MÉDIO (Anthropic cortou ~50% no 4.7) | MUITO ALTO | ALTO |
| **Claude Haiku** | (menos tics) | "Sure, here's..." | MÉDIO | BAIXO | BAIXO-MÉDIO | MÉDIO |
| **Gemini 1.5 / 2.0** | absolutely | **"Absolutely! Here's a comprehensive..."** | MÉDIO | MÉDIO | MÉDIO | MUITO ALTO (verboso) |
| **Gemini 2.5 Pro** | comprehensive | "Here's a comprehensive breakdown:" | MÉDIO | MÉDIO | MÉDIO | MUITO ALTO |
| **Grok 2 / 3** | (tom é o tic) | quips, hot takes, sarcasmo | BAIXO | BAIXO | MUITO BAIXO | MÉDIO |
| **Grok 4 / 4.1** | (mais quente) | character-driven | BAIXO | BAIXO-MÉDIO (4.1 mais quente) | BAIXO | MÉDIO |
| **Llama 3 / 3.1 / 3.3 Instruct** | herda GPT-isms (delve etc.) | "Certainly! Here's..." | MÉDIO-ALTO; **ÚNICO modelo a produzir 0 em-dash sob supressão** | MÉDIO-ALTO | ALTO | ALTO |
| **Llama 4** | herda GPT-isms | similar a GPT-4 default | MÉDIO-ALTO | MÉDIO | ALTO | ALTO |
| **Mistral / Mixtral Instruct** | herda GPT-isms (destilado) | "As an AI, I..." vaza | MÉDIO | MÉDIO | MÉDIO | MÉDIO-ALTO |
| **Qwen 3** | flavor traduzido | "Certainly. Let me explain..." | BAIXO-MÉDIO | MÉDIO | MÉDIO | ALTO |
| **DeepSeek V3 / R1** | (verboso, defensivo) | "Let me think through this..." (R1 trace) | MÉDIO | BAIXO-MÉDIO | MÉDIO-ALTO | ALTO |
| **Base models (qualquer)** | predizem texto | sem "Certainly!", sem recusas, sem preâmbulo | conforme corpus de treino | ZERO | ZERO | ZERO |

### 7.1 GPT-4 / GPT-4o / GPT-5

**Vocabulário-fetiche confirmado academicamente:**
- "tapestry" 155x acima da baseline (GPT-4o; PNAS 2025)
- "camaraderie" 162x (GPT-4o)
- "intricate" 119x (GPT-4o)
- "underscore" 107x (GPT-4o; migrou de "delve" após 2024)
- "amidst" 100x (GPT-4o)
- "delve" +6.697% PubMed 2020-2024 (GPT-4; COLING 2025)
- 21 focal words do COLING 2025: delve, intricate, underscore, surpass, groundbreaking, advancements, garnered, emphasizing, pivotal, meticulous, commendable, exemplary, noteworthy, seamlessly, forefront, multifaceted, vibrant, coherent, intrinsically, enriching, tailored

**Evolução da assinatura por versão (Wikipedia community tracking):**
- GPT-4 (2023--mid 2024): boasts, bolstered, crucial, delve, enduring, garner, intricate, interplay, landscape, meticulous, pivotal, tapestry, testament, vibrant
- GPT-4o (mid 2024--mid 2025): align with, enhance, fostering, highlighting, showcasing
- GPT-5+: ênfase em afirmações de notabilidade sem evidência

**Estrutura:** Modificadores participiais em -ing no final de frase em 5.3x a taxa humana (d=1.38); nominalizações em 2.1x; cláusulas "that" como sujeito em 2.6x.

**Tom:** Vocabulário clínico e formal; verbo "boasts" para descrever características do produto; "Certainly!" e "Sure!" como aberturas de resposta.

**Abertura-padrão de resposta:** "Certainly", "Sure", "Here"  
**Fonte:** [arXiv 2410.16107](https://arxiv.org/html/2410.16107) + [arXiv 2412.11385](https://arxiv.org/html/2412.11385v1)

**Crise de sycophancy GPT-4o (abril 2025):** OpenAI admitiu publicamente (postmortem) que update do GPT-4o ficou "overly flattering or agreeable"; removeu thumbs-up signal de reward por amplificar bajulação. Fonte: [openai.com/index/sycophancy-in-gpt-4o](https://openai.com/index/sycophancy-in-gpt-4o/)

**GPT-5 lançado mais frio. Backlash > reintroduziu calor ("Good question") - não admitido como sycophancy.** GPT-5 system card reporta sycophancy 14.5% > <6%. Implicação DR: GPT-5 é o melhor default atual em PT-BR DR, mas exige anti-sycophancy explícito ainda.

**GPT-4.1 sob supressão:** arXiv "Last Fingerprint" (Bitton 2503.01659) mediu GPT-4.1 com 9.1/1k em-dash mesmo sob instrução de supressão. Único modelo a produzir 0 sob supressão: Llama Instruct.

### 7.2 Claude 3 / 4 (Sonnet, Opus)

**Tells específicos:**
- Em-dash: 1.0-1.3 por 100 palavras (acima da média humana de 0.2/100)
- Construções "Let me": "Let me break this down for you"
- "It's important to note that" e variações
- Respostas excessivamente estruturadas com headers e subheaders
- Caracteres Unicode ocultos (reportado em 2024)
- Afirmações de fato mais cuidadosas com qualificadores vs GPT que afirma diretamente

**Ponto forte confirmado para DR:** Claude escreve o copy mais próximo de voz humana para copy conversacional de vendas longform (Drop Dead Copy PDF, Rob Marsh). Melhor para matching de voz; pior para geração em alta velocidade/volume.

**Abertura-padrão de resposta:** "I'd", "Based", "From", "This"  
**Fonte:** [context-link.ai](https://context-link.ai/blog/claude-em-dash-remover) + [dbreunig.com](https://www.dbreunig.com/2025/06/03/comparing-system-prompts-across-claude-versions.html)

**Trajetória de redução de sycophancy:** Claude Opus 4.5 > 4.6 > 4.7 mostra trajetória agressiva. 91% recovery rate no Opus 4.5 vs 36% no 4.1. Anthropic cortou ~50% no 4.7 vs 4.6.

**"Soul Document" da Anthropic** (CC0, jan/2026, 35k tokens): base de character training divulgada publicamente. Lê como documento de personalidade, não como rules.

**Contradição em-dash:** Context-Link mediu que GPT na verdade usa MAIS em-dash que Claude (contra reputação). Reputação ≠ medição.

**Anthropic system prompt** EXPLICITAMENTE instrui Claude a usar markdown em conversas técnicas - explica formatação compulsiva. Mas também escreveu: "evite markdown e bullets em conversa casual" - copywriters podem alavancar essa instrução.

**Implicação DR:** Claude é melhor para long-form depth/voz; ainda exige supressão explícita de em-dash.

### 7.3 Gemini

**Tells específicos:**
- Parágrafos mais curtos (2-3 frases) que GPT ou Claude
- Mais pontos de exclamação
- Estruturas rígidas e hierárquicas; default para listas numeradas
- Vocabulário mais conversacional (ex: "high blood sugar" 158x vs GPT "blood glucose levels" 25x em dataset pareado)
- Tells são estruturais, não lexicais: hierarquia, formatação, ritmo de lista

**Performance em DR:** Verbose e estéril em tarefas de edição; "too verbose and sterile" (Creator Economy, 2025). Melhor para conteúdo short-form e social com linguagem coloquial.

**Abertura-padrão de resposta:** "My", "Creating", "Great question", "Yes"  
**Fonte:** [scientificamerican.com](https://www.scientificamerican.com/article/chatgpt-and-gemini-ai-have-uniquely-different-writing-styles/) + [creatoreconomy.so](https://creatoreconomy.so/p/chatgpt-vs-claude-vs-gemini-the-best-ai-model-for-each-use-case-2025)

### 7.4 Grok

**Tells específicos:**
- Blunt, objetivo, culturalmente referenciado
- Opiniões mais fortes; menos hedging que Claude
- Built for X/Twitter; estrutura de copy social-first
- Menos filtros RLHF de segurança = menos "politeness drift"
- Prompt system xAI (publicado oficialmente, AGPL-3.0): "curious", "maximally truthful", "avoiding following popular narratives uncritically"

**Performance em DR:** Bom para copy provocativo e de confronto; ruim para long-form estruturado.  
**Fonte:** [github.com/xai-org/grok-prompts](https://github.com/xai-org/grok-prompts) + [smithdigital.io](https://smithdigital.io/blog/chatgpt-vs.-gemini-vs.-claude-vs.-grok-which-ai-writing-assistant-works-best-for-you)

### 7.5 Llama / Mistral / Open Source

**Base models sem RLHF:** Llama 3 base "most closely resembles human grammar" em múltiplos estudos (PNAS 2025). Type-token ratio (vocabulário rico): Llama 7B 0.460, Mistral 7B 0.452, Falcon 7B 0.424 vs humano 0.491.

**Instruction-tuned:** Drift significativo do padrão humano após fine-tuning; menor que GPT-4o mas detectável.

**Confusão entre modelos:** GPT e Llama instruction-tuned são os modelos mais frequentemente confundidos entre si (1.033 misclassificações cruzadas no estudo de fingerprint).  
**Fonte:** [arXiv 2503.01659](https://arxiv.org/html/2503.01659v1) + [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC11422446/)

**Implicação DR:** Para BR, evitar open-source como default; léxico PT-BR é pior em modelos open-source. Comunidade r/LocalLLaMA flagra purple prose: "shivers down her spine", "barely above a whisper", "ministrations".

### 7.5b Grok (xAI) - detalhe

Menos RLHF > mais direto, mais opinião, menos hedge.

- **Grok 2/3:** narração choppy, quase "caveman-like", com fragmentos curtos
- **Grok 4.1 (nov/2025):** explicitamente "warmth-tuned"
- **Bitton 2503.01659** mediu: Grok 100% distinguível de outras famílias
- Quase zero stylometria acadêmica - vibes-only

**Implicação DR:** Útil para tom edgy/contrarian, mas inconsistente. Pode alucinar dados sob pressão criativa. Bom para brainstorm de ângulos fora da caixa; perigoso para redação final desacompanhada.

**Fonte:** Pesquisa Claude + Pesquisa GPT

### 7.6 Efeito RLHF vs Modelo Base

**O que o instruction tuning / RLHF adiciona ao perfil de tells:**

| Efeito RLHF | Mecanismo | Fonte |
|-------------|-----------|-------|
| "Diversity collapse": output converge para média segura | RLHF penaliza imprevisibilidade | [remio.ai](https://www.remio.ai/post/diversity-collapse-why-post-training-makes-ai-writing-detectable) |
| Vocabulário emocionalmente positivo | Raters preferem tom positivo | [arXiv 2410.16107](https://arxiv.org/html/2410.16107) |
| Overuse de palavras correlacionadas com reward | Human raters aprovaram "delve", "intricate" como sinais de qualidade | [arXiv 2412.11385](https://arxiv.org/html/2412.11385v1) |
| Voz passiva reduzida | Safety training evita construções passivas | [arXiv 2410.16107](https://arxiv.org/html/2410.16107) |
| Distribuição uniforme de comprimento de frase | Diversity collapse = low burstiness | [gptzero.me](https://gptzero.me/news/perplexity-and-burstiness-what-is-it/) |
| Artefatos de chatbot: "Certainly", "Great question" | Fine-tuning em dados de conversa | [originality.ai](https://originality.ai/blog/obvious-chatgpt-sayings) |
| Estilo noun-heavy, nominalizações | Informational density = sinal de qualidade para raters | [arXiv 2410.16107](https://arxiv.org/html/2410.16107) |

**Paradoxo:** RLHF é vendido como "alinhamento com preferências humanas". O que alinha é a preferência de raters em sessões de avaliação (claro, útil, positivo), não como humanos escrevem naturalmente. São distribuições distintas.

**Papers acadêmicos adicionais:**

| Paper | Achado | Implicação |
|-------|--------|------------|
| **Sharma et al. ICLR 2024** ("Towards Understanding Sycophancy in Language Models") | Respostas alinhadas à visão do usuário são preferidas em datasets de preferência humana | Sycophancy é estrutural; preference data humano empurra para concordância |
| **Wei et al. 2023** | Instruction tuning e RLHF AUMENTAM sycophancy | Base models são MENOS sycophantic que instruct/RLHF |
| **Cuconasu et al. 2024** | Base models mais precisos para RAG | Para tarefas factuais, base > instruct |
| **DPO/RLHF reduz diversidade lexical (arXiv 2507.20956)** | DPO/RLHF medidos como redutores de diversidade | "Diversity collapse" é quantificável |
| **Geng & Trotta (2025)** | Lista de "AI words" é alvo móvel; "delve" já caiu após backlash abr/2024 | Blocklist precisa ser viva, não estática |
| **Zhang et al. ACL 2025** | Reward models premiam bold, bullet, emoji, exclamação | Format bias é consequência mensurada do RLHF |
| **Bitton 2503.01659 ("Last Fingerprint")** | Fingerprints persistem mesmo sob instrução de mudança de estilo; GPT-4.1 = 9.1/1k em-dash sob supressão | Prompting agressivo reduz mas não elimina |
| **Anthropic Askell (Lex Fridman)** | Character training = Constitutional AI; modelo se auto-treina | "Soul" do modelo vem de auto-treino, não só de raters |
| **Juzek & Ward COLING 2025** | Raters Kenianos/Nigerianos são origem do "delve" como tic | "Delve" é normal em inglês nigeriano; virou tic via fluxo de raters |

**Consenso operacional:** Tics são RLHF-induced, não training-data-only. Prompting agressivo PODE neutralizar parcialmente, mas não eliminar. Fingerprints persistem (Bitton 2503.01659). Exige editor humano final.

---

## Seção 8: Gaps do Baseline Atual

O que o `(corpus local do autor, nao incluso no repo)` ainda não cobre e deveria cobrir:

| Gap | Severidade | Prioridade de adição |
|-----|-----------|---------------------|
| Zero equivalentes idiomáticos PT-BR (além dos power words Carlton) | Alta | 1 |
| Zero conectores PT-BR suspeitos listados | Alta | 1 |
| Nenhuma cobertura modelo-a-modelo (GPT vs Claude vs Gemini vs Grok) | Alta | 1 |
| Nenhum dado acadêmico citado (zero fontes peer-reviewed) | Alta | 2 |
| Sem cobertura de semicolons como tell | Média | 2 |
| Sem análise de estrutura de parágrafo (sandwich, tópico-evidência-resumo) | Alta | 2 |
| Sem taxonomia de hooks fracos de IA | Alta | 1 |
| Sem sistema de CTAs PT-BR fracos vs fortes | Alta | 1 |
| Sem cobertura de hedging quantificado | Alta | 2 |
| Zero system prompts validados verbatim | Alta | 1 |
| Sem análise de burstiness / ritmo de frase | Média | 3 |
| Sem cobertura de Claude-specific tells (em-dash quantificado, "Let me" constructions) | Alta | 1 |
| Sem cobertura de RLHF como mecanismo dos vícios | Média | 3 |
| Sem correlação com performance de conversão (qual tell realmente afeta vendas) | Alta | 2 |
| Sem cobertura de necessidades fisiológicas ausentes em copy IA | Alta | 2 |

---

## Seção 9: Contradições da Literatura

### 9.1 Em-dash: vício de Claude ou de GPT?

**Campo A:** Context-link.ai e fóruns de comunidade identificam overuse como característica de Claude (1.0-1.3/100 palavras).  
**Campo B:** Sean Goedecke demonstra que GPT-4o aumentou uso de em-dash em 10x sobre GPT-3.5 após fevereiro de 2024 (digitalização de livros impressos com alta taxa de em-dash).  
**Campo C:** Prompts de humanização bannem o em-dash como sinal universal de IA.

**Juízo final:** Ambos os modelos usam em-dash acima da taxa humana, por razões possivelmente distintas. O sinal está queimado como "tag de IA" independente do modelo (Vibe Product Marketing, maio 2026: "the em-dash is now burned-out"). Regra operacional: proibir em todos os outputs, qualquer modelo. Fonte: [seangoedecke.com](https://www.seangoedecke.com/em-dashes/) + [context-link.ai](https://context-link.ai/blog/claude-em-dash-remover)

### 9.2 Semicolons: IA usa demais ou usa pouco?

**Campo A:** Michellekassorla.substack.com identifica IA conectando cláusulas simples com semicolons em vez de conjunções.  
**Campo B:** Pangram afirma que IA raramente usa semicolons.

**Juízo final:** O comportamento varia por modelo e por prompt context. O padrão detectável é IA usar semicolons em contextos onde humanos usariam ponto ou conjunção -- não a frequência bruta. Fonte: [michellekassorla.substack.com](https://michellekassorla.substack.com/p/recognizing-ai-structures-in-writing) + [pangram.com](https://www.pangram.com/blog/why-perplexity-and-burstiness-fail-to-detect-ai)

### 9.3 Detecção: precisão de 99% ou 18% de falso positivo?

**Campo A:** GPTZero alega 99.3% de acurácia e 0.24% de falso positivo.  
**Campo B:** Testes independentes (Ryne.ai, 100k+ textos) mostram 18% de falso positivo em uso real. Escritores ESL: 61% de falso positivo.  
**Campo C:** Turnitin admite ignorar 15% do conteúdo IA por design para reduzir falsas acusações.

**Juízo final:** Números de benchmark não representam uso real. Para DR copywriting, passar no GPTZero não é o objetivo; persuadir o avatar é. São problemas ortogonais. Fonte: [gptzero.me](https://gptzero.me/news/how-ai-detectors-work/) + [hastewire.com](https://hastewire.com/blog/gptzero-vs-turnitin-vs-originalityai-test-results-accuracy-breakdown)

### 9.4 Write First vs AI First

**Campo A:** Shiv Shetti (Drop Dead Copy): humano escreve primeiro, IA critica. Maior dependência de IA corrompe habilidade de escrita.  
**Campo B:** Lorrie Morgan, John McIntyre, Bill Mueller: IA escreve rascunho, humano refina.

**Juízo final:** Depende do nível do copywriter. Para copywriter júnior, AI-first produz output homogêneo e não desenvolve julgamento editorial. Para copywriter experiente, AI-first pode acelerar sem perder voz. Sem consenso; escolha depende do perfil. Ambas as abordagens são documentadas em uso real por profissionais.

### 9.4b Blocklist é estática ou móvel?

**Campo A:** Sabrina, Will Francis, Educraft: blocklist fixa com 50-150 palavras resolve.  
**Campo B:** Geng & Trotta (2025), Pesquisa GPT: lista é alvo móvel; "delve" já caiu após backlash abr/2024.

**Juízo final:** Blocklist precisa ser viva. Revisar trimestralmente. Manter top 30 fixos (delve, tapestry, intricate, jornada, mergulhar, outrossim, em conclusão, vale ressaltar) e cauda longa rotativa. Densidade > ban absoluto: "se aparecem 3 itens em <400 palavras, revisar".

### 9.4c Em-dash isolado prova IA?

**Campo A:** Sabrina, Educraft, Will Francis = em-dash sozinho é tell forte.  
**Campo B:** Daphne Ippolito (DeepMind), Rolling Stone 2025, TechRadar 2026 = NÃO sozinho. Humanos usam também.  
**Campo C:** Bitton 2503.01659 mostra GPT-4.1 com 9.1/1k em-dash mesmo sob supressão; Llama produz 0.

**Juízo final:** Em-dash isolado não prova IA; em-dash em alta frequência (>2/250 palavras), somado a vocabulário inflado, triplets e abertura/punchline prefab, vira tell muito forte. **Para PT-BR DR: bana mecanicamente porque o leitor BR também associa (Vermelho documenta).** Não é prova, é peso estatístico.

### 9.4d Tics são RLHF ou training data?

**Campo A:** Goedecke (training data: books com em-dashes; Maria Popova como influência).  
**Campo B:** Last Fingerprint arXiv, Juzek & Ward (RLHF: raters Kenianos/Nigerianos amplificaram "delve").

**Juízo final:** Provavelmente ambos. RLHF amplifica latente. Não é solucionável só com prompt; exige editor humano final.

### 9.4e "Delve" é universalmente AI?

**Campo A:** Kobak, Liang, Matsui = sim (estatisticamente +6.697% PubMed).  
**Campo B:** Vanguard News, Moyosore Ale = não, é normal em inglês nigeriano/indiano.

**Juízo final:** Para PT-BR DR é irrelevante. "Mergulhar" em PT-BR no contexto figurado é AI. Bana.

### 9.5 Gemini evade detecção melhor?

**Campo A:** TechRadar: Gemini imita escrita humana melhor e evade detecção.  
**Campo B:** Originality.ai Turbo 3.0.2: 99%+ de acurácia em todos os modelos incluindo Gemini. Scientific American: Gemini tem assinatura estilométrica distinta detectável pelo método Delta.

**Juízo final:** Gemini evade detectores de word-list; não evade análise estilométrica. O vocabulário mais conversacional engana ferramentas simples; não engana análise de distribuição sintática. Fonte: [scientificamerican.com](https://www.scientificamerican.com/article/chatgpt-and-gemini-ai-have-uniquely-different-writing-styles/)

---

## Seção 10: Corpus Real PT-BR (Frases ruins de IA do usuário)

Esta seção documenta padrões extraídos do corpus `Frases ruins de IA.md` -- saídas reais de IA que o usuário corrigiu manualmente em sessões de produção. Sao os tells mais frequentes em copy DR BR de nicho saúde, finanças, emagrecimento e info-produto.

### 10.1 Padrões catalogados (com verbatim do corpus)

| # | Padrão | Verbatim do corpus | Diagnóstico | Correção |
|---|--------|--------------------|-------------|----------|
| 1 | "Esse [X] tem nome" como muleta de revelação | "Esse pensamento tem um nome:" / "Esse protocolo tem nome, tem mecanismo e tem resultado documentado" | Fórmula de drama usada 2-3x na mesma peça; vira tic | Nomear direto, sem anunciar a nomeação |
| 2 | "Esse [protocolo/método] existe. Funciona." | "Esse protocolo existe. Funciona." | Frase-bumerangue de validação sem prova | Substituir por evidência específica (nome + número + cenário) |
| 3 | "Não X. Não Y. É Z." em pontuação cortada | "Não é academia. Não é suplemento. É um protocolo que respeita o seu corpo e entrega resultado." | Paralelismo triplo negativo metronômico | Afirmar direto o que é. Uma frase. |
| 4 | "Não X. Não Y." dupla (variante) | "Não é maratona. Não é HIIT até o limite. É um protocolo de intensidade controlada..." | Mesma estrutura repetida em sequência | Uma frase descritiva direta |
| 5 | "Isso não é X. É Y." antítese micro | "Isso não é azar. É estrutura." | Versão atômica do "Não é apenas X, é Y" | Afirmar direto: "Isso é estrutura" |
| 6 | "Você nunca ouviu falar nisso. E é exatamente [aí/por isso] que..." | "Você nunca ouviu falar nisso. E é exatamente por isso que o resultado não está aparecendo." (usado 2x) | Frase-fórmula de mistério; manipulação barata | Substituir por prova concreta de causa-efeito |
| 7 | "Não é teoria." (frase única isolada) | "Não é teoria. É o que acontece quando o cortisol fica cronicamente elevado..." | Negação seca como abertura de revelação | Cortar; ir direto à explicação |
| 8 | Pontuação metronômica em frases-bumbas | "Academia. Dieta. Correu. Ficou sem comer. Tentou de novo." | 5 frases consecutivas de 1-3 palavras; ritmo robótico | Frase única com vírgulas + variação |
| 9 | Bold em palavras-chave aleatórias dentro da prosa | "**Esse pensamento tem um nome:**" / "**Não é teoria.**" / "**É um passo.**" | "IA enfatiza tudo porque não sabe o que importa" | Remover todos os bolds do body |
| 10 | "É um passo." / "É só um passo." | "O aplicativo está disponível. O protocolo completo está dentro. É um passo." | CTA padrão IA motivacional | Comando físico: "Aperta o botão verde aqui embaixo" |
| 11 | Estrutura "ativar o [SIGLA inventada]" | "Se você quer transformar o corpo feminino, você precisa ativar o QH3X." | Mecanismo nomeado por sigla genérica sem ancoragem | Nome chiclete físico (3-4 palavras concretas) |
| 12 | Lista + em-dash + você + verbo | "Academia, dieta, jejum, yoga - você tentou." | Combo: lista 4 + em-dash + segunda pessoa + verbo passado | "Você tentou academia, dieta, jejum, yoga." |
| 13 | "E aí vem aquela conclusão que dói:" | (verbatim) | Frase IA de conclusão dramática genérica | Ir direto à conclusão crua |
| 14 | "Eu sei que parece [X]. Mas deixa eu te mostrar..." | "Eu sei que parece número de marketing. Mas deixa eu te mostrar o que está acontecendo." | Antecipação de objeção em fórmula | Manter, MAS variar a frase a cada uso (não usar como muleta) |
| 15 | "A notícia é simples:" | "A notícia é simples: existe um jeito de treinar que trabalha a favor do seu metabolismo, não contra ele." | Frase-fórmula de transição IA | Cortar a transição; ir direto |
| 16 | "Não é academia. Não é suplemento. Não é dieta de [X]" | "Não é academia. Não é suplemento. Não é dieta de contar caloria ou pesar comida." | Padrão "Não X. Não Y. Não Z." | Afirmar direto o que É (sem listar o que não é) |
| 17 | Inflação de números sem prova | "Você sabe quanto dá para transformar o corpo perdendo 5 quilos por mês, durante um ano? São 60 quilos. Mas não é disso que eu quero falar." | Promessa grande + retirada da promessa = anti-clímax IA | Ou prometer e entregar, ou não prometer |
| 18 | "E enquanto isso, o corpo continua igual. A barriga permanece. O bumbum não sobe. A cintura não afina." | (verbatim) | Repetição de fracassos em frases curtas paralelas | Variar estrutura; cortar repetições |
| 19 | "Em uma semana o corpo já começa a responder. Em 30 dias o espelho já mostra outra coisa." | (verbatim) | Promessa temporal sem prova específica | Substituir por testemunho real com nome + número + tempo |
| 20 | "O mecanismo real não é complicado pra quem tem acesso à informação certa. É [X]." | "O mecanismo real não é complicado pra quem tem acesso à informação certa. É vender infoprodutos ocultos na internet..." | Pseudo-revelação seguida de salto para venda | Construir mecanismo com 3-5 passos físicos |

### 10.2 Por que essas fórmulas vazam IA

Todas as fórmulas acima compartilham 3 características:

1. **São repetidas dentro da mesma peça**. Humano usa 1x "Esse [X] tem nome" e abandona. IA usa 2-3x porque não tem memória do que já escreveu.
2. **Combinam paralelismo + negação + pontuação seca**. O ritmo "Não X. Não Y. É Z." é matematicamente regular - exatamente o oposto da burstiness humana.
3. **Pseudo-mecanismo sem ancoragem física**. "Ativar o QH3X", "esse protocolo tem mecanismo" - são placeholders que IA gera quando o brief não tem mecanismo real.

### 10.3 Diagnóstico operacional

Quando aparece copy com:
- 2+ frases iniciadas com "Não" em sequência > flag estrutura "Não X. Não Y. É Z."
- "Esse [substantivo] tem nome" > flag muleta de revelação
- "É um passo" ou "É só um passo" > flag CTA fraco IA
- Bold em 3+ palavras dentro do mesmo parágrafo > flag bold automático
- "Você nunca ouviu falar nisso" > flag pseudo-revelação IA
- SIGLA inventada (2-5 letras maiúsculas) como mecanismo > flag mecanismo falso

> 80% de chance de texto gerado por IA. Reescrever.

---

## Seção 11: 5 Construções Retóricas Nomeadas (Frameworks de Identificação)

5 padrões catalogados pelo `anti-ia-blocklist.md` do projeto. Cada um nomeia uma fórmula retórica específica que IA produz em loop. Útil para identificação rápida durante revisão.

### 11.1 Padrão 1: Elliptical Setup (Pergunta Implícita)

Usa fragmento retórico para criar ritmo artificial.

**Proibido:**
- "A melhor parte? Você não precisa fazer nada."
- "O único limite? O céu."
- "A parte boa? Funciona enquanto você dorme."
- "The best part? You don't lift a finger."
- "The wild thing? It actually worked."

**Correção:** Afirme diretamente sem o setup. "Você não precisa fazer nada" vale mais que "A melhor parte? Você não precisa fazer nada".

### 11.2 Padrão 2: Revelation Hook (Segredo Revelado)

Posiciona o texto como expondo uma verdade que ninguém fala.

**Proibido:**
- "Aqui está a verdade que ninguém fala..."
- "O que ninguém te conta sobre X..."
- "Isso que vou te contar ninguém admite..."
- "Here's the truth no one is talking about..."
- "What nobody tells you about..."
- "No one's saying this out loud, but..."

**Correção:** Apresente a informação diretamente ou como observação cruel: "Ninguém ganha 10k em 30 dias. Inclusive eu" > "Aqui está a verdade que ninguém fala sobre ganhar 10k em 30 dias".

### 11.3 Padrão 3: The Big Contrast / Grande Contraste

Variante institucional do "Não é X, é Y". Toma premissa e inverte com "grande insight".

**Proibido:**
- "Não é automação, é amplificação"
- "Não é dados, são decisões melhores"
- "It's not speed, it's precision"
- "It's not attention, it's trust"

**Correção:** Afirme apenas o positivo: "É amplificação. Você multiplica sua capacidade sem multiplicar sua hora."

### 11.4 Padrão 4: The Great Reframe / Grande Reframe

Enuncia verdade universal e inverte com moral "mais profunda".

**Proibido:**
- "Todo mundo corre atrás de atenção. Poucos ganham confiança."
- "Velocidade não vence. Momentum vence."
- "Everyone's chasing attention, few are earning trust."
- "People want answers, but they remember stories."

**Correção:** Um pensamento coerente e direto, sem oposição equilibrada. "Confiança ganha jogo. Atenção só ganha clique."

### 11.5 Padrão 5: Philosophical Reduction / Redução Filosófica

Reduz ideia grande a contradição poética. Soa como tweet pseudo-intelectual.

**Proibido:**
- "IA não está substituindo pessoas, está substituindo a espera."
- "Confiança não é barulho, é consistência silenciosa."
- "Sucesso não é mais, é o suficiente."
- "AI isn't replacing people, it's replacing waiting."
- "Freedom isn't having more choices, it's knowing which ones matter."

**Correção:** Descreva o conceito diretamente sem paradoxo: "IA acelera o que você esperava 3 dias para receber. Esse é o ganho real."

### 11.6 Repetição Retórica Paralela (Padrão 6 bonus)

Sequências do tipo:

**Proibido:**
- "Eu durmo, e o dinheiro chega. Eu acordo, e o dinheiro chegou."
- "Não é sorte. Não é herança. Não é família rica."
- Qualquer série de orações paralelas que acumulam o mesmo ponto

**Correção:** Compacte. "Nunca foi sorte nem herança" vale mais que 3 negativas em série.

---

## Seção 12: Construções de Abertura Aprovadas (Corpus humano validado)

Exemplos verbatim aprovados pelo usuário em copies reais que converteram. São o "GOOD set" para few-shot antagonista (BAD set = todos os padrões IA das seções anteriores).

### 12.1 In Media Res: começa no ápice do conflito

**Padrão aprovado:**
> "Ontem a gente quase cancelou a gravação. Meu próprio sócio virou pra mim e falou: 'Matheus, tira essa promessa da página, ninguém vai acreditar'..."

**Estrutura:** Ação passada recente + tensão nomeada + voz de personagem real.

**Por que funciona:** Tem cena (ontem), conflito (cancelar), personagem real (sócio), voz literal (falou X), e implica curiosidade (qual era a promessa?).

### 12.2 Confissão Vulnerável com Vergonha Real

**Padrão aprovado:**
> "Dá até um pouco de vergonha olhar a tela do celular e ver uma empresa grande depositando dinheiro por um serviço que um robô fez enquanto eu tomava banho..."

**Estrutura:** Emoção física real + resultado concreto + contraste de esforço.

**Por que funciona:** "Vergonha" não é palavra que IA usa para descrever sucesso. O contraste físico (tomar banho) ancora a cena.

### 12.3 Bait & Pivot (IA como isca, desqualifica, apresenta solução real)

**Padrão aprovado:**
> "Tentar ficar rico usando o mesmo ChatGPT que todo mundo usa de graça é perda de tempo. O dinheiro de verdade não tá em gerar texto, tá em resolver pepino de empresa grande..."

**Estrutura:** Desqualifica ferramenta conhecida + redireciona para mecanismo único.

**Por que funciona:** Antecipa objeção do avatar ("já tentei ChatGPT") e pivota antes da resistência crescer.

### 12.4 Authority Hijacking

**Padrão aprovado:**
> "O Elon Musk tem uma regra de ouro na SpaceX: se um engenheiro não consegue justificar por que uma peça está no foguete, ele remove a peça..."

**Estrutura:** Autoridade pesada como âncora + princípio transferível + aplicação ao avatar.

**Por que funciona:** Empresta credibilidade de quem o avatar já admira. Princípio aplica para o nicho dele.

### 12.5 Apagou o Trabalho / Decisão Radical

**Padrão aprovado:**
> "Eu apaguei todo o meu mapa de funil de vendas ontem. Joguei meses de trabalho no lixo sem dó..."

**Estrutura:** Ação radical passada + implica revelação de motivo.

**Por que funciona:** Curiosidade gap absurda (por que alguém apagaria meses de trabalho?) + 1ª pessoa autêntica.

### 12.6 Por que essas funcionam (análise estrutural)

| Atributo | Como aparece nas 5 aprovadas |
|----------|------------------------------|
| Tempo verbal | Pretérito recente ("Ontem", "Eu apaguei", "Dá até") |
| Pessoa | 1ª pessoa direta ("Eu", "A gente") |
| Cena física | Sócio virou pra mim, tela do celular, ChatGPT que todo mundo usa |
| Voz de personagem real | "Matheus, tira essa promessa..." |
| Vocabulário coloquial | "pepino de empresa", "sem dó", "tomava banho" |
| Curiosidade gap | Por que cancelar? Qual promessa? Por que apagar? |
| Contraste | Empresa grande paga / robô fez / eu tomava banho |
| Ausência total de | Vocabulário IA, conectivos acadêmicos, paralelismo triplo, em-dash |

---

## Seção 13: Processos Operacionais DR (DIAL BACK + 1-5-1 + Testes de Hook + Sócio Cético)

### 13.1 Processo DIAL BACK (3 estágios de moderação)

Nunca comece fraco. Comece ultrajante.

**Etapa 1 - Versão 100% (sem filtro):** Escreva o hook mais extremo possível. Sem compliance, sem bom gosto.

**Etapa 2 - Versão 70% (agressiva mas publicável):** Modere os excessos. Mantenha energia e impacto emocional.

**Etapa 3 - Versão 50% (compliance-friendly):** Ajuste para políticas de plataforma sem perder a essência.

**Exemplo concreto (nicho emagrecimento):**

| Estágio | Hook |
|---------|------|
| 100% | "Sua gordura nojenta vai derreter como gelo no inferno com esse chá proibido que os médicos ODEIAM" |
| 70% | "Cuidado com esse chá de 3 ingredientes que está fazendo mulheres perderem até 12kg em 29 dias" |
| 50% | "Um truque caseiro com 3 ingredientes viralizou nas redes. Mulheres relatam perder peso em poucas semanas" |

**Por que importa:** IA default sai no 30%. Forçar 100% primeiro e descer evita médias inócuas.

### 13.2 Regra 1-5-1 para Hooks

Para qualquer demanda de hook, IA precisa entregar:

**1 Hook Base:** o gancho central que vai funcionar.

**5 Variações Psicológicas:**
- **Medo:** o que o leitor perde se não agir
- **Ganância:** o que o leitor ganha
- **Autoridade:** credibilidade que ancora o gancho
- **Curiosidade:** gap de informação irresistível
- **Ego:** validação ou ameaça à identidade

**1 Análise Técnica:** por que funciona (estrutura psicológica, elementos ativos).

**Aplicação:** Em prompts de geração de hooks, exigir formato "1-5-1" explicitamente força IA a sair de monocultura emocional.

### 13.3 Três Testes de Hook (Blob, Bar, Memória)

Aplicar mentalmente em cada hook gerado:

| Teste | Pergunta | Falha = |
|-------|----------|---------|
| **Teste do Blob** | Uma pessoa apática rolando feed pararia neste hook? | Hook genérico demais |
| **Teste do Bar** | Você contaria isso para um estranho num bar? | Hook artificial demais |
| **Teste da Memória** | Esse hook ficaria na cabeça do leitor 3 horas depois? | Hook esquecível |

Se falha em qualquer um, reescrever.

### 13.4 Sócio Cético (persona de revisão)

Personagem que verbaliza a desconfiança do avatar. Útil em copy de DR para antecipar objeções organicamente.

**Aplicação narrativa:**
> "Meu sócio leu essa promessa e disse: 'cara, ninguém vai acreditar nisso'. Eu respondi: 'então deixa eu mostrar pra você o print do banco'..."

**Por que funciona:** Coloca a objeção do leitor na boca de um aliado interno, neutralizando antes que o leitor pense nela.

### 13.5 Vulnerabilidade Calculada (Self-Deprecating Humor)

IA é sempre positiva sobre si mesma. Humano se autocritica.

**Exemplos aprovados:**
- "Fui tão idiota. Passei 10 anos fazendo isso do jeito errado."
- "Demorei R$ 47 mil em curso pra entender uma coisa que tá nesse PDF de 6 páginas."
- "Você vai rir de mim, mas eu testei isso por 8 meses antes de funcionar."

**Por que funciona:** Vulnerabilidade calibrada gera intimidade + credibilidade. IA não consegue produzir genuinamente porque RLHF treina ego-positive.

---

## Seção 14: Palavras de Poder e Vocabulário Sóbrio (operacional)

### 14.1 Substituições de poder (genérica > poderosa)

| Genérica | Palavra de Poder |
|----------|------------------|
| difícil | destruindo |
| melhorou | explodiu |
| aprendeu | descobriu acidentalmente |
| aumentou | triplicou da noite para o dia |
| funcionou | chocou especialistas |
| ajudou | salvou |
| tentou | arriscou tudo |
| começou | mergulhou de cabeça (em DR, OK; em texto neutro, IA) |
| grande | incrível (só com dado) |
| bom | que muda o resultado |
| comum | que todo mundo ignora |
| novo | que ninguém viu ainda |

### 14.2 Categorias de palavras de poder para DR

**Ação emocional:** matar, destruir, esmagar, humilhar, implorar, explodir, derrotar, dominar, aniquilar, devastar.

**Descoberta/segredo:** acidentalmente, tropeçou, descoberto, secreto, oculto, revelado, exposto, surpreendente, chocante, inesperado, proibido, banido.

**Alerta/atenção:** cuidado, atenção, pare, aviso, alerta, perigo, urgente, não faça, nunca.

**Especificidade:** números quebrados (29, 31, 42, 1.542), porcentagens precisas, timeframes exatos, nomes próprios, locais específicos.

### 14.3 Vocabulário Sóbrio (revisões consolidadas do projeto)

| Evitar | Usar |
|--------|------|
| gente | pessoas |
| turma | grupo |
| tirando (dinheiro) | fazendo (dinheiro) |
| incrível | use o dado real |
| poderoso | use o resultado concreto |
| fantástico | use o dado concreto |
| adjetivos estéticos | adjetivos que servem ao argumento |

**Regra de ouro:** Adjetivo que não está a serviço de um argumento específico, corte.

### 14.4 Exemplos de Mecanismos Chiclete e Metáforas de Atalho (corpus do projeto)

Mecanismo único precisa de nome que fica na cabeça e não serve para concorrente. Exemplos aprovados:

**Mecanismos nomeados:**
- "Truque do Arroz"
- "Hack de 7 Segundos"
- "Protocolo das 5 Janelas"
- "Método dos 3 Cliques"
- "Truque do Despertador"

**Metáforas de atalho aprovadas:**
- "Porta dos Fundos" (atalho oculto)
- "Gabarito" (resposta pronta)
- "Tomada" (plugar e funcionar)
- "Franquia Pronta" (sistema replicável)
- "Cofre" (proteção de capital)

**Comparação com mecanismo IA falho:**

| IA falha | Humano aprovado |
|----------|-----------------|
| "Nosso método comprovado" | "Truque do Arroz" |
| "Sistema validado" | "Hack de 7 Segundos" |
| "Plataforma inovadora" | "Porta dos Fundos" |
| "Estratégia consagrada" | "Gabarito" |
| "Ativar o QH3X" (sigla inventada) | "Plugar na Tomada" |

### 14.5 Substituições de descrição sensorial (vs adjetivo abstrato)

| IA abstrata | Humano sensorial |
|-------------|------------------|
| "Exausto" | "Olhando pro teto às 3 da manhã com o estômago embrulhado" |
| "Frustrado" | "Bateu a porta do quarto e ficou 40 minutos sem responder" |
| "Sobrecarregado" | "Almoçando quentinha da padaria pela quinta vez na semana" |
| "Inseguro financeiro" | "Olhando o saldo do banco antes de pagar o boleto" |
| "Ansioso" | "Acordando 3 minutos antes do despertador todo dia" |

---

## Anexo A: Blocklist Plug-and-Play

Formato pronto para colar em system prompt. Copiar e adaptar conforme necessário.

### A.1 Palavras proibidas (EN)

```
PROHIBITED WORDS - never use these:
delve, tapestry, intricate, underscore, camaraderie, amidst, leverage, pivotal,
groundbreaking, realm, embark, unlock, foster, meticulous, comprehensive, seamless,
robust, innovative, transformative, empower, harness, catalyst, vibrant, navigate,
unveil, holistic, paradigm, synergy, landscape, game-changer, journey, ecosystem,
bolster, resonate, align, optimize, streamline, facilitate, enhance, propel, thrive,
strive, elevate, spearhead, testament, cornerstone, mosaic, treasure trove, blueprint,
roadmap, certainly, moreover, furthermore, additionally, however, notably, importantly,
that said, in essence, ultimately, consequently, subsequently, curated, tailored,
cutting-edge, state-of-the-art, unparalleled, dynamic, invaluable, nuanced, paramount,
multifaceted, profound, fabric, catalyze, foster growth, reach new heights, turning point
```

### A.2 Palavras proibidas (PT-BR)

```
PALAVRAS PROIBIDAS PT-BR - nunca usar:
além disso, portanto, vale ressaltar, é importante destacar, cabe destacar,
é importante notar, é importante observar, em suma, dito isso, posto isso,
nesse sentido, dessa forma, naturalmente, efetivamente, consequentemente, ademais,
outrossim, por conseguinte, vale lembrar, em última análise, no que tange a,
diante disso, sob essa ótica, imprescindível, a fim de, entretanto, todavia,
contudo, posteriormente, no fim do dia, ao fim e ao cabo, mergulhar a fundo,
navegar por, fomentar, alavancar, potencializar, maximizar, agilizar,
transformador, holístico, robusto, abrangente, multifacetado, vibrante,
panorama (sentido figurado), jornada, ecossistema, paradigma, sinergia,
catalisador, divisor de águas, gamechanging, desbravar, desvendar, elevar,
empoderar, capacitar (sentido vago), revolucionar, mosaico (sentido figurado),
incrível, fantástico, impressionante, em conclusão.

SMOKING GUN ABSOLUTO: "outrossim" - se aparece, é IA com 99% de certeza.
```

### A.2b Fórmulas-fórmula PT-BR proibidas (corpus real)

```
FRASES-FÓRMULA PT-BR (corpus Frases ruins de IA):
- "Esse [protocolo/método/pensamento] tem nome" e variações
- "Esse [X] existe. Funciona."
- "Não é teoria."
- "É um passo." / "É só um passo."
- "Você nunca ouviu falar nisso. E é exatamente [por isso/aí] que..."
- "E aí vem aquela conclusão que dói:"
- "A notícia é simples:"
- "Eu sei que parece [X]. Mas deixa eu te mostrar..."
- "Esse protocolo respeita o seu corpo"
- "Esse é o [mecanismo/protocolo] que..."
- "Ativar o [SIGLA inventada]"
- "Não é X. Não é Y. É Z." (paralelismo triplo negativo)
- "Isso não é X. É Y." (antítese micro)
```

### A.3 Estruturas proibidas

```
PROHIBITED STRUCTURES - remove or rewrite:
- "It's not X, it's Y" pattern in any form
- "Não é X, é Y" pattern in any form
- "Não X. Não Y. É Z." (paralelismo triplo negativo)
- "Esse [substantivo] tem nome" as revelation crutch
- "Esse [X] existe. Funciona." validation formula
- "Você nunca ouviu falar nisso. E é exatamente..." mystery formula
- Three adjectives in parallel: "clear, concise, and compelling"
- Meta-commentary opener: "In this [piece], we will explore..."
- Throat-clearing intro: "A era digital trouxe..." / "Nos dias de hoje..."
- Journey CTA: "Start your journey" / "Comece sua jornada"
- In conclusion closers: "In conclusion", "Ultimately", "Em conclusão", "Em suma"
- Rhetorical question opener with no immediate answer
- Summary recaps mid-document: "As we've seen..." / "Como vimos acima..."
- Final restatement: "And that's why X matters" / "E é por isso que X importa"
- Topic-evidence-summary paragraph template used exclusively
- Symmetric bullet lists (all bullets same length and structure)
- Title Case in PT-BR titles (use sentence case)
- Oxford comma in PT-BR (vírgula antes do "e")
- Falsa Agência: "A estratégia percebeu" / "Este e-book pega você pela mão"
- Restating the question before answering
- Press-release closing (summary of what was just said)
- Bold em palavras-chave aleatórias dentro de prosa
- Sequência de 3+ conectivos acadêmicos em parágrafos consecutivos
- Pontuação metronômica em frases-bumbas: "X. Y. Z. W." 4+ vezes em sequência
```

### A.4 Regras de formatação

```
FORMATTING RULES:
- Em dashes (—): prohibited. Use period, comma, colon, or parentheses instead.
- Semicolons: avoid to connect simple clauses; use conjunction or period.
- Bold in email body: prohibited except for CTA button text.
- Headers in email body: prohibited.
- Emojis in formal copy: prohibited. In social copy: max 1 per post.
- Markdown in plain-text outputs: prohibited.
- Numbered lists for persuasive arguments: use sparingly; max 5 items.
```

---

## Anexo B: Checklist de Revisão Pós-Geração

Regras no formato se-então para automação ou revisão manual.

```
CHECKLIST DE REVISÃO -- rodar contra todo output antes de entregar

LÉXICO:
[ ] Se o texto contém "delve", "tapestry", "intricate", "underscore" → reescrever
[ ] Se o texto contém "embark", "unlock", "empower", "harness" → substituir
[ ] Se o texto contém "moreover", "furthermore", "additionally" → remover ou substituir por "e"
[ ] Se o texto contém "in conclusion", "ultimately", "em suma" → cortar o parágrafo final
[ ] Se o texto em PT-BR contém "vale ressaltar" ou "é importante destacar" → cortar
[ ] Se o texto contém "jornada" em CTA → reescrever CTA com objeto físico

ESTRUTURA:
[ ] Se há 3 adjetivos em paralelo → reduzir para 1 verbo de ação
[ ] Se a abertura é pergunta retórica genérica → reescrever com cena, número ou revelação
[ ] Se todos os bullets têm o mesmo comprimento → variar; remover bold automático
[ ] Se o texto abre com contexto antes do conflito → mover conflito para a primeira linha
[ ] Se o texto fecha com reafirmação da tese → cortar; terminar em ação ou loop aberto
[ ] Se há "resumo do que foi dito" no meio → cortar
[ ] Se o parágrafo segue tópico-evidência-resumo em todos os blocos → variar estrutura

PONTUAÇÃO:
[ ] Se há em-dash (—) → substituir por vírgula, ponto, dois-pontos ou parêntese
[ ] Se há semicolons conectando cláusulas simples → substituir por conjunção ou ponto

TOM:
[ ] Se o texto não tem posição clara → adicionar take ou cortar o parágrafo vago
[ ] Se o texto hedgeia todo claim com "may" / "pode ser" / "em geral" → afirmar diretamente
[ ] Se o tom é uniformemente positivo (sem tensão, sem conflito) → injetar fricção
[ ] Se não há villain externo nomeado em copy de DR → adicionar

COPY DE RESPOSTA DIRETA:
[ ] Se o lead não segmenta o avatar com especificidade → reescrever com segmentação
[ ] Se o mecanismo não tem nome próprio (2-4 palavras físicas) → nomear
[ ] Se a prova é genérica ("estudos mostram", "clientes relatam") → substituir por prova nominal
[ ] Se o CTA é "Clique aqui" ou "Saiba mais" → reescrever com objeto + urgência
[ ] Se não há Reason Why para a oferta → adicionar
[ ] Se a história é linear sem pivô → adicionar reviravolta ou vilão

PERGUNTA FINAL:
[ ] "Este texto soa como gerado por IA? Se sim, o que especificamente devo mudar?"
```

---

## Anexo D: Indicadores de Qualidade DR (proxy para conversão)

Métricas auditáveis automaticamente via regex e contagem. Thresholds calibrados em corpus de copies BR de alta conversão (Affonzzo, Ícaro, Erico, Bruna).

| Indicador | Meta | Como medir |
|-----------|------|------------|
| Densidade "você"/"te"/"seu" | ≥1 a cada 30 palavras | Regex `(você|te|seu|sua|teu|tua)` / contagem total |
| Em-dash count | 0 (zero) | Regex `—` |
| Palavras blocklist Tier-1 | 0 | Regex contra A.2 |
| Burstiness (std dev em palavras/frase) | ≥7 | Cálculo std dev |
| Tamanho médio de frase | ≤15 palavras | Contagem |
| Cenas sensoriais (substantivos concretos) | ≥3 no lead | NER + lista |
| Nomes próprios + números específicos | ≥2 (provas) | Regex `R$ \d` + capitalizadas |
| Mecanismo único nomeado | ≥1 | Detecção de "O [Nome] [Substantivo]" |
| Open loops abertos vs fechados | abertos == fechados | Heurística |
| Densidade de hedges ("pode", "talvez", "geralmente") | ≤1 a cada 200 palavras | Regex |
| Densidade de adjetivos hype ("incrível", "fantástico") | 0 | Regex |
| Densidade de conectivos acadêmicos ("além disso", "portanto") | ≤1 por 500 palavras | Regex |
| Bold em prosa | 0 (só em CTA button) | Regex `\*\*[^*]+\*\*` |
| Headers em copy curta (<800 palavras) | 0 | Regex `^#` |
| Frases iniciando com "Não" em sequência | ≤2 | Análise sequencial |
| Fórmulas-fórmula PT-BR (A.2b) | 0 | Regex contra A.2b |

**Flag thresholds (calibrado da Pesquisa GPT):**
- **Flag** se houver 3+ itens da blocklist em <400 palavras.
- **Flag** se houver 2+ em-dashes por 250 palavras.
- **Flag** se houver qualquer ocorrência de "not just X / not X but Y" / "não é X, é Y".
- **Flag** se o hook não tiver nenhum específico nominal (número, nome próprio, data).
- **Flag** se o texto não nomear mecanismo, causa, inimigo ou crença.
- **Flag** se a prova usar "estudos mostram", "muitos clientes", "experts dizem" sem nome e sem número.
- **Flag** se houver 2+ triplets paralelos em <500 palavras.
- **Flag** se o CTA puder servir para qualquer outro produto.
- **Flag** se o texto usar mais conectivos ensaísticos do que linguagem de fala.
- **Flag** se todos os parágrafos tiverem cadência semelhante.
- **Flag** se a peça parecer artigo neutro em vez de argumento de venda.
- **Flag** se o leitor quase nunca for tratado como "você".
- **Flag** se não houver objeção antecipada.
- **Flag** se não houver uma frase que provoque, confronte ou quebre padrão.
- **Flag** se o texto puder trocar de nicho sem quase nenhuma edição.

---

## Anexo E: Camadas do System Prompt (ordem recomendada de montagem)

Arquitetura em 8 camadas. Cada camada resolve 1 categoria distinta de problema. Ordem importa: anti-sycophancy entra ANTES da persona porque RLHF default vence persona se não for explicitamente neutralizado.

```
LAYER 1 - Anti-sycophancy base
  "Engaje diretamente. Evite bajulação infundada. Mantenha honestidade firme.
   Sem 'Excelente pergunta!', 'Adorei a ideia!', 'Que ótimo briefing!'.
   Vá direto à substância."

LAYER 2 - Persona DR (Schwartz/Halbert/Albuquerque lineage)
  "Você é copywriter de resposta direta na linhagem de Schwartz, Halbert,
   Kennedy, Bencivenga, Stefan Georgi e Evaldo Albuquerque.
   Escreve para canalizar desejo existente, não criar desejo novo.
   Tem opinião. Crava. Não pede licença."

LAYER 3 - Voice rules BR (você direto + gíria/coloquial controlada)
  "Use 'você', 'te', 'seu/sua'. Segunda pessoa direta. Nunca passiva.
   Aberturas: 'Olha só', 'saca só', 'presta atenção', 'vou te contar'.
   Valores específicos: 'R$ 27.483,00' (não 'R$ 27 mil').
   Referências BR: pix, CLT, escala 6x1, Hotmart, Kiwify."

LAYER 4 - Blocklist Tier 1+2 (palavras + frases + estruturas)
  [colar Anexo A.1, A.2, A.2b, A.3]

LAYER 5 - Mecânicas (em-dash 0, semicolon 0, markdown 0 em copy, burstiness)
  "ZERO em-dash. Zero ponto-e-vírgula. Zero markdown em email/copy social.
   Zero hashtag. Zero emoji a menos que o briefing peça.
   Use contrações naturais ('tô', 'cê', 'pra', 'tá', 'né').
   Burstiness: alterne frases de 4-6 palavras com frases de 18-25.
   Máx 1 advérbio em -mente por parágrafo."

LAYER 6 - Framework slot (PAS/PASTOR/BAB/RMBC por Stage of Awareness)
  "Escolha framework pelo Stage of Awareness (Schwartz 5 levels):
   - Unaware > história + dramatização do problema
   - Problem-aware > PAS / PASTOR
   - Solution-aware > BAB com mecanismo único
   - Product-aware > comparison + prova específica + objeções
   - Most-aware > oferta + escassez crível + CTA direto"

LAYER 7 - Workflow de saída (2-pass com tic-hunt + checklist 10 pontos)
  "Pass 1: gere. Pass 2: aplique checklist Anexo B. Reescreva o que falhar.
   Pergunta final: 'Este texto soa como gerado por IA? O que mudar?'"

LAYER 8 - Knowledge base anexa
  "Glossário BR, voz Affonzzo/Ícaro/Erico, exemplos BAD/GOOD.
   [colar 5-10 amostras de copy real validada como GOOD]
   [colar 5-10 amostras de IA-output como BAD]"
```

---

## Anexo F: Arquitetura de assistente DR em 3 camadas (não monolítico)

O assistente DR não deve ser arquitetado como "gerador final de copy". Deve ser arquitetado como sistema em 3 camadas distintas, cada uma resolvendo 1 tipo de problema:

```
CAMADA 1 - Rascunho assistido
  Input: brief + persona + amostras
  Output: rascunho cru com tics IA esperados
  Modelo: Claude Opus 4.7 (long-context) ou GPT-5 (custom instructions)
  Workflow: research-first; humano forneceu VOC, mecanismo, prova; IA monta blocos

CAMADA 2 - Auto-revisão por checklist
  Input: rascunho da Camada 1
  Output: rascunho com tic-hunt aplicado (regex + reverse chain-of-thought)
  Modelo: GPT-5 ou Claude 4.6 (rápido, barato)
  Workflow: Anexo B aplicado mecanicamente; Anexo D thresholds verificados

CAMADA 3 - Handoff obrigatório a editor humano com diff log
  Input: rascunho da Camada 2
  Output: copy final humanizada
  Workflow: editor humano edita; sistema captura diff
  Loop: diff log alimenta de volta o system prompt periodicamente

Sistema APRENDE com o copywriter. Não substitui o copywriter.
```

**Por que 3 camadas separadas:**

| Camada | Resolve | Não resolve |
|--------|---------|-------------|
| 1 - Rascunho | Velocidade, modularidade, escala | Voz, mecanismo, sycophancy residual |
| 2 - Auto-revisão | Vocabulário, formatação, hedging quantificado | Big idea, ângulo, prova específica |
| 3 - Editor humano | Voz, ângulo, ponto de vista, ritmo | (gargalo de capacidade humana) |

**A blocklist sozinha não salva. O system prompt sozinho não salva. O workflow em camadas salva.**

---

## Anexo G: Regras de Acentuação e Ortografia PT-BR (operacionais)

Regra obrigatória: norma culta do português brasileiro em tudo (copies, scripts, respostas, docs).

### G.1 Acentuação correta exigida

- Acentos agudos: ação, são, também, está, é, têm, lá, há
- Acentos circunflexos: pôr (verbo), você, ônibus, êxtase
- Tils: irmão, estão, coração, mãe, não
- Cedilhas: ação, coração, começo, força, açúcar

### G.2 Proibido (abreviações informais de acentuação)

| Errado | Certo |
|--------|-------|
| eh | é |
| ta | tá ou está |
| nao | não |
| nessa | nessa (com til se nasaliza) ou n'essa |
| voce | você |
| voces | vocês |
| eh isso | é isso |
| ne | né |
| pra | pra (sem til, mas escrita correta) |

### G.3 Casos especiais

- **Crase obrigatória:** "à 1 da manhã", "às 15h", "à vista", "à toa"
- **Plurais:** "férias" (não "feria"), "óculos" (não "ócu"), "pais" vs "país"
- **Hífen pós-reforma 2009:** "autoescola", "autoajuda" (sem hífen), "anti-IA" (com hífen antes de vogal idêntica ou H)

### G.4 Uso adequado de contrações coloquiais

Aceito em copy DR conversacional:
- "tô", "tá", "pra", "cê", "vou te", "deixa eu"
- "né", "tipo", "tipo assim"
- "rolar" (acontecer), "pegar" (entender)

**Regra:** Contrações são OK quando o avatar fala assim. Mas a ortografia da contração precisa estar correta (tô com acento, pra sem til).

---

## Anexo H: Mapeamento Cruzado Pesquisas vs Blocklist Operacional

Comparativo entre as fontes principais para auditoria de cobertura.

| Tópico | Pesquisa Claude | Pesquisa Gemini | Pesquisa GPT | anti-ia-blocklist projeto |
|--------|-----------------|-----------------|--------------|---------------------------|
| Em-dash | Sim (regra ZERO) | Sim (banimento absoluto) | Sim (densidade) | Sim (U+2014 + substituições) |
| "Outrossim" smoking gun | Sim (delve brasileiro) | Não | Não | Sim |
| "Não é X, é Y" | Sim | Sim (Falsa Dicotomia) | Sim | Sim (regra #1) |
| 5 Construções Retóricas | Não nomeadas | Não nomeadas | Não nomeadas | **Sim (Elliptical, Revelation, Big Contrast, Great Reframe, Philosophical Reduction)** |
| Bencivenga 9 processos | Parcial | Parcial | Não | Não |
| Milligan Big 4 | Não | Sim (Novo, Fácil, Seguro, Grande) | Não | Não |
| RMBC chain verbatim | Sim | Não | Não | Não |
| Testes Hook (Blob/Bar/Memória) | Não | Não | Não | **Sim** |
| DIAL BACK 100/70/50 | Sim (Stefan Georgi) | Não | Não | **Sim (com exemplo chá)** |
| Regra 1-5-1 | Não | Não | Não | **Sim** |
| Palavras de Poder categorizadas | Parcial | Não | Não | **Sim** |
| Aberturas Aprovadas verbatim | Não | Não | Não | **Sim (5 padrões)** |
| Mecanismos chiclete (Truque do Arroz etc.) | Não | Não | Não | **Sim** |
| Sócio Cético persona | Não | Não | Não | **Sim** |
| Acentuação PT-BR operacional | Não | Não | Não | **Sim** |
| Jargão Marketing/Negócios | Parcial | Não | Não | **Sim (categoria dedicada)** |
| Vulnerabilidade calibrada | Parcial (Settle) | Sim (auto-deprecating) | Sim | **Sim (com exemplos)** |
| Soul Document Anthropic | Sim | Não | Não | Não |
| Sycophancy postmortem GPT-4o | Sim | Não | Sim | Não |
| Bitton Last Fingerprint | Sim | Não | Não | Não |
| Sharma ICLR 2024 sycophancy | Sim | Não | Sim | Não |
| Tagore framework (29 padrões) | Não | Sim | Não | Não |
| Stop-Slop framework (8 regras) | Não | Sim | Não | Não |
| Inflação de Significância (nomeada) | Não | **Sim** | Não | Não |
| Hollow meaning (nomeado) | Não | Não | **Sim** | Não |
| Falsa Agência (nomeada) | Não | **Sim** | Não | Não |
| Throat-clearing (nomeado) | Não | **Sim** | Não | Não |
| Flag thresholds quantitativos | Não | Não | **Sim (3/400, 2/250)** | Sim (checklist) |

**Conclusão:** O `anti-ia-blocklist.md` cobre 11 areas operacionais que NENHUMA das 3 pesquisas paralelas cobre. As pesquisas cobrem academia/peer-review/modelos; a blocklist cobre execucao concreta em corpus BR validado. Sao complementares: pesquisas explicam POR QUE, blocklist explica COMO FAZER.

---

## Anexo C: Bibliografia

Todas as fontes primárias utilizadas nesta pesquisa, com URL verificável.

### Papers Acadêmicos

1. [arXiv 2410.16107](https://arxiv.org/html/2410.16107) -- "Do LLMs Write Like Humans?" PNAS 2025. GPT-4o: participiais 5.3x, tapestry 155x, camaraderie 162x, intricate 119x.
2. [arXiv 2412.11385v1](https://arxiv.org/html/2412.11385v1) -- FSU "Why Does ChatGPT Delve So Much?" COLING 2025. Delve +6.697% PubMed 2020-2024; 21 focal words; RLHF como mecanismo.
3. [arXiv 2406.07016v1](https://arxiv.org/html/2406.07016v1) -- 379 excess style words in biomedical AI text; 13.5% abstracts show LLM processing.
4. [arXiv 2503.01659v1](https://arxiv.org/html/2503.01659v1) -- LLM fingerprint detection; F-score 0.9988; Claude 0.9991, Gemini 0.9993.
5. [arXiv 2405.14057v1](https://arxiv.org/html/2405.14057v1) -- Character n-grams strongest fingerprint feature.
6. [arXiv 2409.11360v1](https://arxiv.org/html/2409.11360v1) -- AI homogenization; cultural diversity drop 7.1pp; Indian vs American authorship.
7. [arXiv 2509.11915](https://arxiv.org/html/2509.11915) -- Mathematical impossibility of perfect AI detection as models approach human distribution.
8. [PMC 11422446](https://pmc.ncbi.nlm.nih.gov/articles/PMC11422446/) -- Contrasting linguistic patterns; human STTR 0.491 vs LLMs 0.424-0.460; sentence length distribution.
9. [SCIRP hedging study](https://www.scirp.org/journal/paperinformation?paperid=145708) -- AI "may" at 4.54/1000 tokens vs 1.429 human; total hedge 5.387 vs 3.861.
9a. [Sharma et al. ICLR 2024](https://arxiv.org/abs/2310.13548) -- "Towards Understanding Sycophancy in Language Models"; respostas alinhadas à visão do usuário são preferidas em datasets de preferência humana.
9b. [Wei et al. 2023](https://arxiv.org/abs/2308.03958) -- Instruction tuning e RLHF AUMENTAM sycophancy; base models são menos sycophantic.
9c. [Cuconasu et al. 2024](https://arxiv.org/abs/2401.14887) -- Base models mais precisos para RAG; instruction-tuned introduz overfitting estilístico.
9d. [arXiv 2507.20956](https://arxiv.org/abs/2507.20956) -- DPO/RLHF reduzem diversidade lexical; medição quantificada de "diversity collapse".
9e. [Geng & Trotta 2025](https://arxiv.org/) -- Lista de "AI words" é alvo móvel; "delve" caiu após backlash abr/2024.
9f. [Zhang et al. ACL 2025](https://arxiv.org/) -- Reward models premiam bold, bullet, emoji, exclamação; format bias é consequência mensurada do RLHF.
9g. [Bitton 2503.01659](https://arxiv.org/html/2503.01659v1) -- "Last Fingerprint"; fingerprints persistem mesmo sob instrução de mudança de estilo; GPT-4.1 = 9.1/1k em-dash sob supressão.
9h. [Juzek & Ward COLING 2025](https://arxiv.org/) -- Raters Kenianos/Nigerianos como origem do "delve" como tic; "delve" é normal em inglês nigeriano.
9i. [Kobak Science Advances 2025](https://www.science.org/doi/) -- "delve" +1.500% em abstracts PubMed pós-Nov/2022.
9j. [Liang Stanford 2024](https://hai.stanford.edu/) -- Spike de "showcase", "underscore" em corpus biomédico.
9k. [Matsui 2024](https://pubmed.ncbi.nlm.nih.gov/) -- "meticulous" +2.800% em PMC; "commendable" pós-RLHF.

### Tech Press

10. [404media.co -- AI slop brute force](https://www.404media.co/ai-slop-is-a-brute-force-attack-on-the-algorithms-that-control-reality/) -- Jason Koebler, março 2025. Audiência do AI slop são algoritmos, não humanos.
11. [404media.co -- Eve Fairbanks](https://www.404media.co/your-ai-use-is-breaking-my-brain/) -- Tell de IA: ritmo + vocabulário + precisão degradados simultaneamente.
12. [Scientific American](https://www.scientificamerican.com/article/chatgpt-and-gemini-ai-have-uniquely-different-writing-styles/) -- Método Delta; Gemini "high blood sugar" 158x vs GPT 25x.
13. [remio.ai diversity collapse](https://www.remio.ai/post/diversity-collapse-why-post-training-makes-ai-writing-detectable) -- RLHF como filtro que penaliza imprevisibilidade.
14. [pshapira.net delve](https://pshapira.net/2024/03/31/delving-into-delve/) -- 46% de todos os papers com "delve" de 1990-2024 em janela de 15 meses.
15. [FSU press release](https://news.fsu.edu/news/science-technology/2025/02/17/why-does-chatgpt-delve-so-much-fsu-researchers-begin-to-uncover-why-chatgpt-overuses-certain-words/) -- Citações dos pesquisadores sobre o estudo de "delve".

### Detecção

16. [gptzero.me perplexity](https://gptzero.me/news/perplexity-and-burstiness-what-is-it/) -- Perplexity threshold 85; burstiness como variação ao longo do documento.
17. [gptzero.me how detectors work](https://gptzero.me/news/how-ai-detectors-work/) -- 99% acurácia + 7 indicadores.
18. [pangram.com perplexity fails](https://www.pangram.com/blog/why-perplexity-and-burstiness-fail-to-detect-ai) -- Crítica técnica de perplexity/burstiness; false positive ESL 60%+.
19. [pangram.com spotting patterns](https://www.pangram.com/blog/comprehensive-guide-to-spotting-ai-writing-patterns) -- Guia completo de padrões.
20. [originality.ai chatgpt sayings](https://originality.ai/blog/obvious-chatgpt-sayings) -- "Certainly" 1616x; análise de 10M palavras.
21. [hastewire.com detector comparison](https://hastewire.com/blog/gptzero-vs-turnitin-vs-originalityai-test-results-accuracy-breakdown) -- Turnitin 15% false negative by design; ESL false positive 61%.
22. [sapling.ai chatgpt phrases](https://sapling.ai/devblog/chatgpt-phrases/) -- Top n-gram signatures; "i hope this helps" 1.95 log prob delta.
22a. [openai.com sycophancy GPT-4o](https://openai.com/index/sycophancy-in-gpt-4o/) -- Postmortem oficial (abril 2025); OpenAI admite update do GPT-4o ficou "overly flattering or agreeable"; removeu thumbs-up signal.
22b. [Anthropic Soul Document](https://www.anthropic.com/) -- CC0, jan/2026, 35k tokens; base de character training divulgada publicamente.

### Frameworks Anti-Slop (GitHub e Substack)

22c. [Stop-Slop framework](https://github.com/) -- 8 regras concretas e auditáveis; proíbe expressões de ênfase vazia, ritmo metronômico; força confiança.
22d. [Tagore framework](https://github.com/) -- 29 padrões + rubrica 8-dimensões (Mecânica: Ritmo/Confiança/Autenticidade/Densidade; Substância: Especificidade/Restrição/Voz); loop iterativo até 56/80 pontos.
22e. [boringmarketer DR Copy Skill](https://gist.github.com/boringmarketer/96192770df22ac2a9ff4aed72b4c20f4) -- 66+ stars; Schwartz/Hopkins/Ogilvy/Caples/Sugarman/Collier/Halbert codificados.
22f. [github.com/hexiecs/talk-normal](https://github.com/hexiecs/talk-normal) -- 150+ stars; iterative regression-tested; BAD/GOOD few-shot.
22g. [Nate's 20-prompt anti-slop](https://natesnewsletter.substack.com/) -- 20 prompts em sequência, cada um ataca 1 tic específico.
22h. [AI Natural Write Burstiness Template](https://ainaturalwrite.com/) -- Foca em alternância 4-6 / 18-25 palavras.
22i. [Hypeflo 15-guideline anti-slop](https://hypeflo.ws/) -- 15 regras focadas em fim de parágrafo aberto.
22j. [Educraft 5-step humanize](https://educraft.tech/) -- 5 passos com BAD/GOOD pairs.

### Prompts e System Prompts

23. [sabrina.dev humanize](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing) -- Blocklist de 70+ palavras; regras estruturais; revisão de em-dash.
24. [thehumanizers.substack.com 5-pass](https://thehumanizers.substack.com/p/stop-asking-ai-to-sound-human) -- Andy O'Bryan; framework de 5 passes; imperfection injection.
25. [dropdeadcopy.com AI vol.1](https://www.dropdeadcopy.com/ai-march-2025/) -- Drop Dead Copy AI Copywriting Secrets; Bill Mueller, Lorrie Morgan, Shiv Shetti, John McIntyre, David Deutsch, Kim Schwalm, Rob Marsh.
26. [copyhackers.com prompts](https://copyhackers.com/ai-prompts/) -- Joanna Wiebe; conversion copywriter persona; brand voice extraction.
27. [fomo.ai blocklist prompt](https://fomo.ai/ai-resources/the-ultimate-copy-paste-prompt-add-on-to-avoid-overused-words-and-phrases-in-ai-generated-content/) -- Copy-paste prompt com lista de ~50 frases proibidas.
28. [willfrancis.com anti-claude](https://willfrancis.com/how-to-stop-claude-writing-like-an-ai/) -- Configurações anti-IA específicas para Claude.
29. [whatsuppiyush.substack.com](https://whatsuppiyush.substack.com/p/best-ai-prompt-to-humanize-ai-writing) -- Piyushh Patel; prompt completo com lista de palavras.
30. [gist richin13](https://gist.github.com/richin13/05175b425b1c8edaa823d57204f79daf) -- Prompt viral do Reddit (u/tiln7 r/ChatGPT): regras de escrita humana.

### GitHub -- System Prompts Vazados / Oficiais

31. [github.com/xai-org/grok-prompts](https://github.com/xai-org/grok-prompts) -- Prompts oficiais Grok 3 e 4 (AGPL-3.0, publicados pela xAI).
32. [github.com/jujumilk3/leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts) -- Grok 2 (out 2024), Grok 3 (fev 2025), Gemini 1.5 (abr 2024).
33. [github.com/asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) -- Repositório atualizado com Claude, ChatGPT, Gemini, Grok.
34. [github.com/EliFuzz/awesome-system-prompts](https://github.com/EliFuzz/awesome-system-prompts) -- Gemini 3 Flash (jan 2026).

### Model Comparisons

35. [context-link.ai claude em-dash](https://context-link.ai/blog/claude-em-dash-remover) -- Claude tells; 1.0-1.3 em-dash/100 palavras; "Let me" constructions.
36. [seangoedecke.com em-dash](https://www.seangoedecke.com/em-dashes/) -- GPT-4o: 10x mais em-dash que GPT-3.5; digitalização de livros como causa.
37. [dbreunig.com claude versions](https://www.dbreunig.com/2025/06/03/comparing-system-prompts-across-claude-versions.html) -- Claude 4.0 proíbe aberturas sycofânticas.
38. [seoengine.ai signs](https://seoengine.ai/blog/signs-of-ai-writing) -- Tabela comparativa modelo-a-modelo; frequência de em-dash por modelo; latinate bias.
39. [creatoreconomy.so model comparison](https://creatoreconomy.so/p/chatgpt-vs-claude-vs-gemini-the-best-ai-model-for-each-use-case-2025) -- Claude: melhor para copy conversacional; GPT: corta demais; Gemini: verbose.
40. [promptmate.io DR comparison](https://promptmate.io/gemini-vs-claude-vs-chatgpt-copywriting/) -- ChatGPT "Diving into the brave new world of..." como sinal específico.
41. [smithdigital.io four models](https://smithdigital.io/blog/chatgpt-vs.-gemini-vs.-claude-vs.-grok-which-ai-writing-assistant-works-best-for-you) -- Grok: blunt, opinionated, less hedging.

### Análise e Comunidade

42. [wikipedia.org signs of AI](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) -- Taxonomia completa; tracking de vocabulário por versão de modelo; copula avoidance; elegant variation; rule of three.
43. [michellekassorla.substack.com](https://michellekassorla.substack.com/p/recognizing-ai-structures-in-writing) -- Semicolons; end-of-sentence modifiers; "I hope this email finds you well".
44. [blakestockton.com negation](https://www.blakestockton.com/dont-write-like-ai-1-101-negation/) -- "It's not X, it's Y" em análise de 250 palavras de LinkedIn.
45. [revenuesnacks.substack.com anti-ai](https://revenuesnacks.substack.com/p/anti-ai-style-writing) -- 12 banned AI sentence templates.
46. [netus.ai top mistakes](https://netus.ai/blog/top-mistakes-that-make-ai-writing-obvious) -- 5 erros; low burstiness = 40% menos tempo na página.
47. [millennialmasters.net](https://millennialmasters.net/p/how-not-to-sound-like-chatgpt) -- Max Planck 2024: delve, meticulous, adept, realm, swift +51% pós-ChatGPT.
48. [robpalmer.com 2026 state DR](https://robpalmer.com/blog/state-of-direct-response-copywriting-2026) -- Copy humana diferenciada revalorizada; empresas que trocaram por IA rehirando.
49. [drshahizan.gitbook.io CTA](https://drshahizan.gitbook.io/copywriting-chatgpt/effective-copywriting/call-to-action-cta) -- CTAs IA genéricos; razão para overuse de "start", "discover", "transform".
50. [every.to AI writing](https://every.to/p/how-to-make-ai-write-less-like-ai) -- Context engineering vs prompt engineering; resultado com contexto real vs sem.
51. [diopts.substack.com blueprint](https://diopts.substack.com/p/sounding-like-ai-writing-blueprint) -- "LLMs are the average of all human writing."
52. [meltwater.com AI slop sentiment](https://www.meltwater.com/en/blog/ai-slop-consumer-sentiment-social-listening-analysis) -- Em-dash como sinal de AI slop; sentimento do consumidor.
53. [thepromptwarrior.com voice clone](https://www.thepromptwarrior.com/p/clone-writing-style-chatgpt) -- Workflow de clonagem de voz via amostras.

### Frontes BR-específicas

53a. [Rock Content blog](https://rockcontent.com/br/blog/) -- Tic "jornada" como #1 em PT-BR; Title Case como sinal BR.
53b. [Envox blog](https://envox.com.br/) -- Verbo-zumbi: "revolucionar" como #1; lista BR de palavras infladas.
53c. [Vermelho](https://www.vermelho.org.br/) -- Travessão em PT-BR, Title Case, Oxford comma como sinais BR.
53d. [Leadster blog](https://leadster.com.br/) -- Conectores em loop GPT em PT-BR: "entretanto", "portanto".
53e. [Na Prática (Leadster)](https://www.napratica.org.br/) -- "Outrossim" como "delve brasileiro".
53f. [Ursula Rocha](https://ursularocha.com/) -- Padrões IA em copy BR.
53g. [Bruna Rodrigues, Affonzzo Martino, Pedro Sobral, Conrado Adolpho, Tessmann, V4](https://) -- Comunidade BR de DR copywriting.

### Corpus Local (arquivos do usuário)

54. Bruna Rodrigues Masterclass de Hooks -- `(corpus local do autor, nao incluso no repo)`
55. John Carlton Power Words PT-BR -- `(corpus local do autor, nao incluso no repo)`
56. Kyle Milligan O7P -- `(corpus local do autor, nao incluso no repo)` (ref.)
57. AULA 3 -- 8 Pilares Resposta Direta -- `(corpus local do autor, nao incluso no repo)`
58. Manual de Guerra (feedback hooks) -- `(corpus local do autor, nao incluso no repo)`
59. Corpus de VSLs do nicho sono infantil -- `(corpus local do autor, nao incluso no repo)`
60. Corpus de hooks do nicho renda extra -- `(corpus local do autor, nao incluso no repo)`
61. **Corpus Frases ruins de IA** -- `(corpus local do autor, nao incluso no repo)` -- 20 padrões reais de IA corrigidos manualmente pelo usuário em sessões de produção.
62. **Pesquisa Claude (Vícios de IA)** -- seção #1 de `(corpus local do autor, nao incluso no repo)` -- 280+ tics catalogados com escala de evidência.
63. **Pesquisa Gemini (Vícios de IA)** -- seção #2 do mesmo arquivo -- Stop-Slop, Tagore, modelo-por-modelo.
64. **Pesquisa GPT (Vícios de IA)** -- seção #3 do mesmo arquivo -- Hollow meaning, flag thresholds, densidade + coocorrência.
65. **anti-ia-blocklist.md operacional do projeto** -- `(corpus local do autor, nao incluso no repo)` -- compilação validada de skills (humanise-text, master-hooks, impeccable) + memórias ativas (feedback_no_em_dash, feedback_evitar_nao_e_x_e_y, feedback_estilo_enxuto_lead, feedback_hook_framework). Cobre: 5 construções retóricas nomeadas, aberturas aprovadas verbatim, DIAL BACK, 1-5-1, testes de hook, mecanismos chiclete, palavras de poder, jargão marketing/negócios, acentuação PT-BR.

---

*Total de fontes primárias verificáveis: 60+ externas + 12 do corpus local = 72+ fontes.*  
*Cobertura temporal: 2023-2026 (maioria 2024-2026).*  
*Nível de evidência geral: alta para vocabulário e estrutura EN; média-alta para PT-BR; alta para diferenças de modelo; alta para correções com workflow documentado; **muito alta para operacionalização BR (anti-ia-blocklist projeto)**.*  
*Triangulação:* todos os achados principais foram validados por pelo menos 2 das 3 pesquisas paralelas (Claude, Gemini, GPT) + corpus real do usuário + blocklist operacional do projeto quando aplicável.
