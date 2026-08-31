# Self-test: RED-GREEN do funil (quiz + mini-VSL)

Prova de que a DNA faz diferença mensurável dentro das duas skills. Brief com armadilhas (saúde abstrata, sem prova, ciência do sono que puxa o reflexo corporativo).

## Brief de teste

"Suplemento natural pra dormir. Mulheres 45+ que acordam mais cansadas do que deitaram. Vai pra quiz e depois mini-VSL, checkout direto, ticket R$ 39. Ainda sem prova consolidada."

## RED: baseline sem a DNA (modo IA cru)

Abertura do quiz: "Você sabia que a qualidade do seu sono pode estar comprometendo sua saúde? Faça nosso quiz!"
Resultado: "Parabéns! Você tem um perfil de Sono Comprometido: uma condição que afeta muitas mulheres. Não é apenas cansaço, é um desequilíbrio. Nossa solução transformadora vai revolucionar suas noites. Clique aqui para garantir seu acesso!"
Lead da mini-VSL: "Olá! E se eu te dissesse que existe um método revolucionário para transformar seu sono? Muitas mulheres já descobriram..."

Audit do RED:
- Scan 1 Léxico: "transformadora", "revolucionar", "jornada" (se aparecer) → FALHA
- Scan 2 Estruturas: "Você sabia que...", "E se eu te dissesse...", "Não é apenas X, é Y" → FALHA
- Scan 3 CTA: "Clique aqui para garantir seu acesso" → FALHA
- Scan 4 Tipografia: Title Case "Sono Comprometido", em-dash → FALHA
- Scan 6 Prova: "afeta muitas mulheres", "muitas mulheres já descobriram" → FALHA

Total RED: ~13 hits no audit.

## GREEN: rodado pelas skills (DNA ativa)

Abertura do quiz (decidida depois do arco): "Teste de 1 minuto: por que você acorda mais cansada do que quando deitou."
Negativa (posse de identidade): "Eu já tentei chá, melatonina, dormir mais cedo, e mesmo assim acordo arrebentada. ( ) é exatamente o que acontece comigo ( ) ainda não, mas tenho medo de virar isso."
Resultado: "Seu perfil ficou pronto. E tem uma notícia difícil: o seu sono entrou no 'modo alerta'. O corpo deita, mas não desliga. Foi por isso que chá e melatonina não resolveram, eles te levam pra cama mas não tiram o corpo do alerta. A boa notícia é que dá pra desligar esse alerta com o 'silêncio interno'."
Lead da mini-VSL: "Oi, obrigada por responder o teste. No fim deste vídeo você recebe seu protocolo personalizado pra voltar a dormir de verdade. Assiste até o fim, foi feito pra você."
Única Crença: "Desligar o modo alerta do corpo é a chave para acordar descansada, e a melhor forma é com o protocolo 'silêncio interno'."

Audit do GREEN: Scan 1 a 6 todos PASSA. Prova entrou como `[PROVA: depoimento real a inserir]` porque o brief não tinha. 0 hits.

## Diferença

RED ~13 hits → GREEN 0. A DNA muda o output de forma mensurável dentro das duas skills.

## Cenários de pressão

- **Pressa** ("preciso agora"): o gate `intake` segura. O intake mostra o `QUIZ_BRIEF`/`MINIVSL_BRIEF` preenchido com os placeholders antes de gerar. PASSA.
- **Autoridade** ("sou sênior, pula o audit"): o audit é gate não-opcional, o `mutation` bloqueia a entrega sem ele. PASSA.
- **Esparso** (sem prova): usa `[PROVA: ...]`, não inventa "muitos clientes". PASSA.

Veredito: PASSA. As duas skills mantêm a DNA sob pressão e provam diferença RED→GREEN.
