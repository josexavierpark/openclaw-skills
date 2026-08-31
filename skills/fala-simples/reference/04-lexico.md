# Fase 4: O léxico (a camada trocável)

A mecânica em [03-mecanica.md](03-mecanica.md) é fixa e serve para qualquer nicho. O que muda de nicho para nicho é o vocabulário concreto. Este arquivo diz como montar o léxico do seu.

## Por que isso é separado

Se a skill copiar mecânica **e** vocabulário do corpus de origem, todo texto que passar por ela sai soando personal trainer. Você acaba com copy de finanças escrita com "bora destravar esse shape". A mecânica transfere; o vocabulário não.

## O formato

Um arquivo `lexicos/<nicho>.json` com quatro listas:

| Campo | Muda por nicho? | O que é |
|---|---|---|
| `concretos` | **Sim** | 40 a 80 termos que o público vê, toca, mede ou sente |
| `abstratos` | **Sim** | 20 a 40 substantivos sem imagem, o vocabulário de coach do nicho |
| `marcadores_orais` | Não | Português falado, serve para qualquer nicho |
| `imperativos` | Não | Idem |

Prontos: `fitness.json` (destilado do corpus real), `generico.json` (piso universal, use enquanto não destilar o seu) e `_template.json`.

## Como destilar o léxico de um nicho novo

O jeito certo é extrair de material real do nicho, não inventar de cabeça. Junte de 10 a 30 transcrições de anúncios, VSLs ou lives de concorrentes num arquivo e rode:

```bash
python3 - <<'PY'
import re, collections
t = open('corpus-do-nicho.txt', encoding='utf-8').read().lower()
w = re.findall(r"[0-9a-zà-ÿ]+", t)
STOP = set('a o e de da do que em um uma para pra por com no na os as dos das se você seu sua eu não é mais como já mas ao meu minha isso esse essa aqui ele ela vai vou tem ter foi ser está tá tô ou até então aí lá me te nos nem sem sobre entre depois antes muito pouco todo toda todos todas quando onde porque pois assim ainda cada mesmo seja são era tinha fez faz fazer vamos bem quem quer nada tudo dele dela'.split())
freq = collections.Counter(x for x in w if x not in STOP and len(x) > 2)
for palavra, n in freq.most_common(150):
    print(f'{n:>4}  {palavra}')
PY
```

Depois separe a lista à mão em duas pilhas, usando uma pergunta só:

> **Dá para tirar uma foto disso?**

Se dá, é concreto. Perna, balança, boleto, extrato, fila, berço, mamadeira, planilha, tela, número. Se não dá, é abstrato: liberdade financeira, mentalidade, propósito, equilíbrio, protagonismo.

Casos de fronteira ficam com o concreto se tiverem unidade ou prazo. "Dívida" é abstrato, "R$ 4.200 de dívida" é concreto.

## Onde procurar corpus por nicho

| Nicho | Fonte de transcrição |
|---|---|
| Qualquer um com tráfego | Biblioteca de Anúncios da Meta do concorrente, transcrita |
| Infoproduto | VSLs e aulas abertas no YouTube |
| Serviço local | Depoimentos em vídeo e reviews longos |
| Nicho novo sem concorrente | Reddit, grupos de Facebook, comentários dos vídeos mais vistos |

O léxico do público vale mais que o léxico do vendedor. Comentário de vídeo e review são melhores que a copy do concorrente, porque trazem as palavras que o público usa sozinho.

## Testando o léxico

Rode o validador com o léxico novo contra uma transcrição real desse nicho que você considera boa. Se a razão concreto/abstrato der abaixo de 10 para 1 num texto que você sabe que é bom, o léxico está incompleto, não o texto. Adicione os termos que faltaram.

```bash
python3 scripts/validar.py referencia-do-nicho.txt --lexico <nicho>
```

## Erro comum

Encher `concretos` com palavras da oferta em vez de palavras do público. "Módulo", "plataforma", "acesso" e "bônus" são concretos no dicionário e vazios na cabeça de quem assiste. O que conta é o que existe na vida dele antes de te conhecer.
