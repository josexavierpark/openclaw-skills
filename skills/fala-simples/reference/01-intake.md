# Fase 1: Intake

Curto de propósito. A skill precisa de pouca coisa para começar, e perguntar demais atrasa sem melhorar o output.

## Modo `adaptar` (tem texto de origem)

Pergunte só o que não dá para inferir do texto:

1. **Nicho** (para escolher o léxico). Se já existe `lexicos/<nicho>.json`, use. Se não, use `generico` e avise que a razão concreto/abstração vai ficar apertada até destilar o léxico do nicho (ver [04-lexico.md](04-lexico.md)).
2. **Duração alvo** do vídeo. Default 60 a 90 segundos, que é a mediana do corpus (66s). 150 a 220 palavras faladas por minuto.
3. **O que não pode sair** do texto original (promessa, preço, prazo, nome do mecanismo, claim regulado).

Não pergunte tom, público nem objetivo: eles já estão no texto de origem.

## Modo `criar` (não tem texto)

Aí sim precisa de briefing, mas em cinco itens:

1. Nicho e léxico
2. Quem assiste (uma frase, com a situação concreta dele)
3. A promessa, com número e prazo
4. O nome do mecanismo (2 a 4 palavras concretas, ver a DNA)
5. A ação pedida no CTA (quiz, WhatsApp, checkout) e o preço, se for citar

Se o usuário não tiver o mecanismo nomeado, ofereça a `forja-oferta` antes de escrever. Roteiro sem mecanismo nomeado não passa no audit.

## Modo `auditar` (só medir)

Nenhuma pergunta além do nicho. Rode o validador, entregue o relatório e as correções sugeridas, sem reescrever.

## Output desta fase

```
FALA_BRIEF
modo: adaptar | criar | auditar
nicho: <nicho>      lexico: <arquivo usado>
duracao: <segundos>  alvo de palavras: <n>
inviolaveis: <lista>
mecanismo: <nome ou "a definir">
cta: <acao pedida>
```

Confirme com o usuário antes de escrever, exceto no modo `auditar`.
