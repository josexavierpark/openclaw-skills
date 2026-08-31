# Fase 6: Revisor Anti-AI-Slop

## Objetivo

Auditar cada par (falado + texto na tela) contra a blocklist quantitativa. Reescrever pares que disparem flags. Marcar como APROVADO os que passam limpos. Esta fase é obrigatória e não-negociável.

## Inputs

- Todos os pares falado+texto da Fase 5
- Consulta obrigatória a:
  - `references/antislop-blocklist.md` (palavras + fórmulas-fórmula proibidas)
  - `references/antislop-smoking-guns.md` (25 padrões estruturais)
  - `references/antislop-5-construcoes.md` (Elliptical, Revelation, Big Contrast, Great Reframe, Philosophical Reduction)
  - `references/antislop-checklist.md` (regras se-então adaptadas pra hook curto)

## Checklist de auditoria (executar em cada par)

Para cada par falado + texto na tela, rodar nesta ordem:

### 1. Em-dash (—)

- **Threshold:** 0 ocorrências obrigatório
- **Regex mental:** procura por `—`
- **Ação se flagar:** substituir por vírgula, ponto, dois-pontos ou parênteses
- **Memória:** `feedback_no_em_dash.md`

### 2. Palavras da blocklist

- **Threshold:** 0 ocorrências
- **Lista crítica que SEMPRE flaga:**
  - jornada, mergulhar, alavancar, empoderar, capacitar (sentido vago), fomentar
  - transformador, holístico, robusto, abrangente, multifacetado, vibrante, dinâmico, intricado
  - panorama (figurado), ecossistema, paradigma, sinergia, catalisador, divisor de águas, mosaico (figurado)
  - outrossim, vale ressaltar, é importante destacar, cabe destacar, em suma, dessa forma, naturalmente, posteriormente
  - incrível, fantástico, impressionante (sem dado concreto), descubra agora, garante sua vaga
- **Ação se flagar:** substituir por equivalente coloquial. Ver tabela em `references/antislop-blocklist.md`

### 3. Fórmulas-fórmula PT-BR

- **Threshold:** 0 ocorrências
- **Padrões que sempre flagam:**
  - "Não é X, é Y" (em qualquer variante: "Não X. Não Y. É Z.", "It's not X, it's Y", "Não é só X, é Y")
  - "Esse [protocolo/método/pensamento] tem nome:" como muleta de revelação
  - "Esse [X] existe. Funciona." (validação sem prova)
  - "A verdade que ninguém [te conta/fala/admite]"
  - "Aqui está a verdade que ninguém fala"
  - "Você nunca ouviu falar nisso. E é exatamente por isso..."
  - "E aí vem aquela conclusão que dói:"
  - "A notícia é simples:"
- **Ação se flagar:** reescrever a frase de forma direta, sem o setup retórico
- **Memória:** `feedback_evitar_nao_e_x_e_y.md`

### 4. As 5 construções retóricas proibidas

Ver `references/antislop-5-construcoes.md`. Resumo:

| Construção | Exemplo do padrão | Como reescrever |
|---|---|---|
| Elliptical Setup | "A melhor parte? Você não precisa fazer nada." | Afirme direto: "Você não precisa fazer nada." |
| Revelation Hook | "Aqui está a verdade que ninguém fala..." | Vá direto na informação |
| Big Contrast | "Não é automação, é amplificação" | Afirme só o positivo |
| Great Reframe | "Todo mundo corre atrás de X. Poucos ganham Y." | Um pensamento direto |
| Philosophical Reduction | "IA não está substituindo pessoas, está substituindo a espera" | Descreva direto sem paradoxo |

- **Threshold:** 0 ocorrências de qualquer das 5
- **Ação se flagar:** reescrever segundo a correção da tabela acima

### 5. Acentuação PT-BR

- **Threshold:** 100% correto (norma culta)
- **Erros frequentes a checar:**
  - "está" (não "esta" como verbo)
  - "é" (não "e")
  - "câmara/câmera"
  - "pé", "café", "vídeo"
  - "também"
  - "tá", "pô", "cê" (mantêm acento gráfico quando aplicável)
