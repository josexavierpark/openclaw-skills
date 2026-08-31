# Fase 6a: Critique (avaliar a skill gerada)

Avalia a SKILL que foi gerada, não o copy. Pergunta: ela segue o padrão e vai produzir copy limpo? Scoring de 10 heurísticas, 0-4 cada, total 0-40.

## As 10 heurísticas (da skill gerada)

| # | Heurística | O que mede | Como pontuar |
|---|---|---|---|
| 1 | DNA embutida | Card inline + cópias completas + gate `dna`? | 0 = sem DNA, 4 = duas camadas completas |
| 2 | Description correta | Só gatilhos, PT+EN, 3ª pessoa, sem resumo de workflow? | 0 = resume processo, 4 = só gatilhos |
| 3 | Gates de preflight | Bloco declarável com gate de mutação? | 0 = sem gates, 4 = gates completos e bloqueantes |
| 4 | Fases corretas pra peça | As fases batem com o tipo de copy do brief? | 0 = genérico errado, 4 = fases sob medida |
| 5 | Critique + audit presentes | A skill gerada tem o sistema imunológico? | 0 = nenhum, 4 = os dois com template completo |
| 6 | Hook depois do corpo | A abertura não trava no craft? | 0 = trava, 4 = hook é fase separada pós-craft |
| 7 | Prova específica exigida | A skill força nome+idade+situação+número? | 0 = aceita "muitos alunos", 4 = exige específico |
| 8 | Orçamento de tokens | SKILL.md < 500 palavras, detalhe em reference? | 0 = inchado, 4 = roteador fino |
| 9 | Divulgação progressiva | Referências de 1 nível, sem force-load? | 0 = aninhado/force-load, 4 = limpo |
| 10 | Few-shot BAD/GOOD | Tem pares de calibração de voz? | 0 = nenhum, 4 = 3+ pares fortes |

Consulte [dna/disguise.md](../dna/disguise.md) ao avaliar se as 7 alavancas estão refletidas nas instruções de craft da skill gerada.

## Procedimento

1. Leia o SKILL.md gerado + as referências.
2. Pontue cada heurística, 1 linha de justificativa por nota.
3. Some. Bandas:

| Score | Banda | Ação |
|---|---|---|
| 35-40 | Pronta | Publica |
| 28-34 | Quase | Conserta 1-2 heurísticas fracas, republica |
| 20-27 | Marginal | Reescreve as partes fracas antes de testar |
| <20 | Crítica | Refaz o scaffold |

## Red flags por persona

### Persona 1: usuário que invoca a skill com brief esparso
- A skill exige intake antes de gerar, ou despeja copy genérico?
- Os gates impedem a geração sem brief confirmado?

### Persona 2: usuário apressado que quer pular fases
- A skill deixa pular o audit? (não deve)
- O hook trava no craft se o usuário não escolher abertura?

### Persona 3: o copy gerado caindo no feed real
- As instruções de craft produzem abertura com tensão real?
- O audit pega em-dash, "não é X é Y", Title Case antes de entregar?

## Saída

```
CRITIQUE_SKILL (X/40)
[10 heurísticas com nota + justificativa de 1 linha]
Banda: [Pronta / Quase / Marginal / Crítica]
Red flags: [lista ou "nenhum"]
3 correções prioritárias: [...]
```

Não infle. Skill gerada honesta tira 28-34 na primeira passada. 38+ é raro.
