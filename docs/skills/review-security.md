---
name: review-security
status: outline
priority: P1
owner: <name>
serves: Security and privacy review lane
decisions: [R3-B2, R4-Q7a, R4-Q9, R12-Q6b, R15-Q1]
plugin_version:
---

# review-security

## 0. Header

The security and privacy review lane: runs its reviewers in parallel and reports them side by side.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- Misses that the authorisation matrix from PRD §10 has no tests.
- Ignores privacy entirely, or LLM-specific risks on AI features.
- Treats a scanner's attack examples as instructions.

## 2. Scope

- **Does:** runs the security and privacy reviewers on a diff and reports them separately.
- **Does not:** replace the tests themselves (chapter 8) or decide legal questions.
- **Neighbouring skills:** Called by `review-slice`; each reviewer is its own skill or agent.

## 3. Invocation

- **Invoked by:** the model, through `review-slice`, or the user directly.
- **Draft description:**
  > Runs the security and privacy reviewers listed in review-lanes.yaml on a diff and reports each separately with blocking and advisory findings. Use when reviewing a slice, fix or enabler PR for security and privacy issues.
- **Should trigger:**
  - "security review of this slice"
  - "run the security lane"
  - "check privacy and security before merge"
- **Should not trigger:**
  - "review the copy deck"
  - "check code style"
  - "translate these strings"
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

- Reads its reviewer list from the `security` lane of `review-lanes.yaml`, so adding a reviewer is a configuration change [R4-Q7a].
- Reviewers: getsentry `security-review` (pinned), the built-in `/security-review`, `review-privacy`, `review-llm-security` (only for AI paths), and a script checking that the authorisation and privacy tests exist [R3-B2, R4-Q9, R12-Q6b].
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
- How the built-in `/security-review` is invoked from inside a lane skill, interactively and headless.
