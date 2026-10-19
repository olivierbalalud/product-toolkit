# 1. Lifecycle and Gates

This chapter defines the statuses each artifact moves through, the gate that guards each move, who signs it, and how the gate is enforced. Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md), which is authoritative where this chapter is unclear.

Artifacts and their IDs (`UC-012`, `US-012.1`, `PRD-012.1`, `ENB-004`, `DCR-012.1-01`, `ADR-0007`, `TRD-012.1`) are defined in [chapter 2](02-artifacts-and-ids.md). How to do the work inside each status is in the [design playbook](03-design-playbook.md) and the [dev playbook](04-dev-playbook.md).

## 1.1 The shape of the flow

```mermaid
flowchart LR
  UC[Use case<br/>complete] --> US[Stories cut]
  US --> D[Draft]
  D -->|picked by a founder| E[Exploring]
  E -->|Design-complete gate| DC[Design-complete]
  DC -->|Dev-ready gate| DR[Dev-ready]
  DR -->|slice starts| ID[In development]
  ID -->|Done gate| DN[Done]
  DN -.->|outcome review date| OR[Outcome reviewed]
  DC -.->|DCR| E
  DR -.->|DCR| E
  ID -.->|DCR| E
```

- **Design** covers everything up to Design-complete. The three personas (PM, UX, Eng) review only here [R1-Q12].
- **Development** covers Dev-ready to Done. No persona reviews; the review lanes take over [R4-Q7′].
- **Granularity:** one user story = one PRD = one slice = one slice PR [R1-Q9]. Work that no single story owns is an **enabler slice** (`ENB-…`) [R3-A3].
- **Status lives in each artifact's frontmatter** (`status:`), and `doc/product/index.md` is generated from it. There is no separate tracker [R3-A4].

## 1.2 PRD statuses

| Status | Meaning | Where the work happens |
|---|---|---|
| `Draft` | A story exists, with draft acceptance criteria and the use-case extensions it touches. | `doc/product/use-cases/UC-…/stories/US-…/` on `main` |
| `Exploring` | Flows, screens, copy and prototypes are iterated freely. No reviews. | A `design/PRD-…` branch and worktree [R1-Q10, R4-Q5′] |
| `Design-complete` | The design is signed off. Its `.feature` files are frozen [R3-Q1a]. The design PR has merged into `main`. | `main` |
| `Dev-ready` | Everything a developer needs is decided: ADRs accepted, TRDs written, blocking enablers scheduled. | `main` |
| `In development` | The slice is being built. | A `slice/PRD-…` branch and worktree |
| `Done` | The slice PR has merged. The PRD is now a point-in-time record and is not rewritten [R4-Q8e′]. | `main` |

After `Done`, the lifecycle has no more statuses. The **outcome review** is a section of the PRD that is filled in on a set date [R4-Q4e].

**Enabler slices** follow a shorter lifecycle, `Draft → Dev-ready → In development → Done`, with no design phase [R7-Q2]. The exception is an enabler that adds a design-system component: it goes through *Exploring* and the UX persona review before Dev-ready.

**Design change requests** have their own status, `Exploring → Design-complete` [R7-Q3]. The PRD's own `status:` does not change while a DCR is open. The PRD lists the DCR under `open_dcrs:`, and the tickets it affects pause until it closes.

## 1.3 Before a PRD exists: the use case gate

A use case moves through `Draft → Ready for review → Under review → Complete` [R7-Q1]:

| Status | Meaning |
|---|---|
| `Draft` | Being written or clarified. |
| `Ready for review` | The driver considers it complete against the criteria below. |
| `Under review` | The extension checker has run and reviewers are commenting. |
| `Complete` | The driver has signed it off. Stories may now be cut from it. |

Stories are only cut from a **complete** use case [R4-Q2]. A use case is complete when:

1. Every field of the Cockburn "fully dressed" format is filled [R1-Q6].
2. Every main-scenario step has been run through the **failure-category checklist**:
   - invalid input
   - not found
   - duplicate
   - no permission
   - conflict or concurrent edit
   - timeout or external system down
   - partial failure
   - quota or limit reached
   - stale data
   - cancel or abandon
   - privacy request
3. Each resulting extension has a handling outcome, or is marked `deferred` or `out-of-scope` [R1-Q7].
4. Stakeholders and their interests are listed.
5. The inputs it draws on (personas, journeys) are cited by ID [R3-A5].

Stories are then cut as **vertical paths** that deliver value on their own, pass INVEST, and fit about one week of slice work [R4-Q3]. Extensions that no story handles yet stay visible in the generated `coverage.md`.

## 1.4 Draft → Exploring

**Entry condition** [R2-Q4]: a story with draft acceptance criteria and the list of use-case extensions it touches. During *Exploring*, the acceptance criteria may still be written in the PRD's source language [R3-C1].

**Who moves it:** a founder picks the PRD **manually and explicitly**. The `priority:` field in the frontmatter informs the choice but does not make it [R6-Q1].

