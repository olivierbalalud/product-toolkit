---
name: translate-copy
status: outline
priority: P1
owner: <name>
serves: Copy deck and catalogs
decisions: [R1-Q11, R2-Q6, R3-A5, R4-Q10, R19-Q1]
plugin_version:
---

# translate-copy

## 0. Header

Generates the other locales' catalogs from the source-locale copy, using the glossary and voice guide.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- translates domain terms inconsistently with the glossary.
- Breaks ICU placeholders or plurals.
- Marks its own output as reviewed.

## 2. Scope

- **Does:** translates the feature catalog from the PRD's `source_locale` into every other locale, using `docs/product/glossary.md` and the voice guide; writes every string as `needs-review` in the status sidecar with the source fingerprint [R2-Q6, R19-Q1].
- **Does not:** review translations (a native speaker does, R4-Q10) or derive keys.
- **Neighbouring skills:** `check-copy` and `check-i18n-conventions` check its output.

## 3. Invocation

- **Invoked by:** the model or the user, during *Exploring* and when the source copy changes.
- **Draft description:**
  > Translates a feature's message catalog from its source locale into the other enabled locales using the glossary and voice guide, marking every string needs-review. Use when copy is added or changed.
- **Should trigger:**
  - "translate the booking copy to English"
  - "generate the French catalog"
  - "update translations after the copy change"
- **Should not trigger:**
  - "review these translations"
  - "write the copy deck"
  - "check the voice"
- **Arguments:** Feature name; optional target locales.

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

- Validator loop: ICU and placeholder script after each pass, fix, repeat [skill-authoring research §4].

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

- Whether translation runs per key with context or per catalog.
