---
prd: PRD-012.1
analysed_against: <main commit SHA>
refreshed_at_slice_start: <commit SHA or empty>   # [R4-Q8′ step 0]
---
<!-- Copied to …/stories/US-012.1-<slug>/fit.md. Written by the check-fit skill during Exploring,
     reviewed by the SWE persona [R4-Q8a]. The draft contract is written against it. -->

# Fit analysis: PRD-012.1

## 1. Existing specs

<!-- Key 1 [R4-Q8b′]. Compare each new scenario with the .feature files on main.
     Done PRD = implemented behaviour; Dev-ready / In development = committed, not built yet. -->

| New scenario | Existing scenario | Its PRD and status | Class | Action |
|---|---|---|---|---|
| Book a free room | `UC-009.1` in PRD-009.2 | Done | duplicate / refines / contradicts / independent | reuse / amend (R4-Q8e′) / new |

**Overlap with PRDs still in Exploring** (open `design/` branches, warning only):

## 2. API

<!-- Key 2: OpenAPI diff of contract.draft.yaml against the generated spec (e.g. oasdiff). -->

| Path and method / schema | Diff | Class | Consumers |
|---|---|---|---|
| `POST /bookings` | changed | reuse / extend / change (breaking) / new | <PRDs or apps that use it> |

## 3. Behaviour run

<!-- Key 3: the new scenarios bound to the existing business layer. Green = exists, red = gap. -->

| Scenario | Result | Notes |
|---|---|---|
| | green / red | |

## 4. Code

<!-- Key 4: glossary terms within the domain layout, plus test tags. Production code carries no IDs. -->

| Concept | Found at | Class | Follows the target structure? |
|---|---|---|---|
| | `src/domains/<d>/app/business/usecases/…` | reuse / extend / change / new | yes / no → characterisation tests, port wrap or ENB [R4-Q8d] |

## 5. Misalignments and their resolution

<!-- Rules [R4-Q8c]: for user-visible behaviour the signed PRD wins unless other features depend on it;
     then backward-compatible extension, or a listed breaking change, or a DCR. Architecture → ADR. -->

| Misalignment | Resolution | Link |
|---|---|---|
| | extension / listed breaking change / DCR / ADR / ENB | |