**Limits** [R4-Q6]:
- at most **3 PRDs in *Exploring* per driver**;
- enabler slices that block feature slices go first.

**Inside *Exploring*, anything goes** [R2-Q4]. There are no reviews and no gate checks. The driver may use Claude Design as a sketchpad, but only the real-stack prototype and the markdown artifacts count [R1-Q5, R2-Q1].

## 1.5 Exploring → Design-complete

This is the main design gate. It is passed through the **design PR** from `design/PRD-…` into `main` [R4-Q5′].

### Checklist

| Item | Requirement | Decision |
|---|---|---|
| (a) | Use-case extension coverage is green: every extension the story touches maps to a scenario or is marked `deferred` / `out-of-scope`. | R2-Q3, R1-Q7 |
| (b) | BDD scenarios cover every acceptance criterion, including failure paths. They are English Gherkin and are the only acceptance criteria. | R2-Q3, R3-C1 |
| (c) | A flow map lists every screen and transition, with entry and exit points. | R2-Q3 |
| (d) | A **state matrix** per screen covers empty, loading, error, partial, success, no-permission and stale data. | R2-Q3 |
| (e) | The key information and key actions on each screen are traced to the story. | R2-Q3 |
| (f) | The copy deck is complete in the source language and follows the voice guide. | R2-Q3, R2-Q6 |
| (g) | Only design-system components are used. New components are raised as enabler slices. | R2-Q3 |
| (h) | Accessibility basics: focus order, keyboard use, labels, contrast through tokens. | R2-Q3 |
| (i) | Responsive behaviour is defined. | R2-Q3 |
| (j) | Authorisation per action: who may do what. | R2-Q3 |
| (k) | Privacy data inventory: personal data shown or collected, purpose, retention. It includes the analytics event properties. | R2-Q3, R4-Q4c |
| (l) | A draft API contract that the prototype mocks against, written against the fit analysis. | R2-Q3, R4-Q8a |
| (m) | Technical questions are listed and linked to ADRs. | R2-Q3 |
| (n) | The PM, UX and Eng persona reviews are recorded in `reviews.md`. | R2-Q3 |
| (o) | **Expected outcome and measurement plan:** user benefits with observable signals; numeric targets once `metrics_stage: growth`; events listed in the tracking plan. | R4-Q4a–c |
| (p) | **Fit analysis** (`fit.md`): each endpoint, use case and data entity classed as reuse, extend, change or new. | R4-Q8a |

### Reviews and sign-off

- The **UX review lane's guideline checks** (accessibility, web guidelines, UX rules, copy and voice, state matrix) run on the prototype first. Their reports feed the UX persona [R4-Q7d].
- The **PM, UX and Eng persona reviewer agents** run on the PRD and prototype [R1-Q12].
- **Two humans sign**: the PRD's driver plus one other founder or developer. One person may hold all three roles [R4-Q1]. With two founders, both sign every design gate.
- If the PRD **amends** scenarios of an earlier PRD (`amends:`), that earlier PRD's driver also signs [R4-Q8e′].

### What happens on merge

- The `.feature` files are **frozen**. A wording tweak for testability is allowed; any change in meaning needs a DCR [R3-Q1a].
- The prototype's screens are captured into Figma on a frozen `PRD-… / design-complete` page [R3-Q7].
- A `Proposed` ADR does **not** block this gate. It blocks the next one [R1-Q13].

## 1.6 Design-complete → Dev-ready

[R5-Q1]

| Requirement | Notes |
|---|---|
| Every linked ADR is `Accepted`. | If an ADR's outcome changes the UX, the PRD goes back to *Exploring* through a DCR [R1-Q13]. |
| A TRD exists wherever the standard stack and existing ADRs don't answer the PRD's technical questions. | |
| Every enabler slice this slice depends on is `Done`, or will merge before the tickets that need it. | A missing *measurement* enabler does not block this gate: the slice is built against a fake analytics port [R4-Q4d]. |
| The slice still fits about one week of work. | Otherwise split the story [R4-Q3]. |
| The PRD has no open questions left. | |

**One sign-off:** the developer who will take the slice. No personas.

## 1.7 Dev-ready → In development

The developer creates the `slice/PRD-…` branch and worktree and sets the status [R4-Q5′].

**Limit:** at most **2 slices in development per developer**; each slice may run several agents [R4-Q6].

The first step of the slice is to **refresh the fit analysis** against current `main`. If the code has moved, the tickets change. If the design must change, open a DCR [R4-Q8′].

## 1.8 In development → Done

This gate is passed through the **slice PR** into `main`. There are no personas; PM and UX only do acceptance on staging, which is not a gate [R2-Q5].

