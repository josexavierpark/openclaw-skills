# Fase 1: Roteamento (os 16 modos)

Detecte o modo pelo pedido. Se os inputs obrigatórios estão na mensagem, produza direto. Se falta algo, faça UMA pergunta compacta listando só os campos que faltam. Nunca faça entrevista em série.

## Tabela de modos

| # | Modo | Inputs obrigatórios | Motor | Entregável |
|---|---|---|---|---|
| 1 | Bater o controle | anúncio original | [engine-modelagem.md](engine-modelagem.md) | Hook original intacto + 4 hooks novos + body batido |
| 2 | Anúncio do zero (7/8 dígitos) | MUS/gancho, MUP, avatar, expert, nicho | [engine-criacao.md](engine-criacao.md) | 3 hooks + body completo (anatomia inteira) |
| 3 | Ganchos | MUS, MUP, nicho (ângulo opcional) | [hooks.md](hooks.md) | 10 hooks: 5 puxando MUP + 5 puxando MUS |
| 4 | Estrutura invisível | anúncio | [engine-modelagem.md](engine-modelagem.md) | Esqueleto psicológico bloco a bloco (trecho + rótulo) |
| 5 | Reescrever com outro ângulo | anúncio + ângulo alvo | [engine-modelagem.md](engine-modelagem.md) | Anúncio reescrito inteiro sob a nova lente |
| 6 | Bullets | anúncio (ou promessa + mecanismo) | [componentes.md](componentes.md) | CTA com valor + transição + 5-9 bullets |
| 7 | Melhorar CTA | anúncio ou CTA atual | [componentes.md](componentes.md) | CTA com valor completo |
| 8 | Adicionar depoimento | anúncio | [componentes.md](componentes.md) | Transição + depoimento + retorno à argumentação |
| 9 | Transformar em UGC | anúncio (persona UGC opcional) | [variantes.md](variantes.md) | Versão UGC falada |
| 10 | Variações para teste | anúncio (n e eixos opcionais) | [variantes.md](variantes.md) | 5 versões: científica, emocional, conspiratória, UGC, prova social |
| 11 | Adaptar para outro nicho | anúncio + nicho destino (+ MUP/MUS novos se houver) | [engine-modelagem.md](engine-modelagem.md) | Anúncio adaptado, estrutura preservada |
| 12 | Ajustar tom | anúncio + dial (agressivo/emocional/científico/conspiracional) | [engine-modelagem.md](engine-modelagem.md) | Anúncio no novo tom |
| 13 | Análise | anúncio | [analise.md](analise.md) | Diagnóstico: forte/fraco/onde perde/o que falta/como bater |
| 14 | Mais promessas e provas | anúncio | [componentes.md](componentes.md) | Versão expandida (promessas dimensionais + provas fortes) |
| 15 | Hooks visuais | anúncio ou hook textual + nicho | [hooks.md](hooks.md) | Hook textual + hook visual + cenas 1-4 |
| 16 | Hook → anúncio completo | hook pronto (+ nicho; MUP/MUS se houver) | [engine-criacao.md](engine-criacao.md) | Anúncio completo construído a partir do hook, com estrutura do swipe |

## Regras de roteamento

- Pedidos compostos ("bate o controle e me dá 5 variações") rodam os modos em sequência, um preflight só.
- Anúncio colado sem pedido explícito: pergunte qual modo em 1 linha, oferecendo os 3 mais prováveis pelo contexto.
- Modos 4 e 13 são diagnósticos: não passam por critique/audit de copy (não há peça nova), só pela DNA nas próprias mensagens.
- Todos os outros modos terminam em critique → audit → polish antes da entrega.
- Inputs opcionais nunca viram pergunta. Assuma o default declarado na tabela e siga.

## Menu (invocação sem argumento)

```
forja-ads: o que você quer forjar?

Diagnóstico: 4. estrutura invisível | 13. análise
Cirurgia: 6. bullets | 7. CTA | 8. depoimento | 12. tom | 14. mais promessas/provas
Reescrita: 1. bater controle | 5. outro ângulo | 9. UGC | 10. variações | 11. outro nicho
Criação: 2. do zero | 3. ganchos | 15. hooks visuais | 16. do hook ao anúncio

Cola o anúncio (ou o hook) junto com o número e eu já produzo.
```
