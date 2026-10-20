---
name: check-flow-conformance
status: outline
priority: P1
owner: <name>
serves: UX lane
decisions: [R4-Q7a, R2-Q5, R3-C2]
plugin_version:
---

# check-flow-conformance

## 0. Header

Checks that the rendered screens match `flows.md` and the copy deck.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- Misses a missing screen or transition from the flow map.
- Accepts literal text where the copy deck has a key.
- Can't tell intended visual change from regression.

## 2. Scope

- **Does:** renders the flows with Playwright, compares screens, transitions, key information and actions with `flows.md`, and text with the copy deck; reads Chromatic visual diffs against the design-complete snapshot [R2-Q5].
- **Does not:** judge visual taste, or change the design.
- **Neighbouring skills:** Runs in the UX lane; `check-state-matrix` covers states.

## 3. Invocation

- **Invoked by:** the model, as a reviewer in its lane, or the user directly.
- **Draft description:**
  > Checks that the built or prototype screens match the PRD's flow map, screens, key actions and copy deck. Use when reviewing a slice that changes UI.
- **Should trigger:**
  - "does the build match the flows"
  - "conformance check against flows.md"
  - "compare the screens with the design-complete snapshot"
- **Should not trigger:**
  - "write the flow map"
  - "review the backend"
  - "check translations"
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

- Uses the `playwright` MCP server from `.mcp.json` [R4-Q7e].
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

- How Chromatic results are fetched in a headless run.
