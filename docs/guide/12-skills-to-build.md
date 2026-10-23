# 12. Skills to Build

The Claude Code skills the framework needs and nobody publishes, how they are specified, built and tested, and in what order. They are **specified here and built later in the monorepo**; this repository creates no skills [R1-Q2]. Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md). Practices and facts come from the [skill authoring research](../research/skill-authoring.md) (2026-10-19).

## 12.1 Principles

1. **Start from an observed gap.** A skill exists because Claude gets something wrong without it. Its spec names those failures, and they become its first evals ([research §2](../research/skill-authoring.md)) [R25-Q4].
2. **Scripts check, the model judges.** Anything a script can decide (frontmatter, required files, ID cross-references, coverage counts, ICU syntax) is a script with JSON output and exit codes, so CI can run it without an agent. The model judges only what a script can't [R5-Q4′].
3. **Written to the portable core.** Each skill folder uses only the open Agent Skills format; Claude Code wiring lives in the plugin; adapters for other tools are built only when one is adopted [R5-Q4a, R5-Q4b].
4. **Interactive and headless.** Skills that serve a gate or a review lane run the same way in a session and in CI: inputs from arguments or files, never a question; results in files; an exit code for the gate.
5. **Short and front-loaded.** `SKILL.md` under 500 lines, references one level deep, the rules that must always hold at the top, because only the first 5,000 tokens of a skill survive context compaction ([research §1](../research/skill-authoring.md)).
6. **One naming pattern:** short, verb-first, kebab-case, used through the plugin namespace, e.g. `/<plugin>:check-gate` [R5-Q4d].
7. **Use Claude Code's mechanisms rather than override them** [R16-P].

## 12.2 Where they live

```
tools/claude-marketplace/                 the monorepo's marketplace [R24-Q1]
  .claude-plugin/marketplace.json         our plugin + pinned third-party entries
  plugins/<plugin>/
    .claude-plugin/plugin.json
    skills/<name>/                        Layer 1: portable skill folders
      SKILL.md
      references/  assets/  scripts/
    agents/                               Layer 2: reviewer subagents (skills: preloads)
    hooks/hooks.json                      Layer 2: hooks, if any
    evals/<case>/                         Layer 2: `claude plugin eval` cases
```

| Layer | Holds | Portable? | Decision |
|---|---|---|---|
| 1. Skill | `SKILL.md` with only `name`, `description` (≤ 1,024 characters) and optional `license`, `compatibility`, `metadata`; plain Markdown with relative paths; deterministic logic in `scripts/` | Yes | R5-Q4a |
| 2. Claude wiring | Reviewer subagents with `skills:`, hooks, evals, `plugin.json`. Claude-only frontmatter keys are allowed in `SKILL.md` when ignoring them elsewhere does no harm, and each spec lists them | No | R5-Q4a, R5-Q4b |
| 3. Adapters | Codex `agents/openai.yaml`, `.agents/skills`, a shared `AGENTS.md` | Built only when a second tool is adopted | R5-Q4a |

MCP servers used by reviewers are declared in the monorepo's `.mcp.json`, because plugin subagents ignore `mcpServers` [R4-Q7e].

## 12.3 Inventory

Specs are in [`../skills/`](../skills/), written from [`skill-spec.md`](../templates/skill-spec.md). **Full** specs fill all 19 sections; **outline** specs fill the header, problem, scope, invocation, composition and open questions, and are completed just before the skill is built [R25-Q4].

### P0: needed for the first PRD

| Skill | Serves | Does | Spec |
|---|---|---|---|
| `check-gate` | Every gate (CI and local) | Checks a status change against its gate; generates `coverage.md` and `docs/product/index.md` | [full](../skills/check-gate.md) |
| `write-use-case` | Use case → Complete | Writes a user-goal, fully dressed use case; checks the actor and system grid and an example per extension; renumbers safely | [full](../skills/write-use-case.md) |
| `write-stories` | Stories cut | Cuts value-based vertical stories, checks INVEST, writes Draft PRDs with `extensions:` and `touches:`, regenerates coverage | [full](../skills/write-stories.md) |
| `write-scenarios` | *Exploring* | A story's English Gherkin, grouped under `Rule:` blocks, starting from its extensions' examples [R27-Q1′, R28-A] | [full](../skills/write-scenarios.md) |
| `check-fit` | Exploring, slice start | Writes `fit.md` from the four keys: specs, API, behaviour, code | [full](../skills/check-fit.md) |
| `review-design` | Design-complete, DCRs | Runs the PM, UX and Eng persona reviewers in parallel, including the threat check | [full](../skills/review-design.md) |

### P1: needed for the first slice

