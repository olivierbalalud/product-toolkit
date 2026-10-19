# 3. Design Playbook

How to take a use case from a rough idea to a PRD that passes the Design-complete gate. The gates themselves are in [chapter 1](01-lifecycle-and-gates.md), the files in [chapter 2](02-artifacts-and-ids.md) and the [templates](../templates/). Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md).

Skills are named by their role here. Their exact names, sources and pins are in [chapter 11](11-tooling-and-plugins.md) (third-party) and [chapter 12](12-skills-to-build.md) (ours).

## 3.1 Principles

1. **Three layers, kept apart** [R1-Q4]:
   - **Flow**, per PRD: screens, transitions, key information and key actions.
   - **Look**, global: tokens, design-system components and motion presets. A PRD never designs the look; it only uses it.
   - **Voice**, global guide plus a per-PRD copy deck.
2. **Code is the source of truth for the look** [R1-Q3]. Figma is a synced consumer for review and annotation [R2-Q1].
3. **Prototypes are built in the real stack**: Next.js and shadcn components from the design system, with mocked data [R1-Q5]. Anything sketched elsewhere is exploration only.
4. **Readable copy from the first screen**: a button says "Next step" or "Étape suivante", never a key like `screen1.panel2.next.label` [R1-Q4].
5. **Edge cases come from the use case, not the story**: extensions found by the failure-category check, then covered by scenarios [R1-Q7, R4-Q2].
6. **Inside *Exploring*, anything goes**. Reviews happen at the gate, not during iteration [R2-Q4].

## 3.2 Step 1: Complete the use case

**Who:** the use case's driver, with Claude Code.

1. Pick a use case from `docs/product/index.md`. Set `status: Draft` and `driver:`.
2. Gather the inputs it draws on (personas, journeys, pain points) from `docs/product/inputs/` and cite them by ID [R3-A5]. Existing material is imported as input, not rewritten.
3. With the **use-case writer** skill, fill in the Cockburn "fully dressed" fields from [`use-case.md`](../templates/use-case.md) [R1-Q6].
4. Run every main-scenario step through the **failure-category grid**. Every "yes" becomes an extension `UC-012.<step><letter>` with a handling outcome, or is marked `deferred` or `out-of-scope` with a reason [R4-Q2].
5. Check domain words against `docs/product/glossary.md`. Add new terms in both languages.
6. Set `status: Ready for review`. The **extension checker** runs and reviewers comment (`Under review`). The driver signs it off as `Complete` [R7-Q1].

Interview-style skills such as `grill-with-docs` and `domain-modeling` help when the use case is still vague [R3-B1].

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

1. With the **story writer**, cut the use case into **vertical paths**: the main scenario or a coherent part of it, plus the extensions that path must handle [R4-Q3].
2. Check each story against **INVEST** (Bill Wake, 2003), read for this framework as follows. Split any story that would take more than about one week of slice work.

   | Letter | Criterion | What it means here |
   |---|---|---|
   | **I** | Independent | It can be designed, built and shipped without waiting for another story. Shared work it needs is an enabler slice, not another story. |
   | **N** | Negotiable | It states the user's need, not a fixed solution; flows and screens are worked out in *Exploring*. |
   | **V** | Valuable | It delivers a benefit the user notices on its own, traced to PRD §3a. A technical layer alone is not a story. |
   | **E** | Estimable | The team can size it. If not, it lacks information (a fit analysis, a spike, an ADR) or is too big. |
   | **S** | Small | About one week of slice work at most [R4-Q3]. |
   | **T** | Testable | Its acceptance can be written as Gherkin scenarios that pass or fail. |
3. Each story becomes a folder `stories/US-012.1-<slug>/` with a `prd.md` started from [`story.md`](../templates/story.md), at `status: Draft` [R9-Q1].
4. Regenerate `coverage.md`. Extensions no story handles yet stay visible there until a story claims them [R4-Q3].

## 3.4 Step 3: Start exploring

**Who:** a founder picks the PRD explicitly [R6-Q1]; the PRD's driver then works on it.

1. Check the work-in-progress limit: at most **3 PRDs in *Exploring* per driver** [R4-Q6].
2. Create the design worktree and branch:

   ```bash
   make design PRD=PRD-012.1 SLUG=book-room
   ```

   The script creates the branch `design/PRD-012.1-book-room` from `origin/main` (or opens it if it exists) in the worktree `.claude/worktrees/design-PRD-012.1-book-room`, sets up a **frontend-only** environment on its own port, running against mocks, and then launches `claude --worktree design-PRD-012.1-book-room`, which reopens that folder [R2-Q9, R4-Q5′, R16-Q0].
