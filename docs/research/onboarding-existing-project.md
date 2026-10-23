# Onboarding an existing project

Notes for bringing a project that already has partial product artifacts into the framework, and for choosing the first use case to build the [`write-use-case`](../skills/write-use-case.md) skill against. Written on 2026-10-20 from the guide and the skill specs; the guide stays authoritative. The adoption rules themselves are in [chapter 13](../guide/13-adoption.md). Facts about the product monorepo stay in [`monorepo-fit.md`](../context/monorepo-fit.md); this note is generic and uses the meeting room booking domain.

**Brief.** Before building the design skills, map which skills each step of the design process ([chapter 3](../guide/03-design-playbook.md)) uses. Then work out how to bring an existing project into the framework when it already has partial product artifacts: informal use cases written inside an architecture document, plus personas, journeys and pain points in an audit deliverable. Restructure them into the framework's artifacts in a separate copy of the product repo, on a branch apart from the audit branch, without touching the existing local checkout or this repo's docs. Find the minimal inputs needed to write one concrete use case, as the worked example for building and iterating on `write-use-case`.

## 1. Skills by design step

"Ours" are the skills the framework builds ([chapter 12](../guide/12-skills-to-build.md)); "full" or "outline" is the state of their spec. Third-party skills are in [chapter 11](../guide/11-tooling-and-plugins.md).

| Step | Work | Skill | Kind |
|---|---|---|---|
| **1. Complete the use case** | Level, steps, duration classes, failure grid, extensions | `write-use-case` | ours, full, P0 |
| | Interview when the use case is vague | `grill-with-docs` | third-party |
| | Glossary terms | `domain-modeling` | third-party |
| | Use case gate (`Complete`) | `check-gate` | ours, full |
| **2. Cut stories** | Vertical stories, INVEST, Draft PRDs with `extensions:` and `touches:` | `write-stories` | ours, full |
| | Regenerate `coverage.md` and `index.md` | `check-gate` | ours, full |
| **3. Start exploring** | Branch, worktree, environment | `make design` (a script) | — |
| | Personal skills that clash with the project's | `check-setup` | ours, outline |
| **4. Explore** | Flows and state matrix (`flows.md`) | *no writer skill*; `ui-ux-pro-max` helps | third-party |
| | Prototype in the real stack | `frontend-design`, `shadcn`, Next.js skills, `ui-ux-pro-max`; motion: `emil-design-eng`; Figma MCP or Claude Design `/design-sync` | third-party |
| | Copy deck | `ux-copy`, `ux-writing` | third-party |
| | Other locales | `translate-copy` | ours, outline |
| | Gherkin scenarios | `write-scenarios` | ours, full |
| | Fit analysis and draft contract | `check-fit` | ours, full |
| | Outcome and measurement, PRD §10–§13 | *no skill*: by hand with Claude | — |
| **5. Prepare the gate** | UX lane guideline checks | `review-ux`, running `accessibility`, `check-web-guidelines`, `ui-ux-pro-max`, `check-copy`, `check-state-matrix` | ours (outline) and third-party |
| | PM, UX and Eng persona reviews, with the threat check | `review-design` | ours, full |
| | Local gate check | `check-gate` | ours, full |
| **6. Design-complete** | CI gate check, sign-offs | `check-gate` | ours, full |
| **DCR** | Steps 4–5 for the change only | as above | — |
| **Design-system enabler** | Tokens, new components | `sync-tokens`, `shadcn` | ours (outline) and third-party |

Not used in design: `check-flow-conformance`, `check-bdd-conventions`, `check-i18n-conventions`, `review-slice`, `review-code`, `review-security`, `review-privacy`, `review-llm-security` (development lanes).

**Gaps.** No skill writes `flows.md`, the outcome and measurement plan, or PRD §10–§13. Steps 1 and 2 need only `write-use-case`, `write-stories` and the mechanical part of `check-gate`; `write-use-case` can be built first and alone, since its `check_grid.py` covers the gate items it needs.

## 2. Bringing an existing project in

