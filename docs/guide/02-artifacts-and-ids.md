# 2. Artifacts and IDs

This chapter lists every artifact the framework uses, its ID format, where its file lives, and the frontmatter fields the gate check reads. Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md). The statuses themselves are in [chapter 1](01-lifecycle-and-gates.md); the templates are in [`../templates/`](../templates/).

## 2.1 ID rules

- **Every ID has a typed prefix.** No bare one-letter prefixes, which collide across artifact types [R3-A3].
- **IDs are never reused**, even when an artifact is rejected or deleted. The rule an existing decision register may already have carries over [R3-A2].
- **Step and extension IDs may be renumbered only before they freeze.** `write-use-case renumber` rewrites every reference while every PRD that references the use case is `Draft` or *Exploring*. After that, an inserted step takes a decimal number (`3.1`, extension `UC-012.3.1a`) and a removed step or extension is marked `retired` [R28-Q19′].
- **Child IDs embed their parent's number**, so the parent can be read from the ID alone.
- **IDs appear in file and folder names, branch names, commit scopes, Gherkin tags and test markers.** They do not appear in production code, where they would go stale [R4-Q8b′].

| Artifact | ID format | Example | Parent |
|---|---|---|---|
| Use case | `UC-NNN` | `UC-012` | — |
| Use-case extension | `UC-NNN.<step><letter>`; `UC-NNN.<first>-<last><letter>` for a range of steps; `UC-NNN.*<letter>` for any step [R31-Q3] | `UC-012.3a` (step 3, first extension); `UC-012.3.1a` after an inserted step [R28-Q19′]; `UC-012.3-6a` (steps 3 to 6); `UC-012.*a` (any step; in backticks in Markdown, where a bare `*` is emphasis) | Use case |
| User story | `US-NNN.N` | `US-012.1` | Use case |
| PRD | `PRD-NNN.N` | `PRD-012.1` (same number as its story, 1:1) | Story |
| TRD | `TRD-NNN.N` | `TRD-012.1` | PRD |
| Design change request | `DCR-NNN.N-NN` | `DCR-012.1-01` | PRD |
| Enabler slice | `ENB-NNN` | `ENB-004` | — |
| ADR | `ADR-NNNN` | `ADR-0007` | — |
| Metric | `MET-NNN` | `MET-003` | Tracking plan (metric catalogue) [R8-Q3] |
| Dimension | `DIM-NNN` | `DIM-001` | Tracking plan (dimension catalogue) [R23-Q2] |
| Analytics event | `EVT-NNN`, plus a snake_case event name | `EVT-014` / `room_booked` | Tracking plan [R8-Q4] |
| Slice ticket | `NN-slug` (file name, unique within its story) | `03-reject-duplicate.md` | Story [R6-Q2] |
| Input [R30-Q1] | `PER-NNN` persona, `JRN-NNN` journey, `PP-NNN` pain point, `BLK-NNN` blocker, `OBJ-NNN` objection, `HYP-NNN` hypothesis | `BLK-003` | — |

`ENB` stands for **enabler**: work that no single story owns but that stories depend on, such as CI, the app shell, a new design-system component or an infrastructure piece [R3-A3].

## 2.2 Where artifacts live

The layout of the product monorepo, as far as specs are concerned [R3-Q1a–h]:

```
docs/
  product/
    index.md                       GENERATED: every artifact with status, driver, priority
    settings.yaml                  product-wide settings, e.g. metrics_stage [R8-Q2]
    glossary.md                    bilingual domain glossary [R3-A5]
    tracking-plan.md               events and metric catalogue [R4-Q4c]
    inputs/                        one file per kind: personas.md, journeys.md, pain-points.md,
                                   blockers.md, objections.md, hypotheses.md [R3-Q1d, R30-Q3]
      id-map.md                    old → new IDs of imported material [R30-Q2]
    enablers/
      ENB-004-<slug>/
        enb.md
        tickets/NN-<slug>.md   [R8-Q1]
    use-cases/
      UC-012-<slug>/
        use-case.md
        coverage.md                GENERATED: extension → claiming stories → scenarios [R3-Q1b]
        stories/
          US-012.1-<slug>/
            prd.md
            flows.md               flow map, screens, key info and actions, state matrix (touches: ui)
            copy.md                copy deck (touches: ui)
            fit.md                 fit analysis [R4-Q8a]
            contract.draft.yaml    draft API contract (touches: api) [R28-Q5]
            features/*.feature     English Gherkin [R3-Q1a]
            reviews.md             persona reviews and sign-offs
            design-export/         final Claude Design export, if design_tool is claude-design [R18-Q6]
            dcr/DCR-012.1-01-<slug>.md
            tickets/NN-<slug>.md   written by to-tickets on the slice branch [R6-Q2]
  design/
    voice-and-tone.md              shared core plus per-locale rules [R2-Q7]
    design-system.md
    motion.md                      motion policy and intent catalogue [R3-Q6′]
  adr/
    NNNN-<slug>.md                 MADR [R3-A2]
    analysis/                      supporting analysis for ADRs
  trd/
  ops/
```

