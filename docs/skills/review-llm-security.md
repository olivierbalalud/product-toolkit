---
name: review-llm-security
status: outline
priority: P1
owner: <name>
serves: Security and privacy lane, AI paths only
decisions: [R12-Q6b, R12-Q6c, R14-Q5]
plugin_version:
---

# review-llm-security

## 0. Header

Reviews AI features against the OWASP Top 10 for LLM Applications (2026 edition).

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- Misses prompt injection through user or third-party content.
- Accepts unbounded model output reaching the UI or tools unchecked.
- Doesn't notice an AI feature without an eval set.

## 2. Scope

- **Does:** reviews diffs under the LLM gateway or AI feature paths against the OWASP Top 10 for LLM Applications 2026; checks that PRD §11b lists an eval set with a threshold [R12-Q6b, R14-Q5].
- **Does not:** run the evals, or review non-AI code.
- **Neighbouring skills:** `review-security` runs it only when AI paths change; the Eng persona does the design-time prompt-injection check [R12-Q6c].

## 3. Invocation

- **Invoked by:** the model, as a reviewer in its lane, or the user directly.
- **Draft description:**
  > Reviews changes to AI features and the LLM gateway against the OWASP Top 10 for LLM Applications. Use when a diff touches prompts, model configuration, the LLM gateway or code handling model output.
- **Should trigger:**
  - "review the LLM feature for security"
  - "OWASP LLM check on this prompt change"
  - "is this agent tool use safe"
- **Should not trigger:**
  - "review the login form"
  - "check the tracking plan"
  - "run unit tests"
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

- Preloads a pinned local summary of the OWASP LLM Top 10 2026 (see [security, privacy and AI](../foundations/security-privacy-ai.md)).
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

- The exact paths of the LLM gateway and AI features, so the lane rule can trigger it.
- Whether the OWASP agentic Top 10 is added for agent features.