3. **Choose the design tool** for this PRD, Figma or Claude Design, and record it as `design_tool:` in the PRD frontmatter. It stays fixed for the whole exploration, so mockups and code stay aligned in style. Switching means restarting the exploration in the other tool from the current prototype routes [R18-Q4].
4. Check that the tool's copy of the design system is in sync with code: `docs/design/design-system.md` records the commit each copy was last synced from ([chapter 6](06-design-system-and-figma.md)) [R18-Q3].
5. Set `status: Exploring` and commit with the PRD as scope: `docs(PRD-012.1): start exploring`.

## 3.5 Step 4: Iterate on flows, screens and copy

This is the loop that *Exploring* exists for. Repeat until the driver is satisfied; nothing here is reviewed yet, and no change needs a DCR [R2-Q4, R18-Q7].

### Start from what is built

If the PRD changes screens that already exist, start from **what is built**: the running app on `main` and its `as-built` page in Figma. Never start from an earlier PRD's files in either tool, which may be out of date [R18-Q1]. In Claude Design, recreate the current screen from screenshots of the running app, using the synced design system; Claude Design can't open Figma frames as editable screens. In Figma, duplicate the `as-built` page.

### Flow

- Draw the flow map and list the screens in [`flows.md`](../templates/flows.md): purpose, key information, key actions, each traced to the story [R2-Q3 (c, e)].
- Name interactions by **intent** from `docs/design/motion.md` ("confirm success", "reveal details"), never by animation [R3-Q6′].
- Fill the **state matrix** for every screen: empty, loading, error, partial, success, no permission, stale data [R2-Q3 (d)].

### Prototype

- Build the screens under `src/apps/web/app/(prototypes)/`, which is excluded from production builds [R3-Q1g].
- **Use only design-system components** [R2-Q3 (g)]. If a needed component doesn't exist, raise an enabler slice with `adds_ds_component: true`; it goes through its own design review [R7-Q2]. Third-party blocks enter the design system only through an enabler slice [R3-Q5′].
- Mock the data with MSW against the draft API contract [R2-Q9, R3-Q1g].
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

## 3.6 Step 5: Write the scenarios

1. Turn the draft acceptance criteria into **English Gherkin** in `features/`, using [`feature.feature`](../templates/feature.feature), whatever the PRD's source language [R3-Q1a, R3-C1].
2. Cover every acceptance criterion and every extension the story handles, including failure paths [R2-Q3 (a, b)].
3. Tag each scenario with the story and the use-case step or extension: `@US-012.1 @UC-012.3a` [R3-Q1a].
4. Use the glossary's **English** terms for domain words [R3-C3]. Refer to UI text by **copy key**, and only where the wording matters [R3-C2].
5. Reuse the wording of existing step definitions where it fits, so existing steps bind [R4-Q8b′].
6. Regenerate `coverage.md` and check that the story's extensions are covered.

The `.feature` files are the only acceptance criteria. The PRD links to them instead of restating them [R3-C1].

## 3.7 Step 6: Analyse the fit with what exists

**Who:** the **fit-check** skill, reviewed by the SWE persona at the gate [R4-Q8a].

The fit analysis ([`fit.md`](../templates/fit.md)) uses four keys, strongest first [R4-Q8b′]:

| Key | What the agent does | Needs a running service? |
|---|---|---|
| 1. Existing specs | Compares each new scenario with the `.feature` files on `main`: duplicate, refines, contradicts or independent. Checks open `design/` branches for overlap, as warnings. | No |
| 2. API | Diffs the draft contract against the OpenAPI the FastAPI app generates, e.g. with `oasdiff`. | No: the spec can be generated from the app object (inferred) |
| 3. Behaviour | Binds the new scenarios to the existing business layer with fakes and runs them. Green = exists, red = gap. | No: fakes stand in for adapters |
| 4. Code | Searches glossary terms in the domain folders, and artifact tags in tests. | No |

Then:

- Write the **draft API contract** (`contract.draft.yaml`) against the analysis, and point the mocks at it [R2-Q3 (l), R4-Q8a].
- Resolve each misalignment by the rules of R4-Q8c: for anything the user sees, the PRD wins unless other features depend on the old behaviour; then a backward-compatible extension, a breaking change that lists every consumer, or a DCR. An architecture choice becomes an ADR.
- If a new scenario **contradicts** an earlier PRD's scenario, follow R4-Q8e′: amend a `Done` PRD through `amends:` and edit its `.feature` file in this design PR; raise a DCR on a PRD that isn't built yet; settle overlaps with PRDs in *Exploring* directly with their driver.
- List technical questions in PRD §14 and open a `Proposed` ADR for each architecture gap [R1-Q13]. A proposed ADR does not block this gate.

## 3.8 Step 7: Define the outcome and how to measure it

