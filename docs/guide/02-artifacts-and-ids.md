# 2. Artifacts and IDs

This chapter lists every artifact the framework uses, its ID format, where its file lives, and the frontmatter fields the gate check reads. Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md). The statuses themselves are in [chapter 1](01-lifecycle-and-gates.md); the templates are in [`../templates/`](../templates/).

## 2.1 ID rules

- **Every ID has a typed prefix.** No bare one-letter prefixes, which collide across artifact types [R3-A3].
- **IDs are never reused**, even when an artifact is rejected or deleted. The rule an existing decision register may already have carries over [R3-A2].
- **Child IDs embed their parent's number**, so the parent can be read from the ID alone.
- **IDs appear in file and folder names, branch names, commit scopes, Gherkin tags and test markers.** They do not appear in production code, where they would go stale [R4-Q8b′].

| Artifact | ID format | Example | Parent |
|---|---|---|---|
| Use case | `UC-NNN` | `UC-012` | — |
| Use-case extension | `UC-NNN.<step><letter>` | `UC-012.3a` (step 3, first extension) | Use case |
| User story | `US-NNN.N` | `US-012.1` | Use case |
| PRD | `PRD-NNN.N` | `PRD-012.1` (same number as its story, 1:1) | Story |
| TRD | `TRD-NNN.N` | `TRD-012.1` | PRD |
| Design change request | `DCR-NNN.N-NN` | `DCR-012.1-01` | PRD |
| Enabler slice | `ENB-NNN` | `ENB-004` | — |
| ADR | `ADR-NNNN` | `ADR-0007` | — |
| Metric | `MET-NNN` | `MET-003` | Tracking plan (metric catalogue) [R8-Q3] |
| Analytics event | `EVT-NNN`, plus a snake_case event name | `EVT-014` / `room_booked` | Tracking plan [R8-Q4] |
| Slice ticket | `NN-slug` (file name, unique within its story) | `03-reject-duplicate.md` | Story [R6-Q2] |

`ENB` stands for **enabler**: work that no single story owns but that stories depend on, such as CI, the app shell, a new design-system component or an infrastructure piece [R3-A3].

## 2.2 Where artifacts live

The layout of the product monorepo, as far as specs are concerned [R3-Q1a–h]:

```
doc/
  product/
    index.md                       GENERATED: every artifact with status, driver, priority
    settings.yaml                  product-wide settings, e.g. metrics_stage [R8-Q2]
    glossary.md                    bilingual domain glossary [R3-A5]
    tracking-plan.md               events and metric catalogue [R4-Q4c]
    inputs/                        personas, journeys, pain points, objections [R3-Q1d]
    enablers/
      ENB-004-<slug>/
        enb.md
        tickets/NN-<slug>.md   [R8-Q1]
    use-cases/
      UC-012-<slug>/
        use-case.md
        coverage.md                GENERATED: extension → scenarios [R3-Q1b]
        stories/
          US-012.1-<slug>/
            prd.md
            flows.md               flow map, screens, key info and actions, state matrix
            copy.md                copy deck
            fit.md                 fit analysis [R4-Q8a]
            contract.draft.yaml    draft API contract
            features/*.feature     English Gherkin [R3-Q1a]
            reviews.md             persona reviews and sign-offs
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
| Use case | `use-case.md` | When a use case is picked for clarification | `Draft → Ready for review → Under review → Complete` [R7-Q1] | Its driver |
| Story | the story folder, with its PRD | When stories are cut from a complete use case [R4-Q3] | Follows its PRD | The PRD's driver |
| PRD | `prd.md` and its sibling files | With its story | `Draft → … → Done` [R1-Q8] | Its driver |
| Feature files | `features/*.feature` | During *Exploring* | Frozen at Design-complete; changed later only by a DCR or an amendment [R3-Q1a, R4-Q8e′] | The PRD's driver |
| Fit analysis | `fit.md` | During *Exploring*, refreshed at slice start [R4-Q8a, R4-Q8′] | Follows its PRD | The SWE persona reviews it |
| Design change request | `dcr/DCR-…md` | When a UX change is needed after Design-complete [R2-Q4] | `Exploring → Design-complete` [R7-Q3] | The PRD's driver |
| Ticket | `tickets/NN-slug.md` | At slice start, by `to-tickets` | `status` and `blocked_by` in frontmatter [R6-Q2] | The developer |
| Enabler slice | `doc/product/enablers/ENB-…/enb.md` [R8-Q1] | When a story or an adoption step needs shared work | `Draft → Dev-ready → In development → Done` [R7-Q2] | A developer |
| ADR | `doc/adr/NNNN-slug.md` | When a feasibility or architecture gap appears [R1-Q13] | MADR statuses; a `Proposed` ADR blocks Dev-ready | Its author |
| TRD | `doc/trd/` | When the stack and ADRs don't answer a PRD's technical questions [R5-Q1] | — | A developer |
| Tracking plan | `doc/product/tracking-plan.md`: events (`EVT-…`) and the metric catalogue (`MET-…`) | With the first PRD that measures something | Living document | The founders |

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
| `adrs`, `trds` | Linked ADRs and TRDs. | R4-Q4 |
| `enablers` | Enabler slices this PRD depends on. | R4-Q4d, R5-Q1 |
| `amends` | Scenarios of earlier PRDs this PRD changes. | R4-Q8e′ |
| `amended_by` | Later PRDs or `fix/` branches that changed this PRD's scenarios. | R4-Q8e′, R5-Q2 |
| `open_dcrs` | Design change requests not yet closed. | R7-Q3 |
| `outcome_review_due` | Date of the outcome review: Done plus the measurement window. | R4-Q4e |

### Product-wide setting

`metrics_stage: discovery | growth` decides whether numeric success targets are mandatory in PRDs. The founders switch it. It lives in `doc/product/settings.yaml`, which the gate check reads [R4-Q4b, R8-Q2].

## 2.5 Traceability

How an ID travels from the spec to the code and back:

| Where | Form | Example | Decision |
|---|---|---|---|
| Branch | `<kind>/<ID>-<slug>` | `slice/PRD-012.1-book-room`, `design/DCR-012.1-01-new-copy` | R4-Q5′, R10-Q1 |
| Worktree | branch name with `/` replaced by `-` | `slice-PRD-012.1-book-room` | R4-Q5′ |
| Commit scope | the artifact ID | `docs(PRD-012.1): add state matrix` | R4-Q5′ |
| Gherkin | tags on each scenario | `@US-012.1 @UC-012.3a` | R3-Q1a |
| Other tests | a pytest marker or test tag | the extension or story ID | R4-Q8b′ |
| UI text in steps | copy-deck key, only where wording matters | `"checkout.payment.submit"` | R3-C2 |
| Domain words in steps | the glossary's English term | — | R3-C3 |

From these tags, a script generates `coverage.md` (extension → scenarios, committed) and CI produces the traceability report (extension → scenario → result per test layer, as a CI artifact) [R3-Q1b].

## 2.6 Language of each artifact

| Artifact | Language | Decision |
|---|---|---|
| Use cases, PRDs, flows, copy deck, reviews | The document's `source_locale` | R1-Q11 |
| Gherkin `.feature` files | **English only**, whatever the PRD's language | R3-Q1a amendment |
| ADRs, TRDs, code, comments, commits | English | R1-Q11 |
| UI strings | Source locale in the copy deck; other locales generated and marked `needs-review` | R2-Q6 |

A PRD written in French links to its English `.feature` files rather than restating the acceptance criteria in French. An agent can render a French reading view on demand, which is never authoritative [R3-C1].
