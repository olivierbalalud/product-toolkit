---
name: review-privacy
status: outline
priority: P1
owner: <name>
serves: Security and privacy lane
decisions: [R4-Q7a, R4-Q9, R9-Q2, R21-Q1, R23-Q3]
plugin_version:
---

# review-privacy

## 0. Header

Reviews a diff for privacy by design against the PRD's privacy inventory, French tracker rules and the GDPR.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- Accepts personal data in logs or analytics properties.
- Misses an event marked `consent: exempt` that doesn't meet every CNIL condition.
- Lets a dimension snapshot carry personal data.

## 2. Scope

- **Does:** checks the diff against PRD §11 and §11b: data minimisation, retention and erasure paths, no personal data in logs, responses limited to their purpose; every tracking-plan property's privacy class and each event's consent value; history capture of `as-at-event` dimensions [R4-Q9, R9-Q2, R21-Q1, R23-Q3].
- **Does not:** give legal advice, decide on a DPIA, or write the privacy tests.
- **Neighbouring skills:** `review-security` runs it; the [GDPR one-pager](../foundations/gdpr-one-pager.md) is its reference.

## 3. Invocation

- **Invoked by:** the model, as a reviewer in its lane, or the user directly.
- **Draft description:**
  > Reviews code and the tracking plan for GDPR and CNIL privacy rules: personal data in logs and analytics, consent for trackers, retention and erasure. Use when a diff touches personal data, events or AI features.
- **Should trigger:**
  - "privacy review of this slice"
  - "does this event need consent"
  - "check personal data handling in PR 9"
- **Should not trigger:**
  - "check WCAG contrast"
  - "review the Gherkin style"
  - "refresh the Vercel guidelines"
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

- Preloads a reference file summarising the GDPR one-pager and the CNIL audience-measurement conditions.
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

- Whether CNIL guidance is pinned as a local reference copy (like the Vercel guidelines) or cited by link only.
