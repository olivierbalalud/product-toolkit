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
| Personas, journeys, pain points, objections | `docs/product/inputs/`, cited by ID from use cases | R3-A5 |
| A domain glossary, e.g. a French → English one | `docs/product/glossary.md`, used by spec writing and by translation | R3-A5 |
| Informal use cases | Kept as inputs; rewritten in the fully dressed format when picked | R3-A5, R1-Q6 |
| An existing decision register | **Frozen** as a historical log; new decisions are ADRs, which may cite the entries they supersede | R3-A2 |
| Bare one-letter IDs | Replaced by typed IDs for new artifacts | R3-A3 |
| A local markdown ticket tracker | Its pattern carries on in the story and enabler `tickets/` folders | R6-Q2, R13-Q1 |

## 13.3 Settle the target first

Before the first enabler, the monorepo settles by **ADR** each place where its current direction differs from the target stack: front end, services, runtime, deployment, website and repository layout. For one specific monorepo, the list is in [`monorepo-fit.md`](../context/monorepo-fit.md) [R3-A1, R26-Q1].

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
| 7 | **The other P0 skills**: `write-use-case`, `write-scenarios`, `write-stories`, `check-fit`, `review-design` ([chapter 12](12-skills-to-build.md)). Built in parallel with 3–6; done before the first PRD leaves *Exploring* | The first design gate |

`check-gate`'s scripts are part of enabler 1 [R26-Q2].

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

1. Pick a use case that touches little existing code, so the first run tests the process rather than the legacy.
2. Run it end to end: use case → stories → *Exploring* → Design-complete → Dev-ready → slice → Done.
3. Hold a short **retrospective**. What the framework got wrong becomes a new round in this repository's decision log, then a guide update. Repeat after the third PRD [R26-Q3].
