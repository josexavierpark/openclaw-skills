# Fase 2: Blueprint (o padrão canônico de skill de copy)

A forma que toda skill de copy gerada herda. Derivada da copy-ads e da impeccable. Aplique este padrão ao `SKILL_BRIEF`.

## A topologia padrão

```
nome-da-skill/
├── SKILL.md              # roteador fino: gates + workflow + invocação + formato de saída
├── reference/            # uma referência por fase, carregada sob demanda
│   ├── <fase>.md
│   └── ...
├── dna/                  # cópia completa da DNA + card (camada sob demanda)
│   ├── disguise.md
│   ├── ai-tells.md
│   └── dna-card.md
└── swipe/ ou banco/      # opcional: matéria-prima, se a skill tiver banco próprio
```

## As partes obrigatórias do SKILL.md gerado

Toda skill de copy gerada tem, nesta ordem:

1. **Frontmatter** com `name`, `description` (só gatilhos), `user-invocable: true`.
2. **Parágrafo de identidade** (2-3 frases): que peça produz, princípio central inviolável.
3. **Restrições absolutas**: o blocklist da DNA, adaptado ao formato. Ver [templates/blocklist.template.md](../templates/blocklist.template.md).
4. **Localização da DNA e do banco**: paths absolutos referenciáveis.
5. **Gates de preflight**: bloco `<NOME>_PREFLIGHT` declarável. Ver [templates/preflight.template.md](../templates/preflight.template.md).
6. **Workflow obrigatório**: tabela de fases com referência e função.
7. **Como invocar**: sem argumento (menu), com brief direto, sub-comandos parciais.
8. **Few-shot BAD/GOOD**: 3-7 pares de calibração de voz, tirados da DNA e adaptados ao formato.
9. **Formato de saída padrão**: bloco com metadata (brief, exemplares, audit, critique score).
10. **Princípios operacionais e comportamento esperado**.

## As fases por tipo de peça

Adapte as fases ao `peca` do brief. Mínimo recomendado por tipo:

| Peça | Fases recomendadas |
|---|---|
| Anúncio cold | intake, disguise, retrieval, craft, hook, critique, audit, polish |
| VSL | intake, big-idea/lead, retrieval, craft (blocos: lead, story, mecanismo, prova, oferta, fechamento), critique, audit, polish |
| E-mail | intake, ângulo, craft (assunto + corpo + CTA), sequência (se múltiplos), critique, audit, polish |
| Sales page | intake, estrutura, retrieval, craft (por bloco), prova, oferta, critique, audit, polish |
| Headline/lead | intake, retrieval, craft (5-10 variações), testes de hook, audit |
| Upsell/downsell | intake, ponte com a oferta principal, craft, critique, audit, polish |

**Regras transversais a toda peça:**

- O hook/abertura é decidido DEPOIS do corpo, nunca travado no craft (regra da copy-ads).
- Toda fase de craft termina num **production bar** (exit gate com checklist).
- Toda skill tem **critique** (10 heurísticas /40 + personas) e **audit** (scans binários). Ver templates.
- Prova sempre específica (nome + idade + situação + número). Nunca inventada.

## Fases fixas que toda skill gerada precisa ter

Independente da peça, sempre inclua:

- **critique**: scoring quantitativo. Template em [templates/critique.template.md](../templates/critique.template.md).
- **audit**: scans binários contra o blocklist da DNA. Template em [templates/audit.template.md](../templates/audit.template.md).
- **polish**: refinamento cirúrgico final.

Essas três são o "sistema imunológico" que mantém a DNA viva no output. Nenhuma skill gerada sai sem elas.

## Onde a DNA entra no workflow gerado

- O `dna-card.md` é inlinado/referenciado no SKILL.md gerado, carregado em toda invocação como `dna=loaded` no preflight.
- A fase de craft consulta o card antes de cada bloco.
- A fase de audit consulta a DNA completa (`dna/ai-tells.md`) para os scans.
- A fase de critique consulta a DNA completa (`dna/disguise.md`) para pontuar as 7 alavancas.

Detalhe completo da injeção: [dna-injection.md](dna-injection.md).
