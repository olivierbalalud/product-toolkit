---
name: check-bdd-conventions
status: outline
priority: P1
owner: <name>
serves: Code lane; design gate
decisions: [R3-Q1a, R3-C1, R3-C2, R3-C3, R14-Q2]
plugin_version:
---

# check-bdd-conventions

## 0. Header

Checks Gherkin and pytest-bdd step definitions against the framework's conventions.

## 1. Problem and baseline

*Expected, to be observed* before building [R25-Q4]:

- Accepts French Gherkin or French step names.
- Misses a scenario without `@US`/`@UC` tags, or a copy key without `@ui`.
- Accepts domain words not in the glossary.

## 2. Scope

- **Does:** checks `.feature` files (English only, tags, glossary terms, copy keys only where wording matters, `@ui` rules) and step definitions (reuse of existing wording, fakes at the business layer) [R3-Q1a, R3-C2, R3-C3, R14-Q2].
- **Does not:** write scenarios (`write-stories`) or run tests.
- **Neighbouring skills:** `write-stories` writes; this checks. In the code lane and before the design gate.

## 3. Invocation

- **Invoked by:** the model, as a reviewer in its lane, or the user directly.
- **Draft description:**
  > Checks Gherkin feature files and pytest-bdd step definitions against the project's BDD conventions: English only, tags, glossary terms, copy keys, @ui rules. Use when feature files or step definitions change.
- **Should trigger:**
  - "check my feature files"
  - "are these Gherkin scenarios tagged right"
  - "review the step definitions"
- **Should not trigger:**
  - "write the use case"
  - "check French typography"
  - "review the prototype"
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

- Tag, `@ui` and vocabulary checks are a script (also used by `check-gate`); wording and reuse are judged.
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

- Whether the step-vocabulary check lives here or in `check-gate`.