Folders are nested by use case so that PRDs worked on in parallel touch separate folders [R3-Q1c]. Test results and reports are never committed: they are CI artifacts. The only committed traceability is the generated `coverage.md` [R3-Q1b].

**Generated files are never edited by hand:** `index.md` and every `coverage.md`.

## 2.3 Artifact catalogue

| Artifact | File | Created | Lifecycle | Owner |
|---|---|---|---|---|
| Use case | `use-case.md`, at the user-goal level [R28-Q1] | When a use case is picked for clarification, on a `uc/` branch [R28-Q20] | `Draft → Complete` [R28-Q11] | Its driver |
| Story | the story folder, with its PRD | When stories are cut from a complete use case [R4-Q3] | Follows its PRD | The PRD's driver |
| PRD | `prd.md` and its sibling files | With its story | `Draft → … → Done` [R1-Q8] | Its driver |
| Feature files | `features/*.feature` | During *Exploring* | Frozen at Design-complete; changed later only by a DCR or an amendment [R3-Q1a, R4-Q8e′] | The PRD's driver |
| Fit analysis | `fit.md` | During *Exploring*, refreshed at slice start [R4-Q8a, R4-Q8′] | Follows its PRD | The SWE persona reviews it |
| Design change request | `dcr/DCR-…md` | When a UX change is needed after Design-complete [R2-Q4] | `Exploring → Design-complete` [R7-Q3] | The PRD's driver |
| Ticket | `tickets/NN-slug.md` | At slice start, by `to-tickets` | `status` and `blocked_by` in frontmatter [R6-Q2] | The developer |
| Enabler slice | `docs/product/enablers/ENB-…/enb.md` [R8-Q1] | When a story or an adoption step needs shared work | `Draft → Dev-ready → In development → Done` [R7-Q2] | A developer |
| ADR | `docs/adr/NNNN-slug.md` | When a feasibility or architecture gap appears [R1-Q13] | MADR statuses; a `Proposed` ADR blocks Dev-ready | Its author |
| TRD | `docs/trd/` | When the stack and ADRs don't answer a PRD's technical questions [R5-Q1] | — | A developer |
| Inputs | `docs/product/inputs/`, one heading per item, starting with its ID [R30-Q3] | When existing material is imported [R3-A5], or when research adds an item | Blockers only: `open`, `resolved` or `accepted` [R30-Q16]; the others have no status | The founders |
| Tracking plan | `docs/product/tracking-plan.md`: events (`EVT-…`) and the metric catalogue (`MET-…`) | With the first PRD that measures something | Living document | The founders |

## 2.4 Frontmatter fields

These are the fields the gate check relies on. Each template in [`../templates/`](../templates/) shows the full frontmatter.

### Common to specs

| Field | Meaning | Decision |
|---|---|---|
| `id` | The artifact's typed ID. | R3-A3 |
| `status` | One of the artifact's lifecycle statuses. | R3-A4 |
| `driver` | The one human accountable for it. | R4-Q1 |
| `priority` | Informs which item a founder picks next; never picks it automatically. | R6-Q1 |
| `source_locale` | The language the document is written in (`en` or `fr` for now). | R1-Q11 |

### PRD only

