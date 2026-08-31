# Fase 4: Critique (scoring do quiz)

Avalia o quiz gerado contra 10 heurísticas, 0-4 cada, total 0-40. Não é review solto, é tabela com nota e 1 linha de justificativa por nota. Consulte [dna/disguise.md](../dna/disguise.md) para as 7 alavancas.

## As 10 heurísticas

| # | Heurística | Como pontuar |
|---|---|---|
| 1 | Cria problema (não só identifica) | 0 = quiz de pesquisa que só pergunta, 4 = instala uma limitação invisível que a pessoa não sabia que tinha |
| 2 | Arco Positiva→Neutra→Negativa | 0 = ordem aleatória ou salto pro negativo, 4 = três fases limpas com transição |
| 3 | Posse negativa na identidade | 0 = nenhuma negativa de "eu sou/eu tenho", 4 = 2-3 negativas que forçam a admissão na identidade |
| 4 | Micro-compromisso e inércia | 0 = perguntas soltas, 4 = triplo compromisso + saída + telas de reforço |
| 5 | Mecanismo nomeado | 0 = "esse método", 4 = nome chiclete sensorial em aspas, problema e solução nomeados |
| 6 | Página de resultado | 0 = só "parabéns", 4 = conforto → má notícia → mecanismo do problema → virada |
| 7 | Personalização real | 0 = todos no mesmo resultado (fora teste seco), 4 = ramificação e resultado que espelha as respostas |
| 8 | Captura no lugar certo | 0 = pede e-mail no começo, 4 = captura no fim como pedágio do plano |
| 9 | Prova específica | 0 = "muitos alunos", 4 = nome + idade + situação + número, ou placeholder explícito |
| 10 | Zero reflexos de IA | 0 = 5+ hits do blocklist, 4 = zero (sem em-dash, sem "não é X é Y", sem Title Case) |

## Procedimento

1. Leia o quiz inteiro (arco + resultado + abertura + headline). 2. Pontue cada heurística com 1 linha. 3. Some.

| Score | Banda | Ação |
|---|---|---|
| 35-40 | Excepcional | Liberar |
| 28-34 | Pronto | Liberar + 1-2 melhorias |
| 20-27 | OK | Liberar + 3-4 melhorias |
| <20 | Crítico | Reescrever |

## Red flags por persona

- **Cético que já tentou de tudo:** a promessa conflita com o histórico de fracasso dele? O problema criado explica por que nada funcionou antes?
- **Pessoa apressada no celular:** a primeira pergunta entra leve e rápida, sem pedir dados? As negativas têm saída para não travar?
- **Quem desconfia de quiz:** parece interrogatório (só identifica) ou parece um diagnóstico que entende a pessoa?

## Saída

```
CRITIQUE QUIZ (X/40)
[10 heurísticas com nota + justificativa de 1 linha]
Banda: [...]
Red flags: [...]
3 melhorias prioritárias: [...]
```

Não infle. Quiz honesto tira 28-32 na primeira passada. Justifique cada nota.
