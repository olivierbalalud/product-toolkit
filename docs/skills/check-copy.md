---
name: check-copy
status: outline
priority: P1
owner: <name>
serves: UX lane; copy deck at the design gate
decisions: [R2-Q6, R2-Q7, R3-D6, R1-Q4]
plugin_version:
---

# check-copy

## 0. Header

Checks UI copy against our voice guide, in every locale, including French typography.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- Accepts *tu* or *points médians* in French copy.
- Misses the non-breaking space before `: ; ! ?`.
- Lets raw keys appear where readable copy should be.

## 2. Scope

- **Does:** checks the copy deck and catalogs against `docs/design/voice-and-tone.md`: shared core plus per-locale rules (*vous*, epicene wording, French typography, ~30% expansion budget); flags raw keys in prototypes [R2-Q7, R1-Q4].
- **Does not:** translate (`translate-copy`), or apply the Vercel writing rules where our guide differs [R3-D6].
- **Neighbouring skills:** Runs beside `ux-copy` in the UX lane; precedence is our voice guide > Vercel writing > Vercel web [R3-D6].

## 3. Invocation

- **Invoked by:** the model, as a reviewer in its lane, or the user directly.
- **Draft description:**
  > Checks UI copy and message catalogs against the product's voice guide, including French typography and inclusive wording. Use when reviewing a copy deck, catalogs or prototype screens.
- **Should trigger:**
  - "check the copy deck against our voice"
  - "review the French strings"
  - "is this error message on-voice"
- **Should not trigger:**
  - "translate the copy to English"
  - "check contrast ratios"
  - "review the API"
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

- Typography checks (non-breaking spaces) run as a script; tone is judged by the model.
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

- Whether the typography script also runs as a lint in CI, outside the lane.
