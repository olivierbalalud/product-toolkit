# 4. Development Playbook

How to take a `Dev-ready` PRD to `Done` as one slice and one slice PR. The gates are in [chapter 1](01-lifecycle-and-gates.md), the tests in [chapter 8](08-testing.md) and the review lanes in [chapter 9](09-review-lanes.md). Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md).

## 4.1 Principles

1. **One story, one PRD, one slice, one PR** [R1-Q9]. The slice is done when the whole feature works end to end, not when a layer is.
2. **No personas during development** [R1-Q12]. The review lanes and a human reviewer take over [R4-Q7′].
3. **Tests first**, in a fixed order, with fakes behind ports for the business layer [R4-Q8′].
4. **The hexagon applies to the business layer only**: `business/` imports neither FastAPI nor SQLAlchemy. Technical services behind the ports take whatever shape they need [R3-Q1f].
5. **Code may already exist.** The slice reuses and extends it, and changes it only by the rules of §4.8 [R4-Q8c, R4-Q8d].
6. **The design is fixed.** A UX change found during the slice is a DCR, never a quiet fix [R2-Q4, R4-Q7c].

## 4.2 Step 1: Pick a Dev-ready PRD

1. Check the limit: at most **2 slices in development per developer** [R4-Q6]. Enabler slices that block feature slices go first.
2. Read, in this order: the PRD, its `features/`, `fit.md`, `contract.draft.yaml`, the linked ADRs and TRDs, and the enabler slices it depends on.
3. Confirm the enablers it needs are `Done` or will merge before the tickets that need them [R5-Q1].

## 4.3 Step 2: Open the slice

```bash
make slice PRD=PRD-012.1 SLUG=book-room
```

The script creates the branch `slice/PRD-012.1-book-room` from `origin/main` (or opens it) in the worktree `.claude/worktrees/slice-PRD-012.1-book-room`, runs `make env-up` there to give it its own ports, Compose project and database, and launches `claude --worktree slice-PRD-012.1-book-room`. Two slices can then run side by side ([chapter 5](05-worktrees-and-parallelism.md)) [R2-Q9, R4-Q5′, R16-Q0].

Set `status: In development` and commit: `docs(PRD-012.1): start slice`.

## 4.4 Step 3: Refresh the fit analysis

Run the fit check again against current `main` and update `fit.md` [R4-Q8′ step 0]:

