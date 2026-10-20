---
name: review-ux
status: outline
priority: P1
owner: <name>
serves: UX review lane
decisions: [R4-Q7a, R4-Q7b, R4-Q7c, R4-Q7d]
plugin_version:
---

# review-ux

## 0. Header

The UX review lane: runs its reviewers in parallel and reports them side by side.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- Reviews screenshots only, missing states the state matrix lists.
- Silently 'fixes' a flow or copy change in the slice instead of raising a DCR.
- Applies Vercel's Title Case over our voice guide.

## 2. Scope

- **Does:** runs the UX reviewers on a diff or a prototype and reports them separately. A finding that would change the agreed design is reported as **needs a DCR**, not as a fix [R4-Q7c].
- **Does not:** change the design, the tokens or the copy deck.
- **Neighbouring skills:** Called by `review-slice`; each reviewer is its own skill or agent.

## 3. Invocation

- **Invoked by:** the model, through `review-slice`, or the user directly.
- **Draft description:**
  > Runs the UX reviewers listed in review-lanes.yaml on a diff and reports each separately with blocking and advisory findings. Use when reviewing a slice, fix or enabler PR for UX issues.
- **Should trigger:**
  - "UX review of this slice"
  - "run the UX checks on the prototype before the gate"
  - "check accessibility and states on PR 7"
- **Should not trigger:**
  - "review the API contract"
  - "run the security lane"
  - "write the Gherkin scenarios"
- **Arguments:** Base ref or PR number.

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

- Reads its reviewer list from the `ux` lane of `review-lanes.yaml`, so adding a reviewer is a configuration change [R4-Q7a].
- Reviewers: `ui-ux-pro-max`, addyosmani `accessibility` (WCAG 2.2), `check-web-guidelines`, `review-animations`, `ux-copy` plus `check-copy`, `check-state-matrix`, `check-flow-conformance` (Playwright from `.mcp.json`, Chromatic diffs) [R4-Q7a].
- Also runs on prototypes before the design gate, feeding the UX persona and `reviews.md` [R4-Q7d].
- Reviewer subagents preload the upstream skills they need through `skills:`; MCP servers come from the project `.mcp.json` [R4-Q7e].
- A **leaf** reviewer: `Agent` removed from its tools, so it starts no subagents [R15-Q2].
- Aggregation: reports side by side, no merge, no cross-reviewer ranking [R4-Q7a]. Each finding is `blocking` or `advisory` [R4-Q7c].

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

- How a plugin subagent's `skills:` names a plugin skill (bare or `plugin:name`) — test before relying on it (chapter 9).
- Which paths trigger it besides `src/apps/web/` and `src/packages/ui/` (R4-Q7b).
