---
name: review-outcome
status: outline
priority: P2
owner: <name>
serves: Outcome review after Done
decisions: [R4-Q4e, R22-Q1, R8-Q3, R23-Q2]
plugin_version:
---

# review-outcome

## 0. Header

Helps the driver fill in a PRD's outcome review on its due date.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- reports numbers for the wrong window or the wrong dimension time (as-now vs as-at-event).
- Calls an outcome met without a baseline.
- Rewrites the rest of a Done PRD.

## 2. Scope

- **Does:** lists overdue reviews from `docs/product/index.md`, gathers the §3 signals and §3b metrics for the window (default 4 weeks, R22-Q1), drafts §17 (met / missed / inconclusive, numbers, follow-up) for the driver to confirm [R4-Q4e].
- **Does not:** edit anything but §17, or query production data directly unless an analytics source is configured.
- **Neighbouring skills:** Reads the tracking plan's metric and dimension catalogues [R8-Q3, R23-Q2].

## 3. Invocation

- **Invoked by:** the user (the PRD's driver).
- **Draft description:**
  > Drafts the outcome review of a Done PRD from its success signals and metrics for the review window. Use when a PRD's outcome review is due or overdue.
- **Should trigger:**
  - "which outcome reviews are due"
  - "draft the outcome review for PRD-012.1"
  - "did this feature meet its target"
- **Should not trigger:**
  - "write the PRD"
  - "plan the next sprint"
  - "review the code"
- **Arguments:** PRD ID.

## 4. Inputs

_To be completed before building (R25-Q4)._

## 5. Outputs

_To be completed before building (R25-Q4)._

## 6. Procedure

_To be completed before building (R25-Q4)._

## 7. Scripts vs judgement

_To be completed before building (R25-Q4)._

## 8. Files

_To be completed before building (R25-Q4)._

## 9. Composition

- Analytics or BI access through whatever the BI ADR chooses (R4-Q4d).

## 10. Claude Code wiring

_To be completed before building (R25-Q4)._

## 11. Portability

_To be completed before building (R25-Q4)._

## 12. Headless and CI

_To be completed before building (R25-Q4)._

## 13. Security and privacy

_To be completed before building (R25-Q4)._

## 14. Gotchas

_To be completed before building (R25-Q4)._

## 15. Evaluation plan

_To be completed before building (R25-Q4)._

## 16. Definition of done

_To be completed before building (R25-Q4)._

## 17. Maintenance

_To be completed before building (R25-Q4)._

## 18. Open questions

- How it reads metrics before a BI stack exists.
