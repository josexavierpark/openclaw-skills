# Fase 7: Publish (instalar e registrar)

Só roda depois de `test=pass`. Instala a skill nova nos diretórios certos.

## Pré-condição

```
FORJASKILL_PREFLIGHT: ... test=pass ...
```

Se `test` ainda está `pending` ou `reprova`, NÃO publique. Volte pro test-harness.

## Onde as skills vivem

As skills de copy do usuário ficam em:

```
~/.claude/skills/<nome-da-skill>/
```

É onde estão copy-ads, forja-oferta, swipe-builder, master-hooks, hooks-nativos. A skill nova vai pro mesmo lugar (já é onde o scaffold escreveu, se você seguiu o blueprint).

## Passos

### 1. Confira a estrutura final

```bash
find ~/.claude/skills/<nome> -type f | sort
```

Esperado: SKILL.md, reference/*.md (uma por fase), dna/ (3 arquivos), e banco/swipe se aplicável.

### 2. Verifique o frontmatter

```bash
head -6 ~/.claude/skills/<nome>/SKILL.md
```

Confira: `name` bate com o diretório, `description` só com gatilhos, `user-invocable: true`.

### 3. Verifique o orçamento de tokens

```bash
wc -w ~/.claude/skills/<nome>/SKILL.md
```

Alvo < 500 palavras no corpo.

### 4. Confirme o registro

Skills em `~/.claude/skills/` são detectadas automaticamente. Para confirmar que apareceu, o usuário pode rodar `/<nome>` numa sessão nova ou checar a lista de skills disponíveis.

### 5. Relatório final

```
SKILL PUBLICADA: <nome>
Local: ~/.claude/skills/<nome>/
Peça: [tipo de copy]
Fases: [lista]
DNA: duas camadas (card + completa), sincronizável via sync-dna
Critique: X/40
Test harness: PASSA
Invocar com: /<nome>

Próximos passos:
- Rodar /<nome> numa sessão nova pra testar de verdade
- Catalogar swipe pra ela com /swipe-builder se precisar de banco
- Atualizar a DNA depois com sync-dna quando a pesquisa evoluir
```

## Modo de exportação

Se o usuário quer exportar a skill pra outra máquina, a estrutura já é autossuficiente (a DNA está copiada dentro de `dna/`, não referenciada por path externo). Basta zipar o diretório inteiro. Lembre o usuário que a DNA exportada é um snapshot: pra atualizar, ele roda `sync-dna` na máquina de origem antes de exportar.
