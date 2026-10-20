# Skills landscape: Claude Code skills, plugins and agents for the product-development framework

Status: research notes, captured 2026-10-19. Companion to [`tooling-landscape.md`](tooling-landscape.md), which already covers mattpocock/skills, affaan-m/ECC, wshobson/agents and the Figma MCP/plugin. Those four are re-checked here against the skill-scout security criteria only.

Nothing was installed. Every fetched file was treated as untrusted data: it was read and pattern-scanned, and no script was executed. Install counts are the skills.sh **page** values (the search API returns different numbers). Stars come from the GitHub API on 2026-10-19. "(unverified)" marks a claim that could not be confirmed against a primary source.

## Shortlist

| Area | Recommend | Notes |
|---|---|---|
| Grilling, ADR, glossary, PRD → tickets, TDD, code review | **mattpocock/skills** (already installed): `grill-with-docs`, `domain-modeling`, `to-spec`, `to-tickets`, `tdd`, `code-review`, `implement-spec` | Re-check is clean. Skip `misc/git-guardrails-claude-code` (it writes `settings.json`, a strict G2 flag). `to-prd` and `ubiquitous-language` no longer exist at HEAD. |
| UI/UX design intelligence | **nextlevelbuilder/ui-ux-pro-max** (the `ui-ux-pro-max` skill folder only) | Offline, stdlib-only Python search over local CSVs. Do not install the whole plugin: its sibling `design` skill reads `~/.claude/.env` and calls 3 third-party image APIs. |
| UI generation baseline | **anthropics/skills `frontend-design`** | Apache-2.0, instruction-only, 1.0M installs. |
| shadcn/ui | **shadcn-ui/ui `shadcn`** (official) | Runs `` !`npx shadcn@latest info --json` `` when it loads (unpinned, Socket Warn). Acceptable for the vendor CLI, but note it. |
| Next.js App Router | **vercel/next.js `skills/`** (official, moved from vercel-labs/next-skills) | Cache Components, partial prefetching, bundle, dev loop. |
| FastAPI + Pydantic | **fastapi/fastapi `fastapi`** (official, MIT) | Instruction-only. |
| Storybook | **storybookjs/mcp Claude plugin** (official, MIT) | Thin skills that delegate to `storybook ai` (Storybook ≥ 10.5) and `@storybook/addon-mcp`. |
| Playwright | **microsoft/playwright-cli `playwright-cli`** + **currents-dev `playwright-best-practices`** | E2E BDD: **vitalets/playwright-bdd** (the library maintainer's own skill). |
| Accessibility | **addyosmani/web-quality-skills `accessibility`** (WCAG 2.2) | Alternatives: jakubkrehel `better-accessibility`, knowledge-work `accessibility-review`. |
| UX writing | **anthropics/knowledge-work-plugins `ux-copy`** + **content-designer `ux-writing`** | English only. French is a gap. |
| Motion | **emilkowalski `emil-design-eng`** | Skip `improve-animations` (zero-width chars, strict G2). |
| PR review, commits, feature flow | **claude-plugins-official `pr-review-toolkit`, `commit-commands`, `feature-dev`** (Anthropic) | No hooks. |
| i18n | **lingui/skills** or **i18next/i18next-cli `i18next-localization`** (both official) | Pick the one matching the library decision in tooling-landscape §12. next-intl has no usable skill. |

**Gaps (write our own):** Cockburn fully dressed use cases with extensions; edge-case / extension coverage analysis; PM, UX and engineering persona reviews (Every's `ce-doc-review` personas are a usable MIT reference); a user-story + Gherkin template under a commercial-friendly licence; pytest-bdd; DTCG / Style Dictionary token pipeline; next-intl; AI translation EN↔FR with glossary and ICU validation; French typography and UX writing; UI state coverage (empty/loading/error); privacy by design / GDPR at CNIL level; Docker Compose per worktree.

---

## 1. Method notes

### Framework applied

skill-scout (`../skill-scout`, read-only): `CLAUDE.md` and `framework/*.md` as of 2026-10-18/19.

| Parameter | Value used | Origin |
|---|---|---|
| Must harness | Claude Code | Team uses Claude Code + VS Code |
| Licence profile | `copyleft-ok` (default) | Not set by the user |
| Depth | `standard` (~50 gathered, ~15 inspected) | Default. In practice more were gathered (see counts below). |
| ClawHub | excluded (default) | — |
| Tessl MCP | not used | Tessl was read through public pages only |
| Credentials | none | No env keys were read and no `.env` was opened |

**Counts:** about 7,400 unique skill IDs returned by the per-item queries. 95 candidates had their skills.sh page read. 38 repos were downloaded or partially fetched for L3 inspection. 26 third-party audit detail pages were read.

### Sources queried (all on 2026-10-19)

**L1**
- **skills.sh public search API** (`/api/search?q=…&limit=100`): 120 queries, one or more per requirement item. Examples: `use cases cockburn`, `gherkin`, `pytest-bdd`, `dtcg`, `style dictionary`, `next-intl`, `icu`, `french`, `microcopy`, `docker compose`, `gdpr`, `git worktrees`, `conventional commits`. The API rate-limits at 30 requests/minute; failed queries were retried.
- **skills.sh skill pages** and per-scanner audit pages (`/<id>/security/<scanner>`), read for 95 candidates.
- **anthropics/skills**: git tree.
- **anthropics/claude-plugins-official** `.claude-plugin/marketplace.json`: 315 plugins, filtered by keyword.
- **officialskills.sh**: the vendor index page.
- **Tessl registry**: three public pages.

**L2 (90-day window)**
- Claude Code CHANGELOG (v2.1.303)
- Vercel changelog (skills.sh audits)
- Datadog Security Labs
- Zenity via CSO Online
- BeyondTrust
- OSV malicious-package entries
- Mondoo, as surfaced by search
- Web searches for incidents and for gap items

**L3**
- GitHub API metadata for 38 repos (unauthenticated, 60 requests/hour).
- codeload tarballs (commit SHA taken from the tarball header).
- `raw.githubusercontent.com` for the skill folders of large repos: fastapi/fastapi, formatjs/formatjs, github/awesome-copilot, vercel/next.js, EveryInc/compound-engineering-plugin.

### Deviations from skill-scout (read these before trusting the verdicts)

1. **No intake interview.** The requirement list in the task was used as-is. No priorities (must, should, nice) were confirmed, and no process-research expansion was done, so there are no derived steps and no per-cell practices.
2. **No numeric Fit, Rank or tier.** Without confirmed cells and practices, Cell Fit can't be computed. The verdicts map loosely to skill-scout tiers:
   - **recommend** ≈ likely Trial or better: gates passed, security ≥ 85, credible provenance.
   - **consider** ≈ Assess: gates passed, but with low uplift, a single maintainer, staleness or partial coverage.
   - **reject** ≈ Avoid: a gate failed or the risk is High.
3. **L3 review was orchestrator-run, not done by reviewer subagents.** The review was:
   - an automated scan of every file in each downloaded repo against the red-flag patterns in `security-checklist.md`, plus two patterns from L2 (Claude `!` dynamic-context lines and frontmatter `hooks:`);
   - a byte-level scan for zero-width, bidi, variation-selector and tag characters;
   - a manual read of every hit, plus every hook manifest and every hook or script that ships in a recommended install unit.

   Not every file was read line by line. Coverage is **partial** for the large repos (ECC: 4,621 files; impeccable: 4,071; shadcn-ui/ui; claude-plugins-official), and their verdicts say so.
4. **Content hashes** are a 16-hex-character SHA-256 over the relative paths and bytes of the skill folder (§6). They do not match skill-scout's cache key format. Nothing was written to `~/.cache/skill-scout/`.
5. **Not queried:** Smithery, SkillsMP, awesome-copilot `llms.txt`, claude-plugins.dev, claude.ai/directory, Simon Willison, AINews, HN. Reason: time and API budget.
6. **officialskills.sh** was queried once, for its whole page, not once per stack product.
7. **Gates were applied strictly as written.** Several strict outcomes look harsh for first-party or consented behaviour. They are listed in §7 as proposed framework tuning, and they were not relaxed here.

---

## 2. Candidate table

**Columns**
- **Inst./★**: skills.sh page installs / GitHub stars.
- **Audits**: skills.sh third-party scanners in the order Gen Agent Trust Hub / Socket / Snyk (P = Pass, W = Warn, F = Fail).
- **Sec**: our graded G2 score (100 minus deductions), or the gate that failed.
- All repos were live and not archived on 2026-10-19, so G4 passed everywhere unless the table notes a deprecation.

### Design phase

| Skill / plugin | Repo @ commit | Covers | Inst. / ★ | Licence | Security signals and audit results | Verdict |
|---|---|---|---|---|---|---|
| `grill-with-docs`, `grill-me`, `grilling` | mattpocock/skills @49dd158 | Grilling and requirements interviews; writes ADRs and a glossary | 1.2M, 1.4M / 297k | MIT | P/P/P. Instruction-only. The official marketplace pins the same SHA (49dd158). Sec 100. | **recommend** (installed) |
| `domain-modeling` | mattpocock/skills | Glossary, domain model, ADR | 848K | MIT | P/P/P. Sec 100. | **recommend** |
| `to-spec`, `to-tickets`, `implement-spec` | mattpocock/skills | PRD/spec → tickets → parallel worktree implementation | 690K, 685K | MIT | `to-tickets` Snyk W011 (reads issue bodies, an indirect-injection surface): explained, no deduction. `to-prd` is listed on skills.sh (352K) but **absent at HEAD**; this confirms the rename to `to-spec`. Sec 100. | **recommend** |
| `misc/git-guardrails-claude-code` | mattpocock/skills | Git safety hooks | — | MIT | Writes hooks into `.claude/settings.json` or `~/.claude/settings.json` after asking the user (`SKILL.md:24,41,61`). This is the *persistence/tampering: harness settings* flag, always confirmed. | **reject** (strict G2; see §7) |
| `write-spec` | anthropics/knowledge-work-plugins @33eeda1 (product-management) | PRD, goals/non-goals, success metrics, acceptance criteria | 3.5K / 30k | Apache-2.0 | P/P/W (Snyk W011, optional tracker reads): explained. Skill folder is instruction-only. The plugin bundles remote MCP connectors. Sec 100 (folder). | **consider**: Cowork-oriented, overlaps `to-spec` |
| `spec-driven-development`, `interview-me`, `documentation-and-adrs` | addyosmani/agent-skills @aeac41d | Spec, requirements interview, ADR | 60K, 52K, 59K / 108k | MIT | P/P/P. The repo's `hooks/sdd-cache-*.sh` use `curl -I` but are not wired (there is no `hooks/hooks.json`). Sec 100. | **consider**: second opinion to mattpocock |
| `architecture-decision-records` | affaan-m/ECC @76aaa77 | ADR | 4.4K / 284k | MIT | P/P/P. Instruction-only folder. Sec 100. | **consider** (cherry-pick the folder) |
| `user-story`, `prd-development` | deanpeters/Product-Manager-Skills @cfcb697 | User stories (Cohn format + Gherkin AC), PRD | 4.0K, 4.6K / 7.5k | **CC BY-NC-SA 4.0** | P/P/P. Frontmatter uses many non-spec keys (`intent`, `type`, `theme`, `best_for`, …). | **consider as reference only**: NonCommercial terms clash with a commercial B2B startup (G3: flagged) |
| `use-case-writer` | phucnt-bazone-vietnam/use-case-writer @695cd6c | Use cases (Wiegers/IIBA 13-field template; cites Cockburn's coffee-break test; normal, alternative and exception courses) | 7 / 150 | MIT (LICENSE file; GitHub shows NOASSERTION) | P/P/W. Snyk W021 "hidden Unicode" traced to U+FE0F emoji variation selectors: explained. Single author, no push since 2026-05-16. Sec 100. | **consider as a seed** for our own Cockburn skill. Not Cockburn "fully dressed". |
| `usecases` (Pi package `usecases-skill` 0.2.0) | gitverse.ru/ars/usecases-skill | Cockburn-style use cases (summary, user-goal and subfunction levels; PlantUML) | — | MIT (per pi.dev) | Not inspected: found by L2 only, hosted outside GitHub, published 2026-10-15 (under a month old). | **not evaluated** (open point) |
| `gherkin-authoring` | intent-driven-dev/skills @15aa678 | BDD/Gherkin authoring and review | 45 / 10 | MIT | P/P/W (Snyk W011 on user-supplied text: generic, explained). 95-line, instruction-only skill, created 2026-07. | **consider**: solid but tiny and young |
| `gherkin-from-stories`, `behave-testing` (Tessl tiles) | testland/qa | Stories → Gherkin; behave | — / 11 | MIT | Tessl quality 70%, Snyk "Low". 340-skill repo created 2026-05. Not inspected at L3. | **not evaluated** |
| `ce-doc-review` | EveryInc/compound-engineering-plugin | PM/UX/engineering **persona reviews** of specs: product-lens, design-lens, feasibility, security-lens, scope-guardian, adversarial | 3.6K / 25.6k | MIT | Ships a 2,465-line `peer-job-runner.py` and a 1,213-line `cross-model-doc-review.sh`. When a lens activates, the shell script sends the document to *other* model providers (Codex, Grok, Gemini) via `npx -y acpx@$VERSION`, and writes a temp `settings.json` (`cross-model-doc-review.sh:228,321`). Our score: about 50, so risk High. | **consider as reference only**: borrow the persona briefs (`references/personas/*.md`), don't install |
| `design-critique` | anthropics/knowledge-work-plugins (design) | UX persona review | — | Apache-2.0 | Instruction-only folder. | **consider** |

### UI/UX

| Skill / plugin | Repo @ commit | Covers | Inst. / ★ | Licence | Security signals and audit results | Verdict |
|---|---|---|---|---|---|---|
| `ui-ux-pro-max` (skill folder) | nextlevelbuilder/ui-ux-pro-max-skill @56ea9cf (v2.15.0) | Design systems, palettes, typography, UX rules, accessibility checks, shadcn/Tailwind/Next.js stack guidelines | 404K / 137k | MIT | P/P/P. Tessl: quality 87%, impact 1.86× vs baseline, Snyk pass (same commit). Scripts are stdlib-only (csv, re, json…), make no network calls, and with `--persist` write `design-system/` into the project only (`design_system.py:1053`). Three scripts exceed 500 lines (`design_system.py` 1,668; `validate_data.py` 1,095; `core.py` 993): −10. **Sec 90.** | **recommend** (folder only) |
| `ui-ux-pro-max` (whole plugin) | same | + `design`, `brand`, `banner-design`, `slides`, `ui-styling`, `design-system` | — | MIT | The `design` skill's `logo/`, `icon/` and `cip/generate.py` load keys from `~/.claude/skills/.env` and `~/.claude/.env` and call `api.atlascloud.ai`, `api.muapi.ai` and Gemini. This is documented, so not a red flag, but it touches credentials and makes 3 third-party network calls. A 2026-07 Skillselion page reported "HIGH, 2 of 3 scanners" (secondary). The current skills.sh page shows 3 passes. | **consider** (only if logo/banner generation is wanted) |
| `frontend-design` | anthropics/skills @dbd4588 | Distinctive production UI | 1.0M / 182k | Apache-2.0 (`LICENSE.txt`) | P/P/P. Instruction-only. Sec 100. Also shipped as the official `frontend-design` plugin. | **recommend** |
| `impeccable` | pbakaus/impeccable @0665bd8 (v4.6.0) | UI audit/critique/polish/harden, UI states, UX copy, motion | 344K / 83k | Apache-2.0 | P/W/P. The `scripts/impeccable` launcher **downloads a platform binary from GitHub releases at runtime and execs it** (checks a SHA-256 sidecar from the same origin). This is remote fetch-and-run as a prerequisite, so the contextual exemption doesn't apply. `/impeccable hooks on` writes hooks into `.claude/settings.local.json` or `~/.claude/settings.json` (`reference/hooks.md`). `live-browser.js` is 550 KB. Ships a vendored minified `modern-screenshot.umd.js`. | **reject** (G2: confirmed fetch-and-run + settings writes) |
| `shadcn` | shadcn-ui/ui @ba1503c | shadcn/ui components, registry, presets, theming | 115K / 126k | MIT | P/W/P. Socket: "load-time pre-execution, mutable @latest". `SKILL.md:17` is `` !`npx shadcn@latest info --json` ``, which runs before the model reads the skill (the Datadog "dynamic context" pattern). `allowed-tools` is scoped to `npx/pnpm dlx/bunx shadcn@latest *`. Unpinned: −10. **Sec 90.** Risk Medium (judgement). | **recommend** (vendor CLI; pin the version in `components.json` workflows) |
| `tailwind-design-system` | wshobson/agents @0874a27 (frontend-mobile-development) | Tailwind v4 (`@theme`, oklch), tokens | 69K / 41k | MIT | P/P/P. Instruction-only. Sec 100. | **consider** |
| `nextjs-app-router-patterns` | wshobson/agents | Next.js App Router | 32K | MIT | P/P/P. References "Next.js 14" and nothing newer: likely stale. | **consider** (prefer the official Next.js skills) |
| `next-*` skills (`next-cache-components-*`, `next-partial-prefetching-*`, `next-bundle-optimizer`, `next-dev-loop`) | vercel/next.js `canary/skills` | Next.js App Router, caching, runtime verification | not on skills.sh | MIT (Next.js repo) | `vercel-labs/next-skills` README: "have moved … to the Next.js repository … version-matched". Suggests `npx @next/codemod@latest`: −10. **Sec 90.** No third-party audits. | **recommend** |
| `vercel-react-best-practices`, `vercel-composition-patterns` | vercel-labs/agent-skills @063bee9 | React | 817K, 404K / 33k | MIT (frontmatter); no repo LICENSE | P/P/P. | **consider** |
| `web-design-guidelines`, `writing-guidelines` | vercel-labs/agent-skills | UI review, writing | 756K, 99K | **none found** (no frontmatter licence, no repo LICENSE) | Both fetch their rules at runtime from an unpinned `raw.githubusercontent.com/.../main/command.md` and follow the "output format instructions" in it. Snyk W012 on `writing-guidelines`: "runtime URL that controls agent" (high). | **reject** (G3 no licence; runtime remote instructions) |
| Figma skills (`figma-use`, `implement-design`, …) + plugin | figma/mcp-server-guide @bdd857f (plugin 2.2.157) | Figma design → code, Code Connect, write-to-canvas | 8.7K, 5.9K / 2.1k | **none found** (no LICENSE at any level; GitHub shows none; marketplace entry has no licence) | P/P/P on `figma-use`. W/W on `implement-design` (W011 high: ingests arbitrary Figma files). ZWJ inside emoji in the bundled `.d.ts`: not a flag. Remote MCP `mcp.figma.com`. | **reject as a skill** (G3). Use the Figma remote MCP server directly as an adjacent tool (see tooling-landscape §2). |
| Storybook plugin (`stories`, `storybook-init`, `storybook-setup`, `storybook-upgrade`) | storybookjs/mcp @4589b69, `packages/claude-plugin` | Storybook stories, preview, UI states via `storybook ai` | not on skills.sh / repo ★ n/a | MIT | No hooks, no MCP config, instruction-only. `npm create storybook@latest`, `npx storybook add @storybook/addon-mcp` unpinned: −10. **Sec 90.** `plugin.json` version 0.0.0 (no version marker), so risk Medium. The `stories` description says "Invoke FIRST … no exceptions", an aggressive trigger. | **recommend** (official; requires Storybook ≥ 10.5) |
| `accessibility` | addyosmani/web-quality-skills @afa8da9 | WCAG 2.2 | 62K / 3.0k | MIT | P/P/P. Sec 100. | **recommend** |
| `better-accessibility`, `better-writing` | jakubkrehel/skills @4c66b1f | Accessibility, writing | 28K, 27K / 8.0k | MIT | P/P/P. Sec 100. Repo created 2026-07. | **consider** |
| `accessibility-review` | anthropics/knowledge-work-plugins (design) | WCAG review | 4.0K | Apache-2.0 | P/P/W (W011): explained. | **consider** |
| `wcag-audit-patterns`, `interaction-design` | wshobson/agents (ui-design) | WCAG; micro-interactions and loading/skeleton states | 12K, 16K | MIT | P/P/P. Sec 100. | **consider** |
| `ux-copy` | anthropics/knowledge-work-plugins (design) | Microcopy, errors, empty states, CTAs | 4.5K | Apache-2.0 | P/P/P. 107 lines. Sec 100. | **recommend** |
| `ux-writing` | content-designer/ux-writing-skill @98cacde | UX writing, voice chart, error templates | 2.6K / 241 | MIT | P/P/P. 417 lines plus references and templates. Single maintainer, so risk Medium. Sec 100. | **recommend** |
| `emil-design-eng`, `review-animations` | emilkowalski/skills @2d22863 | Motion and micro-interactions | 366K, 237K / 47k | MIT | P/P/P. Clean. **But** `improve-animations/PLAN-TEMPLATE.md:19,22,29,35` contain U+200B before code fences (a fence-escape trick). Under the strict *hidden content* rule, that folder fails. | **recommend** `emil-design-eng`, `review-animations`. **Reject** `improve-animations` (strict). |
| `microinteractions`, `ux-heuristics` | wondelai/skills @c172996 | Micro-interactions, heuristics | 6.5K, 8.8K / 2.5k | MIT | P/P/P. Scan hits are documentation only. Not read in depth. | **consider** |
| `loading-states`, `design-token`, `localization-design` | Owl-Listener/designer-skills @9a6930c | UI states, tokens, localisation design | 2.1K, 2.1K, 1.6K / 3.0k | MIT | P/P/P. Very thin (`loading-states` is 36 lines, `design-token` 27), so uplift is about 0. | **reject** (low uplift) |
| `design-tokens`, `token-build` (DTCG, Style Dictionary) | plugin87/ux-ui-agent-skills; ilikescience/design-tokens-skill; yonatangross/orchestkit | DTCG tokens, Style Dictionary build | 466, 411, 174, 200 | various | Not inspected (installs below 500, outside the depth cut). | **not evaluated**: gap candidates |

### i18n

| Skill / plugin | Repo @ commit | Covers | Inst. / ★ | Licence | Security signals and audit results | Verdict |
|---|---|---|---|---|---|---|
| `lingui-best-practices` (+5 sibling skills) | lingui/skills @2be6e69 | Lingui, ICU, extraction, i18next → Lingui migration | 742 / 9 | MIT | P/P/P. Official vendor org. Its 20 scripts are eval fixtures. Sec 100. | **recommend if Lingui is chosen** |
| `i18next-localization` | i18next/i18next-cli @933364e | i18next setup, extraction, ICU/MF2, AI translation via Locize (optional) | 84 / 244 | MIT | P/P/W. Snyk W012 points at a community Svelte plugin, not relevant here: explained. `allowed-tools: Bash(npx i18next-cli *)` is unpinned: −10. Mild R1: Locize upsell, but explicitly optional ("ask the developer one question"). **Sec 90.** | **recommend if i18next is chosen** |
| `localization-review` | formatjs/formatjs (`.agents/skills/`) | ICU syntax, placeholders, glossary, locale formatting review (read-only) | 319 / 14.7k | **none found at repo or skill level** | P/P/P. 368 lines, high quality. | **reject on G3 as written**. Open point: npm packages are MIT; ask upstream to add a LICENSE. |
| `next-intl-add-language` | github/awesome-copilot | next-intl | 9.3K / 40k | MIT | P/P/P. 19 lines with hard-coded paths (`src/middleware.ts`). Uplift about 0. | **reject** |
| `i18n-sync` | affaan-m/ECC | JSON locale sync | 777 | MIT | P/P/P. | **consider as a reference** |
| `humaniseur-fr` | samber/cc-skills @123cb15 | French writing: 38 AI-pattern fixes, register, partial typography (Pattern 20: guillemets with non-breaking spaces; keeps U+00A0/U+202F) | 3.9K / 232 | MIT | P/P/P. `allowed-tools` has no Bash. Single maintainer, so risk Medium. Sec 100. | **consider**: partial for French UX writing and typography |

### Development

| Skill / plugin | Repo @ commit | Covers | Inst. / ★ | Licence | Security signals and audit results | Verdict |
|---|---|---|---|---|---|---|
| `tdd` | mattpocock/skills | TDD | 1.1M | MIT | P/P/P. Sec 100. | **recommend** (installed) |
| `code-review` | mattpocock/skills | Code review (standards + spec) | 761K | MIT | P/P/W (W011): explained. | **recommend** (installed) |
| `test-driven-development`, `using-git-worktrees`, `dispatching-parallel-agents` | obra/superpowers @bb92a77 | TDD, worktrees, parallel agents | 254K, 213K, 214K / 302k | MIT | Folders P/P/P and clean. The **plugin** has a `SessionStart` hook (`hooks/session-start`) that injects the whole `using-superpowers` skill wrapped in `<EXTREMELY_IMPORTANT>` into every session. Mondoo flags that skill for "manipulative framing" (third-party, severity not stated). `brainstorming` Socket W: `scripts/server.cjs` shell exec via env var. | **consider** the folders. Don't install the plugin alongside mattpocock (competing process). |
| `pr-review-toolkit`, `code-review`, `feature-dev`, `commit-commands`, `code-simplifier` | anthropics/claude-plugins-official @ea10b21 (internal) | PR review agents, feature workflow, commit/push/PR | — / 43k | Apache-2.0 (per-plugin LICENSE) | No hooks. `commit-commands` uses local `` !`git status` `` / `` !`git diff HEAD` `` dynamic context (no network). Sec 100. | **recommend** |
| `security-guidance` | claude-plugins-official (2.0.14) | Security review on edit/commit/stop | — | Apache-2.0 | `SessionStart` hook runs `ensure_agent_sdk.py`, which `pip install`s **unpinned** `claude-agent-sdk` into `~/.claude/security/agent-sdk-venv` (`ensure_agent_sdk.py:6,436`). `Stop` and commit hooks call `api.anthropic.com`. Strictly this is *hooks that run network calls without the user acting*, which is confirmed. It is documented and has a kill switch (`SECURITY_GUIDANCE_DISABLE=1`). | **reject under strict G2** (see §7). Otherwise a strong first-party option. |
| `claude-security` | claude-plugins-official (0.12.0) | Deep vulnerability scan of your code | — | Apache-2.0 | Hooks: banner, local metrics, push/PR tips. The `PermissionRequest` hook only **denies** an unanswered prompt after 60 s (`hooks.py:303-310`). Scripts partly read. | **consider** |
| `security-review` | getsentry/skills @f57ada2 | OWASP-style code security review (Python/JS) | 20K / 1.1k | Apache-2.0 | **F/F/P.** Gen: "CRITICAL – INDIRECT_PROMPT_INJECTION" (ingests the code under review). Socket: "Malware HIGH" on `references/supply-chain.md`. Our review: the triggers are attack *examples* in a reference file, e.g. `supply-chain.md:244` (reverse shell) and `:258` (`curl … \| bash` labelled `// DANGEROUS`). This is a **contextual** flag: risk High until the user signs off. | **consider after sign-off** |
| `commit` | getsentry/skills | Conventional commits | 4.7K | Apache-2.0 | P/P/P. | **consider** |
| `conventional-git` | samber/cc-skills | Conventional commits, commitlint | 3.8K | MIT | P/P/P. | **consider** |
| `conventional-commit` | github/awesome-copilot | Conventional commits | 17K | MIT | Gen W: "PROMPT_INJECTION … 'no confirmation needed' in Step 5". Explained: it tells the agent to commit without confirming. | **reject** (behaviour conflicts with review-before-commit) |
| `fastapi` | fastapi/fastapi (`fastapi/.agents/skills/fastapi`) | FastAPI, Pydantic, `Annotated` deps, SSE | 12.9K / 103k | MIT | P/P/P. 7 instruction files. Sec 100. | **recommend** |
| `fastapi-patterns` | affaan-m/ECC | FastAPI (`Annotated`, lifespan) | 4.5K | MIT | P/P/P. 514 lines. | **consider** |
| `python-development` plugin (`fastapi-pro`, `python-testing-patterns`, …) | wshobson/agents | FastAPI, pytest | 36K (testing) | MIT | P/P/P. No hooks. No pytest-bdd content. | **consider** |
| `hexagonal-architecture` | affaan-m/ECC | Ports and adapters | 4.4K | MIT | P/P/W. Snyk W009 "money access" from a Stripe example adapter: false positive, explained. TypeScript examples, no Python. Sec 100. | **consider** (cherry-pick the folder; adapt for Python) |
| `architecture-patterns` | wshobson/agents | Clean/hexagonal/DDD | 24K | MIT | P/P/P. | **consider** |
| `playwright-cli` | microsoft/playwright-cli @b85c7a7 | Playwright browser automation | 190K / 14k | Apache-2.0 | P/W/W. Socket: example credentials in `references/running-code.md`. Snyk W011: browsing. Both explained. | **recommend** |
| `playwright-best-practices` | currents-dev/playwright-best-practices-skill @283d5cb | Playwright test practice | 96K / 402 | MIT | P/P/P. Sec 100. Org-maintained (Currents). | **recommend** |
| `playwright-bdd` | vitalets/playwright-bdd @2084276 | Gherkin-first E2E with Playwright (TS) | 341 / 808 | MIT | P/P/P. Instruction-only. Written by the library's author. Sec 100. | **recommend** (for Playwright BDD) |
| `webapp-testing` | anthropics/skills | Playwright (Python) local testing | 182K | Apache-2.0 | P/W/W. `with_server.py` uses `shell=True` on CLI args: explained. | **consider** |
| `supabase-postgres-best-practices` | supabase/agent-skills @c9be0e9 | Postgres indexes, RLS, EXPLAIN | 451K / 2.9k | MIT | P/P/P. Supabase-centric, so a **transfer** to plain PostgreSQL (Coverage ≤ 50). | **consider** |
| `postgresql-table-design` | wshobson/agents | PostgreSQL schema | 28K | MIT | P/P/P. | **consider** |
| `docker-patterns` | affaan-m/ECC | Docker, Compose | 5.8K | MIT | P/P/P. No per-worktree Compose content. | **consider** |
| `k8s-manifest-generator`, `helm-chart-scaffolding`, `k8s-security-policies` | wshobson/agents | Kubernetes | 11K, 12K, 15K | MIT | P/P/P. | **consider** |
| `gdpr-compliant` | github/awesome-copilot | GDPR engineering (DPIA, retention, CNIL references) | 1.6K | MIT | P/P/P. 283 lines. Sec 100. | **consider**: partial |
| `gdpr-data-handling` | wshobson/agents | GDPR data handling | 15K | MIT | P/W/P. Socket: DSAR examples lack authz: explained. 73 lines, thin. | **consider** (weak) |
| `static-analysis` etc. | trailofbits/skills @5c99c03 | Security tooling | — / 7.6k | **CC-BY-SA-4.0** | Not inspected in depth. | **not evaluated** (copyleft, flagged) |
| ECC plugin (full install) | affaan-m/ECC v2.2.3 | Everything | — | MIT | `hooks/hooks.json` (auto-loaded) registers **27 hooks** on PreToolUse/PostToolUse/Stop/SessionStart/SessionEnd. Each runs an inline `node -e` bootstrap that scans `~/.claude/plugins/cache`. `mcp-health-check.js` makes HTTPS calls. Several hooks write under `~/.claude`. Permission decisions found are deny-only (`hookify-runtime.js:611,725`; `gateguard-fact-force.js:2088`). Review incomplete (4,621 files). | **reject the full plugin** (risk High: hook surface, unreviewed). Cherry-picked instruction-only folders are fine. |
| wshobson plugins (`python-development`, `frontend-mobile-development`, `ui-design`, `documentation-generation`, `agent-teams`) | wshobson/agents | Stack agents and skills | — | MIT | These plugins ship no hooks (hooks exist only in the unrelated `protect-mcp` and `review-agent-governance`). Instruction-only skills. | **consider** (as in tooling-landscape) |

---

## 3. Coverage matrix

The "best candidate" is the strongest one that passes every gate. "Partial" means it covers part of the item. "Gap" means nothing adequate passed the gates.

| Requirement item | Best candidate | Status |
|---|---|---|
| Use case elicitation (Cockburn fully dressed, extensions) | phucnt `use-case-writer` (Wiegers/IIBA template, alternative/exception courses) | **gap: write our own**. Use it as a seed. The Pi `usecases-skill` is unevaluated. |
| User stories | knowledge-work `write-spec` / mattpocock `to-tickets` | **partial**. deanpeters `user-story` fits best but is CC BY-NC-SA, so reference only. |
| PRD writing | mattpocock `to-spec` (alternative: knowledge-work `write-spec`) | covered |
| BDD / Gherkin acceptance criteria | intent-driven-dev `gherkin-authoring`; vitalets `playwright-bdd` for executable E2E | **partial** (young, tiny skill) |
| Edge-case / extension coverage analysis | — | **gap: write our own** |
| PM / UX / engineering persona reviews | Every `ce-doc-review` persona briefs (reference only); knowledge-work `design-critique` | **gap: write our own** (borrow the MIT persona briefs) |
| Grilling / requirements interviews | mattpocock `grill-with-docs` | covered (installed) |
| ADR writing | mattpocock `grill-with-docs` / `domain-modeling` | covered |
| Glossary / domain modelling | mattpocock `domain-modeling` | covered |
| Design systems | `ui-ux-pro-max` (folder) + `frontend-design` | covered |
| Design tokens (DTCG, Style Dictionary) | — (ui-ux-pro-max `design-system` uses `$value` tokens, one DTCG mention) | **gap: write our own** (low-install DTCG skills unevaluated) |
| shadcn/ui | shadcn `shadcn` (official) | covered (note the `@latest` load-time exec) |
| Tailwind v4 | wshobson `tailwind-design-system` | partial / consider |
| Next.js App Router | vercel/next.js `skills/` (official) | covered |
| React | vercel-labs `vercel-react-best-practices` | consider |
| Figma | Figma remote MCP server (adjacent, not a skill) | **skills fail G3 (no licence)** |
| Storybook | storybookjs/mcp Claude plugin (official) | covered (needs Storybook ≥ 10.5) |
| Accessibility (WCAG) | addyosmani `accessibility` (WCAG 2.2) | covered |
| UX writing / voice and tone / microcopy | knowledge-work `ux-copy` + content-designer `ux-writing` | covered (English) |
| Micro-interactions / motion | emilkowalski `emil-design-eng` | covered |
| UI state coverage (empty/loading/error) | wshobson `interaction-design`, knowledge-work `ux-copy` (empty states) | **partial**. impeccable `harden`/`onboard` cover it but fail G2. Write our own checklist. |
| i18n: next-intl / i18next / ICU | lingui/skills or i18next `i18next-localization` (official); formatjs `localization-review` would be best for ICU review but has no licence | **next-intl: gap**. Lingui/i18next covered. ICU review: G3-blocked. |
| AI translation EN↔FR (then other Latin languages) | i18next-localization (Locize-backed AI translation, optional) | **gap: write our own** (glossary, `description` context, ICU/placeholder validation in CI) |
| French typography / UX writing | samber `humaniseur-fr` (partial typography) | **gap: write our own** |
| TDD | mattpocock `tdd` | covered |
| pytest | wshobson `python-testing-patterns` | consider |
| pytest-bdd | — (the search returned only tiny unrelated hits) | **gap: write our own** |
| Playwright | microsoft `playwright-cli` + currents `playwright-best-practices` | covered |
| Hexagonal / ports and adapters | ECC `hexagonal-architecture` (TS examples) | partial: adapt for Python |
| FastAPI + Pydantic | fastapi/fastapi `fastapi` (official) | covered |
| PostgreSQL | wshobson `postgresql-table-design`; supabase (transfer) | consider |
| Docker Compose | ECC `docker-patterns` | **partial**. Per-worktree Compose is a gap (see tooling-landscape §13). |
| Kubernetes | wshobson `k8s-manifest-generator` / `helm-chart-scaffolding` | consider |
| Security review | official `pr-review-toolkit` + built-in `/security-review`; getsentry `security-review` after sign-off; `claude-security` | partial (`security-guidance` fails strict G2) |
| Privacy by design / GDPR | awesome-copilot `gdpr-compliant` | **gap at CNIL/DPIA depth: write our own** |
| Code review | mattpocock `code-review` + official `pr-review-toolkit` | covered |
| Git worktrees + parallel agents | Claude Code native worktrees + mattpocock `implement-spec`; superpowers `using-git-worktrees` as reference | covered |
| Conventional commits | official `commit-commands`; samber `conventional-git` or getsentry `commit` | covered |

---

## 4. Vetoes and gate failures found

### L2: ecosystem incidents and deprecations (90-day window)

**Incidents**
- **Trojanized skills on skills.sh (Zenity).** The campaign began 2026-07-11, was reported 2026-08-07, and passed 1.7M combined installs. The fake orgs were `getpaperclipai` and `browser-use-headless`, and one skill was named `paperclip-board`. Clean copies were later updated with a malicious `setup-installation.md` that installed a credential stealer from a GitHub release ([CSO Online](https://csoonline.com/article/4206851/trojanized-ai-skills-gain-1-7m-installs-in-agent-targeted-attack.html)). None of our candidates is involved. Lesson: pin to a commit SHA, and re-review on every update.
- **Datadog Security Labs (2026-05-11).** `!` dynamic-context commands run before the model sees the skill. A cloned repo can bring skills in without any marketplace install. Mitigation: `"disableSkillShellExecution": true` ([Datadog](https://securitylabs.datadoghq.com/articles/malicious-skills-supply-chain-risks-in-coding-agents-with-dynamic-context/)). This applies to shadcn `shadcn`, to the official `commit-commands` and `claude-security`, and to every skill using `` !`…` ``.
- **BeyondTrust.** Hooks declared in skill frontmatter run as unsandboxed processes. They demonstrated a reverse shell via a PostToolUse hook ([BeyondTrust](https://www.beyondtrust.com/blog/entry/claude-code-hooks-c2-skill-security)). No candidate in this report declares `hooks:` in its SKILL.md frontmatter (scan result).
- **GitHub account-rename repo-jacking** ([CraftedSignal brief](https://feed.craftedsignal.io/briefs/2026-03-agent-skill-hijacking/)) and the **OWASP Agentic Skills Top 10, AST02** ([OWASP](https://owasp.org/www-project-agentic-skills-top-10/ast02)). Both support SHA-pinned installs.
- **skills.sh audits** (Gen, Socket, Snyk) since 2026-02-17. Malicious skills are hidden from search, and the CLI shows audits from `skills@1.4.0` ([Vercel](https://vercel.com/changelog/automated-security-audits-now-available-for-skills-sh)).

**Deprecations (G4)**
- `vercel-labs/next-skills` → successor **vercel/next.js `skills/`**.
- `openai/skills` (`figma-implement-design`, `security-threat-model`) → successor openai/plugins (per `sources.md`).
- mattpocock `to-prd` and `ubiquitous-language` are removed at HEAD but still listed on skills.sh.

### G2: security (strict application)

| Candidate | Flag | Evidence |
|---|---|---|
| pbakaus/impeccable | Remote fetch-and-run (a prerequisite, so not contextual); persistence (harness settings) | `.claude/skills/impeccable/scripts/impeccable` downloads `https://github.com/pbakaus/impeccable/releases/download/engine-v$version/...` and `exec`s it; `reference/hooks.md` writes into `.claude/settings.local.json` / `~/.claude/settings.json` |
| claude-plugins-official `security-guidance` | Hook that runs network calls without the user acting | `hooks/hooks.json` SessionStart → `ensure_agent_sdk.py` (unpinned `pip install claude-agent-sdk`, `:436`); Stop/commit hooks → `llm.py` urllib calls to `api.anthropic.com` |
| mattpocock `git-guardrails-claude-code` | Persistence (harness settings) | `SKILL.md:24,41,61` |
| emilkowalski `improve-animations` | Hidden content (U+200B) | `PLAN-TEMPLATE.md:19,22,29,35` |

**Contextual flag, awaiting sign-off:** getsentry `security-review`. Scanner verdicts are Gen CRITICAL and Socket "Malware HIGH". Both are refuted by `references/supply-chain.md:244,258`, which are attack examples.

### G3: licence

| Candidate | Result |
|---|---|
| figma/mcp-server-guide (all skills and the plugin) | No licence at any level → fail |
| vercel-labs `web-design-guidelines`, `writing-guidelines` | No licence → fail |
| formatjs `localization-review` | No licence found at skill or repo root → fail (open point) |
| deanpeters/Product-Manager-Skills | CC BY-NC-SA 4.0 → passes `copyleft-ok` flagged, but NonCommercial |
| trailofbits/skills | CC-BY-SA-4.0 → passes, flagged |

### Explained scanner warnings (no deduction)

- Snyk W011 "third-party content exposure" on mattpocock `code-review`/`to-tickets`, knowledge-work `write-spec`/`code-review`/`accessibility-review`, `doc-coauthoring`, `webapp-testing`, `playwright-cli`, `gherkin-authoring`.
- Snyk W009 on ECC `hexagonal-architecture` (Stripe example).
- Snyk W021 on `use-case-writer` (U+FE0F).
- Socket anomalies on `web-artifacts-builder` (`init-artifact.sh` untar), `webapp-testing` (`shell=True`), `playwright-cli` (example credentials), shadcn (`@latest` load-time exec), `gdpr-data-handling` (example code).

---

## 5. Open and unverified points

- **Licences.**
  - Figma's skills repo and formatjs's `localization-review` may carry licence terms we couldn't find, for example in the npm package or in Figma's developer terms. Ask upstream before treating the G3 failures as final.
  - Whether deanpeters's NonCommercial clause covers internal use of a skill at a commercial company is a legal question. It was not resolved here.
- **Strict-rule outcomes** (security-guidance, mattpocock git-guardrails, impeccable's hook installer, emilkowalski U+200B) depend on framework wording. They are proposed for tuning in §7, and need the user's decision.
- **getsentry `security-review`** needs a recorded user sign-off on the contextual scanner flag before it can be tiered.
- **Not inspected:**
  - the DTCG/Style Dictionary skills (plugin87, ilikescience, orchestkit, glebis);
  - testland/qa (340 skills, including `gherkin-from-stories` and `i18n-string-coverage`);
  - the Pi `usecases-skill` (gitverse.ru);
  - storybookjs/react-native skills;
  - wondelai, apart from the scan.
- **Partial reviews:** ECC, impeccable, shadcn-ui/ui and claude-plugins-official were scanned in full but not read line by line. The superpowers plugin hook was read; its other scripts were not.
- **Install counts:**
  - skills.sh page counts may be cumulative or weekly; the page doesn't say.
  - Stale entries (mattpocock `to-prd`: 352K) still count installs for paths that no longer exist.
  - Star counts of 280k–300k (ECC, mattpocock, superpowers) are unusually high. Treat popularity as a weak signal.
- **Storybook plugin:** whether `storybook ai` and `@storybook/addon-mcp` handle a monorepo `packages/ui` with shadcn source components is unverified.
- **Next.js skills** live on the `canary` branch. Whether they track the stable release line was not checked.
- **Mondoo's finding on superpowers `using-superpowers`:** the severity was not read from the primary page.
- **Claude Code changelog:** `disableSkillShellExecution` exists, and in auto mode skill `!` commands follow default-mode permission rules. Whether `!` commands in project skills run before trust confirmation in a freshly cloned repo was not re-tested.

---

## 6. Evidence: commits and content hashes

Commit SHAs come from the codeload tarball headers on 2026-10-19 (HEAD of the default branch).

**Commit SHAs**

| Repo | Commit |
|---|---|
| mattpocock/skills | 49dd158d1076134a641b33efb035946536778336 (same SHA the official marketplace pins) |
| obra/superpowers | bb92a77741419a4ab5f06e711a283343f1ada0c3 (same as the official pin) |
| nextlevelbuilder/ui-ux-pro-max-skill | 56ea9cf174ed86786187daa9de0e6247cb0747e4 (same as Tessl's reviewed revision) |
| anthropics/skills | dbd4588f9e1033efb41dad4bef2f7947c8993d44 |
| anthropics/claude-plugins-official | ea10b213686c90bb1984b2016937310e05336cf3 |
| anthropics/knowledge-work-plugins | 33eeda1e8fd856455b05479d13a0f85b5f803744 |
| shadcn-ui/ui | ba1503c64472b82256d9de95e2e62c5901a38e8b |
| storybookjs/mcp | 4589b69a081272508be2b00220f38b9d6ee488de |
| lingui/skills | 2be6e699bb0d107dfa3790d0c7c551b34e306a1b |
| i18next/i18next-cli | 933364ee283b2b6a805ad1ae8c936a01a2de2dae |
| vitalets/playwright-bdd | 208427673f665a28d4d249de75a91ee8385bd126 |
| microsoft/playwright-cli | b85c7a736bb473bf55b584e54a09ffa698d6d871 |
| currents-dev/playwright-best-practices-skill | 283d5cbc5d11aac1abda058b16ad22c317d54dc0 |
| addyosmani/web-quality-skills | afa8da942115f2961fdbfa80807ea0b232ff6c00 |
| addyosmani/agent-skills | aeac41d4d005999432bb7312f7ff06383a91d59d |
| emilkowalski/skills | 2d228630ba1446365f614a108cb8252f1feda202 |
| content-designer/ux-writing-skill | 98cacde4ba2dd10ed28df43a8d53eef1e321c539 |
| samber/cc-skills | 123cb155f5ab5751fc13c8027fbfa5eb0d3773c6 |
| getsentry/skills | f57ada2d0b640406ea7e25b11d636c530e77c58b |
| affaan-m/ECC | 76aaa77df6adc5b889e689007bf99b9a4f74af34 |
| wshobson/agents | 0874a27b17a22e2b7c2e2bcd725768e0803cad06 |
| pbakaus/impeccable | 0665bd812ae0908fcab17b96fd4f840defb882d9 |
| figma/mcp-server-guide | bdd857feb374fa58e21a364f56f31288eb7cc2fe (the official marketplace pins f2789420) |
| supabase/agent-skills | c9be0e931b7930f7d02126d04774d904c381e7d7 |
| phucnt-bazone-vietnam/use-case-writer | 695cd6c14ec5e05e67380e2d05dde79909fcd207 |

**Content hashes** of skill folders (first 16 hex characters of SHA-256):

| Skill folder | Hash |
|---|---|
| ui-ux-pro-max | 7938868f27b62f3e |
| frontend-design | 89496d5dd00f4810 |
| ux-copy | f7addd20b733b196 |
| accessibility-review | 987e6d7620600250 |
| write-spec | be9823943cc5f15f |
| shadcn | 7182424be706c4c6 |
| fastapi | d6e1ac271e36a620 |
| storybook claude-plugin | 4c4e01da73861a7a |
| lingui-best-practices | e9203a6614803adf |
| i18next-localization | 18664e3215bf9247 |
| playwright-bdd | db55c68596e2f328 |
| playwright-best-practices | b68745f4bd933ea6 |
| humaniseur-fr | 90a94a423acf8f82 |
| conventional-git | 696c8cea1d18ed73 |
| ux-writing | b231c56952bc3789 |
| hexagonal-architecture | 9bcc7b90143ab607 |
| using-git-worktrees | 48c8a1040e378e0c |
| getsentry security-review | 11055500b40ff886 |
| gdpr-compliant | 9c88af335bc125c5 |
| web-quality accessibility | 48861fac56e62fd4 |
| emil-design-eng | 51f2537e04d15911 |
| use-case-writer | 38c8d1cc06fd57f3 |
| next.js skills | 31416914c336001f |

---

## 7. Proposed framework tuning (for skill-scout; not applied)

These came up while applying the rules. Per skill-scout's `CLAUDE.md`, they are proposals until the user agrees.

1. **Zero-width joiners and variation selectors inside emoji graphemes** (U+200D, U+FE0F) should not count as *hidden content*. They appeared in the Figma `.d.ts`, the emilkowalski catalog, use-case-writer and lingui. Suggestion: exempt them when the neighbouring code point is an emoji.
2. **Consented writes to harness settings**, i.e. hook installers that ask first (mattpocock git-guardrails, impeccable `hooks on`), are currently always a confirmed red flag. Consider making them *contextual* when the skill asks first, writes only to project scope, and shows the diff.
3. **First-party bootstrap hooks** (security-guidance's SessionStart `pip install`) need a rule. Option: make them contextual when the publisher is the harness vendor and the install is pinned (it isn't pinned today, so this case would still fail).
4. **Add two red-flag patterns that the checklist lacks:**
   - **Load-time dynamic context**: `` !`…` `` lines in SKILL.md (Datadog, 2026-05). Network or unpinned commands there should carry at least a deduction.
   - **Runtime remote instructions**: skills that fetch their own rules from an unpinned URL at run time (Vercel `web-design-guidelines` and `writing-guidelines`; Snyk code W012).
5. **Stale directory entries.** skills.sh keeps install counts for skill paths that were removed upstream (mattpocock `to-prd`). G4 should check that the path still exists at HEAD.
6. **Seed list:** propose adding `storybookjs/mcp` and `vercel/next.js/skills` as known first-party sources. Neither shows up in skills.sh search results.
