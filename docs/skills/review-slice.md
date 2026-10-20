---
name: review-slice
status: outline
priority: P1
owner: <name>
serves: Done gate: runs the applicable review lanes
decisions: [R4-Q7a, R4-Q7b, R7-Q4, R15-Q1, R15-Q3]
plugin_version:
---

# review-slice

## 0. Header

A thin orchestrator that decides which review lanes apply to a PR and runs them.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- Runs every lane on every diff, wasting budget on UX checks for backend-only changes.
- Merges the lanes' findings into one ranked list, so a security issue hides behind code nits.
- Re-runs all lanes after a small fix instead of only those whose files changed.

## 2. Scope

- **Does:** picks the lanes for the PR type and diff (code and security always; UX when `src/apps/web/` or `src/packages/ui/` changed), runs them, re-runs only the lanes whose files changed after fixes, and posts one summary comment per lane.
- **Does not:** review anything itself, rank findings across lanes, or fix code.
- **Neighbouring skills:** `review-code`, `review-security`, `review-ux` do the reviewing; `check-gate` reads the outcome at Done.

## 3. Invocation

- **Invoked by:** the user, and CI on a PR marked ready for review or when a re-review is requested [R15-Q3]. Model-invocable so CI and other skills can call it.
- **Draft description:**
  > Runs the applicable review lanes (code, security and privacy, UX) on a slice, fix or enabler PR and reports each lane separately. Use when a PR is ready for review or a re-review is requested.
- **Should trigger:**
  - "review this slice before I open the PR"
  - "run the review lanes on PR 42"
  - "re-review after my fixes"
- **Should not trigger:**
  - "review this Figma mockup"
  - "explain this function"
  - "write the tests for this ticket"
- **Arguments:** PR number or base ref; optional `--lanes` to force a subset.

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

- Reads the lanes from `review-lanes.yaml` ([example](../templates/review-lanes.yaml)) [R4-Q7a].
- Invokes each applicable lane skill through the Skill tool, in parallel where the harness allows; otherwise one after another [R5-Q4a].
- Aggregation: one section and one PR comment **per lane**, never merged or reranked [R4-Q7a].

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

- How CI passes the PR context to a headless run, and how a re-review request is detected.
- Where the 'files changed since last review' state is kept between runs.