1. **Work in a separate copy.** Clone the product repo into a new folder (`git clone --no-hardlinks <local checkout> <new folder>`, which only reads the source) and work there in a Claude Code session started in that folder. The existing checkout and its branches are never touched. Add the hosted repo as a second remote for pushing.
2. **Branch from the main branch**, not from the branch that holds the existing material. Import that material as copies and record the commit they come from; re-import if it changes there [R30-Q14].
3. **Give the inputs typed IDs** [R3-A3]. Bare one-letter prefixes (`P1`, `J1`, `H1`) collide across artifact types. Round 30 set them to `PREFIX-NNN`: `PER-` personas, `JRN-` journeys, `HYP-` hypotheses, `PP-` pain points, `BLK-` blockers, `OBJ-` objections. The import rewrites the IDs only and keeps the old ones in `inputs/id-map.md` [R30-Q1, R30-Q2].
4. **Import the inputs unchanged** into `docs/product/inputs/`, one file per kind [R3-A5, R30-Q3]. Blockers are broadened from buying blockers to anything that stops a customer or user buying or adopting; they take the light format of [`blockers.md`](../templates/blockers.md) [R30-Q4′, R30-Q21′]. Importing principles or constraints from an architecture document is optional; each becomes an ADR when a PRD first needs it [R30-Q9′].
5. **Import the glossary** into `docs/product/glossary.md`, in both languages, including any glossary candidates the material lists.
6. **Copy the templates** needed now (`use-case.md`; `story.md` when stories are cut).
7. **Map the use cases.** Start each candidate user-goal use case as a `Draft` file holding only its title, primary actor and inputs; `docs/product/index.md` is generated from them and never edited by hand. Informal use cases stay as inputs and are rewritten in the fully dressed format one at a time, when picked [R3-A5, R1-Q6]. Expect `write-use-case` to flag:
   - a use case with two actors and a wait between them (an invitation that waits up to 72 hours to be accepted): split it at the wait point [R29-Q2];
   - a use case written once per technical option: the option is an ADR, and the use case is written once, with the options as variations;
   - a login or setup flow that is a subfunction rather than a user goal [R28-Q1].
8. **For each use case:** `write-use-case`, the `uc/UC-…` PR, then `write-stories`. Until CI runs the gate check, a use case reaches `Complete` on a local `check_grid.py` run plus the PR review, and CI checks it again later [R30-Q11]. The first use case comes before the skill exists: writing it is how the skill is built (§5).
9. **Settle the stack before the first *Exploring*.** The prototype stage assumes the confirmed stack. Where the product repo's own decisions differ ([`monorepo-fit.md`](../context/monorepo-fit.md)), an ADR in the product repo settles it first. Use cases, stories and `write-use-case` don't depend on the stack, so they start right away [R30-Q10].

## 3. Minimal path to the first use case

The use case the skills are built against may differ from the first PRD's, which should touch little existing code [R30-Q12]. The worked example, in the neutral domain: **a facilities manager imports the company's meeting rooms from a spreadsheet**. In the product repo, the equivalent is whichever use case has the same shape: an upload followed by long processing whose results need review.

1. **A copy and a branch**, as in §2, then `uc/UC-001-<slug>`.
2. **Only the inputs it cites, unchanged.** The quickest path imports the existing deliverable as one file and cites IDs inside it, putting off the split. The example needs: the primary actor's persona; the stakeholders (people who book rooms, the DPO); the journey stages for capture and review; the pain points and blockers the upload addresses.
3. **A facts note** in `inputs/`, with a source per fact: decisions already taken (what enters as validated, who reviews, consent), how the current system behaves (formats accepted, how long processing takes, whether it is synchronous), and what is not built yet. It fixes the example's inputs across iterations, so it doubles as the **eval fixture**.
4. **The glossary subset** the use case uses.
5. **Interview answers prepared** by the driver:
   - which horizon: what exists today, or the target?
   - one file or a batch? A batch whose processing takes minutes is a `background` step [R29-Q1];
   - the transfer and the processing are two system steps: the transfer is `long`, with progress shown by the client and cancel by aborting it [R29-Q8]; the processing is `background`, followed by a step that tells the actor the outcome, through which channel [R29-Q5];
   - what needs review after import: rows flagged for review end the use case at a **wait point**, and the review is its own use case [R29-Q2];
   - the same file imported twice (duplicate), or a new version of it (update or conflict);
   - personal data in the file, such as the names of room owners (privacy-request line);
   - cancel during processing: what happens to rows already stored (partial failure);
   - who may import, and who may not (an administrator without data rights);
   - limits: formats, size, number of rows.
6. **A baseline run without the skill.** In the product clone, ask Claude to write the use case from the template and the inputs with no skill, and keep the result. The spec's §1 says to replace the expected failures with observed ones before building; the baseline becomes §1 and the first eval case.