| Field | Meaning | Decision |
|---|---|---|
| `use_case`, `story` | Links to the parent use case and story. | R4-Q4 |
| `extensions` | The use-case extensions the story handles; the only list of them. Several stories may claim the same one. | R4-Q3, R28-Q4, R28-Q9 |
| `touches` | `ui`, `api` or both: decides which companion files the gate requires (`flows.md`, `copy.md` with `ui`; `contract.draft.yaml` with `api`). Free to change until Design-complete, then through a DCR. | R28-Q5, R28-Q18 |
| `adrs`, `trds` | Linked ADRs and TRDs. | R4-Q4 |
| `enablers` | Enabler slices this PRD depends on. | R4-Q4d, R5-Q1 |
| `amends` | Scenarios of earlier PRDs this PRD changes. | R4-Q8e′ |
| `amended_by` | Later PRDs or `fix/` branches that changed this PRD's scenarios. | R4-Q8e′, R5-Q2 |
| `open_dcrs` | Design change requests not yet closed. | R7-Q3 |
| `outcome_review_due` | Date of the outcome review: Done plus the measurement window. | R4-Q4e |
| `design_tool` | `figma` or `claude-design`; fixed once *Exploring* starts. | R18-Q4 |

### Blockers

A blocker is a condition, seen from a customer's or user's side, that stops them buying or adopting the product. `blockers.md` has a *Buying* and an *Adoption* section, and each blocker sits in the earliest stage where it bites. Its text says who is blocked, where in the journey, and each cause, named `product-gap`, `external-limit` or `legal-or-business`, with its evidence [R30-Q4′, R30-Q5′, R30-Q6, R30-Q15′]. Three fields follow its heading ([template](../templates/blockers.md)) [R30-Q21′]:

| Field | Meaning | Decision |
|---|---|---|
| `status` | `open`, `resolved` (the condition no longer holds) or `accepted` (we live with it: a segment excluded or a risk taken). The founders change it in a PR. | R30-Q16 |
| `review_by` | Only when `accepted`: when to look at it again. The gate check warns once it has passed. | R30-Q16, R30-Q20 |
| `evidence` | Only when `resolved`: a link, or one statement of what was done, who confirmed it, when, and where the proof is kept. | R30-Q18′, R30-Q20 |

Blockers never block a gate [R30-Q19]. Responses cite them, never the reverse: a use case in `inputs:`, an ADR or an enabler in `raised_by:`; `index.md` lists each blocker's responses [R30-Q17].

### Product-wide setting

`metrics_stage: discovery | growth` decides whether numeric success targets are mandatory in PRDs. The founders switch it. It lives in `docs/product/settings.yaml`, which the gate check reads [R4-Q4b, R8-Q2].

## 2.5 Traceability

How an ID travels from the spec to the code and back:

| Where | Form | Example | Decision |
|---|---|---|---|
| Branch | `<kind>/<ID>-<slug>` | `uc/UC-012-book-room`, `slice/PRD-012.1-book-room`, `design/DCR-012.1-01-new-copy` | R4-Q5′, R10-Q1, R28-Q20 |
| Worktree | branch name with `/` replaced by `-` (none for `uc/` branches) | `slice-PRD-012.1-book-room` | R4-Q5′ |
| Commit scope | the artifact ID | `docs(PRD-012.1): add state matrix` | R4-Q5′ |
| Gherkin | tags on each scenario | `@US-012.1 @UC-012.3a` | R3-Q1a |
| Other tests | a pytest marker or test tag | the extension or story ID | R4-Q8b′ |
| UI text in steps | domain wording, never a copy key; `@ui` step definitions map it to the key | `I am told the room is no longer free` | R28-Q10 |
| Domain words in steps | the glossary's English term | — | R3-C3 |

From these tags and the stories' `extensions:`, a script generates `coverage.md` (extension → claiming stories → scenarios, committed) and CI produces the traceability report (extension → scenario → result per test layer, as a CI artifact) [R3-Q1b].

## 2.6 Language of each artifact

| Artifact | Language | Decision |
|---|---|---|
| Use cases, PRDs, flows, copy deck, reviews | The document's `source_locale` | R1-Q11 |
| Gherkin `.feature` files | **English only**, whatever the PRD's language | R3-Q1a amendment |
| ADRs, TRDs, code, comments, commits | English | R1-Q11 |
| UI strings | Source locale in the copy deck; other locales generated and marked `needs-review` | R2-Q6 |

A PRD written in French links to its English `.feature` files rather than restating the acceptance criteria in French. An agent can render a French reading view on demand, which is never authoritative [R3-C1].
