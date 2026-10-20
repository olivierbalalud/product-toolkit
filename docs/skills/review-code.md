---
name: review-code
status: outline
priority: P1
owner: <name>
serves: Code review lane
decisions: [R4-Q7a, R13-Q2, R14-Q3]
plugin_version:
---

# review-code

## 0. Header

The code review lane: runs its reviewers in parallel and reports them side by side.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- Reviews only standards and spec, missing pytest-bdd and next-intl conventions.
- Treats low diff coverage as blocking.
- Lets one reviewer's report colour another's.

## 2. Scope

- **Does:** runs the code reviewers on a diff and reports them separately.
- **Does not:** review security, privacy or UX (other lanes); run inside `implement-spec`, which calls `code-review` itself [R13-Q2].
- **Neighbouring skills:** Called by `review-slice`; each reviewer is its own skill or agent.

## 3. Invocation

- **Invoked by:** the model, through `review-slice`, or the user directly.
- **Draft description:**
  > Runs the code reviewers listed in review-lanes.yaml on a diff and reports each separately with blocking and advisory findings. Use when reviewing a slice, fix or enabler PR for code issues.
- **Should trigger:**
  - "review the code of this slice"
  - "code lane on PR 12"
  - "check conventions and spec on my branch"
- **Should not trigger:**
  - "check accessibility"
  - "is this GDPR-compliant"
  - "review the PRD before the design gate"
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

- Reads its reviewer list from the `code` lane of `review-lanes.yaml`, so adding a reviewer is a configuration change [R4-Q7a].
- Reviewers: mattpocock `code-review` (standards and spec), `pr-review-toolkit` agents (hidden failures, test coverage, type design), `check-bdd-conventions`, `check-i18n-conventions`, the diff-coverage check (advisory below 80%) [R4-Q7a, R14-Q3].
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
- Pinned agent names in `pr-review-toolkit` to confirm when pinning (chapter 11).
