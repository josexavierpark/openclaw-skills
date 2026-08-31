# Template: fase critique da skill gerada

Cole como `reference/critique.md` na skill gerada. Avalia o COPY que a skill produz. 10 heurísticas, 0-4, total 0-40. Adapte as heurísticas ao formato.

```markdown
# Critique (scoring do copy)

Avalia o copy gerado contra 10 heurísticas, 0-4 cada. Não é review solto, é tabela com nota. Consulte [dna/disguise.md](../dna/disguise.md) para as 7 alavancas.

## As 10 heurísticas

| # | Heurística | Como pontuar |
|---|---|---|
| 1 | Fluidez (linha-única + conectores de fala) | 0 = blocão acadêmico, 4 = ritmo de fala |
| 2 | Hook/abertura | 0 = genérico, 4 = tensão real na 1ª frase |
| 3 | Especificidade | 0 = abstrato, 4 = 3+ específicos ancorados |
| 4 | Mecanismo nomeado | 0 = "esse método", 4 = nome chiclete em aspas |
| 5 | Storytelling | 0 = "uma cliente", 4 = nome + diálogo + cena |
| 6 | Protagonismo do leitor | 0 = "nós oferecemos", 4 = "você" em cada frase de valor |
| 7 | Ritmo (burstiness) | 0 = frases iguais, 4 = curta/longa alternadas |
| 8 | Objeção via "Mesmo que…" | 0 = refuta de frente, 4 = transcende |
| 9 | Prova específica | 0 = "muitos alunos", 4 = nome+idade+situação+número |
| 10 | Zero reflexos de IA | 0 = 5+ hits no blocklist, 4 = zero |

## Procedimento
1. Leia o copy. 2. Pontue cada heurística com 1 linha de justificativa. 3. Some.

| Score | Banda | Ação |
|---|---|---|
| 35-40 | Excepcional | Liberar |
| 28-34 | Pronto | Liberar + 1-2 melhorias |
| 20-27 | OK | Liberar + 3-4 melhorias |
| <20 | Crítico | Reescrever |

## Red flags por persona
- **Cético:** promessa sem âncora? prova sem nome? abertura genérica?
- **Primeiro contato:** assume familiaridade? jargão sem explicar?
- **Mobile scroll:** 1ª frase fraca? benefício enterrado?

## Saída
\```
CRITIQUE (X/40)
[10 heurísticas com nota + justificativa]
Banda: [...]
Red flags: [...]
3 melhorias prioritárias: [...]
\```

Não infle. Copy real tira 28-32. Justifique cada nota.
```

## Adaptação por peça
- VSL: troque "Hook" por "Lead/Big Idea". Some heurística de escada de preço.
- E-mail: heurística 2 vira "Linha de assunto". Some "1 CTA clara".
- Headline: reduza pra 5-6 heurísticas focadas em hook e especificidade.
