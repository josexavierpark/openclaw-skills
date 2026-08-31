# Auditoria de Slop Score

Medição mecânica de quanto a copy escrita soa a chatbot, contra 49.347 palavras de copy PT-BR que rodou no mercado. Método portado do [The Slop Index](https://theslopindex.com/methodology). Nenhum LLM julga LLM.

## Por que este scan existe

O índice publica o perfil de cada modelo eixo a eixo. O do modelo que escreve esta copy:

| Eixo | Nota | Posição entre 22 modelos |
|---|---|---|
| Concisão | 31,6 | **pior de todos** |
| Templating | 58,4 | acima da mediana |
| Ritmo | 4,2 | **melhor de todos** |
| Tells | 24,9 | 2º melhor |

A blocklist de vocabulário do DNA cobre o eixo de 15% onde o modelo já é quase o melhor do mercado. Os dois eixos onde ele realmente falha somam 65% e não eram medidos por nada. Este scan cobre os quatro.

## Como rodar

```bash
bash scripts/slop-audit.sh <arquivo-da-copy.md>
```

O script acha o validador sozinho, usa o baseline humano e compara contra o histórico de copies que a Forja já escreveu. Se ele sair com código 3, o anti-slop não está instalado: registre isso no relatório e siga o resto do audit.

### Três guardas que o scan aplica sozinho

- **Idioma.** Texto que não é PT-BR é recusado, não pontuado. A régua inteira é de português (`que`, `-mente`, `de/da/do`), e um anúncio em inglês zeraria essas medidas e passaria como copy impecável.
- **Texto curto.** Abaixo de 15 parágrafos, templating passa a ser medido só por esqueleto, com régua própria. Motivo: um anúncio de 200 palavras tem 6 aberturas, e uma coincidência sozinha já vira 17%, contra 1,7% de média num texto de 5 mil palavras. Sem essa guarda, todo anúncio curto era reprovado à toa.
- **Par mais parecido.** O eixo pontua pela média contra todo o histórico, o que dilui um clone único. Quando alguma copy anterior passa de 5% de reuso, o relatório nomeia ela na linha `par mais parecido`. É onde olhar primeiro.

**Templating só existe comparando arquivos.** Na primeira copy da vida o eixo aparece como "não medido" e os 30% se redistribuem, o que é o comportamento correto. Da segunda em diante ele passa a valer, porque o histórico já tem com o que comparar.

## Leitura do resultado

| Slop Score | Veredito |
|---|---|
| 0 a 15 | Passa |
| 16 a 29 | Passa com conserto: ataque o eixo pior antes de entregar |
| 30 ou mais | Reprova. Reescreva os trechos apontados e rode de novo |

Independente do total: **qualquer eixo em 50 ou mais é conserto obrigatório.**

Referência medida: copy de LLM sem prompt de estilo dá 35,9. Copy humana do swipe dá 6,1. Copy boa da Forja fica entre 2 e 14.

## O que fazer com cada eixo

**Concisão alta.** O texto inflou. Sintomas no relatório: frase média acima de 16 palavras, `que/100` acima de 4,2, `-mente/100` acima de 0,8. Conserto mecânico: todo "que" relativo vira ponto final, e todo advérbio em -mente sai ou vira a coisa concreta que ele descreve. Corte sem repor.

**Templating alto.** Você reusou abertura ou esqueleto de outra copy sua, de outro projeto. O relatório nomeia as frases. Reescreva **essas** linhas, não o bloco inteiro. Abertura de parágrafo repetida é a mais fácil de matar e a que mais pesa.

**Ritmo alto.** Cadência lisa. Alvos do corpus humano: 26% das frases com 6 palavras ou menos, cv de 0,63, nenhuma sequência metronômica passando de 6 frases. Conserto: quebre a frase longa em duas e ponha entre elas uma virada de até 4 palavras que não carrega informação, só muda a direção.

**Tells alto.** Só conta o que está **acima da taxa humana**, e o relatório separa isso do que está dentro. Palavra que a copy campeã brasileira usa (`literalmente`, `a verdade é que`, `jornada`, `aqui está`) não é acusação. Corrija apenas as linhas marcadas como ACIMA.

## Formato no relatório final

```
SLOP SCORE: 12,6/100 · concisão 0 · templating 17 · ritmo 38 · tells 0
Veredito: passa com conserto (ritmo)
Consertado: 4 frases longas quebradas nos blocos 3 e 7
```

Se o scan não rodar, escreva `SLOP SCORE: não medido (anti-slop ausente)`. Nunca invente o número.
