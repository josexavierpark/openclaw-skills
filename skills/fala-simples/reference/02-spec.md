# Fase 2: O spec métrico

Os alvos que definem o estilo. Tudo aqui saiu da medição de um corpus real de 26 roteiros falados de resposta direta (6.310 palavras), não de opinião sobre boa escrita.

## Como os alvos foram calibrados (leia antes de discutir um número)

A primeira versão deste spec usou as médias agregadas do corpus inteiro. Ao rodar o validador contra os próprios roteiros de origem, ele reprovou vários deles. Média agregada e distribuição por peça são coisas diferentes, e alvo calibrado na média reprova o original.

A calibração atual usa a distribuição **por roteiro**. Os alvos se dividem em dois níveis:

| Nível | Critério | O que acontece se falhar |
|---|---|---|
| **Assinatura** | O corpus cumpre em praticamente todo roteiro | Bloqueia a entrega |
| **Faixa** | O corpus varia muito de peça para peça | Vira aviso, com a faixa observada |

Com essa calibração, 18 dos 26 originais passam nos alvos derivados do corpus. Os 8 que falham são em boa parte as peças que não são a voz do apresentador: os dois anúncios escritos para leitura na tela (que usam "você receberá", futuro sintético) e os depoimentos gravados por atores. O validador está separando registro, não gerando ruído.

## Alvos de assinatura (bloqueantes)

| Alvo | Valor | Por que é assinatura |
|---|---|---|
| Palavras de até 4 letras | >= 50% | Faixa observada 48,7% a 62,1%. A métrica mais estável do corpus. |
| Palavras com 13+ letras | <= 2,5% | Mediana 1,2%. E no original quase toda ocorrência é a palavra que nomeia o benefício. |
| Futuro sintético (fará, terá, receberá) | 0 | Zero em 24 dos 26. Sempre "vai receber", nunca "receberá". |
| Concreto por abstração | >= 10 : 1 | Zero abstração motivacional em 26 de 26 roteiros. |
| Marcadores orais por 100 palavras | >= 1,0 | Mediana 2,72. Atingido por 22 dos 26 roteiros. |
| Muletas de fala (né? sabe? viu? ó) | 0 | **Regra da casa**, ver abaixo |
| Gulpease (D3) | >= 55 | 25 dos 26 roteiros |
| Flesch adaptado ao PT (D2) | >= 50 | 25 dos 26 roteiros |
| Densidade de "que" por 100 palavras | <= 3,2 | **Regra da casa**, ver abaixo |
| Dois-pontos | 0 | **Regra da casa**, ver abaixo |
| Imperativos por 100 palavras | >= 1,0 | Mediana 1,8. O comando aparece do começo ao fim, não só no CTA. |
| Tamanho médio da frase | 13 a 20 palavras | Mediana 16,3. |
| Desvio do tamanho da frase | >= 5,5 | Mediana 9,6. Mede a alternância, e é o alvo que texto de IA mais falha. |

## A regra da casa (marcada com "casa" no relatório)

Um alvo aqui não vem do corpus: vem de decisão de estilo do usuário, e é mais estrito do que os originais.

**Densidade de "que" <= 3,2 por 100 palavras.** O termômetro da complexidade, e o alvo que mais mudou o resultado prático da skill. Distribuição no corpus:

| Teto | Roteiros do corpus que cumprem |
|---|---|
| <= 3,2 (o alvo aqui) | 19 de 26 |
| <= 3,6 | 23 de 26 |
| <= 4,0 | 25 de 26 |

Um alvo fiel ao corpus ficaria em 4,0. Ele foi rejeitado por um motivo concreto: um roteiro que o usuário considerou complicado demais media **3,93**, e passaria folgado. O teto de 3,2 mira o terço mais simples do corpus, que é exatamente o pedido: o estilo e o tom do corpus, com mais simplicidade que a mediana dele.

Cada "que" relativo pendura uma oração na anterior. Duas ou três numa frase e o ouvinte perde o fio, mesmo com a frase em 18 palavras. Ver [03-mecanica.md](03-mecanica.md) seção 4b.

**Dois-pontos = 0.** A evidência do corpus aqui é fraca de propósito, e é honesto dizer: a pontuação das transcrições foi gerada pelo Whisper, não pelo apresentador, então "o corpus não usa dois-pontos" não prova nada sobre a fala dele. O princípio é que sustenta a regra: quem fala não produz dois-pontos, produz pausa e frase nova. Num roteiro que vai ser lido em voz alta, o dois-pontos denuncia uma construção que a boca não faria.

**Muletas de fala = 0.** Duas famílias: o apêndice colado no fim da oração (né? sabe? viu? tá? entendeu? hein?) e o "ó" solto. O corpus usa 17 apêndices em 6.310 palavras (0,27 por 100) e 15 dos 26 roteiros não usam nenhum. Aqui o alvo é zero para as duas famílias.

