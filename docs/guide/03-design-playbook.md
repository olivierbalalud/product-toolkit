# 3. Design Playbook

How to take a use case from a rough idea to a PRD that passes the Design-complete gate. This chapter is the how-to; the rules each step must meet (statuses, gate criteria, limits, sign-offs) are in [chapter 1](01-lifecycle-and-gates.md) and are linked rather than repeated [R28-Q14]. The files are in [chapter 2](02-artifacts-and-ids.md) and the [templates](../templates/). Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md).

Skills are named by their role here. Their exact names, sources and pins are in [chapter 11](11-tooling-and-plugins.md) (third-party) and [chapter 12](12-skills-to-build.md) (ours).

## 3.1 Principles

1. **Three layers, kept apart** [R1-Q4]:
   - **Flow**, per PRD: screens, transitions, key information and key actions.
   - **Look**, global: tokens, design-system components and motion presets. A PRD never designs the look; it only uses it.
   - **Voice**, global guide plus a per-PRD copy deck.
2. **Code is the source of truth for the look** [R1-Q3]. Figma is a synced consumer for review and annotation [R2-Q1].
3. **Prototypes are built in the real stack**: Next.js and shadcn components from the design system, with mocked data [R1-Q5]. Anything sketched elsewhere is exploration only.
4. **Readable copy from the first screen**: a button says "Next step" or "Étape suivante", never a key like `screen1.panel2.next.label` [R1-Q4].
5. **Edge cases come from the use case, not the story**: extensions found by the failure categories, each with a concrete example, then covered by scenarios [R1-Q7, R4-Q2, R28-Q3].
6. **Inside *Exploring*, anything goes**. Reviews happen at the gate, not during iteration [R2-Q4].
7. **Only what the story touches**: a story without a screen has no flows or copy deck; a story without an API change has no draft contract [R28-Q5].

## 3.2 Step 1: Complete the use case

**Who:** the use case's driver, with Claude Code. **What it must meet:** [chapter 1, §1.3](01-lifecycle-and-gates.md#13-before-a-prd-exists-the-use-case-gate).