1. Write **§3a user benefits**, each with an observable signal [R4-Q4a]. The **"so that" part of the user story** (its benefit, see [§3.3](#what-a-user-story-is)) must trace to one of these benefits: a story whose benefit is not in §3a has no measurable reason to exist.
2. If `docs/product/settings.yaml` says `metrics_stage: growth`, write **§3b success metrics** with baseline, target and window, referencing `MET-` IDs from the metric catalogue [R4-Q4b, R8-Q3].
3. Write the **§4 measurement plan**: each event goes in `docs/product/tracking-plan.md` with an `EVT-` ID, a snake_case name, and a privacy class per property (`none`, `pseudonymous`, `personal`) [R4-Q4c, R8-Q4, R9-Q2].
4. If a metric needs a pipeline, dashboard or BI model that doesn't exist, raise an enabler slice. It doesn't block Dev-ready, but must be done before the outcome review [R4-Q4d].

## 3.9 Step 8: Who, what data, and for whom

- **§10 Who may perform each action:** a role × action table. It becomes the authorisation test matrix [R2-Q3 (j), R4-Q9].
- **§11 Privacy data inventory:** every personal data item shown, collected, logged or sent to analytics, with purpose, legal basis and retention [R2-Q3 (k)].
- **§11b AI use**, when the PRD uses an AI model: model and provider, data sent, human oversight, the transparency notice, the AI Act risk category [R12-Q6a].
- **§13 Accessibility and responsive:** focus order, keyboard use, labels, contrast through tokens, breakpoints [R2-Q3 (h, i)].

## 3.10 Step 9: Prepare the gate

1. Run the **UX lane's guideline checks** on the prototype: accessibility, web guidelines, UX rules, copy and voice, state matrix. Link their reports in `reviews.md` and fix the blocking findings [R4-Q7d].
2. Run the **persona reviewers** (PM, UX, Eng) on the PRD and prototype. Record findings and resolutions in `reviews.md` [R1-Q12]. The Eng review includes a STRIDE-style threat check when the PRD adds an endpoint, a data store or a third party, covering prompt injection when user or third-party content reaches an LLM [R11-Q12, R12-Q6c].
3. **Strongly recommended** for a new flow: test the prototype with 3–5 real users and record the findings in `reviews.md`. It is not mandatory; the gate check only warns [R11-Q10].
4. Run the **gate check** locally to catch missing files or fields before opening the PR [R4-Q12].
5. Empty §15 Open questions as far as possible. Anything left must be gone by Dev-ready [R5-Q1].

## 3.11 Step 10: Pass Design-complete

1. Set `status: Design-complete` and open the **design PR** from `design/PRD-…` into `main` [R4-Q5′].
2. CI runs the gate check on the status change [R4-Q12].
3. **Two people sign** in `reviews.md`: the driver plus one other. Add the earlier PRD's driver if the PRD amends its scenarios [R4-Q1, R4-Q8e′].
4. Merge. From now on:
   - the `.feature` files are frozen [R3-Q1a];
   - the prototype's screens are captured into Figma on a frozen `PRD-012.1 / design-complete` page [R3-Q7];
   - the design worktree can be removed.

## 3.12 From Design-complete to Dev-ready

- Drive each linked ADR to `accepted`. If an ADR's outcome changes the UX, raise a DCR [R1-Q13].
- Write a TRD where the stack and ADRs don't answer §14 [R5-Q1].
- Make sure every enabler slice the PRD depends on is done or will merge first.
- The developer who will take the slice signs Dev-ready [R5-Q1]. Development is in [chapter 4](04-dev-playbook.md).

## 3.13 Changing a design after the gate

Any UX change to a PRD that is past Design-complete, from any source, is a **design change request** [R2-Q4]:

1. Create `dcr/DCR-012.1-01-<slug>.md` from [`dcr.md`](../templates/dcr.md) and add it to the PRD's `open_dcrs:`. The PRD keeps its status [R7-Q3].
2. List the tickets that must pause until the DCR closes.
3. Work the change in its own branch and worktree, `design/DCR-012.1-01-<slug>` and `design-DCR-012.1-01-<slug>`, as in steps 4–9 but for the change only. Commits use the DCR as scope, e.g. `docs(DCR-012.1-01): update copy deck` [R10-Q1].
4. The personas review the change only; two people sign [R2-Q4, R4-Q1]. Set the DCR to `Design-complete`, remove it from `open_dcrs:`, and the paused tickets resume.

To "go back" to Figma, duplicate the PRD's `as-built` page and annotate the duplicate. The annotation is input to a DCR; nothing is merged back automatically [R3-Q7]. A DCR is explored in the PRD's own `design_tool` [R18-Q4]; in Claude Design, start from screenshots of the as-built screens [R18-Q1].

## 3.14 Designing in parallel

- Each PRD has its own folder and worktree, so parallel PRDs don't touch the same files [R3-Q1c].
- Shared layers (tokens, `globals.css`, design-system components, OpenAPI, migrations) change only in their own enabler slice, one at a time [R2-Q9].
- The fit analysis warns when two PRDs in *Exploring* overlap; their drivers settle it before either reaches the gate [R4-Q8e′].
- Worktrees, start scripts and environments are covered in [chapter 5](05-worktrees-and-parallelism.md).