O motivo é prático. O apêndice simula oralidade sem obrigar o texto a mudar: dá para grudar "né?" no fim de qualquer frase de relatório e ela continua sendo de relatório. Quando o piso de marcadores é o único alvo em jogo, o caminho mais barato para batê-lo é encher o roteiro de apêndice, e o resultado soa a imitação de fala. Ver [03-mecanica.md](03-mecanica.md) seção 5b.

**Isso muda a leitura do baseline.** Contra os 26 roteiros de origem:

| Recorte | Aprovados |
|---|---|
| Só os alvos derivados do corpus | 18 de 26 |
| Incluindo as regras da casa (muletas, dois-pontos, "que") | 5 de 26 |

Os 14 originais que a regra das muletas derruba têm de 1 a 3 cada, e o teto de "que" derruba outros 7. Se você quiser fidelidade arqueológica ao corpus em vez do estilo da casa, os alvos a tirar são `apendice`, `doispontos` e `que`.

## Dois bugs de medição já corrigidos (não reintroduza)

**O "ó" casava com o artigo "o".** A comparação de termos rodava sobre o texto sem acento, então a interjeição "ó" virava "o" e casava com todo artigo definido do roteiro. Isso inflou a contagem de marcadores de 3,36 para 5,77 por 100 palavras, e o piso antigo (>= 2,5) foi calibrado em cima do número inflado. Ele reprovava 12 dos 26 originais e empurrava quem usava a skill a encher o texto de apêndice para bater a meta. A comparação de termos de léxico agora roda **com acento**, contra o texto acentuado.

**O apêndice era contado como palavra, não como uso.** "do jeito certo." e "pra quem não sabe," não são apêndices. O detector agora exige a pontuação de fim de oração e ignora "não sabe".

## As 12 Diretrizes

Quatro alvos vêm do documento "As 12 Diretrizes" e foram adotados só depois de medidos contra o corpus: Gulpease (D3), Flesch (D2), ARI (D6) e teto de perguntas (D7). Três fórmulas do documento foram **rejeitadas** por reprovarem o corpus inteiro (Flesch-Kincaid, Gunning Fog, Coleman-Liau: calibradas para inglês). Três viraram scanner em vez de alvo. Detalhe e números em [08-diretrizes.md](08-diretrizes.md).

## Alvos de faixa (avisos)

| Alvo | Faixa | Mediana |
|---|---|---|
| Frases de até 10 palavras | 20% a 50% | 30% |
| Frases sem oração encaixada | >= 28% | 50% |
| Frases abrindo com E/Mas/Então/Aí/Ah | >= 10% | 32% |
| Primeira frase (hook) | <= 30 palavras | 13 |
| Última frase (o tapa) | <= 5 palavras | 1 |
| Penúltima frase (o CTA) | 6 a 45 palavras | 12,5 |
| Densidade de "de" por 100 palavras | <= 3,6 | 2,92 |
| Frases com 21+ palavras | <= 35% | 26,4% |

## Blocklist (bloqueante, independente de medida)

Em-dash, a fórmula "não é X, é Y", e a lista Tier-1 e Tier-2 da DNA (`dna/dna-card.md`). O validador roda essa checagem junto com as métricas.

Uma exceção está codificada no detector: "saiba mais" e "clique aqui" **não** são acusadas quando vêm precedidas de "em", "no" ou "botão". Nesse caso o roteiro está nomeando o botão da plataforma ("toca em Saiba Mais"), que é obrigatório em anúncio de Meta e não é escolha de copy. "Clique aqui e saiba mais sobre a aula" continua sendo pego.

## O alvo que mais importa

Se você só puder olhar um número, olhe o **desvio do tamanho da frase**. Média baixa não significa escrita simples: significa escrita uniforme, que é justamente o ritmo de texto gerado por modelo. O corpus tem média 16 com desvio 9,6, ou seja, alterna frase de 30 palavras com frase de 3. Texto de IA típico fica em desvio 4, com todas as frases do mesmo tamanho.

## Rodando

```bash
python3 ~/.claude/skills/fala-simples/scripts/validar.py rascunho.txt --lexico fitness
python3 ~/.claude/skills/fala-simples/scripts/validar.py - --lexico generico   # via stdin
python3 ~/.claude/skills/fala-simples/scripts/validar.py rascunho.txt --json    # para encadear
```

Exit code 0 aprova, 1 reprova. O relatório traz as frases ofensoras e a ação corretiva de cada falha.

## O que este spec não mede

Ele mede forma, não argumento. Um roteiro pode passar em 15 de 15 alvos e não vender nada, porque não tem oferta, promessa ou mecanismo. O spec é o piso de estilo. A arquitetura persuasiva está em [05-arquitetura.md](05-arquitetura.md) e o julgamento de qualidade em [07-audit.md](07-audit.md).
