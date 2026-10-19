# 9. Review Lanes

How code, security and UX are reviewed by agents before a human reviews the PR. Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md). The example manifest is [`review-lanes.yaml`](../templates/review-lanes.yaml).

## 9.1 Why lanes

`code-review` (mattpocock) reviews a diff on two axes only: **standards** (the repo's documented coding standards plus a baseline of code smells) and **spec** (does the diff do what the spec asked). It does not review security, privacy, UX, accessibility or copy [R4-Q7]. Each of those needs several specialised reviewers, so reviews are grouped into **three lanes**, each one of our own skills that launches its reviewers in parallel [R4-Q7a].

Two rules come from `code-review` and apply to every lane:

- **Reviewers run as separate subagents**, so one reviewer's context doesn't colour another's.
- **Reports are shown side by side, never merged or reranked.** A change can pass one axis and fail another; merging would let one hide the other.

## 9.2 The lanes

| Lane | Reviewers | Decision |
|---|---|---|
| **Code** | mattpocock `code-review` (standards and spec); `pr-review-toolkit` agents (hidden failures, test coverage, type design); our pytest-bdd and next-intl convention checks; the diff-coverage check | R4-Q7a, R14-Q3 |
| **Security and privacy** | getsentry `security-review` (pinned); Claude Code's built-in `/security-review`; our GDPR/CNIL privacy review; for slices touching the LLM gateway or AI features, our OWASP Top 10 for LLM Applications review; a script that checks the authorisation and privacy tests exist | R3-B2, R4-Q7a, R4-Q9, R12-Q6b |
| **UX** | `ui-ux-pro-max` (UX rules); addyosmani `accessibility` (WCAG 2.2); our pinned copy of the Vercel web guidelines; `review-animations` (motion); `ux-copy` plus our copy and voice check (French included); our state-matrix check; a conformance check of `flows.md` and the copy deck against the rendered screens (Playwright), with Chromatic visual diffs | R4-Q7a, R3-D1..D7 |

Each lane reads its reviewers from **`review-lanes.yaml`** in our plugin, so adding or swapping a reviewer is a configuration change, not a rewrite. A thin **`review-slice`** skill runs whichever lanes apply [R4-Q7a].

## 9.3 When each lane runs

| Where | Lanes | Decision |
|---|---|---|
| Before the design gate, on the prototype | The UX lane's guideline reviewers: accessibility, web guidelines, UX rules, copy and voice, state matrix. Their reports feed the UX persona and `reviews.md`. | R4-Q7d |
| Inside `implement-spec`, after the tickets merge | `code-review` only: `implement-spec` calls it itself. This is the fast loop. | R13-Q2 |
| Slice PR | Code and security, always; UX when the diff touches `src/apps/web/` or `src/packages/ui/` | R4-Q7b |
| Fix PR | Code and security, always; UX under the same path rule | R7-Q4 |
| Enabler PR | Code and security, always; UX under the same path rule. An enabler that adds a design-system component always touches the UI package. | R15-Q1 |
| After fixes | Only the lanes whose files changed run again | R4-Q7b |

## 9.4 Findings

| Rule | Decision |
|---|---|
| Every finding is **`blocking`** or **`advisory`**. | R4-Q7c |
| A blocking finding in any lane blocks *Done*; the gate check verifies it. | R4-Q7c, R4-Q12 |
| A UX finding that would change the agreed design (flow, copy, layout) is **not fixed in the slice**: it opens a DCR. | R4-Q7c |
| Diff coverage below 80% is advisory, never blocking. | R14-Q3 |
| An AI eval score below the PRD's threshold is blocking. | R14-Q5 |
| Each lane posts **one summary comment** on the PR. Full reports are CI artifacts and are never committed. | R4-Q7c, R3-Q1b |

## 9.5 How the lanes are built

[R4-Q7e, R5-Q4a]

- The lane skills and their reviewer subagents ship in our **project plugin**, pinned by SHA [R3-B6].
- Each reviewer **preloads** the upstream skills it needs through the subagent `skills:` field. A skill with `disable-model-invocation: true` can't be preloaded, so reviewers only preload model-invocable skills ([skill authoring research](../research/skill-authoring.md)).
- Reviewers that need an MCP server (Playwright, Storybook, Figma) use servers declared once in the monorepo's `.mcp.json`, because plugin subagents ignore `mcpServers`.
- Reviewers are **leaves**: `Agent` is removed from their tools, so they can't start further subagents and a lane's depth and cost stay predictable [R15-Q2].
- Following the portability rules, each lane skill describes its fan-out as optional: if the harness can't run subagents, the reviewers run one after another and their reports stay separate.
- **To test before relying on it:** how a plugin subagent's `skills:` field names a plugin skill (bare name or `plugin:name`) is not documented. Check it in the monorepo before the lanes are built ([chapter 12](12-skills-to-build.md)).

## 9.6 Running the lanes

| Context | How |
|---|---|
| Locally, during a slice | Invoke `review-slice` in the slice worktree. |
| In CI, on a PR | A headless `claude -p` run of `review-slice`, with no questions asked, writing its reports as artifacts and its summary as a PR comment ([chapter 12](12-skills-to-build.md) gives the exact command per skill). |

**When CI runs them** [R15-Q3]: when a PR is marked ready for review, and when a re-review is requested; not on every push. Each run has a cost cap. CI review runs are billed model calls and count against the monthly budget; their spend is reviewed monthly together with the eval spend [R1-Q14, R5-Q4c].
