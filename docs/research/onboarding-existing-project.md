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
8. **For each use case:** `write-use-case`, the `uc/UC-…` PR, then `write-stories`. Until CI runs the gate check, a use case reaches `Complete` on a local `check_grid.py` run plus the PR review, and CI checks it again later [R30-Q11].
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