| Skill | Serves | Does | Spec |
|---|---|---|---|
| `review-slice` | Slice, fix and enabler PRs | Runs the review lanes that apply | [outline](../skills/review-slice.md) |
| `review-code` | Code lane | Runs the code reviewers from `review-lanes.yaml` | [outline](../skills/review-code.md) |
| `review-security` | Security and privacy lane | Runs the security and privacy reviewers | [outline](../skills/review-security.md) |
| `review-ux` | UX lane, and before the design gate | Runs the UX reviewers | [outline](../skills/review-ux.md) |
| `review-privacy` | Security lane | GDPR, CNIL and tracker-consent review | [outline](../skills/review-privacy.md) |
| `review-llm-security` | Security lane, AI slices | Reviews against the OWASP Top 10 for LLM Applications | [outline](../skills/review-llm-security.md) |
| `check-copy` | UX lane | Voice guide and French typography | [outline](../skills/check-copy.md) |
| `check-state-matrix` | UX lane | Every screen × every state | [outline](../skills/check-state-matrix.md) |
| `check-flow-conformance` | UX lane | Rendered screens against `flows.md` and the copy deck | [outline](../skills/check-flow-conformance.md) |
| `check-bdd-conventions` | Code lane | pytest-bdd and Gherkin conventions | [outline](../skills/check-bdd-conventions.md) |
| `check-i18n-conventions` | Code lane | next-intl keys, catalogs and status sidecars | [outline](../skills/check-i18n-conventions.md) |
| `check-web-guidelines` | UX lane | Our pinned copy of the Vercel web and writing guidelines | [outline](../skills/check-web-guidelines.md) |
| `translate-copy` | *Exploring*, slices | Generates other locales from the copy deck, marked `needs-review` | [outline](../skills/translate-copy.md) |
| `sync-tokens` | Design-system enablers | DTCG and Style Dictionary build; a Figma variables diff turned into a PR | [outline](../skills/sync-tokens.md) |
| `check-setup` | Onboarding, any time | The collision "doctor": personal skills, agents and MCP servers that clash with the project's | [outline](../skills/check-setup.md) |

### P2

| Skill | Serves | Does | Spec |
|---|---|---|---|
| `refresh-guidelines` | Maintenance | Human-triggered, pull-only refresh of the pinned Vercel guidelines, with provenance | [outline](../skills/refresh-guidelines.md) |
| `review-outcome` | After Done | Helps fill in the outcome review on its due date | [outline](../skills/review-outcome.md) |

**Not a skill:** the worktree start scripts and per-worktree environments (`make design`, `make slice`, `make dcr`, `make enb`, `make env-up`, `make env-prune`) are an enabler slice ([chapter 5](05-worktrees-and-parallelism.md), [chapter 13](13-adoption.md)) [R25-Q2].

## 12.4 Build order

1. **`check-gate`'s scripts first**, with the `coverage.md` and `index.md` generators. They are plain scripts, run in CI without an agent, and every other step relies on them.
2. **`write-use-case`, `write-stories` and `write-scenarios`**, so the first use case, its stories and their scenarios can be written. `write-use-case` is built in this repo's lab, [`lab/write-use-case/`](../../lab/write-use-case/README.md), on sample use cases from other products, and the driver copies it into the marketplace once it passes its held-out cases [R31-Q6, R31-Q9].
3. **`check-fit` and `review-design`**, so the first PRD can reach Design-complete.
4. **P1 lanes** before the first slice PR: `review-code` and `review-security` first, `review-ux` with its reviewers next.
5. **P2** when the first outcome review is due, or the Vercel guidelines change.

Before step 4, run the checks in §12.6.

## 12.5 Testing and evaluation

[R5-Q4c]

| Layer | How |
|---|---|
| Static | `skills-ref validate` (open-standard conformance) and `claude plugin validate` on every change |
| Scripts | Unit tests, like any code |
| Triggering | About 20 labelled prompts per skill, half that should trigger and half near-misses that shouldn't |
| Output | Cases with fixtures and graders, run **with and without** the plugin by `claude plugin eval` |
| Authoring loop | Anthropic's `skill-creator`, then the cases are kept in `claude plugin eval` format in `evals/` |

CI runs the evals **only on PRs that change the plugin**, with a pinned model, a threshold of 0.8 and a cost cap per run. Eval and review runs are billed API calls and count against the €100 monthly budget, reviewed monthly [R5-Q4c, R15-Q3].

## 12.6 To verify in the monorepo before relying on it

These are documented gaps or unverified points from the research and the chapters. Each is a small check, done when the relevant skill is built:

| Check | Why it matters | Source |
|---|---|---|
| How a plugin subagent's `skills:` field names a plugin skill (`name` or `plugin:name`) | The review lanes preload skills this way | [Research](../research/skill-authoring.md), chapter 9 §9.5 |
| Whether `--bare` loads plugins given with `--plugin-dir` | Headless CI runs | [Research](../research/skill-authoring.md) |
| The `skills` value of a marketplace entry that wraps a bare skill folder | Third-party skill pinning | [R24-Q2] |
| Whether the Code Connect CLI can validate maps in CI | Chapter 6 §6.5 | [R17-Q2] |
| What `/design-sync` requires of `src/packages/ui` (a built `dist/`, or Storybook) | The Claude Design mirror | [Tooling research](../research/tooling-landscape.md), [R18-Q3] |
| How Codex and Gemini treat unknown frontmatter keys | Only if a second tool is adopted | [R5-Q4b] |