- **Ação se flagar:** corrigir o acento
- **Memória:** `feedback_acentuacao_pt_br.md`

### 6. Hedging crônico

- **Threshold:** 0 hedges desnecessários
- **Palavras-flag:** "pode ser que", "talvez", "em geral", "geralmente", "possivelmente"
- **Ação se flagar:** remover ou substituir por afirmação direta. Hook precisa de convicção, não de probabilidade.

### 7. "Eu/meu" sem justificativa

- **Threshold:** preferir "você/seu/sua"
- **Quando "eu/meu" é OK:** estrutura é Vulnerabilidade declarada e o contraste exige (ex: "Pelo último mês eu estive em uma das piores fases da minha vida")
- **Quando não é OK:** "Eu vou te ensinar", "No meu treino eu...", "Minha experiência mostra" → reescreva pra "Você vai aprender", "Olha esse treino", "O que acontece é"

### 8. Title Case PT-BR

- **Threshold:** 0 ocorrências
- **Onde olhar:** texto na tela principalmente. Sentence case obrigatório, exceto no nome do mecanismo nomeado.
- **Ação se flagar:** converter pra sentence case

### 9. Generic CTA / pseudo-pergunta

- **Threshold:** 0 ocorrências
- **Padrões-flag:** "Pronto pra?", "Já parou pra pensar?", "Quer saber como?", "Você gostaria de?"
- **Ação se flagar:** trocar por pergunta específica ou afirmação

### 10. Substantivo SIGLA inventado como mecanismo

- **Threshold:** 0 ocorrências
- **Padrão-flag:** mecanismos como "ativar o QH3X", "sistema ABC-7", "protocolo XYZ"
- **Por quê:** sigla inventada não tem ancoragem física. Hook fica abstrato.
- **Ação se flagar:** trocar por nome chiclete sensorial. "Truque do Aperto", "Janela das 14h", "Brecha do Pix Silencioso".

## Output esperado

Para **cada par auditado**, produza:

```
**[Estrutura X] / Variação Y:**

- Falado original: <texto>
- Texto na tela original: <texto>

Auditoria:
- Em-dash: <ok | flag + correção>
- Blocklist: <ok | flag em "<palavra>" + correção>
- Fórmulas-fórmula: <ok | flag em "<trecho>" + correção>
- 5 construções: <ok | flag tipo <nome> + correção>
- Acentuação: <ok | flag em "<palavra>" + correção>
- Hedging: <ok | flag + correção>
- Eu/meu: <ok | flag + correção>
- Title Case: <ok | flag + correção>
- CTA genérica: <ok | flag + correção>
- Sigla inventada: <ok | flag + correção>

Status: <APROVADO | REESCRITO>

Versão final:
- Falado: <texto final, igual ao original se aprovado, ou reescrito>
- Texto na tela: <texto final>
```

Ao final de todos os pares, imprima:

```
**Resumo da auditoria:**
- Total de pares: <N>
- APROVADOS sem mudança: <N>
- REESCRITOS: <N>
- Flags disparados: <contagem total>

Seguindo pra Fase 7 (Apresentador Final).
```

## Checkpoint

Esta fase **não pausa**. Avance direto pra Fase 7 com os pares finais.

## Regra de reescrita

Quando reescrever, faça **correção mínima** preservando intenção, tom e estrutura. Não reescreva o hook inteiro se só uma palavra dispara flag. Troque a palavra ou substitua o trecho específico.

Se 3+ flags dispararem no mesmo par, o hook tem problema estrutural; reescreva inteiro mas mantenha a estrutura do método (Vidente continua Vidente, não vira Contrário).

## Heurística final

Antes de aprovar qualquer par, faça o teste final:

> Se eu mostrasse esse hook pra um amigo carioca/paulista numa mesa de bar, ele riria de mim ou faria cara de "interessante"?

Se o teste mental falhar, o hook ainda tá com cara de IA. Reescreva.
