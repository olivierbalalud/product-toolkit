# 13. Adoption

How to bring the framework into a product monorepo that already exists. Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md). This chapter stays generic; the facts about one specific monorepo are in [`../context/monorepo-fit.md`](../context/monorepo-fit.md) [R3-Q0a, R5-Q3].

## 13.1 Principles

1. **Brownfield, not a rewrite.** Existing personas, journeys, use cases and glossaries are imported as inputs, not rewritten [R3-A5, R5-Q3].
2. **Enablers first.** No feature slice can pass Done until the enabler slices it depends on exist: CI, the app shell, the design system, i18n, the test harnesses [R5-Q3].
3. **Decisions before code.** Where the monorepo's current direction differs from the framework's target stack, the difference is settled by an ADR in the monorepo, not assumed [R3-A1].
4. **Use Claude Code's mechanisms rather than override them** [R16-P].

## 13.2 Import what exists

| Existing material | Goes to | Decision |
|---|---|---|
| Personas, journeys, pain points, objections, hypotheses | `docs/product/inputs/`, one file per kind, cited by ID from use cases. The import rewrites the IDs only; the prose stays as written | R3-A5, R30-Q2, R30-Q3 |
| Buying blockers | `docs/product/inputs/blockers.md`, broadened to anything that stops a customer or user buying or adopting, in the [light format](../templates/blockers.md) | R30-Q4′, R30-Q21′ |
| A domain glossary, e.g. a French → English one | `docs/product/glossary.md`, used by spec writing and by translation | R3-A5 |
| Informal use cases | Kept as inputs; rewritten in the fully dressed format when picked | R3-A5, R1-Q6 |
| An existing decision register | **Frozen** as a historical log; new decisions are ADRs, which may cite the entries they supersede | R3-A2 |
| Bare one-letter IDs | Replaced by typed IDs for new artifacts and imported inputs (`PER-`, `JRN-`, `PP-`, `BLK-`, `OBJ-`, `HYP-`); `inputs/id-map.md` keeps the old ones | R3-A3, R30-Q1, R30-Q2 |
| Principles or constraints in an architecture document (optional) | One input file with no ID type; each becomes an ADR when a PRD first depends on it | R30-Q9′ |
| A local markdown ticket tracker | Its pattern carries on in the story and enabler `tickets/` folders | R6-Q2, R13-Q1 |

Import on its own branch from the main branch. When the material lives on a branch that isn't merged, record the commit it was taken from, and import it again if it changes there [R30-Q14].

Rewriting an informal use case in the fully dressed format often finds more than one use case in it [R30-Q13]:

- **Several actors with a wait between them**, such as an invitation accepted days later: split at the wait point [R29-Q2].
- **One version per technical option**: write it once with the options as variations, and make the choice of option an ADR.
- **A login or setup flow**: often a subfunction of another use case rather than a user goal [R28-Q1].

## 13.3 Settle the target first

Importing inputs, writing use cases, cutting stories and building `write-use-case` don't depend on the stack, so they start right away [R30-Q10]. Before enabler 3 and the first *Exploring*, the monorepo settles by **ADR** each place where its current direction differs from the target stack: front end, services, runtime, deployment, website and repository layout. For one specific monorepo, the list is in [`monorepo-fit.md`](../context/monorepo-fit.md) [R3-A1, R26-Q1].

## 13.4 The first enabler slices

In this order [R5-Q3, R16-Q0, R26-Q2]:

| # | Enabler | Unblocks |
|---|---|---|
| 1 | **CI with the gate check**: `check-gate`'s scripts, the `coverage.md` and `index.md` generators, lint | Every gate |
| 2 | **Worktree start scripts and environments**: `make design`, `make slice`, `make dcr`, `make enb`, `make env-up` (shared PostgreSQL with pgvector, a cloned database per worktree, offset ports), `make env-prune` | Parallel design and slices |
| 3 | **App shell and design system**: the Next.js app, `src/packages/tokens`, `src/packages/ui`, Storybook, and the two design-system mirrors (the Figma library and the Claude Design design system) | Prototypes, design-system work |
| 4 | **i18n layer**: next-intl, `src/packages/i18n` with catalogs, status sidecars and `locales.ts` | Copy decks, translations |
| 5 | **Test harnesses**: pytest-bdd per domain (version 8 or later, for Gherkin `Rule:` blocks [R28-Q16]), playwright-bdd for `@ui` scenarios | Slices |
| 6 | **Analytics port with its fake** | Measurement plans |
| 7 | **The other P0 skills**: `write-use-case`, `write-scenarios`, `write-stories`, `check-fit`, `review-design` ([chapter 12](12-skills-to-build.md)). Built in parallel with 3–6, except `write-use-case`, which may come first [R30-Q10]; done before the first PRD leaves *Exploring* | The first design gate |

`check-gate`'s scripts are part of enabler 1 [R26-Q2]. Until it lands, a use case reaches `Complete` on a local run of `write-use-case`'s `check_grid.py` plus the PR review, and CI checks it again afterwards [R30-Q11].

## 13.5 Set up Claude Code

| Step | What | Chapter |
|---|---|---|
| Marketplace and plugins | `tools/claude-marketplace/` with our plugin and pinned third-party entries; `extraKnownMarketplaces` and `enabledPlugins` in `.claude/settings.json`; MCP servers in `.mcp.json` | [11](11-tooling-and-plugins.md) |
| mattpocock setup | Run `setup-matt-pocock-skills` once, then edit `docs/agents/issue-tracker.md` to describe the story and enabler `tickets/` folders | [4](04-dev-playbook.md), R13-Q1 |
| Product settings | `docs/product/settings.yaml`: `metrics_stage`, `outcome_review_after` | [10](10-outcomes-and-measurement.md) |
| Design docs | `docs/design/voice-and-tone.md`, `design-system.md`, `motion.md` | [6](06-design-system-and-figma.md), [7](07-i18n-and-voice.md) |
| Collision check | `check-setup` on each developer's machine | [11](11-tooling-and-plugins.md), [12](12-skills-to-build.md) |
| `.gitignore` | `.claude/worktrees/`, `.env.worktree`, `reports/` | [5](05-worktrees-and-parallelism.md), [8](08-testing.md) |

## 13.6 The first PRD

1. Pick a use case that touches little existing code, so the first run tests the process rather than the legacy. The use case the design skills are built against may be another one, picked to exercise most of their procedure: long steps, a wait point, conflicts, the privacy line [R30-Q12].
2. Run it end to end: use case → stories → *Exploring* → Design-complete → Dev-ready → slice → Done.
3. Hold a short **retrospective**. What the framework got wrong becomes a new round in this repository's decision log, then a guide update. Repeat after the third PRD [R26-Q3].
