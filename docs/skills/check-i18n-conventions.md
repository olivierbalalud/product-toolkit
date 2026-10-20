---
name: check-i18n-conventions
status: outline
priority: P1
owner: <name>
serves: Code lane
decisions: [R2-Q6, R3-Q4, R19-Q1, R19-Q2]
plugin_version:
---

# check-i18n-conventions

## 0. Header

Checks next-intl usage, message catalogs and their review-status sidecars.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- Accepts hard-coded strings in components.
- Misses a translation whose source changed but stays `reviewed`.
- Accepts `useExtracted`.

## 2. Scope

- **Does:** checks semantic keys, one catalog per feature per locale, ICU syntax and placeholders, no hard-coded UI strings, no `useExtracted`, the status sidecars and `locales.ts` [R2-Q6, R3-Q4, R19-Q1, R19-Q2].
- **Does not:** translate or judge tone.
- **Neighbouring skills:** `translate-copy` writes catalogs; `check-copy` judges voice.

## 3. Invocation

- **Invoked by:** the model, as a reviewer in its lane, or the user directly.
- **Draft description:**
  > Checks next-intl usage and message catalogs: semantic keys, ICU messages, placeholders, review status and enabled locales. Use when components, catalogs or locale settings change.
- **Should trigger:**
  - "check i18n in this PR"
  - "are the catalogs valid"
  - "any hard-coded strings"
- **Should not trigger:**
  - "translate to French"
  - "is this copy on-voice"
  - "check the database schema"
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

- ICU and placeholder validation and the sidecar hash check are scripts shared with CI.
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

- Which linter rule catches hard-coded strings in TSX.
