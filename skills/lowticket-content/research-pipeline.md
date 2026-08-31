# Research Pipeline — NotebookLM + YouTube, and the authoring format

## Auth (NotebookLM)

```bash
notebooklm login                          # browser OAuth (once)
notebooklm auth check --test --json       # require status:ok AND checks.token_fetch:true
notebooklm language set pt_BR
```
If commands fail with auth errors → re-run `notebooklm login`.

## Phase 1 — Discover sources (YouTube)

```bash
# yt-search skill (also: youtube-search / youtube-transcript / transcript / captions skills)
python3 ~/.claude/skills/yt-search/scripts/search.py "<practitioner query>" --count 8
```
- 3–5 specific queries per deliverable. Use the **practitioner's term** ("flores no bico" > "decoração de bolo").
- Prefer **recent, high-traction** videos when the topic moves fast.
- **Before adopting** a source, transcribe (youtube-transcript/transcript) and skim — confirm it's actually
  about the right intent (wrong-topic sources poison the notebook).

## Phase 2 — Build the notebook (one per deliverable)

```bash
notebooklm create "Deliverable X — research"        # note the returned <id>; use -n <id> in parallel
notebooklm source add "https://youtube.com/watch?v=..."          # best validated videos
notebooklm source add-research "how to do X step by step" --mode deep --no-wait   # deep web research
notebooklm research wait --import-all
notebooklm source list                               # confirm what came in (on-topic?)
```

## Phase 3 — Audited extraction (grounded Q&A)

```bash
notebooklm ask "List, step by step, how to do X. Each step with materials and the right point." --json
notebooklm ask "Most common mistakes in X and how to fix them?" --save-as-note --note-title "Errors X"
```
- `--json` returns **references** (which source) → the basis of the audit.
- `--save-as-note` the key answers → traceability.

## Phase 4–5 — Write + audit

- Write each deliverable in the audience's style: short intro → materials → numbered steps (`Verb …`) →
  "if it happens…" (problem → fix) → golden tip.
- Cross-check every claim against the notebook's sources. Unsupported → confirm or cut.
- **The deliverable is customer-facing ONLY.** It must contain *only* what the end-user reads — nothing
  addressed to you, the creator, or the AI. **Forbidden inside the file:** notes to the creator/AI
  ("observação para mim", "nota: revisar"), source/meta talk ("segundo nossas fontes", "não encontrei"),
  TODOs, "[inserir foto aqui]", placeholders, process talk ("composto a partir de…").
- If something isn't in the sources: research more, or compose from sibling techniques **confidently** — and
  put any review flag in a **SEPARATE file** (e.g. `notas-revisao.md`) or your chat reply, **never inside the
  deliverable**.
- **Final clean-text pass:** read the file as the customer. If a line isn't content they'd want to read, delete it.

## Currency

- Date filters; prefer recent sources when the technique/trend evolves.
- `add-research --mode deep` for broad, grounded web sweeps.
- Convert relative dates to absolute when recording ("this year" → "2026").
- Re-check whether tools/materials/prices changed before fixing them in the content.

## Authoring format — Markdown → app (content reaches the app at 0 tokens/update)

When a deliverable has **many repeating items** (e.g. 12 flowers, 20 lessons), write a **simple Markdown
convention** — readable by a human, predictable for a parser. Few rules: `##` starts an item; `key: value`
are fields; lists use `|` to split sub-fields.

```markdown
## Rosa
nivel: Fácil
bico: Bico 104 (pétala) — lado grosso para baixo
resumo: A flor que mais vende. Feita no bico 104, pétala por pétala.

Separar:
- Brigadeiro branco no ponto de bico, tingido
- Bico 104

Passos:
1. Montar o saco | Encaixe o bico 104 na ponta do saco... | Dica: lado grosso pra baixo.
2. A torrezinha | Faça uma base de massa no centro do armador...

Se acontecer:
- A flor não fica em pé | Volte a massa ao ponto mais firme.
```

- **Becomes app** via (a) a **converter** `gerar-conteudo.mjs` (`## `→item, `key: value`→field, `|`→subfields)
  that writes `data.js`/JSON, or (b) a **runtime parser** in the app. Both: **0 tokens** per update — code
  converts, not the AI. Manual rewrite by AI costs tokens every time → only worth it for content written once.
- **Match the convention to the renderers' schema** (the `.md` fields = the fields the screen uses) — that's
  what makes conversion trivial and typo-proof.
- **Size never decides** (`.md` vs `data.js` differ ~2–4KB, < 0.2% of the app). Choose by editing convenience.

## Enforce the customer-facing rule in CODE (scrub + scan)

The HARD RULE shouldn't rely on the human remembering to clean. If a converter builds the data/PDF, bake it in:

- A **`scrub()`** in the parser that mechanically strips any backstage that slips past review: whole sections
  by heading (`Fontes`, `Referências`, `Como validar`, `Validação`), inline `Fonte: …` anywhere, process
  labels ("baseada em pesquisa", "a validar", "Fórmula Candidata", "candidata", source/blog names), then
  cleans the debris (empty `()`, orphan space before punctuation, double spaces, leading `,`/`;`).
- A **post-build scan**: after writing the JSON/PDF, `grep` the output against a blacklist and **fail/flag the
  build** if any forbidden term leaked. Code doesn't forget — with 100+ items a stray "Fonte:" always slips.

## Cross-references: `.md` → navigable link, never raw `.md` in the UI

Course content cross-refs a lot ("see the Fresh Pasta guide"). In the convention, a `[Text](file.md)` or
`` `file.md` `` is resolved by the converter to an **internal navigable link** with a human title
(`ravioli.md` → "Ravioli"); a **broken** ref is dropped (not a dead link); **no raw `.md` reaches the UI**.

- Build a `slug → {id, title}` map during indexing; ignore the file's numeric prefix when matching (`06-` vs
  `08-`). Replace the match with `<a data-item="ID">Title</a>` (or plain text in a PDF). No match → keep the
  text, drop the link.
