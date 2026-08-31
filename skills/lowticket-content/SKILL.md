---
name: lowticket-content
description: Use when creating the content or deliverables of a low-ticket digital product (course, ebook, mini-course, app) that must be grounded in real research (YouTube + web via NotebookLM), audited against sources, and written truly step-by-step in the audience's language. Also covers generated printable deliverables (worksheets, activity sheets, flashcards, certificates, planners) produced by a code engine (HTML+SVG to PDF), not written by hand. Triggers: criar conteúdo do curso/ebook/app, preencher entregáveis, material do infoproduto, passo a passo confiável, conteúdo fundamentado/auditado, NotebookLM, pesquisa no YouTube, fichas imprimíveis, atividades para imprimir, gerar fichas/worksheets, caderno de atividades, certificado/planner imprimível.
---

# Low-Ticket Content (grounded, step-by-step)

## Overview

Produce the **deliverable content** of a low-ticket product — grounded in real research (YouTube + web),
**audited** against its sources, written **step-by-step in the audience's language**. Research goes into
**Google NotebookLM** (one notebook per deliverable) = the source of truth; the final content comes out as
`.md` (or straight into an app's `data.js`).

**Core principle:** *the obvious must be said*. Low-ticket content sells on clarity and the feeling of being
taken by the hand. Never skip a step, never use jargon without explaining it, never invent.

**Two kinds of deliverable:**
- **Mode A, written content** (course/ebook/app text): the workflow below (research, NotebookLM, audited step-by-step, `.md`/`data.js`).
- **Mode B, generated printables** (worksheets, activity sheets, flashcards, certificates, planners): build a small **code generator** (HTML + SVG rendered to PDF) so output is exact, infinitely varied by seed, fully owned, and reproducible at 0 tokens per change. Engine, print checklist, functional audit and the premium image layer live in `printables-engine.md`. Most principles here still apply (customer-facing only, anti-AI writing, audience's language, say the obvious); Mode B adds a print checklist and a functional (logic) audit on top of the anti-hallucination one.

## When to use

- "Write the content of my course / ebook / app about X", "fill in the deliverables", "infoproduct material"
- Turning a topic into a trustworthy, current, step-by-step deliverable
- Whenever content must be **grounded** (not "AI guesswork")
- **Generated printables** (worksheets, activity sheets, flashcards, certificates, planners) produced by a code engine instead of written by hand: Mode B, see `printables-engine.md`

## Principles (non-negotiable)

1. **The obvious must be said** — the beginner doesn't know the "obvious" step.
2. **Real step-by-step** — one action per step, in true execution order.
3. **Explain each term on first use** — "flower nail (the plastic base where the flower is piped)".
4. **Short sentences** — easy reading for any age.
5. **The audience's language** — name things by what the person recognizes, not the system's term.
6. **Grounded, never invented** — every claim traceable to the notebook's sources.

## HARD RULE — the deliverable is customer-facing ONLY

The output `.md` (or `data.js`) is the **finished product the paying end-user reads**. It must contain
**only** that content — **nothing addressed to you, the creator, or the AI**.

**Forbidden inside the deliverable (zero tolerance):**
- Notes to the creator/AI — "observação para mim", "nota: revisar isto", "creator: check this"
- Warnings or asides aimed at the creator
- Source/meta talk — "segundo nossas fontes", "não encontrei isto nas fontes", "de acordo com o vídeo X"
- TODOs, "talvez adicionar…", "[inserir foto aqui]", placeholders, process talk ("composto a partir de…")

**Where creator-facing flags go instead:** a SEPARATE file (e.g. `notas-revisao.md`) or your chat reply to the
user — **NEVER inside the deliverable**. If something needs human review, write the deliverable clean and put
the flag *outside* it.

**Self-check before saving:** read the final file as if you were the customer. If a line isn't content they'd
want to read, delete it. The deliverable must read like a finished product, start to finish.

**Better than a self-check — enforce it in code:** when a converter builds the data/PDF, put a `scrub()` in it
that strips backstage automatically, plus a post-build `grep` scan that fails on any blacklisted term. See
"Enforce the customer-facing rule in CODE" in `research-pipeline.md`.

## Anti-AI writing filter (apply to ALL content: intros, steps, tips, labels)

Every word the reader sees must read like a sharp human wrote it, not a chatbot. Run this before saving.

- **Banned — hype adjectives:** incrível, surpreendente, poderoso, inovador, revolucionário, exclusivo,
  transformador, imperdível, "solução completa", "experiência única", "leve ao próximo nível", "tudo que você
  precisa". *(EN: game-changer, seamless, robust, cutting-edge, powerful, unleash, unlock, elevate, leverage, delve.)*
- **Banned — empty openers/closers:** "No mundo de hoje", "Na era digital", "Vivemos um tempo em que…", "Não é
  segredo que…", "Imagine só…", "Em resumo", "Em conclusão", "No final das contas", "Vale ressaltar/destacar",
  "É importante notar". *(EN: "In today's fast-paced world", "It's worth noting", "In conclusion", "Furthermore".)*
- **Banned — AI tics:** regra-de-três em tudo ("rápido, fácil e eficiente"); "não apenas X, mas também Y"
  repetido; hedging vazio ("pode ser que", "geralmente") quando você sabe o específico; parágrafo de intro/
  conclusão que só repete o tema; travessão (—) jogado em toda frase; entusiasmo falso com excesso de "!".
- **Do instead:** seja **específico e concreto** (número, nome, ponto, tempo, detalhe sensorial) em vez de
  adjetivo; escreva como quem entende do assunto falando com o leitor; **uma ideia por frase**; voz ativa,
  verbo simples; corte intro/conclusão que não dizem nada; troque elogio por prova.
- **Test:** se a frase poderia vender qualquer coisa (trocar o substantivo e ainda serve), está genérica demais
  — reescreva específica para ESTE assunto.

## Workflow (commands in `research-pipeline.md`)

0. **Map deliverables + audience.** List deliverables; define audience & tone (drives the style). **One
   NotebookLM notebook per deliverable** (focused, auditable — not one shallow "general" notebook).
1. **Research (YouTube + web).** Per deliverable: `yt-search` with 3–5 specific queries (the *practitioner's*
   term, not the academic one). Prefer recent, high-traction videos for currency. **Validate a source's
   intent before adopting it** (transcribe & skim) — wrong-topic sources poison the notebook.
2. **Build the source of truth in NotebookLM.** Add the best YouTube sources + `source add-research` (deep web).
   Set `pt_BR`. Confirm the sources actually match the deliverable's intent.
3. **Audited extraction.** `ask` the notebook **per step**, with `--json` for references; `--save-as-note` the
   key answers for traceability.
4. **Write the content (.md / data.js)** in the audience's style: short intro → materials → numbered steps →
   "if it happens…" (problem → fix) → golden tip.
5. **Anti-hallucination audit + clean-text pass.** Cross-check **every claim** against sources (unsupported →
   confirm or cut). Then strip **all** non-customer text per the HARD RULE above — no meta-notes, no
   creator-facing notes, no TODOs/placeholders.
6. **(Optional) Photo/image plan** per deliverable. **Package** → `data.js` (app), ebook (`docx`/`pdf`), modules.

## Getting content into an app cheaply (if it's for a PWA/app)

The app reads **data**, not `.md`. Many repeating items → write a **readable Markdown convention** and let a
**converter/parser** turn it into `data.js`/JSON (**0 tokens** per update — code converts, not the AI). Few
items written once → manual is fine. Authoring format + details in `research-pipeline.md`.

> **Skill boundary.** This skill owns the **deliverable + the `.md`→data converter** (incl. `scrub`, xref
> resolution, and the single parser that *also* renders material PDFs). The **app shell, service worker, how
> downloads are served/cached, runtime features and deploy** belong to **`premium-pwa-builder`**. Building a
> content app → use both; don't reimplement the other side's lesson.

## Workflow B — generated printables (engine in `printables-engine.md`)

0. **Map deliverables + audience + print spec** (A4 or Letter, B&W or color, age bands, levels). Give each item a unique **code** (`XX-NN`); it prints on the sheet and is the key into the catalog and app.
1. **Ground the method, not only facts.** For activity products the source of truth is the pedagogy/standard behind the exercises. Research it (web), cite it, keep an honest frame (support, not treatment, when health-adjacent).
2. **Build the engine + an owned asset library.** HTML + SVG rendered to PDF (Chrome headless); your own SVG icon set (no license trap). One generator per category calling a shared `run_category`.
3. **Generate + functional audit.** Render a sample of each activity type and Read it back: is the puzzle solvable, the answer unique, the count unambiguous, the sheet exactly 1 page? Fix, then scale.
4. **Catalog as single source of truth** (`catalogo.json`) drives generator + app, plus a per-group "print the whole booklet" PDF.
5. **(Optional) premium colored layer** via image gen for vitrine/upsell, with the hard caveats (logic types stay in code; image gen drops accents and fails rigid puzzles).
6. **Handoff** doc if the product is done-for-you.

The HARD RULE and the anti-AI filter apply to every printed word here too.

## Common mistakes (real, from our build)

| Mistake | Lesson |
|---|---|
| First "flower" sources were about fondant cutters, not piping | **Validate source intent** (transcribe/read) before adding. Practitioner query > generic query |
| Left meta-notes or creator-facing notes in the deliverable ("according to our sources…", "nota: revisar", "[add photo]") | The deliverable is customer-facing ONLY. Assert confidently; put any review flag in a SEPARATE file or the chat (see HARD RULE) |
| One shallow notebook for everything | **One notebook per deliverable** = focused, auditable |
| Skipped the "obvious" | The beginner doesn't know it. **Say the obvious** |
| Pasted raw YouTube transcripts | Let NotebookLM **synthesize with references**; you audit |
| Stale content | Filter by date, deep research, verify current tools/materials/prices |
| (Mode B) A sheet overflowed to 2 pages | Verify page count; size the body to fit; check after every change |
| (Mode B) Emoji glyphs printed in color and broke B&W | Use geometric unicode or drawn SVG, not emoji |
| (Mode B) HTML entities leaked into the catalog (`&ccedil;`) | Decode entities before writing data the app reads |
| (Mode B) A "find the pair" had no solution; a shape count was ambiguous | Functional audit per type: solvable, unique answer, unambiguous |
| (Mode B) Reused "free" printables / clipart | Free is not a commercial license. Use CC0/PLR or draw your own owned assets |
| (Mode B premium) Image gen made a pretty but unsolvable maze and dropped accents | Keep rigid-logic in code B&W; use image gen only for visual types; verify and re-send |

## Quality checklist

- [ ] One on-topic (validated) notebook per deliverable
- [ ] Every claim traceable to a source (or marked for review); **no meta-note in the text**
- [ ] Steps in real order, one action each, the obvious said; each term explained on first use
- [ ] Short sentences, audience's language, imperative verbs
- [ ] "If it happens…" (errors → fixes) per deliverable
- [ ] Current (recent sources, verified practices); absolute dates; no inflated adjectives

**Mode B (printables) also:**
- [ ] Every individual sheet is exactly 1 page (booklets aside); A4/Letter; B&W or color per spec
- [ ] Functional audit passed per type (solvable, unique answer, unambiguous count, real rule)
- [ ] Owned/licensed assets only (no "free" clipart resold); accents render correctly
- [ ] One unique code per item; `catalogo.json` drives generator and app
- [ ] Premium image versions (if any): logic types kept in code; each checked for accents/correctness

## Reference
- **`research-pipeline.md`**: NotebookLM auth + commands, yt-search, per-phase commands, and the readable
  Markdown authoring convention (content to app). (Mode A)
- **`printables-engine.md`**: code engine (HTML+SVG to PDF), owned icon library, print checklist, functional
  audit, catalog-as-source-of-truth, premium image layer with caveats, and the handoff doc. (Mode B)