1. Pick a use case from `docs/product/index.md`. Create the branch `uc/UC-012-<slug>`; set `status: Draft` and `driver:` [R28-Q20].
2. Check the **goal level** with the coffee-break test: one actor, one sitting, goal reached. Turn a summary goal into a short map of user-goal use cases, and a subfunction into a step of the use case that needs it ([goal levels](../foundations/pm-lens.md#22-goal-levels)) [R28-Q1].
3. Gather the inputs it draws on (personas, journeys, pain points) from `docs/product/inputs/` and cite them by ID [R3-A5]. Existing material is imported as input, not rewritten.
4. With the **use-case writer** skill, fill in the fields from [`use-case.md`](../templates/use-case.md). Write steps as intent ("the employee chooses a room"), never as screens or clicks, and mark each `(actor)` or `(system)` [R28-Q6, R28-Q7].
5. Run each step through the failure categories of its kind, and answer the privacy-request line once. Every "yes" becomes an extension `UC-012.<step><letter>` with a handling outcome and a one-line **example** ("Ana books room 3 for 10:00, but Ben booked it a second earlier"), or is marked `deferred` or `out-of-scope` with a reason [R4-Q2, R28-Q3]. An extension you can't give an example for isn't clear yet.
6. Check domain words against `docs/product/glossary.md`. Add new terms in both languages.
7. Open the PR. Reviewers comment on it, the gate check runs, and the driver sets `status: Complete` [R28-Q11]. Stories may be cut in the same PR (step 2).

Interview-style skills such as `grill-with-docs` and `domain-modeling` help when the use case is still vague [R3-B1]. To insert or remove steps later, use `write-use-case renumber`, never hand edits ([chapter 2, §2.1](02-artifacts-and-ids.md#21-id-rules)) [R28-Q19′].

## 3.3 Step 2: Cut stories

**Who:** the use case's driver.

### What a user story is

A user story is a short statement of a need, written from the user's side. It comes from Extreme Programming (Kent Beck, late 1990s) and is described at length in Mike Cohn's *User Stories Applied* (2004). The usual sentence form is the **Connextra template** (Connextra, 2001; usually credited to Rachel Davies), which has three parts:

| Part | Says | Example |
|---|---|---|
| **As a** <role> | who needs it | As an employee |
| **I want** <capability> | what they want to do | I want to book a free meeting room |
| **so that** <benefit> | why: the value they get | so that my team has a place to meet without double bookings |

Ron Jeffries' **three Cs** (2001) explain what a story is for: the **Card** (the short statement), the **Conversation** that works out the details, and the **Confirmation** that shows it is done. In this framework the card is the story statement at the top of the PRD (§2), the conversation is *Exploring*, and the confirmation is the Gherkin scenarios [R3-C1]. A story here is also always a **path through a use case**, never a free-standing wish [R4-Q3].

### Cutting stories

1. With the **story writer**, cut the use case into **vertical paths** by value, not by step ranges [R4-Q3, R28-Q8]:
   - the **first story** is the thinnest path through the *whole* main scenario, with the simplest variation and only the extensions it can't ship without;
   - each **later story** adds extensions, or one item from the use case's "Technology and data variations" (for example, weekly recurring bookings).
2. Check each story against **INVEST** (Bill Wake, 2003), read for this framework as follows. Split any story that would take more than about one week of slice work.

   | Letter | Criterion | What it means here |
   |---|---|---|
   | **I** | Independent | It can be designed, built and shipped without waiting for another story, except the first story of its use case, which every later one builds on [R28-Q8]. Shared work it needs is an enabler slice, not another story. |
   | **N** | Negotiable | It states the user's need, not a fixed solution; flows and screens are worked out in *Exploring*. |
   | **V** | Valuable | It delivers a benefit the user notices on its own, traced to PRD §3a. A technical layer alone is not a story. |
   | **E** | Estimable | The team can size it. If not, it lacks information (a fit analysis, a spike, an ADR) or is too big. |
   | **S** | Small | About one week of slice work at most [R4-Q3]. |
   | **T** | Testable | Its acceptance can be written as Gherkin scenarios that pass or fail. |
3. Each story becomes a folder `stories/US-012.1-<slug>/` with a `prd.md` started from [`story.md`](../templates/story.md), at `status: Draft` [R9-Q1]. It lists the extensions it handles in `extensions:` (several stories may claim the same one) and what it changes in `touches:`: `ui` for a screen, `api` for an endpoint or stored data, or both [R28-Q4, R28-Q5, R28-Q9]. It has no acceptance criteria yet.
4. Regenerate `coverage.md`. Extensions no story claims yet stay visible there until a story claims them [R4-Q3].

## 3.4 Step 3: Start exploring

**Who:** a founder picks the PRD explicitly [R6-Q1]; the PRD's driver then starts it. **Entry condition and limits:** [chapter 1, §1.4](01-lifecycle-and-gates.md#14-draft--exploring).

Choose the design tool for this PRD, Figma or Claude Design (only when `touches` includes `ui`; it stays fixed for the whole exploration [R18-Q4]), then run one command [R28-Q17]:

```bash
make design PRD=PRD-012.1 SLUG=book-room TOOL=claude-design
```

It:

1. counts the driver's open `design/PRD-…` branches and refuses to start a fourth [R4-Q6, R28-Q12];
2. creates the branch `design/PRD-012.1-book-room` from `origin/main` (or opens it if it exists) in the worktree `.claude/worktrees/design-PRD-012.1-book-room`, with a **frontend-only** environment on its own port, running against mocks [R2-Q9, R4-Q5′, R16-Q0];
3. writes `design_tool:` and `status: Exploring` into the PRD;
4. warns when the tool's copy of the design system is older than the last design-system change, from `docs/design/design-system.md` ([chapter 6](06-design-system-and-figma.md)) [R18-Q3];
5. commits `docs(PRD-012.1): start exploring` and launches `claude --worktree design-PRD-012.1-book-room`.

`TOOL` is needed only the first time. Switching tools means restarting the exploration in the other tool from the current prototype routes [R18-Q4].

## 3.5 Step 4: Explore

This is the loop *Exploring* exists for. Nothing is reviewed yet, and no change needs a DCR [R2-Q4, R18-Q7]. There is no fixed order: work on whatever is least clear, and repeat until the driver is satisfied [R28-Q13].

### What the gate needs

The Design-complete checklist is in [chapter 1, §1.5](01-lifecycle-and-gates.md#15-exploring--design-complete). Scaled by `touches:`, *Exploring* produces:

| Output | When | Section below |
|---|---|---|
| Flow map, screens, state matrix (`flows.md`) | `ui` | [Flows and screens](#flows-and-screens) |
| Prototype in the real stack | `ui` | [Prototype](#prototype) |
| Copy deck (`copy.md`) | `ui` | [Copy](#copy) |
| Gherkin scenarios (`features/`) | always | [Scenarios](#scenarios) |
| Fit analysis (`fit.md`) and draft contract (`contract.draft.yaml`) | always; the contract with `api` | [Fit with what exists](#fit-with-what-exists) |
| Outcome and measurement plan (PRD §3–§4) | always | [Outcome and measurement](#outcome-and-measurement) |
| Who may do what, privacy, AI use, accessibility (PRD §10–§13) | always; §13 with `ui` | [Who, what data, and for whom](#who-what-data-and-for-whom) |

A usual order for a UI story: flows → prototype and copy → scenarios → fit and contract → outcome → who and what data. A story without UI usually starts from the scenarios. If `touches:` turns out wrong, change it; it is free until Design-complete [R28-Q18].

### Start from what is built

If the PRD changes screens that already exist, start from **what is built**: the running app on `main` and its `as-built` page in Figma. Never start from an earlier PRD's files in either tool, which may be out of date [R18-Q1]. In Claude Design, recreate the current screen from screenshots of the running app, using the synced design system; Claude Design can't open Figma frames as editable screens. In Figma, duplicate the `as-built` page.

### Flows and screens

- Draw the flow map and list the screens in [`flows.md`](../templates/flows.md): purpose, key information, key actions, each traced to the story [R2-Q3 (c, e)].
- Name interactions by **intent** from `docs/design/motion.md` ("confirm success", "reveal details"), never by animation [R3-Q6′].
- Fill the **state matrix** for every screen: empty, loading, error, partial, success, no permission, stale data [R2-Q3 (d)].

### Prototype

- Build the screens under `src/apps/web/app/(prototypes)/`, which is excluded from production builds [R3-Q1g].
- **Use only design-system components** [R2-Q3 (g)]. If a needed component doesn't exist, raise an enabler slice with `adds_ds_component: true`; it goes through its own design review [R7-Q2]. Third-party blocks enter the design system only through an enabler slice [R3-Q5′].
- Mock the data with MSW against the draft API contract, or against the existing API when the story doesn't change it [R2-Q9, R3-Q1g].
- Prototype code needs no tests, but it must pass lint: tokens only, motion presets only, i18n keys only [R4-Q11].
- Skills that help here: `frontend-design`, `shadcn`, `ui-ux-pro-max`, the Next.js skills [R3-B1].

### Copy

- Write every visible string in [`copy.md`](../templates/copy.md) in the PRD's source language, following `docs/design/voice-and-tone.md` [R2-Q7]. An agent derives the semantic keys (`<feature>.<screen>.<element>`) and writes them to the feature's message catalog [R2-Q6].
- The prototype reads strings through next-intl from the start, so screens show readable copy and keys exist from the first prototype [R1-Q11, R3-Q4].

### In the design tool

Both tools are working material; the record is the prototype in code and the markdown artifacts [R18-Q1, R18-Q2].

| | Figma (`design_tool: figma`) | Claude Design (`design_tool: claude-design`) |
|---|---|---|
| Design system | The Figma library: Obra kit, variables, Code Connect | The design system synced from the repo with `/design-sync` |
| Explore | Mockups built from library components | Prototypes built from the synced components, with chat beside the canvas |
| Into code | The Figma MCP with Code Connect emits our real components into the prototype routes | The "handoff to Claude Code" bundle (designs, chat, README) is re-implemented in the prototype routes |
| Keep | Nothing extra: Figma keeps history | The final export (standalone HTML or the handoff bundle) in `design-export/`, merged with the design PR, because Claude Design has no version history [R18-Q6] |

Rules for both:

- **Never change the look in the tool.** Tokens and components change only through an enabler slice [R18-Q3, R2-Q9].
- **Re-implement in code before the gate.** The gate artefact is always the real-stack prototype, so the lanes, the usability test, Chromatic and the mocks work the same whichever tool was used [R18-Q2].
- **Annotation and visual review** happen in Figma for every PRD: push prototype screens there with code-to-canvas when a visual review helps. The canonical captures happen at the gates [R3-Q7, R18-Q5].

### Scenarios

1. With **`write-scenarios`**, write the story's scenarios in **English Gherkin** in `features/`, using [`feature.feature`](../templates/feature.feature), whatever the PRD's source language [R3-Q1a, R3-C1].
2. Name the **rules** first: each a plain-English sentence such as "A room can't be booked twice for overlapping times", written as a Gherkin `Rule:`. Under each rule, write its scenarios, starting from the examples of the extensions the story claims [R28-A, R28-Q16].
3. Cover the story's main-scenario steps and every extension it claims, including failure paths [R2-Q3 (a, b)].
4. Tag each scenario with the story and the use-case step or extension: `@US-012.1 @UC-012.3a` [R3-Q1a]. Add `@ui` to scenarios that show a screen, at least one per screen in `flows.md` [R14-Q2].
5. Use the glossary's **English** terms for domain words [R3-C3]. Describe what the user sees in domain words ("I am told the room is no longer free"), never by copy key; the `@ui` step definitions map the wording to keys [R28-Q10].
6. Reuse the wording of existing step definitions where it fits, so existing steps bind [R4-Q8b′].
7. Regenerate `coverage.md` and check that the story's extensions are covered.

The `.feature` files are the only acceptance criteria. The PRD links to them instead of restating them [R3-C1].

### Fit with what exists

**Who:** the **fit-check** skill, reviewed by the SWE persona at the gate [R4-Q8a].

The fit analysis ([`fit.md`](../templates/fit.md)) uses four keys, strongest first [R4-Q8b′]:

| Key | What the agent does | Needs a running service? |
|---|---|---|
| 1. Existing specs | Compares each new scenario with the `.feature` files on `main`: duplicate, refines, contradicts or independent. Checks open `design/` branches for overlap, as warnings. | No |
| 2. API | Only with `touches: api` [R28-Q5]. Diffs the draft contract against the OpenAPI the FastAPI app generates, e.g. with `oasdiff`. | No: the spec can be generated from the app object (inferred) |
| 3. Behaviour | Binds the new scenarios to the existing business layer with fakes and runs them. Green = exists, red = gap. | No: fakes stand in for adapters |
| 4. Code | Searches glossary terms in the domain folders, and artifact tags in tests. | No |

Then:

- With `touches: api`, write the **draft API contract** (`contract.draft.yaml`) against the analysis, and point the mocks at it [R2-Q3 (l), R4-Q8a].
- Resolve each misalignment by the rules of R4-Q8c: for anything the user sees, the PRD wins unless other features depend on the old behaviour; then a backward-compatible extension, a breaking change that lists every consumer, or a DCR. An architecture choice becomes an ADR.
- If a new scenario **contradicts** an earlier PRD's scenario, follow [chapter 1, §1.10](01-lifecycle-and-gates.md#110-changing-something-after-a-gate) [R4-Q8e′].
- List technical questions in PRD §14 and open a `Proposed` ADR for each architecture gap [R1-Q13]. A proposed ADR does not block this gate.

### Outcome and measurement

1. Write **§3a user benefits**, each with an observable signal [R4-Q4a]. The **"so that" part of the user story** (its benefit, see [§3.3](#what-a-user-story-is)) must trace to one of these benefits: a story whose benefit is not in §3a has no measurable reason to exist.
2. If `docs/product/settings.yaml` says `metrics_stage: growth`, write **§3b success metrics** with baseline, target and window, referencing `MET-` IDs from the metric catalogue [R4-Q4b, R8-Q3].
3. Write the **§4 measurement plan**: each event goes in `docs/product/tracking-plan.md` with an `EVT-` ID, a snake_case name, and a privacy class per property (`none`, `pseudonymous`, `personal`), and whether it needs consent (`consent: exempt | required`; `exempt` only if it meets every CNIL audience-measurement condition, see the [GDPR one-pager](../foundations/gdpr-one-pager.md)) [R4-Q4c, R8-Q4, R9-Q2, R21-Q1].
4. If a metric needs a pipeline, dashboard or BI model that doesn't exist, raise an enabler slice. It doesn't block Dev-ready, but must be done before the outcome review [R4-Q4d].

### Who, what data, and for whom

- **§10 Who may perform each action:** a role × action table. It becomes the authorisation test matrix [R2-Q3 (j), R4-Q9].
- **§11 Privacy data inventory:** every personal data item shown, collected, logged or sent to analytics, with purpose, legal basis and retention [R2-Q3 (k)].
- **§11b AI use**, when the PRD uses an AI model: model and provider, data sent, human oversight, the transparency notice, the AI Act risk category [R12-Q6a].
- **§13 Accessibility and responsive**, with `touches: ui`: focus order, keyboard use, labels, contrast through tokens, breakpoints [R2-Q3 (h, i)].

## 3.6 Step 5: Prepare the gate

1. With `touches: ui`, run the **UX lane's guideline checks** on the prototype: accessibility, web guidelines, UX rules, copy and voice, state matrix. Link their reports in `reviews.md` and fix the blocking findings [R4-Q7d].
2. Run the **persona reviewers** (PM, UX, Eng) on the PRD and prototype. Record findings and resolutions in `reviews.md` [R1-Q12]. The Eng review includes a STRIDE-style threat check when the PRD adds an endpoint, a data store or a third party, covering prompt injection when user or third-party content reaches an LLM [R11-Q12, R12-Q6c].
3. **Strongly recommended** for a new flow: test the prototype with 3–5 real users and record the findings in `reviews.md`. It is not mandatory; the gate check only warns [R11-Q10].
4. Run the **gate check** locally to catch missing files or fields before opening the PR [R4-Q12].
5. Empty §15 Open questions as far as possible. Anything left must be gone by Dev-ready [R5-Q1].

## 3.7 Step 6: Pass Design-complete

1. Set `status: Design-complete` and open the **design PR** from `design/PRD-…` into `main` [R4-Q5′]. CI runs the gate check on the status change [R4-Q12].
2. Collect the sign-offs in `reviews.md` ([chapter 1, §1.5](01-lifecycle-and-gates.md#reviews-and-sign-off)).
3. Merge. What freezes and what is captured is listed in [chapter 1, §1.5](01-lifecycle-and-gates.md#what-happens-on-merge). The design worktree can then be removed.

## 3.8 From Design-complete to Dev-ready

- Drive each linked ADR to `accepted`. If an ADR's outcome changes the UX, raise a DCR [R1-Q13].
- Write a TRD where the stack and ADRs don't answer §14 [R5-Q1].
- Make sure every enabler slice the PRD depends on is done or will merge first.
- The developer who will take the slice signs Dev-ready ([chapter 1, §1.6](01-lifecycle-and-gates.md#16-design-complete--dev-ready)). Development is in [chapter 4](04-dev-playbook.md).

## 3.9 Changing a design after the gate

Any UX change to a PRD that is past Design-complete, from any source, is a **design change request** [R2-Q4]; the rules are in [chapter 1, §1.10](01-lifecycle-and-gates.md#110-changing-something-after-a-gate). To work one:

1. Create `dcr/DCR-012.1-01-<slug>.md` from [`dcr.md`](../templates/dcr.md) and add it to the PRD's `open_dcrs:`. The PRD keeps its status [R7-Q3].
2. List the tickets that must pause until the DCR closes.
3. Work the change in its own branch and worktree, `design/DCR-012.1-01-<slug>` and `design-DCR-012.1-01-<slug>`, as in steps 4 and 5 but for the change only. Commits use the DCR as scope, e.g. `docs(DCR-012.1-01): update copy deck` [R10-Q1].
4. The personas review the change only; two people sign [R2-Q4, R4-Q1]. Set the DCR to `Design-complete`, remove it from `open_dcrs:`, and the paused tickets resume.

To "go back" to Figma, duplicate the PRD's `as-built` page and annotate the duplicate. The annotation is input to a DCR; nothing is merged back automatically [R3-Q7]. A DCR is explored in the PRD's own `design_tool` [R18-Q4]; in Claude Design, start from screenshots of the as-built screens [R18-Q1].

## 3.10 Designing in parallel

- Each PRD has its own folder and worktree, so parallel PRDs don't touch the same files [R3-Q1c].
- Shared layers (tokens, `globals.css`, design-system components, OpenAPI, migrations) change only in their own enabler slice, one at a time [R2-Q9].
- The fit analysis warns when two PRDs in *Exploring* overlap; their drivers settle it before either reaches the gate [R4-Q8e′].
- Worktrees, start scripts and environments are covered in [chapter 5](05-worktrees-and-parallelism.md).
