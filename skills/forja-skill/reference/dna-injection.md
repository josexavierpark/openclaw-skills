# Fase 3: DNA Injection (duas camadas)

Como embutir o disguise + ai-tells em toda skill gerada. Modelo escolhido: **duas camadas**. Card comprimido sempre ativo + cópia completa sob demanda + comando de sincronização.

## Por que duas camadas

A pesquisa completa soma ~3.300 linhas. Inlinar isso em cada skill quebra o orçamento de tokens (regra da [authoring-rules.md](authoring-rules.md)). Mas precisa estar "forte" em toda invocação. Solução:

- **Camada 1 (sempre ativa):** o [dna-card.md](../dna/dna-card.md) comprimido, ~1 página. Carregado em toda invocação da skill gerada, declarado no preflight como `dna=loaded`. É o blocklist + as 7 alavancas + o checklist de 19 itens.
- **Camada 2 (sob demanda):** as cópias completas `disguise.md` e `ai-tells.md`, lidas só nas fases de critique e audit, quando o detalhe importa.

## O que a skill gerada recebe

Toda skill gerada ganha a pasta `dna/` com três arquivos, copiados de [forja-skill/dna/](../dna/):

```
nome-da-skill/
└── dna/
    ├── dna-card.md     # camada 1: inlinado/referenciado no SKILL.md, sempre ativo
    ├── disguise.md     # camada 2: lido na fase critique
    └── ai-tells.md     # camada 2: lido na fase audit
```

## Procedimento de injeção

### Passo 1: Copie a DNA

```bash
SRC=~/.claude/skills/forja-skill/dna
DEST=<path-da-skill-nova>/dna
mkdir -p "$DEST"
cp "$SRC/dna-card.md" "$SRC/disguise.md" "$SRC/ai-tells.md" "$DEST/"
```

### Passo 2: Referencie a camada 1 no SKILL.md gerado

No bloco de "Restrições absolutas" do SKILL.md gerado, não cole o card inteiro. Referencie e resuma os Tier-1 bloqueantes:

```markdown
## Restrições absolutas (DNA, invioláveis)

Carregue [dna/dna-card.md](dna/dna-card.md) em toda invocação (`dna=loaded`). Os Tier-1 bloqueantes: zero em-dash, zero "Não é X, é Y", zero palavras-vício, zero CTAs fracas, zero Title Case PT-BR, mecanismo sempre com nome chiclete. Lista completa e as 7 alavancas no card.
```

### Passo 3: Plugue a camada 2 nas fases

- Na referência de **critique** gerada: "Consulte [dna/disguise.md](../dna/disguise.md) para pontuar as 7 alavancas."
- Na referência de **audit** gerada: "Rode os scans contra [dna/ai-tells.md](../dna/ai-tells.md) Anexo A."

### Passo 4: Registre o preflight

O bloco de preflight da skill gerada precisa do gate `dna`:

```
<NOME>_PREFLIGHT: ... dna=loaded ...
```

Onde `dna=loaded` significa: o `dna-card.md` foi lido nesta sessão.

## Comando sync-dna

Quando a pesquisa canônica em [forja-skill/dna/](../dna/) evolui, as cópias nas skills geradas ficam velhas. O comando `sync-dna <path>` recopia os três arquivos da fonte para a skill apontada. Use sempre que `disguise.md` ou `ai-tells.md` receberem atualização validada.

```bash
SRC=~/.claude/skills/forja-skill/dna
cp "$SRC/dna-card.md" "$SRC/disguise.md" "$SRC/ai-tells.md" "<path-da-skill>/dna/"
echo "DNA sincronizada em <path-da-skill>/dna/"
```

A fonte única da verdade é sempre [forja-skill/dna/](../dna/). As cópias nas skills geradas são derivadas, nunca editadas à mão.
