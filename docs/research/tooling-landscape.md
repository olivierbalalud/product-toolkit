# Tooling landscape: design ↔ code sync and parallel feature work

Status: research notes, captured 2026-10-19. Refers to [`../brief.md`](../brief.md).
Sources are linked inline. Prices are list prices seen on 2026-10-19. Anything marked **(unverified)** comes from secondary sources, comes from conflicting primary sources, or could not be confirmed.

## Summary

| Tool | Category | Two-way sync? | Free tier | Fit verdict |
|---|---|---|---|---|
| Claude Design (Anthropic) | Rapid prototyping + bridge | **Partial.** Code → design: `/design-sync` uploads the repo's React components. Design → code: a handoff bundle that the agent re-implements, not a diff. | Included in Free/Pro/Max/Team (shared usage limits); Free use from Claude Code unclear | **Strong** for exploration before design-complete, with no new vendor. Not a source of truth: no version history, no token export. |
| Figma (Dev Mode, MCP, Code Connect) | Bridge | **Agent-mediated.** MCP reads designs. MCP write-to-canvas (beta) and code-to-canvas give code → Figma snapshots. Code Connect maps components. No automatic sync. | Starter: 20 MCP calls/month, no Dev Mode or Code Connect | **Best bridge available.** Needs Professional: Full $16, Dev $12 per seat per month. |
| Figma Make | Rapid prototyping | **No.** One-way push to a repo that Make creates, and it overwrites edits made in GitHub. | Needs a paid Full seat | Poor for the monorepo. |
| Builder.io (Projects / Visual Copilot) | Rapid prototyping + bridge | Repo: edits your repo through PRs. Figma: one-way only. | 15 credits/day, 60/month, 1 design system | Optional. Largely overlaps Claude Code plus the Figma MCP. |
| Lovable | Rapid prototyping | Two-way GitHub sync, but only with a **new** repo that Lovable creates. Fixed TanStack Start stack, no Next.js. | 5 credits/day, 30/month | **Poor.** Throwaway prototypes only. |
| Cursor | IDE / agent | n/a. Design Mode edits code from the running app. | Limited free plan | **Redundant** next to Claude Code + VS Code. |
| shadcn studio | Bridge (tokens) + blocks | Manual import/export of tokens between the Figma kit and the shadcn theme. Components are not synced. | Community tier free; paid tiers are lifetime licences ($99–$849) | Useful if you want a paid Figma kit that is aligned with shadcn. |
| Optics | Design-system reference | n/a | MIT | Reference for a registry-based design system only. Single maintainer. |
| ECC (affaan-m) | SDLC harness | n/a | MIT (paid "ECC Pro" app is optional) | Cherry-pick. Do not install the full profile. |
| Matt Pocock skills | SDLC harness | n/a | MIT | **Strong fit.** Grilling, to-spec, to-tickets, tdd and implement-spec (worktree orchestration). Already installed here. |
| wshobson/agents | SDLC harness (stack agents) | n/a | MIT | Cherry-pick the FastAPI, Next.js and TDD plugins. |
| Tokens Studio | Bridge (tokens) | **Yes, for tokens.** Push/pull with Git. | Free plan is limited; whether Git sync is free is unclear | Candidate if tokens must be edited in Figma. |
| Style Dictionary v5 | Token build | One-way build: DTCG JSON → CSS, TS, native | OSS | **Yes.** Generates shadcn `globals.css`, later RN/native. |
| tweakcn | Theming | One-way: editor → CSS | OSS (Apache-2.0) | Use for theme exploration. |
| Storybook + Chromatic Storybook Connect | Bridge | One-way: live stories shown inside Figma | Chromatic: 5k snapshots/month | **Recommended** as the shared "code as seen by designers" view. |
| next-intl / Lingui / i18next | i18n | n/a | OSS | next-intl for web only. Lingui or i18next if one library must cover web and RN. See §12. |
| Claude Code worktrees | SDLC harness | n/a | Built in | **Yes.** `--worktree`, `isolation: worktree`, `.worktreeinclude`, `WorktreeCreate` hook. |

**Synthesis.** No tool offers true two-way sync of screens. What can round-trip reliably is **tokens**. The workable pattern:

- Tokens live in git as DTCG JSON.
- Components live in code: shadcn plus Storybook.
- Figma or Claude Design consumes them through Code Connect, MCP or `/design-sync`.
- Changes that go back from code to the design tool are snapshots (code-to-canvas, or `use_figma` with library components), produced deliberately and reviewed, not auto-merged.

---

## 1. Claude Design (Anthropic)