## 4. What the example covers

`long` and `background` steps, cancel, a notification after a background step, a wait point, duplicate and conflict, no permission, partial failure, quota or limit, and the privacy-request line: most of the `write-use-case` procedure and its evals ([spec §15](../skills/write-use-case.md#15-evaluation-plan)).

## 5. Building the skill from the example

`write-use-case` is specified, not built, when the first use case is picked, so step 8 of §2 runs this loop instead. The first use case is both the first real artifact and the skill's first fixture. *Changed by round 31:* steps 1–9 run in this repo's lab, [`lab/write-use-case/`](../../lab/write-use-case/README.md), on the driver's sample use cases from other products, and the skill is copied to the monorepo when it passes its held-out cases [R31-Q6, R31-Q9]. Step 10 still runs in the product copy: the product's first use case is the first live interview. Lessons that reach `docs/` are rewritten in the neutral domain [R31-Q7]. Practices are from [chapter 12](../guide/12-skills-to-build.md) and the [skill authoring research](skill-authoring.md).

1. **Freeze the fixture.** The inputs it cites, the facts note, the glossary subset and the driver's interview answers (§3, steps 1–5), each in a file. Every run below reads them unchanged, so runs can be compared.
2. **Baseline without the skill** (§3, step 6). A fresh session that has not seen the spec writes the use case from the template and the fixture, reading answers from the answers file. Keep it as `baseline.md`. The template's comments already state most rules, so this measures what the template alone achieves; the skill must do better.
3. **Grade the baseline** by hand against spec [§6](../skills/write-use-case.md#6-procedure) and the [§15](../skills/write-use-case.md#15-evaluation-plan) cases, and list the failures actually seen: missing categories, no cancel on the import, the review kept inside the scenario instead of ending at a wait point, interface words. Compare them with the expected failures of spec §1 [R25-Q4].
4. **Write the gold version**: the baseline corrected by hand into the use case the driver would sign off. It is the expected output of every later run, and the real first use case.
5. **Build `check_grid.py` first, test first.** It is deterministic and is the gate's mechanical check until CI exists [R30-Q11]. `baseline.md` must fail with the errors found in step 3, `gold.md` must pass; each rule of spec [§7](../skills/write-use-case.md#7-scripts-vs-judgement) gets a unit test [R5-Q4′].
6. **Draft the skill** in the layout of spec [§8](../skills/write-use-case.md#8-files). While iterating, keep it as a project skill in the copy (`.claude/skills/write-use-case/`), which a session loads without installing a plugin; move it into the plugin ([§12.2](../guide/12-skills-to-build.md#122-where-they-live)) once its evals pass. The spec's `status` becomes `building` [R25-Q4].
7. **Run with the skill and compare** with the baseline and the gold version, in a fresh session each time, on the same fixture and answers. Anthropic's `skill-creator` runs the with-and-without arms and the comparison [R5-Q4c].
8. **Iterate.** Each gap from the gold version gets one fix: a rule in `SKILL.md`, an example in a reference, a script check, or a gotcha. Re-run after each. Stop when `check_grid.py` passes, the driver would accept the output with wording changes only, and two runs in a row agree.
9. **Generalise.** One example overfits. Add the other §15 cases as small fixtures in the neutral domain (a summary goal, an approval wait point, a button in a step, a term missing from the glossary, a use case written once per technical option, an `inputs:` ID no input defines, `renumber` refused), and the 20 triggering prompts. Keep them in `evals/` in `claude plugin eval` format, threshold 0.8 [R5-Q4c].
10. **Use it, then test it on a held-out case.** The gold version goes through the `uc/UC-…` PR to `Complete` [R28-Q11]. The second use case, never used for tuning, is the real test, and its live interview is the first one not read from a file. Each correction there becomes a gotcha or an eval.
11. **Bring the lessons back here.** The observed failures replace spec §1, new gotchas go to §14, and `status` becomes `built` when the definition of done (§16) holds. Lessons are rewritten in the neutral domain. A change to a rule rather than to the skill's wording (a new category, a new duration class) starts as a grilling round.

**Interview in evals.** The skill interviews the driver ([spec §12](../skills/write-use-case.md#12-headless-and-ci)), which an eval can't. Every run, with or without the skill, reads its answers from the frozen answers file; the live interview is exercised only in step 10.
