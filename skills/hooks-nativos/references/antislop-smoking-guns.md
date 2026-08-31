# 25 Smoking Guns Estruturais (anti-AI-slop)

Padrões de frase, estrutura e formato que denunciam IA mesmo quando o vocabulário está limpo. Adaptado pra contexto de hook curto.

Fonte: `AI-Research/ai-tells-deep-research.md` (Seção 2 + Anexo A.3).

---

## Tabela de detecção rápida

| # | Padrão | Sinal | Como reescrever |
|---|---|---|---|
| 1 | Negação tripla "Não X. Não Y. É Z." | 3 frases paralelas em sequência negando | Afirme só o positivo |
| 2 | Grande dicotomia "Não é X, é Y" | Antítese binária em qualquer forma | Afirmação direta |
| 3 | Revelação falsa "Aqui está a verdade que ninguém fala" | Setup de segredo genérico | Vá direto na informação |
| 4 | Pergunta implícita "A melhor parte?" | Fragmento retórico sem resposta imediata | Afirme sem o setup |
| 5 | "Você nunca ouviu falar nisso" | Pseudo-revelação condescendente | Conte a coisa sem assumir desconhecimento |
| 6 | "Esse [X] tem nome" como muleta | Anúncio de nomeação | Nomeie direto sem o setup |
| 7 | "Esse [X] existe. Funciona." | Validação sem prova | Mostre a prova específica |
| 8 | "É um passo" / "É só um passo" | CTA fraco IA | Comando físico + benefício imediato |
| 9 | Triplo paralelismo adjetival | "X, Y e Z" com 3 adjetivos seguidos | Use 1 verbo de ação |
| 10 | Frase metronômica curta repetida | "X. Y. Z. W." 4+ vezes em sequência curta | Varia o tamanho das frases |
| 11 | Bold em palavras aleatórias | Ênfase sem hierarquia | Tire o bold ou foca em 1 frase-chave |
| 12 | "Ativar o [SIGLA inventada]" | Mecanismo por sigla genérica | Use nome chiclete sensorial |
| 13 | Em-dash (—) frequente | Qualquer ocorrência | Substituir por vírgula, ponto, dois-pontos, parênteses |
| 14 | Ponto-e-vírgula em cláusulas simples | ; como conjunção | Use "e" ou ponto |
| 15 | Throat-clearing intro "No mundo atual..." | Abertura genérica | Cena ou afirmação direta |
| 16 | Title Case em PT-BR | "Como Melhorar Seu Treino" | Sentence case |
| 17 | Vírgula Oxford em PT-BR | "X, Y, e Z" | "X, Y e Z" |
| 18 | CTA "Comece sua jornada" | "Jornada" = sinal IA | "Quero meu acesso", "Pega o teu" |
| 19 | Falsa agência | "A estratégia percebeu", "Este vídeo te leva" | Sujeito agente real |
| 20 | Estilo "wire-copy" / validação dos dois lados | "Embora X tenha méritos, Y também é válido" | Tome posição |
| 21 | Tic-hunt "Esse protocolo respeita seu corpo" | Pseudo-validação vazia | Mostre o que faz especificamente |
| 22 | Frase-fórmula repetida 2+ vezes | "Não é teoria" / "É um passo" várias vezes | Use uma vez ou nenhuma |
| 23 | "E aí vem aquela conclusão que dói:" | Transição dramática genérica | Vá direto na conclusão |
| 24 | "A notícia é simples:" | Frase-fórmula de conclusão | Apresente a informação |
| 25 | Restating the question | Repete a pergunta antes de responder | Responde direto |

---

## Como detectar em hook curto (regras adaptadas)

### Padrões mais frequentes em hook

**Mais comum em hook:**
- #2 (Não é X, é Y) - regra absoluta
- #3 (revelação falsa) - usado pra abrir
- #5 ("você nunca ouviu") - condescendência
- #6 ("esse X tem nome") - como muleta de mecanismo
- #13 (em-dash) - smoking gun universal
- #16 (Title Case PT-BR) - em texto na tela
- #18 (CTA com "jornada") - em CTA final

**Menos comum em hook (mas ainda check):**
- #15 (throat-clearing) - hook não tem espaço pra isso, mas pode aparecer
- #20 (wire-copy) - raro em hook, comum em descrição

### Detecção rápida

Antes de aprovar um par, faça 3 perguntas:

1. **Tem em-dash?** Se sim, flag #13.
2. **Tem "Não é X, é Y" em qualquer forma?** Se sim, flag #2.
3. **Tem palavra da blocklist?** Se sim, flag (ver `antislop-blocklist.md`).

Se passou pelas 3, faça a leitura mental do hook em voz de carioca/paulista de bar. Se soa robotizado em qualquer momento, volta e identifica qual dos 25 padrões disparou.

---

## Exemplos verbatim do corpus

### Smoking gun #1 (Negação tripla)
❌ "Não é academia. Não é suplemento. É um protocolo."
✔️ Afirme só o positivo: "É um protocolo que dispensa academia e suplemento."

### Smoking gun #2 (Grande dicotomia)
❌ "Não é velocidade, é momentum."
✔️ Afirmação direta: "Momentum vence velocidade no longo prazo."

### Smoking gun #3 (Revelação falsa)
❌ "Aqui está a verdade que ninguém fala sobre ganhar 10k em 30 dias..."
✔️ Direto: "Ninguém ganha 10k em 30 dias. Inclusive eu."

### Smoking gun #4 (Pergunta implícita)
❌ "A melhor parte? Você não precisa fazer nada."
✔️ "Você não precisa fazer nada."

### Smoking gun #6 ("Esse X tem nome")
❌ "Esse pensamento tem um nome: ansiedade antecipatória."
✔️ "Ansiedade antecipatória. É isso que tá te travando."

### Smoking gun #12 (SIGLA inventada)
❌ "Ative o QH3X."
✔️ "Aciona o Truque do Aperto."

### Smoking gun #16 (Title Case PT-BR)
❌ "Como Acelerar Seu Treino em 7 Dias"
✔️ "Como acelerar seu treino em 7 dias"

### Smoking gun #18 (CTA "jornada")
❌ "Comece sua jornada de transformação."
✔️ "Quero meu acesso vitalício agora."

---

## Cross-reference

Para detalhamento de cada padrão e exemplos adicionais, consulte:

- `AI-Research/ai-tells-deep-research.md` Seção 2 (banco de frases-cacoete)
- `AI-Research/ai-tells-deep-research.md` Seção 11 (5 construções retóricas - ver também `antislop-5-construcoes.md`)
- `AI-Research/ai-tells-deep-research.md` Anexo A.3 (estruturas proibidas consolidadas)