**What it is**
- Launched 2026-04-17 as an Anthropic Labs research preview on Opus 4.7 ([announcement](https://www.anthropic.com/news/claude-design-anthropic-labs)).
- Produces designs, interactive prototypes, slides and one-pagers, with chat beside a canvas.
- It now runs as an artifact template inside Claude, and in Claude Code through `/design`.
- **The standalone claude.ai/design closes on 2026-12-14.** Design systems should be migrated before then ([get started](https://support.claude.com/en/articles/14604416-get-started-with-claude-design)).

**Plans**
- The support article says: "available on Free, Pro, Max, Team, and Enterprise plans, and it's on by default". For Enterprise, on by default from 2026-10-15.
- Usage counts against the plan's shared limits.
- **Conflict:** the [Claude Code artifacts doc](https://code.claude.com/docs/en/artifacts) says artifacts need Pro or higher.

**Design systems**
- Built from a codebase (GitHub or a local folder), Figma files, PDFs or decks, screenshots and fonts ([design systems](https://support.claude.com/en/articles/14604397)).
- Extracts a guide, tokens and components. An org can hold several systems and publish one as the default.
- Updates happen by "Remix" in chat. There is no automatic refresh.
- One tester found Figma imports less faithful than GitHub imports ([UX Planet](https://uxplanet.org/using-design-systems-in-claude-design-how-good-is-it-bb697a767b44), secondary).

**Claude Code integration** ([commands](https://code.claude.com/docs/en/commands))
- `/design-sync [hint]` is a bundled skill. It converts the repo's React design system and uploads it, so that designs use your real components.
- The first sync checks every component and can take hours on a large repo.
- `/design-login` authorises the sync. It needs the Anthropic API, so it does not work on Bedrock, Vertex or Foundry.
- `/design [brief]` drafts artboards. It needs Claude Code v2.1.265 or later.
- Reportedly only React packages that have a built `dist/` or Storybook qualify ([wmedia](https://wmedia.es/en/tips/claude-code-design-sync-your-components), unverified).

**Handoff and export**
- "Handoff to Claude Code" produces a bundle containing the designs, the chat and a README for the agent. It is sent to the local coding agent or to Claude Code Web.
- Other exports: .zip, PDF, PPTX, Google Slides, standalone HTML, Canva, Vercel, Netlify and others ([tutorial](https://academy.claude.com/tutorials/using-claude-design-for-prototypes-and-ux)).

**Two-way?**
- Code → design: components, through `/design-sync`.
- Design → code: intent plus HTML, which the agent re-implements.
- Blogs call this "two-way sync". The official docs do not describe continuous sync.

**Limitations (official):** no version history yet, basic multi-user editing, import quality depends on the source, inline comments are flaky. For monorepos, link only the relevant package.

**Fit:** the best fit for the "open to iteration" prototype phase. Keep the repo canonical, and do not treat Claude Design output as a design-complete artefact without a separate record, because there is no versioning.

## 2. Figma

**Pricing** ([pricing](https://www.figma.com/pricing/))

| Plan | Full seat | Dev seat | Collab seat | Notes |
|---|---|---|---|---|
| Starter | free | — | — | 150 AI credits/day, up to 500/month |
| Professional | $16 | $12 | $3 | per seat per month |
| Organization | $55 | $25 | — | billed annually |
| Enterprise | $90 | $35 | — | |

Dev Mode is not on Starter ([Dev Mode](https://help.figma.com/hc/en-us/articles/19813618057623)).

**MCP server** ([docs](https://developers.figma.com/docs/figma-mcp-server/))
- Remote server (recommended): `claude mcp add --transport http figma https://mcp.figma.com/mcp`, or Figma's Claude Code plugin, which bundles skills.
- The desktop server needs a Dev or Full seat on a paid plan.
- Rate limits ([limits](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/)):
  - View and Collab seats: 20 calls/month.
  - Professional Full/Dev seats: 200/day, 10/min.
  - Organization: 200/day, 15/min.
  - Enterprise: 600/day.
  - `generate_figma_design`, `create_new_file`, `add_code_connect_map` and `whoami` are exempt.
- Tools ([tools](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/)):
  - Read: `get_design_context`, `get_variable_defs`, `get_metadata`, `get_screenshot`, `search_design_system`, `get_code_connect_map`.
  - Write (remote only): `use_figma` creates and edits frames, components, **variables** and auto layout using your library. Also `generate_figma_design`, `html_to_figma`, `send_code_to_figma`, `upload_assets` and `create_new_file`.
  - The `create_design_system_rules` prompt generates rules files for the repo.
- Write-to-canvas is "free during the beta period" and will become usage-based and paid. Writing outside drafts needs a Full seat ([help](https://help.figma.com/hc/en-us/articles/32132100833559)).

**Code to canvas** ([docs](https://developers.figma.com/docs/figma-mcp-server/code-to-canvas/))
- Captures the running browser UI, one screen or a multi-step flow, into a Figma file. Available from Starter.
- The output is "flat layers, without a connection to your libraries". Matching variables are bound automatically.
- This is the main code → Figma path. It is a snapshot, not a sync.

**Code Connect** ([docs](https://developers.figma.com/docs/code-connect/))
- Maps Figma components to repo components: React, React Native, SwiftUI, Compose, HTML, plus templates. The MCP then emits your real component usage.
- Needs a Dev or Full seat on Professional or above.
- Professional is limited to 1 library and 1 framework, which matters later for web plus native. Organization and above allow several.
- Comes as a UI version (GitHub integration) or a CLI.

**Figma Make**
- Prompt-to-app on React 18 and Vite.
- "One-way push from Figma Make → GitHub", only to a repo Make creates and only to the default branch, and it overwrites GitHub edits ([help](https://help.figma.com/hc/en-us/articles/35463818346647)).
- Make kits can import npm design-system packages ([blog](https://www.figma.com/blog/introducing-make-kits-and-make-attachments/)).
- "Make on your local codebase (Beta)" is announced but not available (unverified timing).

**Variables ↔ code**
- The Variables REST API (read and write) is **Enterprise only** ([REST](https://developers.figma.com/docs/rest-api/variables/)).
- Below Enterprise, tokens move through: MCP `get_variable_defs` (read) and `use_figma` (write); the Plugin API (Tokens Studio, shadcn studio plugin); or native JSON import/export (see §11).

**shadcn Figma kits** ([list](https://ui.shadcn.com/docs/figma))
- Free: Obra shadcn/ui Community (MIT, tracks v4, variables-first), shadcncraft Free Starter (all 8 shadcn styles), and kits by Pietro Schirano and Sitsiilia Bergmann.
- Paid: Obra Pro, shadcncraft, shadcn/studio, Shadcnblocks.

**Fit:** the most complete bridge. Minimum useful setup: Professional with 1 Full seat for the designer and Dev or Full seats for the devs, an Obra or shadcncraft kit, Code Connect, and the remote MCP. Starter is a trial only.

## 3. Builder.io

**Free tier** ([pricing](https://www.builder.io/pricing))
- $0 for 1 user (up to 5).
- 15 agent credits/day, capped at 60/month.
- 1 space and 1 design system.
- GitHub, GitLab and Bitbucket integration; Figma plugin; VS Code extension.
- No built-in MCP, no credit rollover.

**Paid tiers**
- Pro: $24/user/month, 500 credits, built-in MCP.
- Team: $40/user/month, custom MCP servers.

**Naming:** "Fusion" now appears in the docs as **Builder Code Projects** ([docs](https://www.builder.io/c/docs/get-started-fusion)). The old fusion-intro page returns 404, so whether this is a rename is unverified.

**Repo integration**
- Connects to an existing repo and lets you iterate with prompts plus a visual editor.
- Commit Mode "Pull Requests" opens PRs. You can then ask for changes with `@builder-bot` in the PR.
- A design-system repo can be added as context. Automatic component indexing through the CLI is **Enterprise only**.
- Monorepos are not addressed explicitly ([projects overview](https://www.builder.io/c/docs/fusion-projects-overview)).

**Visual Copilot (Figma plugin)**
- Turns a Figma layer into React, Vue, Svelte, Angular, RN or HTML, with Tailwind ([blog](https://www.builder.io/blog/figma-to-tailwind)). The guides date from 2023–24.
- Mapping to your own components is shown only in marketing; how it works and whether the free tier includes it are unverified.

**Two-way?** Code changes come back to the repo as PRs. Nothing writes back to Figma.

**Fit:** marginal. The free tier's 60 credits/month is enough to evaluate it. Its visual editing on your repo overlaps with Claude Code plus Cursor-style tools.

## 4. Lovable

**GitHub sync** ([docs](https://docs.lovable.dev/integrations/github))
- Two-way on one branch (default `main`).
- **Cannot connect to an existing repo**: it always creates a new one. The workaround is to upload a ZIP into a new project.
- Reconnecting creates yet another repo, and moving the project to another workspace breaks the link.

**Stack** ([FAQ](https://docs.lovable.dev/introduction/faq))
- Apps created since 2026-05-13 use TanStack Start; earlier apps use React + Vite.
- "Lovable does not offer a choice of framework" and never uses Next.js.
- Backend is Lovable Cloud or Supabase. No native mobile.
- Tailwind + shadcn was historically the default; this is not stated in current docs (unverified).

**Limits:**
- Free: 5 build credits/day, capped at 30/month ([pricing](https://lovable.dev/pricing)).
- Pro: $25/month for 100 credits (secondary source).

**Fit:** poor for a Next.js monorepo. Use it only for disposable concept prototypes in a separate repo.

## 5. Cursor

**Design Mode** ([blog](https://cursor.com/blog/design-mode), updated 2026-06-05)
- In Cursor's built-in browser you select elements of the running app, draw on it or use voice. The agent edits the source and the app hot-reloads.
- It evolved from the 2.2 Visual Editor (Dec 2025). No Figma integration.

**Recent changes** ([changelog](https://cursor.com/changelog)): shareable canvases from cloud agents, iOS remote control, and cloud computers.

**Pricing** ([pricing](https://cursor.com/pricing))
- Plans: Free, Plus $8 (Grok models only), Premium $30, Ultra $200, Teams $30/user.
- Third-party models are on Premium and above only, billed at API rates.

**Ownership:** the reported acquisition of Anysphere by SpaceX/xAI (announced 2026-06-16) has unverified closing status.

**Fit:** redundant next to Claude Code + VS Code. Its only distinctive feature is point-and-click editing of the running app. That is a way to tweak code, not a design-tool sync.

## 6. shadcn studio

**Pricing** ([pricing](https://shadcnstudio.com/pricing))
- Community: free, with limited access.
- Lifetime licences: Basic $99, Pro $199, Team $449 (15 seats), Enterprise $849.
- The MCP and Figma pages quote "$249", so the site is inconsistent about tiers.

**Theme generator** ([link](https://shadcnstudio.com/theme-generator))
- Choose a shadcn style (Vega, Nova, Maia, Lyra), presets, colors and fonts.
- Pro adds AI generation, a WCAG contrast check and a personal theme registry: `npx shadcn add @ss-themes/<name>`.
- The output format is not stated on the page (CSS vars or OKLCH unverified).

**MCP** ([link](https://shadcnstudio.com/mcp))
- Commands: `/cui` (create), `/iui` (inspire), `/rui` (refine), `/ftc` (Figma → code).
- Listed clients: VS Code, Cursor, Windsurf, Cline. Claude Code is not listed, but it should work as a standard MCP server (unverified).

**Figma kit** ([link](https://shadcnstudio.com/figma))
- Built on Figma Variables aligned with shadcn, with 20+ themes in light and dark. Paid.
- Its plugin imports and exports tokens (OKLCH, HEX, RGB, HSL; Tailwind v4) and converts Figma frames to shadcn code.
- Token round-trip is manual. Components are not synced.

**Blog** ([shadcn React component libraries](https://shadcnstudio.com/blog/shadcn-react-component-libraries/), 2026-05-28, updated 2026-08-20) covers 22 libraries and rarely states licences. Relevant to this team:
- **Theming:** tweakcn.
- **Product UI:**
  - Coss UI: data grids, rich text, filters.
  - ReUI: 100+ components and blocks, ships Storybook.
  - UseLayouts: app shells, sidebars, resizable panels.
  - Solace UI and Square UI: dense B2B UI, tables, forms, command palette.
  - Kokonut UI: Radix modals and drawers.
- **Motion:** Motion Primitives and Smooth UI (both Framer Motion); Lucide Animated (CSS/SVG). Relevant to the separate "micro-interactions" layer in the brief.
- **Docs:** SyntaxKit (Shiki code blocks).
- **Design system:** Optics (§7).
- **Marketing blocks:** Tailark, MVP Blocks, BadtzUI, Cult UI. Low relevance, because the website is outside the monorepo.
- **Low relevance:** Pattern Craft, Fancycomponents, Skiper/UI, Components.work, Ali Imam UI (visual effects).

## 7. Optics

**What it is:** [optics.agusmayol.com.ar](https://optics.agusmayol.com.ar/), repo [AgusMayol/optics](https://github.com/AgusMayol/optics).
- A design system plus resource site by one developer, published as `@optics/design-system`.
- MIT, 234 stars. Last push 2026-04-11 (GitHub API).

**Stack:** Next.js 16, React 19, Tailwind v4, **Base UI** (not Radix), Bun, Turbo.

**Contents**
- 60+ components distributed through a shadcn registry (`bunx shadcn@latest add <item>`).
- Guides on typography, color, materials, accessibility, performance, SEO and animation.
- An MCP page and an llms.txt.

**Figma:** none in the repo. The shadcn studio article's "Figma alignment" claim is unverified.

**Fit:** a reference for building your own shadcn registry and design-system docs. Do not depend on it.

## 8. ECC (affaan-m/ECC)

**What it is:** [repo](https://github.com/affaan-m/ECC). A harness "OS" for Claude Code, plus Codex and Qoder plugins and adapters for other agents.
- MIT, v2.2.3. About 284k stars, pushed 2026-10-19 (GitHub API).
- Its loop: plan → test → implement → review → verify → remember → improve.
- It claims 71 agents, 311 skills, 97 legacy command shims, hooks, rules, memory and "continuous learning", plus the AgentShield config/secrets scanner.
- The optional paid "ECC Pro" GitHub App costs from $19/seat/month.

**Install**
- `/plugin marketplace add https://github.com/affaan-m/ECC` then `/plugin install ecc@ecc`, or `npx ecc-universal@2.2.3 install --guided` with profiles minimal/core/full.
- Do not mix install methods.
- Plugins cannot ship `rules`, so copy them manually.

**Relevant to an SDLC harness**
- **Agents:** `planner`, `architect`, `tdd-guide`, `code-reviewer`, `security-reviewer`, `typescript-reviewer`, `react-reviewer`, `python-reviewer`, `fastapi-reviewer`, `database-reviewer`, `e2e-runner`, `a11y-architect`, `spec-miner`, `pr-test-analyzer`, `silent-failure-hunter`.
- **Skills:**
  - `tdd-workflow`, `hexagonal-architecture`, `contract-first`, `architecture-decision-records`.
  - `i18n-sync`: syncs JSON locale files.
  - `design-system`: extracts tokens to `design-tokens.json` plus CSS variables.
  - `fastapi-patterns`, `python-testing`, `react-patterns`, `react-testing`, `react-native-patterns`, `e2e-testing`, `database-migrations`, `docker-patterns`, `security-review`.
  - `story-lifecycle`: epic → story → sprint.
  - `delivery-gate`: a Stop hook that blocks "done" until checks pass.
  - `verification-loop`, `git-workflow`, `parallel-execution-optimizer`.
- **Commands:** `/plan-prd`, `/prp-prd`, `/prp-plan`, `/prp-implement`, `/orch-add-feature` (research → plan → TDD → review → gated commit), `/quality-gate`, `/code-review`, `/security-scan`.
- **Hooks:**
  - PreToolUse: blocks `npm run dev` outside tmux, runs a pre-commit quality check, and adds a push reminder.
  - PostToolUse: Prettier, `tsc --noEmit`, and a "design quality check".
  - Lifecycle: memory persistence.
  - The v2.0.0 notes list a "worktree lifecycle service" (not inspected).

**Fit:** a large, fast-moving, opinionated set. Cherry-pick a few skills and agents (`delivery-gate`, `hexagonal-architecture`, `fastapi-reviewer`, `i18n-sync` as a reference) rather than installing a profile. Some hooks, such as the tmux dev-server blocker, may conflict with the worktree setup. The quality of individual skills is unverified.

## 9. Matt Pocock skills (aihero.dev/skills)

**What it is:** [page](https://www.aihero.dev/skills), [repo](https://github.com/mattpocock/skills).
- MIT, v1.3.1 (2026-10-04). About 297k stars (GitHub API).
- Install with `npx skills@latest add mattpocock/skills` (editable copies) or as the `mattpocock-skills` Claude Code plugin. The plugin is already installed in this environment.

**Relevant skills**
- **Design phase:**
  - `grilling` / `grill-me`, and `grill-with-docs`, which also writes ADRs and a glossary. This fits the brief's crystallisation step and the gap → ADR rule.
  - `domain-modeling` (GLOSSARY.md, ADRs).
  - `to-spec`: the page still advertises `/to-prd`, but the repo has `to-spec` (rename unverified).
  - `to-tickets`: tracer-bullet tickets with blocking edges.
  - `wayfinder`, `prototype`, `research`.
- **Development phase:**
  - `tdd` (red-green-refactor), `implement`, `implement-spec`.
  - `code-review`: Standards and Spec reviews run in parallel.
  - `pr`, `diagnosing-bugs`, `codebase-design`, `handoff`.
  - `misc/git-guardrails-claude-code`: hooks that block push, `reset --hard` and the like.
  - `misc/setup-pre-commit`.

**Worktrees:** there is no standalone skill; `implement-spec` is the orchestrator.
1. Creates an integration branch.
2. Treats the tickets as a task graph.
3. Runs every ticket whose blockers have landed in parallel, each in an implementer subagent with its own worktree that uses `tdd`.
4. A merger subagent lands the branches.
5. Runs `code-review`, then cleans up.

**Documented pitfalls** (`docs/engineering/implement-spec.md`)
- "Worktrees don't remove collisions; they postpone them to merge time." Their example: parallel tickets added the same i18n string under two different keys.
- "A worktree holds only what git tracks." Tests that depend on gitignored fixtures or credentials skip silently and report green.

**Fit:** the strongest match for the brief's design → PRD → slice process. It has minimal hooks, so it composes with others.

## 10. wshobson/agents

**What it is:** [repo](https://github.com/wshobson/agents). A multi-harness plugin marketplace.
- MIT, about 41k stars, pushed 2026-10-19.
- 94 plugins containing 202 agents, 185 skills and 105 commands.
- Install with `/plugin marketplace add wshobson/agents` then `/plugin install <plugin>@claude-code-workflows`. Single skills install with `npx skills add`.

**Relevant plugins**
- `python-development`: `fastapi-pro` and `python-pro` agents; testing, typing, async and uv skills.
- `frontend-mobile-development`: `frontend-developer` and `mobile-developer`; `nextjs-app-router-patterns`, `tailwind-design-system`, `react-native-architecture`.
- `ui-design`: `design-system-architect`, `ui-designer`, `accessibility-expert`; `/design-review`, `/accessibility-audit`.
- `tdd-workflows`: `/tdd-red`, `/tdd-green`, `/tdd-refactor`, `/tdd-cycle`.
- `backend-development`, `full-stack-orchestration` (`/full-stack-feature`), `comprehensive-review`, `security-scanning`, `database-migrations`, `c4-architecture`.
- `agent-teams`:
  - Provides `/team-feature` and the `parallel-feature-development` skill, which covers file-ownership strategies, vertical vs horizontal slices and interface contracts.
  - Requires the experimental `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.
- `conductor`: a Context → Spec & Plan → Implement workflow with TDD checkpoints. It overlaps the brief's process.

**Gaps:** no i18n, shadcn or Figma plugins found.

**Fit:** modular and less opinionated about process than ECC. Install `python-development`, `frontend-mobile-development` and possibly `ui-design` for stack-specific agents. Treat `conductor` and `agent-teams` as alternatives to compare with `implement-spec`, not as additions.

## 11. Design-token pipelines

**W3C DTCG format**
- First stable version **2025.10**, published 2025-10-28 as a Final Community Group Report. Modules: Format, Color, Resolver ([announcement](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/), [spec](https://www.w3.org/community/reports/design-tokens/CG-FINAL-format-20251028/)).
- Covers aliases, themes and multi-brand, OKLCH and Display P3.
- Not on the W3C Standards Track ([FAQ](https://www.designtokens.org/faq/)).

**Figma Variables**
- REST GET and POST are Enterprise only ([REST](https://developers.figma.com/docs/rest-api/variables)). Lower plans get a 403 "Limited by Figma plan".
- Native JSON import/export is DTCG-aligned and was announced at Schema 2025 ([recap](https://www.figma.com/blog/schema-2025-design-systems-recap/), [help](https://help.figma.com/hc/en-us/articles/15343816063383-Modes-for-variables)). Import matches variables by name and type.
- Forum reports say export drops `description`, adds `$extensions.com.figma.variableId`, and a re-import restored only 2 of 256 variables ([thread](https://forum.figma.com/report-a-problem-6/variable-export-import-broken-53229)). This is a manual file round-trip, not a sync.

**Tokens Studio**
- Its docs describe Git sync as two-way, with push and pull from the plugin. Multi-file sync is "pro" ([docs](https://docs.tokens.studio/token-storage/remote/sync-git-github)).
- The [pricing page](https://tokens.studio/pricing) lists "direct Git-sync" as paid. The Team plan is €39/month (annual). The free plan has 1 editor and 1 project.
- **Conflict:** it is unclear whether single-file GitHub sync is still free.
- Syncing to Figma Variables is a paid feature.

**Style Dictionary**
- v5.0.0 released 2025-05-16; latest 5.7.0. Requires Node 22+.
- Uses DTCG `$value`/`$type`, and references must point to tokens ([migration](https://styledictionary.com/versions/v5/migration/)).
- Natural target: generate shadcn `globals.css` now, and RN/native token files later.
- Alternative: Terrazzo ([docs](https://terrazzo.app/docs/guides/import-from-figma)); its Figma import needs Enterprise.

**shadcn CSS variables (Tailwind v4)** ([theming](https://ui.shadcn.com/docs/theming))
- Tokens are semantic pairs (`--primary` / `--primary-foreground`) in oklch, defined under `:root` and `.dark`.
- They map to utilities with `@theme inline { --color-primary: var(--primary); }`.
- The radius scale derives from `--radius`. Dark mode uses `@custom-variant dark (&:is(.dark *))`.
- A new token (e.g. `warning`) must be added in all three places: `:root`, `.dark` and `@theme inline`.
- CSS-variable mode is chosen at init time.

**tweakcn** ([repo](https://github.com/jnsahaj/tweakcn), Apache-2.0, about 10.5k stars; [site](https://tweakcn.com))
- A visual theme editor for shadcn that outputs Tailwind v3/v4 in oklch or hsl, installable through the shadcn registry.
- One-way, editor → CSS. No Figma link.
- Registry command and MCP details unverified.

**Storybook as a bridge**
- Chromatic's [Storybook Connect](https://www.chromatic.com/docs/figma) plugin links stories to Figma components and shows live stories in Figma, following a chosen branch.
- Needs a Figma editor role and Chromatic collaborator access.
- Chromatic free tier: 5,000 snapshots/month, Chrome only ([pricing](https://www.chromatic.com/pricing)). It also gives visual-regression tests.
- It gives designers a view of the code. It does not change Figma.

**Suggested pipeline (inference, not a vendor recommendation)**
1. `tokens/*.json` (DTCG) in the monorepo is canonical.
2. Style Dictionary builds `globals.css` (shadcn vars plus `@theme inline`), and later RN tokens.
3. Figma Variables receive tokens through Tokens Studio or the shadcn studio plugin, or through native import.
4. Designer changes come back as a PR to `tokens/`, through Tokens Studio Git push or an MCP `get_variable_defs` diff that Claude turns into a PR.
5. Storybook plus Chromatic shows the result to design.

## 12. i18n (Next.js now, React Native later, per-feature source locale)

**next-intl** (4.14.9)
- App Router support: `getTranslations` for Server Components, `NextIntlClientProvider` for Client Components. Messages use ICU and are namespaced ([docs](https://next-intl.dev/docs/getting-started/app-router)).
- Experimental `useExtracted`:
  - Messages are written inline and extracted at dev/build time into JSON or PO, with hashed keys.
  - A `description` gives (AI) translators context.
  - Takes a single `sourceLocale` ([extraction](https://next-intl.dev/docs/usage/extraction)).
- Agent guidance ([page](https://next-intl.dev/docs/workflows/agents)): use `useExtracted`, or rules in CLAUDE.md. It warns that agents translating whole catalogs lack context.
- Web only, so it does not cover RN.

**Lingui** (6.10.0; v6 released 2026-04-22)
- v6 is ESM only, needs Node 22.19+, moved macros to `@lingui/react/macro`, and changed ID hashing ([migration](https://lingui.dev/releases/migration-6)).
- React Native: RN 0.76+ or Expo 52+ on Hermes, with Intl polyfills ([RN](https://lingui.dev/tutorials/react-native)).
- Next.js: needs the experimental `@lingui/swc-plugin`, pinned to match `swc_core` ([swc](https://lingui.dev/ref/swc-plugin)).
- The only option here covering web and RN with one ICU/PO format.

**i18next / react-i18next** (26.5.2 / 17.1.0)
- Runs everywhere, including RN/Expo with `expo-localization`.
- Its own message format is the default. ICU needs `i18next-icu`, and ICU cannot go in JSX children, so it uses `IcuTrans` ([ICU](https://react.i18next.com/misc/using-with-icu-format)).

**Key conventions**
- Semantic namespaced keys (`checkout.payment.submit`) are stable across rewording and natural per feature.
- Source-text or hashed IDs (Lingui, `useExtracted`) mean no key invention and suit agents, but the ID changes when the source wording changes.
- In both cases, use ICU arguments and plurals and never concatenate strings.

**AI translation tools**
- [Lingo.dev CLI](https://lingo.dev/en/cli) (1.17.1):
  - Uses push/pull with a `.lingo/lock.json` lockfile and translates only changed keys.
  - Manual edits are kept unless the source changes.
  - Formats, BYOK and pricing unverified.
- [Tolgee](https://tolgee.io/pricing): the cloud free tier has 30k words and 3 seats. It offers an AI translator with prompts, an MCP server and a Figma plugin.
- Crowdin/Weblate: not researched.
- A Claude script also works: translate from the source catalog using descriptions and a glossary, then validate placeholders and ICU parsing in CI.

**Per-feature source locale (inference, not documented anywhere)**
- **Semantic keys:** easy. Use one namespace per feature (`messages/{locale}/<feature>.json`) and record `sourceLocale: fr|en` in the PRD front-matter or a namespace manifest. The translation step reads that and translates the source into every other locale. Never hand-edit a non-source file without marking it as overridden.
- **Extraction / source-text:** next-intl and Lingui each assume one global `sourceLocale` per config. Mixed fr and en literals would need per-feature catalog configs (Lingui `catalogs` entries; whether a per-catalog source locale is supported is unverified), or a rule that code literals are always en.

**Leaning:** semantic keys plus ICU JSON with next-intl on web keeps per-feature source locale simple. The catalogs remain portable to i18next-icu or Lingui on RN later. If one library across web and RN matters more, evaluate Lingui v6, accepting the experimental SWC plugin.

## 13. Claude Code + git worktrees

Sources: [worktrees](https://code.claude.com/docs/en/worktrees), [hooks](https://code.claude.com/docs/en/hooks#worktreecreate), [settings](https://code.claude.com/docs/en/settings-reference), [changelog](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md). Current CLI is v2.1.303 (npm, 2026-10-18).

**Feature history**
- v2.1.49: `--worktree`/`-w` and subagent `isolation: "worktree"`.
- v2.1.50: `WorktreeCreate`/`WorktreeRemove` hooks and the frontmatter `isolation: worktree`.
- v2.1.76: `worktree.sparsePaths`.

**`claude --worktree <name>`**
- Creates `.claude/worktrees/<name>/` on branch `worktree-<name>`. Add `.claude/worktrees/` to `.gitignore`.
- The repo needs at least one commit. **This repo has none yet**, so the command would fail.
- `claude -w "#1234"` or a PR URL branches from that PR. Reusing a name reopens the worktree; `--resume` continues a session.
- On exit, a clean unnamed worktree is removed automatically; otherwise Claude prompts. `-p` runs never clean up.

**In-session and subagents**
- `EnterWorktree` / `ExitWorktree` tools. Entering a path outside `.claude/worktrees/` needs approval (since v2.1.206).
- Edits, writes, Bash cwd and `git -C` into the main checkout are blocked. `cp` or redirects into it are not caught.
- `isolation: worktree` in `.claude/agents/*.md` gives a temp worktree per run. It loads CLAUDE.md and rules from the main conversation, not from the worktree branch.
- `/batch` fans one change out to 5–30 isolated subagents.
- Agent teams do **not** isolate teammates in worktrees.

**Settings (`worktree.*`)**
- `baseRef`: `"fresh"` (default, `origin/<default>`) or `"head"`. Use `"head"` if subagents must see unpushed work.
- `symlinkDirectories` (e.g. `node_modules`), `sparsePaths` (monorepo), `bgIsolation`.

**`.worktreeinclude`** (gitignore syntax) copies gitignored files such as `.env` into new worktrees. It is ignored when a `WorktreeCreate` hook is configured.

**`WorktreeCreate` hook**
- Replaces the git logic: it reads `name` from stdin and prints the absolute path on its last line.
- It does not fire if the agent runs `git worktree add` itself.
- This is the place to allocate a port block, a compose project and a DB per worktree.
- `${CLAUDE_PROJECT_DIR}` stays at the main checkout; use the hook input `cwd`.

**Shared across worktrees:** `.git`, project plugins, "don't ask again" approvals (since v2.1.211), and untracked `.claude/skills|agents|commands` through read-through.

**Docker Compose** ([project name](https://docs.docker.com/compose/how-tos/project-name/))
- Precedence: `-p` > `COMPOSE_PROJECT_NAME` > top-level `name:` > directory basename.
- Set `COMPOSE_PROJECT_NAME=<app>_<worktree>` explicitly in the per-worktree `.env`.
- Host port mappings still collide, so derive ports from a per-worktree offset, e.g. web `3000+N`, API `8000+N`, Postgres `5432+N`.

**Known pitfalls** (mostly secondary sources, e.g. [Upsun](https://developer.upsun.com/posts/ai/git-worktrees-for-parallel-ai-coding-agents), [Noqta](https://noqta.tn/en/blog/git-worktrees-parallel-ai-coding-agents-guide-2026), plus general practice)
- **Ports:** EADDRINUSE on 3000, 8000 or 5432.
- **Database:** shared DB state; parallel Alembic migrations create multiple heads at merge time.
- **Dependencies:** each worktree needs its own install (pnpm's store keeps this cheap). A symlinked `node_modules` breaks when branches change dependencies. Lockfile conflicts.
- **Missing gitignored files:** `.env` and fixtures are absent, so tests skip silently.
- **Devcontainers:** they break on the worktree `.git` file.
- **Shared hotspots** collide at merge time: i18n catalogs, route registries, `components.json`, `globals.css`, token files, OpenAPI schema and generated clients.
- **ECC's tmux dev-server hook** interacts with per-worktree dev servers.
- Helper tools `workz` and `worktree-compose` exist; both unverified.

---

## Pitfalls of two-way design ↔ code

1. **No declared source of truth per layer.** Two-way sync without a rule for which side wins leads to silent overwrites. Decide per layer:
   - Tokens: git, DTCG.
   - Components: code.
   - Flows and screens: the design tool until design-complete, then code.

   Changes against that direction arrive as reviewed PRs or snapshots, never auto-applied.
2. **Screens and components do not merge.** Only tokens round-trip with reasonable fidelity:
   - Code → Figma is a flat snapshot (code-to-canvas), or an agent rebuild with `use_figma`.
   - Figma or Claude Design → code is a re-implementation.

   Design edits made after implementation must be re-expressed as a change request against the code.
3. **Plan gating.** The Figma Variables REST API is Enterprise only. Code Connect and the useful MCP limits need Professional or above. Tokens Studio's Git sync may be paid, and the docs and pricing disagree. Gates move, as the Figma write-to-canvas beta will become paid.
4. **Lossy round-trips.**
   - Descriptions are dropped from Figma exports.
   - Vendor `$extensions` IDs leak into the repo.
   - Figma modes and aliases do not map one-to-one onto shadcn `:root`/`.dark` pairs plus `@theme inline`.
   - Float rounding between color spaces (Figma vs oklch) creates noisy diffs.
5. **Name drift.** Figma paths like `color/primary/default` and CSS vars like `--primary` need an explicit mapping table. A rename on one side breaks the other.
6. **Bypassing tokens.** Raw hex values in Figma, or arbitrary Tailwind values like `bg-[#123456]`, cause drift. Lint for raw colors and arbitrary values in CI, and check Figma with a token-lint plugin.
7. **Component mapping rot.** Code Connect maps and `/design-sync` uploads go stale when components are renamed. Regenerate them in CI or on release.
8. **Tool-imposed stacks.** Lovable (TanStack Start) and Figma Make (React 18 + Vite) generate code that is not your monorepo's code. Treat their output as a throwaway reference.
9. **Separation of concerns in the brief.** Theme, motion and tone of voice are global layers (tokens, motion presets, copy guidelines). If designers tweak them per screen in the design tool, the change leaks into feature PRs. Route such changes through the token or theme PR path only.
10. **Parallel worktrees amplify drift.** Two features editing tokens, `globals.css` or i18n catalogs at once conflict at merge time. Serialise shared-layer changes, or give them their own ticket with blocking edges.

## Open questions / unverified

- **Claude Design:**
  - Free-plan access from Claude Code (the support article says Free; the Claude Code artifacts doc says Pro+).
  - Whether `/design-sync` handles a monorepo package with shadcn source components but no built `dist/` or Storybook.
  - Whether any token export exists.
  - What replaces version history.
- **Figma:**
  - When the write-to-canvas beta ends, and its future pricing.
  - Availability of "Make on your local codebase".
  - The Professional monthly vs annual price split.
  - Reliability of native Variables JSON round-trip (forum reports of broken re-import).
- **Tokens Studio:** whether single-file GitHub sync is still on the free plan (docs vs pricing conflict).
- **Builder.io:** whether "Fusion" was renamed to "Builder Code Projects"; whether Visual Copilot maps to your own components on the free tier; monorepo support.
- **Lovable:** whether shadcn is still the default UI kit on the TanStack Start stack; official Pro pricing.
- **Cursor:** closing status of the SpaceX/xAI acquisition; whether Claude models are available on current plans.
- **shadcn studio:** the inconsistent tier names and prices ($249 vs $199/$449); the theme output format; Claude Code MCP support.
- **Optics:** the "Figma alignment" claim.
- **Matt Pocock skills:** whether `to-prd` was renamed to `to-spec`.
- **ECC:** quality of individual skills; how the "worktree lifecycle service" behaves.
- **Lingui:** whether a per-catalog source locale is supported. The per-feature source-locale approach in §12 is an inference, not documented practice.
- **Worktree helpers:** `workz` and `worktree-compose` not evaluated.
- **Star counts:** ECC (about 284k) and mattpocock/skills (about 297k) come from the GitHub API on 2026-10-19 and are unusually high. Treat popularity as a weak signal.
