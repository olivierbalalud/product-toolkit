---
name: check-state-matrix
status: outline
priority: P1
owner: <name>
serves: UX lane; design gate item (d)
decisions: [R2-Q3, R4-Q7a, R4-Q7d, R29-Q7]
plugin_version:
---

# check-state-matrix

## 0. Header

Checks that every screen covers the seven states of the state matrix, in the spec and in the prototype or build.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- Accepts a matrix with empty cells or 'n/a' without a reason.
- Doesn't notice the prototype lacks the no-permission or stale-data state.
- Only checks the ideal state.

## 2. Scope

- **Does:** checks `flows.md`'s state matrix (empty, loading, error, partial, success, no permission, stale data) for completeness, then checks each state exists in the prototype or slice [R2-Q3 (d)]. Advisory: a *Loading* cell marked `n/a` for a screen tied to a `wait`, `long` or `background` use-case step, and a *Loading* cell that doesn't match the step's class (progress and cancel for `long`; acknowledgement, status and notification for `background`) [R29-Q7].
- **Does not:** design the missing states.
- **Neighbouring skills:** Runs in the UX lane and before the design gate; `check-flow-conformance` checks the rest of `flows.md`.

## 3. Invocation

- **Invoked by:** the model, as a reviewer in its lane, or the user directly.
- **Draft description:**
  > Checks a PRD's state matrix for missing or unjustified states and that each state exists in the prototype or build. Use before the design gate and when reviewing UI changes.
- **Should trigger:**
  - "are all states covered for these screens"
  - "check the state matrix"
  - "did we design the empty and error states"
- **Should not trigger:**
  - "check the copy tone"
  - "review the database migration"
  - "map the user journey"
- **Arguments:** Base ref or PR number; or paths to review.

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

- Matrix completeness is a script on `flows.md`; finding states in the running app uses Playwright from `.mcp.json`.
- A **leaf** reviewer: `Agent` removed from its tools, so it starts no subagents [R15-Q2].
- Each finding is `blocking` or `advisory` [R4-Q7c].

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

- How to drive the prototype into each state (fixtures in MSW mocks?).
