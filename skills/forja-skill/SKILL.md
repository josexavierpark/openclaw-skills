---
name: forja-skill
description: "Use when the user wants to create, scaffold, generate, standardize, or rebuild a copywriting skill (not the copy itself, the skill that writes copy). Triggers in Portuguese: criar skill de copy, gerar nova skill, montar skill de anúncio/VSL/e-mail/sales page, fazer uma skill que escreve copy, forja-skill, padronizar minha skill de copy. Triggers in English: create a copy skill, build a copywriting skill, scaffold a new skill, generate a skill that writes copy, standardize a copy skill."
user-invocable: true
---

# forja-skill

Meta-skill que cria skills de copy. Toda skill gerada nasce com a arquitetura padrão (roteador + gates + fases + critique + audit + polish) e a **DNA anti-AI-slop em duas camadas**: card comprimido sempre ativo + pesquisa completa sob demanda.

Não escreve copy: escreve a skill que escreve copy.

## Quando não usar

- Para escrever a peça (use a skill final: copy-ads, master-hooks, hooks-nativos).
- Para skill que não é de copy (use a writing-skills).
- Para anúncio cold: já existe a copy-ads, ofereça clonar o padrão.
- Para catalogar swipe (use a swipe-builder).

## A DNA

Fonte única em [dna/](dna/): [disguise.md](dna/disguise.md) (7 alavancas, o que EXECUTAR), [ai-tells.md](dna/ai-tells.md) (blocklist, o que EVITAR) e [dna-card.md](dna/dna-card.md) (1 página, sempre ativa). **Regra suprema:** nenhuma skill nasce sem a DNA. Ver [dna-injection.md](reference/dna-injection.md).

## Gates de preflight

Antes de escrever qualquer arquivo de skill, declare:

```
FORJASKILL_PREFLIGHT: brief=pass sources=pass|n/a blueprint=loaded dna=loaded authoring=loaded test=pending mutation=open
```

| Gate | Verificação |
|---|---|
| `brief` | `SKILL_BRIEF` confirmado pelo usuário (fase 1) |
| `sources` | `BLUEPRINT_DESTILADO` confirmado, ou `n/a` se não há fontes |
| `blueprint` | [blueprint.md](reference/blueprint.md) carregado |
| `dna` | [dna-card.md](dna/dna-card.md) lido, injeção definida |
| `authoring` | [authoring-rules.md](reference/authoring-rules.md) carregado |
| `test` | `pass` só após o test-harness. Começa `pending` |
| `mutation` | Todos acima (menos `test`) passaram |

`mutation=open` libera o scaffold; `test=pass` libera o publish. Pare se algum falhar.

## Meta-workflow (8 fases)

| Fase | Referência | O que faz |
|---|---|---|
| 1. Intake | [intake.md](reference/intake.md) | Entrevista pra escopar a skill. Output: `SKILL_BRIEF` |
| 2. Destilar fontes | [destilar.md](reference/destilar.md) | Se há documentos: extrai o método. Pula com `n/a` |
| 3. Blueprint | [blueprint.md](reference/blueprint.md) | Aplica o padrão canônico ao brief |
| 4. DNA injection | [dna-injection.md](reference/dna-injection.md) | Card inline + cópia completa + sync |
| 5. Scaffold | [templates/](templates/) | Escreve os arquivos a partir dos templates |
| 6. Authoring pass | [authoring-rules.md](reference/authoring-rules.md) | Corrige `description`, tokens, naming |
| 7. Test harness | [test-harness.md](reference/test-harness.md) | RED-GREEN-REFACTOR: roda brief real, audita o output |
| 8. Publish | [publish.md](reference/publish.md) | Instala e registra |

Ordem fixa. Pause após o intake, a destilação (se houver) e o scaffold para confirmar.

## Como invocar

- **Sem argumento:** ofereça as 4 ações: criar do zero, padronizar uma existente, `sync-dna`, ou testar um path.
- **Com path direto:** modo padronização. Compare com o blueprint, gere o plano de migração, confirme antes de mutar.
- **Parciais:** "só intake", "padronizar [path]", "sync-dna [path]", "testar [path]".

## Princípios operacionais

- A `forja-skill` aplica a DNA nas próprias mensagens: sem em-dash, sem clichê de IA, PT-BR acentuado.
- Toda skill gerada herda os gates, o critique e o audit. O `description` dela descreve SÓ gatilhos, nunca o workflow.
- Nunca invente swipe ou prova. Aponte para o banco ([swipe-builder](../swipe-builder/)) ou peça ao usuário.
- Releia o `SKILL_BRIEF` antes de cada fase. Não falsifique o test-harness: se o output falha no audit, conserte a skill, não o relatório.
