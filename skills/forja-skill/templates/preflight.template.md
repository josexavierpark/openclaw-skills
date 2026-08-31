# Template: bloco de preflight

Cole no SKILL.md gerado, na seção "Gates de preflight". Troque `<NOME>` pelo nome da skill em maiúscula e adapte os gates às fases dela.

```markdown
## Gates de preflight

Antes de qualquer escrita de copy, declare:

\`\`\`
<NOME>_PREFLIGHT: intake=pass dna=loaded retrieval=pass blocklist=loaded mutation=open
\`\`\`

| Gate | Verificação |
|---|---|
| `intake` | Brief declarado e confirmado pelo usuário |
| `dna` | `dna/dna-card.md` lido nesta sessão |
| `retrieval` | Exemplares/matéria-prima selecionados (se a skill tem banco) |
| `blocklist` | Restrições absolutas da DNA ativas |
| `mutation` | Todos os gates acima passaram |

Se algum gate falhar, pare e informe o que falta.
```

## Regras

- Sempre inclua os gates `dna` e `mutation`. São obrigatórios.
- O gate `intake` (ou equivalente de brief) é obrigatório: nada de gerar copy sem brief.
- Adapte os gates do meio à peça: VSL pode ter `big-idea=pass`; e-mail pode ter `angulo=pass`.
- O nome do bloco em maiúscula, terminando em `_PREFLIGHT` (ex: `COPADS_PREFLIGHT`, `VSL_PREFLIGHT`).
