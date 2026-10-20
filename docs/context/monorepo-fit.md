# Monorepo Fit

**Scope.** This file records structural facts only about the product monorepo, as seen in a read-only inspection on 2026-10-19 (branch `docs/arch-audit`, HEAD `482a940`). By decision R3-Q0a it contains no product concepts, internal names or business content. The framework docs elsewhere in this repo stay generic.

**Status of the code.** The current code is an early demo that was vibe-coded (R3-Q0b). The framework targets the *confirmed* stack: Next.js + shadcn, FastAPI, Kubernetes, and the company website in a separate repo.

## Divergences between the confirmed target and the monorepo's own docs

The monorepo's in-progress architecture audit (`docs/arch-audit/`) and its decision register take different positions from the confirmed target. These divergences must be settled through ADRs in the monorepo, not in this repo.

| Topic | Confirmed target | Monorepo docs today |
|---|---|---|
| Frontend | Next.js + React + shadcn + Tailwind | A registered decision keeps server-side rendering with htmx and no build step, and rejects an SPA. The audit plans to mount the existing server-rendered routes in FastAPI gradually. React and shadcn appear only as a wish for the login UI. |
| Services | FastAPI everywhere | A registered decision says "no FastAPI". The audit's "standardise on FastAPI" is not yet registered. Phase H0 puts only the upload/document service behind HTTP. |
| Runtime | Gunicorn/Uvicorn workers | A single uvicorn worker, forced by the memory of the embedded models. Several workers need a shared model service first. |
| Deployment | Docker in dev; Kubernetes for staging and prod | Docker Compose on a single host. The next horizon plans VMs with self-run Postgres. There is no staging environment and Kubernetes is not decided. |
| Website | Separate repo | Served today by the same app (landing page and legal pages). The audit plans it as a separate deployable *inside* the monorepo. |
| Repo layout | `apps/`, `services/`, `packages/` (R3-Q1, pending) | A monorepo is decided: a shared core plus one package per compartment, with no directory naming yet. |

## Existing spec and decision conventions

- **Decision register:** in French, with sequential `D<n>` IDs. The register is an index, and the decision text lives in phase plan files. A rule in `CLAUDE.md` says a decision must be registered before code cites it, and numbers are never reused. Decisions taken outside the register are flagged and wait for registration.
- **There are no ADRs, TRDs, user stories or Gherkin files.** PRDs are planned, but their template is not decided.
- **Use cases:** a handful exist, in English, in an informal format: actors, precondition, numbered steps, variants inline, an audit-trail list. They are not in Cockburn format, and extensions are not labelled.
- **Personas and journeys:** role-based proto-personas with evidence tags and jobs-to-be-done, journeys as Mermaid diagrams, plus pain points, buying blockers, hypotheses and customer objections. All are numbered. These are natural *inputs* to use cases.
- **Tracker:** a local markdown "wayfinder": a `map.md` plus `tickets/NN-slug.md` with frontmatter (`type`, `mode` AFK/HITL, `status`, `blocked_by`). Grilling, research and prototype tickets call the matching skills.
- **Glossary:** `CONTEXT.md`, a French→English glossary (term, definition, examples, terms to avoid).
- **ID collisions:** bare-letter prefixes are reused across artifact types. `T` is both a task and a technical verdict. `P` is a persona, a decision round and a debt. `H1` is both a horizon and a hypothesis. → Settled in Round 30: imported inputs take typed IDs (`PER-`, `JRN-`, `PP-`, `BLK-`, `OBJ-`, `HYP-`), with a table of the old IDs [R30-Q1, R30-Q2]. The monorepo's buying blockers become blockers, which also cover adoption [R30-Q4′].

## Language and git conventions

- `CLAUDE.md` says new code, tests, comments, docs and commits are in **English**. Existing French identifiers and the French domain vocabulary in the schema stay as they are, with no mass renaming.
- The UI is French only, with no i18n layer. Screen strings sit in Python constant modules.
- Commits follow English Conventional Commits now; older history is free-form French. Branches are `<type>/<kebab>`. No PR or review process is documented.

## Testing and tooling baseline

- pytest, in a flat `tests/` with about 140 files. Tests run against a real Postgres with the real database roles, and a "run twice on the same DB" target exists.
- There is already a hexagonal core: ports, fake adapters injected at the composition roots, recorded cassettes at the port level, and architecture tests that enforce dependency rules.
- Security and privacy tests exist: row-level security and roles, sessions, secrets, erasure and redaction.
- No Playwright/e2e tests, **no CI**, no `.claude/` directory, no design tool, no Storybook. Accessibility work is ad-hoc (`aria-*` only, no WCAG/RGAA reference).
- The UI has a hand-written CSS file with custom-property tokens (no dark mode), and Jinja macros act as a component library.
- Capacity: two founders at about 3 days a week each, working with Claude Code.

## Implications for the framework

1. Plan for **brownfield adoption**. Existing personas, journeys and use cases are imported as inputs, not rewritten.
2. Decide how **ADRs relate to the existing decision register** (R3-A2).
3. Define **typed ID prefixes** (R3-A3).
4. Accept that the first slices will be **enabler slices**: CI, the Next.js app shell, the tokens package, an i18n layer and Playwright. No feature slice can meet the Done gate (R2-Q5) until they exist.
5. The FR→EN glossary pattern can be reused as the translation glossary (R2-Q6).
