# Fase 2: Destilar fontes (quando há documentos)

Roda quando o brief aponta documentos como matéria-prima: curso, swipe, método, pesquisa, transcrição, PDFs. Pula com `n/a` quando a skill não tem fontes externas.

## Princípio

Extrai a **estrutura reutilizável** das fontes, não o vocabulário de superfície. Estrutura migra entre nichos, vocabulário não. É o mesmo movimento do retrieval da copy-ads e da destilação que gerou o [disguise.md](../dna/disguise.md) das 12 cartas do swipe Paulo Sanx.

## Gate

`sources=pass` quando o `BLUEPRINT_DESTILADO` foi declarado e confirmado pelo usuário. `sources=n/a` quando não há fontes (skill nasce só da DNA + brief).

## Procedimento

1. **Liste as fontes** (paths ou texto colado). Confirme em uma frase o que vai ler.
2. **Leia tudo.** Para cada fonte, identifique:
   - Movimentos persuasivos, na ordem (a estrutura)
   - Arquétipos de abertura
   - Tratamento de prova, de objeção e de CTA
   - Tom e registro
   - Mecanismos nomeados (e o padrão de nome)
3. **Separe forma de tema.** Forma é reutilizável (movimentos, ritmo, arquétipos). Tema é do nicho original, descartável.
4. **NÃO copie:** frases inteiras, jargão de catálogo, frases-fórmula, mesmo presentes na fonte. Algumas fontes preservam tics de IA; eles ficam de fora.
5. **Declare o blueprint destilado** e espere confirmação.

## Output: BLUEPRINT_DESTILADO

```
BLUEPRINT_DESTILADO (de [fontes])
Movimentos: 1. [...] 2. [...] 3. [...]
Arquétipos de abertura: [...]
Prova / objeção / CTA: [...]
Tom: [1 frase]
Padrão de nome de mecanismo: [...]
O que NÃO carregar (tema do nicho original): [...]

Confirma antes de eu montar a skill em cima disso?
```

## Como o destilado vira parte da skill

O blueprint destilado entra como referência de domínio da skill nova (ex: `reference/metodo.md`), **em cima da DNA universal** (disguise + ai-tells). A skill gerada sabe o método das suas fontes E nasce com o filtro anti-slop.

- Fontes que são **exemplares** (cartas, anúncios, e-mails): além do blueprint, catalogue cada um com a [swipe-builder](../../swipe-builder/) ou crie um banco próprio na skill.
- Fontes que são **teoria/método**: viram reference, não banco.

## Regra crítica

Se as fontes contradizem a DNA (ex: uma carta usa em-dash ou "não é X é Y"), a DNA vence. A fonte ensina a estrutura, a DNA governa a execução.
