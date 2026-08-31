# Fase 5: Authoring Pass (regras de autoria de skill)

Regras da `writing-skills` adaptadas ao domínio de copy. Aplique este passo depois do scaffold, antes do test-harness. Corrige os vícios mais comuns de skill mal escrita.

## Regra 1: o campo `description` (a mais importante)

O `description` descreve SÓ condições de gatilho. Nunca resume o workflow.

Testes da Anthropic mostraram que quando a descrição resume o processo, o modelo segue a descrição em vez de ler a skill inteira. Uma descrição que dizia "code review between tasks" fez o modelo rodar UMA review quando a skill mandava DUAS.

```yaml
# RUIM (resume o processo, o modelo pula a skill)
description: Use para criar anúncios - faz intake, retrieval, craft, hook, critique

# BOM (só gatilhos)
description: "Use when the user wants to create cold-traffic ads. Triggers PT: criar anúncio, copy de anúncio frio. Triggers EN: cold traffic ad, organic ad."
```

Checklist do `description`:
- [ ] Começa com "Use when…" e lista gatilhos/sintomas
- [ ] Escrito em 3ª pessoa (entra no system prompt)
- [ ] Gatilhos em PT e EN
- [ ] NÃO resume as fases do workflow
- [ ] Dentro de 1024 caracteres no total do frontmatter

## Regra 2: orçamento de tokens

- SKILL.md gerado: alvo < 500 palavras de corpo (fora frontmatter). Verifique:

```bash
wc -w <path>/SKILL.md
```

- Detalhe pesado vai pra `reference/`, não pro SKILL.md.
- Cada referência de fase: foco numa fase só.
- A DNA completa nunca é inlinada (ver [dna-injection.md](dna-injection.md)).

## Regra 3: divulgação progressiva

- SKILL.md é roteador fino: gates + tabela de fases + invocação. Nada de detalhe de fase.
- Uma referência por fase, carregada sob demanda.
- Referências de um nível só. Nunca SKILL → ref-A → ref-B aninhado.
- Nunca force-load com `@path`. Use links markdown ou nome da skill.

## Regra 4: nomenclatura

- Nome com letras, números e hífen. Sem parênteses, sem maiúscula, sem espaço.
- Nome diz o que faz, orientado a ação ou objeto claro. Evite "helper", "utils", "geral".
- Arquivos de fase: nome da fase (`intake.md`, `craft.md`, `critique.md`).

## Regra 5: estrutura mínima do SKILL.md gerado

Confira que o SKILL.md gerado tem, na ordem:

1. Frontmatter (name, description, user-invocable)
2. Parágrafo de identidade
3. Restrições absolutas (DNA camada 1)
4. Gates de preflight
5. Tabela de workflow
6. Como invocar (menu, brief direto, parciais)
7. Few-shot BAD/GOOD
8. Formato de saída padrão
9. Princípios operacionais

## Regra 6: a skill aplica a DNA nas próprias mensagens

A skill gerada deve respeitar a DNA não só no copy que produz, mas nas mensagens que manda pro usuário. Sem em-dash, sem "não é X é Y", sem clichê de IA, PT-BR acentuado. Adicione isso aos "princípios operacionais" da skill gerada.

## Anti-padrões (rejeite no authoring pass)

- `description` que resume o workflow.
- SKILL.md inchado com detalhe de fase que devia estar em reference.
- Exemplo multi-idioma diluído. Um exemplo excelente bate cinco medianos.
- História narrativa de sessão ("na sessão de ontem encontramos…"). Padrão reutilizável, não causo.
- Referência aninhada em mais de um nível.
- DNA inlinada inteira (quebra o orçamento de tokens).

## Saída do authoring pass

```
AUTHORING_PASS:
  description: ok (só gatilhos, PT+EN, 3ª pessoa)
  tokens: <N> palavras no SKILL.md (alvo <500)
  naming: ok
  estrutura: 9 partes presentes
  dna_nas_mensagens: declarado
  anti_padroes: nenhum encontrado
```
