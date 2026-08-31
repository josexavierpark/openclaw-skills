# Checklist anti-AI-slop pós-geração (adaptado pra hook curto)

Versão operacional do Anexo B do `ai-tells-deep-research.md`, filtrada e adaptada pra context de hook de vídeo curto. Regras se-então pra Fase 6 (Revisor Anti-AI-Slop).

---

## Como usar

Rodar em ordem contra cada par (falado + texto na tela). Se qualquer regra dispara, **flag** + correção. Marcar par como REESCRITO ou APROVADO no final.

---

## Bloco A: léxico

1. **Se** contém "jornada", "mergulhe", "alavanque", "empodere", "transformador", "outrossim", "vale ressaltar" → **flag** + substituir pela coluna direita da tabela em `antislop-blocklist.md`

2. **Se** contém "descubra agora", "garante sua vaga", "embarque" → **flag** + reescrever com comando físico específico

3. **Se** contém "intricado", "abrangente", "holístico", "robusto", "multifacetado" → **flag** + substituir por palavra direta

4. **Se** contém "incrível", "fantástico", "impressionante" SEM dado concreto que justifique → **flag** + substituir por specifico ou cortar

5. **Se** em hook em inglês: contém "delve", "tapestry", "embark", "unlock", "leverage", "harness" → **flag** + substituir

---

## Bloco B: estrutura

6. **Se** tem 3 adjetivos em paralelo ("rápido, fácil e eficaz") → **flag** + reduzir pra 1 verbo de ação

7. **Se** abertura é pergunta retórica genérica ("Você já parou pra pensar?", "Já se perguntou?") → **flag** + reescrever com cena, número ou afirmação contra-intuitiva

8. **Se** o falado começa com contexto antes de declarar tema → **flag** + mover tema pra primeira frase

9. **Se** há "Não é X, é Y" em qualquer forma (inclusive "Não X. Não Y. É Z." e "Isso não é X. É Y.") → **flag** + reescrever como afirmação direta. Memória `feedback_evitar_nao_e_x_e_y.md`.

10. **Se** há "Esse [protocolo/método/pensamento] tem nome:" como muleta → **flag** + nomeie direto sem o setup

11. **Se** há "A melhor parte?", "O único limite?", "O segredo?" como fragmento retórico → **flag** + afirmar direto

12. **Se** há "Aqui está a verdade que ninguém fala" ou variantes → **flag** + apresentar a info direto

---

## Bloco C: pontuação

13. **Se** há **em-dash (—)** em qualquer posição → **flag** + substituir por vírgula, ponto, dois-pontos ou parênteses. Memória `feedback_no_em_dash.md`. **REGRA INVIOLÁVEL.**

14. **Se** há ponto-e-vírgula conectando 2 cláusulas curtas → **flag** + substituir por ponto ou conjunção

15. **Se** há vírgula Oxford em PT-BR ("X, Y, e Z") → **flag** + remover a vírgula antes do "e"

16. **Se** texto na tela está em **Title Case PT-BR** ("Como Acelerar Seu Treino") → **flag** + converter pra sentence case ("Como acelerar seu treino"). Mecanismo nomeado entre aspas mantém Title Case próprio.

---

## Bloco D: tom e voz

17. **Se** o hook não tem posição clara, hedgeia tudo ("pode ser que", "talvez", "em geral", "geralmente", "possivelmente") → **flag** + afirmar direto

18. **Se** o tom é uniformemente positivo (zero tensão, zero conflito, zero vilão) → **flag** + injetar fricção

19. **Se** o falado usa "eu/meu/minha" 2+ vezes sem motivo de identificação por vulnerabilidade → **flag** + reescrever com "você/seu/sua"

20. **Se** acentuação PT-BR está incorreta em qualquer palavra → **flag** + corrigir. Memória `feedback_acentuacao_pt_br.md`. Norma culta sempre.

21. **Se** o vocabulário é corporativo ("estratégia", "plataforma", "ecossistema", "performance") sem necessidade técnica → **flag** + substituir por equivalente de bar (ver `disguise-alavancas.md`)

---

## Bloco E: específico de hook de vídeo

22. **Se** mecanismo central não tem nome chiclete e o hook fala "método" 2+ vezes → **flag** + nomeie o método em aspas + Title Case próprio (ex: "Truque do Aperto")

23. **Se** mecanismo é nomeado como sigla inventada ("QH3X", "Sistema ABC-7") → **flag** + substituir por nome sensorial

24. **Se** texto na tela tem 10+ palavras → **flag** + reduzir pra 5-7

25. **Se** falado tem 5+ linhas → **flag** + cortar pra 1-4

26. **Se** prova social no hook é genérica ("muitos clientes", "estudos mostram") → **flag** + substituir por nome + número + cena específicos

27. **Se** o hook poderia trocar de nicho sem nenhuma edição → **flag** + adicionar especificidade do nicho

---

## Bloco F: testes finais

28. **Pergunta:** "Se eu mostrasse esse hook pra um amigo carioca/paulista em mesa de bar, ele riria ou faria cara de 'interessante'?"

    Se a resposta é "riria de mim" → o hook ainda tá com cara de IA. Volta e reescreve.

---

## Resumo de flags críticos (não-negociáveis)

Estes 5 flags são absolutos. Qualquer ocorrência reescreve obrigatório:

1. **Em-dash** (regra 13)
2. **"Não é X, é Y"** em qualquer variante (regra 9)
3. **"Outrossim", "Vale ressaltar"** e similares (regra 1)
4. **"Jornada"** em CTA ou em qualquer contexto (regra 1)
5. **Acentuação errada** (regra 20)

---

## Output da Fase 6 (formato)

Pra cada par auditado:

```
**[Estrutura X] — Variação Y:**

- Falado original: <texto>
- Texto na tela original: <texto>

Auditoria (10 dimensões):
1. Em-dash (#13): <ok | flag>
2. "Não é X, é Y" (#9): <ok | flag>
3. Blocklist (#1-5): <ok | flag em "<palavra>">
4. Fórmulas (#10-12): <ok | flag>
5. 5 construções: <ok | flag tipo <nome>>
6. Acentuação (#20): <ok | flag em "<palavra>">
7. Title Case (#16): <ok | flag>
8. Hedging (#17): <ok | flag>
9. Eu/meu (#19): <ok | flag>
10. Especificidade (#26-27): <ok | flag>

Status: <APROVADO | REESCRITO>

Versão final:
- Falado: <texto>
- Texto na tela: <texto>
```