| Requirement | Decision |
|---|---|
| All Gherkin scenarios pass: business layer with fakes, and Playwright-BDD on the UI. | R2-Q5, R4-Q8′ |
| Technical tests pass, including integration tests against a real Postgres. | R2-Q5, R4-Q8′ |
| Security and privacy tests pass: authorisation matrix, privacy inventory, relevant OWASP ASVS L1 items, dependency and secret scanning. | R4-Q9 |
| The OpenAPI diff shows no breaking change the PRD doesn't list. | R4-Q8c |
| No review lane (code, security and privacy, UX) has an open **blocking** finding. | R4-Q7a–c |
| The events in the measurement plan are emitted, asserted in tests through the analytics port, and visible on staging. | R4-Q4c |
| Message catalogs exist for every locale; non-source strings may still be `needs-review`. | R2-Q5, R4-Q10 |
| Visual conformance is checked against the design-complete snapshot (Storybook / Chromatic or screenshots). | R2-Q5 |
| No prototype route for this PRD remains. | R4-Q11 |
| A human has reviewed the slice PR. | R2-Q5, R4-Q7′ |

**On merge:** an `as-built` page is captured into Figma [R3-Q7], and the PRD's `outcome_review_due:` is set [R4-Q4e].

## 1.9 After Done

- **Production release of translations** [R4-Q10]: every string in a locale enabled for production must be reviewed by a native speaker. A locale can be switched off in production until its review is complete. Staging has no such rule.
- **Outcome review** [R4-Q4e]: on `outcome_review_due`, the driver fills in the PRD's *Outcome review* section: `met`, `missed` or `inconclusive`, the numbers, and the follow-up (a new story, a DCR on a later PRD, or nothing). Any measurement enabler must be `Done` by then [R4-Q4d]. The generated index lists overdue reviews.

## 1.10 Changing something after a gate

| Situation | What happens | Decision |
|---|---|---|
| A UX change to a PRD that is `Design-complete`, `Dev-ready` or `In development`, found at any time | A **design change request** (`DCR-…`). Only the change goes back through *Exploring*, and the persona review covers only that change. The PRD keeps its status; the affected tickets pause until the DCR is `Design-complete`. | R2-Q4, R7-Q3 |
| A UX finding from the review lanes during the slice | Not fixed silently: it opens a DCR. | R4-Q7c |
| A purely technical change | Stays in development. No DCR. | R2-Q4 |
| A new PRD contradicts a `Done` PRD | The earlier PRD is **not** reopened. The new PRD lists the scenarios it changes (`amends:`), its design PR edits the older `.feature` files, and the earlier PRD gains `amended_by:`. | R4-Q8e′ |
| A new PRD contradicts a PRD that is `Dev-ready` or `In development` | Not allowed directly. The change goes to that PRD as a DCR; the new PRD waits or drops the conflicting scenario. | R4-Q8e′ |
| Two PRDs in `Exploring` overlap | The two drivers settle it before either reaches Design-complete. | R4-Q8e′ |
| A bug: the code doesn't match an existing scenario | A `fix/` branch: fix it, add a regression test tagged with the scenario. No PRD. | R5-Q2 |
| Review lanes on any `fix/` PR | The code and security lanes always run; the UX lane runs when the diff touches the web app or the UI package. | R7-Q4 |
| A bug: a case is missing from the specs, the intended behaviour is clear and nothing visible changes | The fix PR adds the scenario to the `Done` PRD's `.feature` file; that PRD gains `amended_by: fix/…`; the other founder signs. | R5-Q2 |
| A bug whose fix would change the UX | A new story, through the full lifecycle. | R5-Q2 |

The current truth about behaviour is always the `.feature` files and use cases on `main`, with the generated `coverage.md`. PRDs record decisions; they are not living documents after `Done` [R4-Q8e′].

## 1.11 Enforcement

A **gate check** runs on every PR that changes a `status:` field, both as one of our own skills and as a CI job [R4-Q12]. It checks:

- the frontmatter;
- that the files the target status requires exist;
- that the generated coverage has no gaps;
- the sign-offs in `reviews.md`;
- the status of linked ADRs;
- for `Done`: that no review lane has an open blocking finding.

A failed check blocks the status change. The checks that a script can do mechanically are done by a script, so that CI needs no agent for them; the agent judges only what the script cannot ([chapter 12](12-skills-to-build.md), R5-Q4′).

## 1.12 Summary of sign-offs

| Gate | Agents | Human sign-off |
|---|---|---|
| Use case → Complete | Use-case writer and extension checker | The use case's driver |
| Draft → Exploring | None | A founder picks it |
| Exploring → Design-complete | UX lane guideline checks; PM, UX and Eng personas | Two people: the driver plus one other (plus earlier drivers for amendments) |
| Design-complete → Dev-ready | Gate check | The developer taking the slice |
| DCR → Design-complete | Personas, on the change only | Two people, as for the design gate |
| In development → Done | Code, security and privacy, and UX review lanes; gate check | A human review of the slice PR |
| Bug fix that adds a scenario | Code and security lanes, plus UX if the UI is touched | The other founder |