- If code has moved since Design-complete, the tickets in the next step take it into account.
- If the design must change, open a DCR ([chapter 3, §3.13](03-design-playbook.md#313-changing-a-design-after-the-gate)) and pause the tickets it affects [R7-Q3].
- If an architecture gap appears, open a `Proposed` ADR and pause only the tickets it affects; the others carry on. If the ADR's outcome changes the UX, it becomes a DCR [R13-Q3].

## 4.5 Step 4: Cut the tickets

Run `to-tickets` on the PRD [R4-Q7′]. It:

1. explores the code and proposes **tracer-bullet tickets**: each one a narrow but complete path through every layer, verifiable on its own, sized for one fresh context window;
2. gives each ticket its **blocking edges**;
3. asks the developer to approve the breakdown;
4. writes one file per ticket in the story folder, `tickets/NN-<slug>.md`, with `status` and `blocked_by` in frontmatter [R6-Q2].

`to-tickets` and `implement-spec` find the tracker through `docs/agents/issue-tracker.md`, which `setup-matt-pocock-skills` writes once per repo. Its default local layout is `.scratch/<feature>/issues/` with the fields in the body; edit that file to describe ours instead: tickets in `stories/US-…/tickets/` or `enablers/ENB-…/tickets/`, fields in frontmatter. Check on the first slice that both skills follow it [R13-Q1].

Prefactoring comes first: "make the change easy, then make the easy change" (`to-tickets`). A wide mechanical refactor is sequenced as expand, migrate in batches, contract.

## 4.6 Step 5: Implement the tickets in parallel

Run `implement-spec` with the slice branch as the **integration branch** [R4-Q7′]. It works the **frontier**, the tickets whose blockers are all done:

1. Each unblocked ticket goes to an **implementer subagent** in its own worktree, based on the slice branch, using the `tdd` skill.
2. When one finishes, a **merger subagent** merges it into the slice branch, which may unblock more tickets.
3. When all tickets are done, it runs `code-review` on the slice branch and fixes what it raises. This is the fast review loop: `implement-spec` calls `code-review` itself, so the full code lane runs later, on the slice PR [R13-Q2].
4. It cleans up the subagent worktrees.

Subagent worktrees keep the names Claude Code generates; only the slice worktree follows our naming [R4-Q5′].

## 4.7 The test-first order

Each ticket follows this order, for the layers it touches [R4-Q8′]. Technical unit tests come with each step.

| Step | What | Where in the domain | Tests |
|---|---|---|---|
| 0 | Refresh the fit analysis (once per slice, §4.4) | `fit.md` | — |
| 1 | Finalise the contract: reconcile the draft with the existing OpenAPI | `app/schemas/` (Pydantic) | OpenAPI diff against `main` |
| 2 | Bind the scenarios: pytest-bdd step definitions against the business layer, with fakes. Scenarios that already pass are existing behaviour; the rest fail. Add characterisation tests first where untested code will change. | `tests/bdd/steps/`, `tests/fakes/` | pytest-bdd |
| 3 | Business logic until the scenarios pass | `app/business/{model,usecases,ports}` | pytest-bdd, unit |
| 4 | Adapters for the ports | `app/adapters/{db,<external>}` | integration, against a real Postgres |
| 5 | API layer | `app/api/` | API tests, OpenAPI diff check |
| 6 | Promote the UI (§4.9) | `src/apps/web/` | Playwright-BDD |
| 7 | Security and privacy (§4.10) | `tests/security/` | authorisation matrix, privacy tests |

An import-linter contract keeps the business layer free of framework imports [R3-Q1f].

## 4.8 Working with code that already exists

| Situation | Rule | Decision |
|---|---|---|
| A behaviour the PRD needs already exists | Reuse it; its scenario already passes in step 2. | R4-Q8b′ |
| Existing behaviour must change, and nothing else depends on it | The signed PRD wins. | R4-Q8c |
| Existing behaviour must change, and other features depend on it | A backward-compatible extension if possible; otherwise a breaking change only if the PRD lists every consumer. The OpenAPI diff in CI blocks any breaking change not listed. Failing both, a DCR. | R4-Q8c |
| Code to change has no tests | Add **characterisation tests** that pin today's behaviour before changing it. | R4-Q8d |
| Code doesn't follow the target structure | Touch only what the slice needs. Reach old code through a port (strangler pattern) rather than rewriting it. Restructuring a whole module is an enabler slice. | R4-Q8d |
| A shared layer must change (tokens, `globals.css`, design-system components, OpenAPI shared by others, migrations) | Only in its own enabler slice, one at a time. | R2-Q9 |

## 4.9 Promoting the UI

1. **Move** the prototype routes from `(prototypes)/` into the real routes. Don't copy them: a prototype left after `Done` fails CI [R4-Q11].
2. Replace the MSW mocks with the API client generated from the domain's OpenAPI (`src/packages/api-client/`) [R3-Q1g].
3. Write the Playwright-BDD step definitions. Steps that name a copy key resolve it through the next-intl catalogs, so the same scenarios run in every locale [R3-C2].
4. Generate the catalogs for the other locales with the translation skill; generated strings stay `needs-review` [R2-Q6, R4-Q10].
5. Emit the events in the measurement plan through the **analytics port**, and assert them in tests with its fake [R4-Q4c]. If the real pipeline doesn't exist yet, the fake is enough for `Done` [R4-Q4d].

## 4.10 Security and privacy tests

The minimum for every slice [R4-Q9]:

- **Authorisation:** tests generated from PRD §10, every role × action, both allowed and denied.
- **Privacy:** tests derived from PRD §11: retention; erasure and pseudonymisation; no personal data in logs; API responses return only what their purpose needs.
- **Security:** the OWASP ASVS level 1 items relevant to the slice.
- **CI-wide:** dependency scanning and secret scanning.

## 4.11 Step 6: Review and open the slice PR

1. Open the slice PR from `slice/PRD-…` into `main` and set `status: Done` in it [R4-Q5′].
2. The review lanes run [R4-Q7b]:
   - **code** and **security and privacy**, always;
   - **UX**, when the diff touches `src/apps/web/` or `src/packages/ui/`.
3. Each lane posts one summary comment; full reports are CI artifacts [R4-Q7c].
4. Fix every **blocking** finding. After fixes, only the lanes whose files changed run again [R4-Q7b].
5. A UX finding that would change the agreed design opens a DCR instead of a fix [R4-Q7c].
6. A human reviews the PR [R4-Q7′].

## 4.12 Step 7: Pass Done

The gate check verifies the Done checklist ([chapter 1, §1.8](01-lifecycle-and-gates.md#18-in-development--done)) [R4-Q12]. On merge:

- the screens are captured into Figma on an `as-built` page [R3-Q7];
- `outcome_review_due:` is set in the PRD [R4-Q4e];
- the slice worktree can be removed.

PM and UX accept the feature on staging; that acceptance is not a gate [R2-Q5]. Production release of a locale waits for its native review [R4-Q10].

## 4.13 Bugs

A bug is fixed on a `fix/` branch, outside the lifecycle [R5-Q2]:

| Case | What to do |
|---|---|
| The code doesn't match an existing scenario | Fix it and add a regression test tagged with that scenario. No PRD. |
| A case is missing from the specs, the intended behaviour is clear, and nothing visible changes | Add the scenario to the `Done` PRD's `.feature` file in the fix PR; the PRD gains `amended_by: fix/…`; the other founder signs. |
| The fix would change the UX | It becomes a new story. |

The code and security lanes run on every `fix/` PR; the UX lane when the web app or UI package is touched [R7-Q4].

## 4.14 Enabler slices

An enabler slice follows the same steps from §4.3, with its own `enb/ENB-…` branch and its `tickets/` folder next to `enb.md` [R4-Q5′, R8-Q1]. It has no PRD, so there is no fit analysis against scenarios, no UI promotion and no measurement plan, unless its own done criteria ask for them. An enabler that adds a design-system component goes through *Exploring* and the UX persona review first [R7-Q2].
