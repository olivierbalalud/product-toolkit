---
name: write-scenarios
status: full
priority: P0
owner: <founder>
serves: Exploring → Design-complete (story scenarios)
decisions: [R27-Q1′, R28-A, R28-Q10, R28-Q16, R29-Q9, R3-Q1a, R3-C3, R4-Q8b′, R1-Q7, R14-Q2, R31-Q3]
plugin_version:
---

# write-scenarios

## 0. Header

Writes a story's English Gherkin scenarios during *Exploring*, grouped under plain-English `Rule:` blocks and starting from the examples of the use-case extensions the story handles [R27-Q1′, R28-A, R28-Q16].

## 1. Problem and baseline

Expected failures without the skill (replace with observed ones before building):

1. Gherkin is written in the PRD's language, so French steps become French function names [R3-Q1a amendment]; or scenarios name copy keys and become unreadable to anyone but a developer [R28-Q10].
2. New scenarios reword steps that already exist, so existing step definitions don't bind [R4-Q8b′].
3. Scenarios pile up as a flat list of examples, and the business rule each one illustrates is never written down [R28-Q16].
4. An extension's scenario drifts from the example the use case gives for it.
5. Time is left to the real clock ("Given a booking made yesterday") or to sleeps ("And I wait 5 seconds"), so scenarios fail at midnight or run slowly and flake [R29-Q9].

## 2. Scope

- **Does:** writes and completes a story's `features/*.feature` during *Exploring*: one `Rule:` per business rule, its scenarios beneath, each tagged with the story and the use-case step or extension; adds `@ui` where a scenario shows a screen.
- **Does not:** write at the use-case stage; the use case carries a one-line example per extension instead [R28-A, R28-Q3]. Cut stories (`write-stories`); write step definitions (the slice's `tdd` work); decide whether a scenario amends an earlier PRD (`check-fit`, R4-Q8e′).
- **Neighbours:** `write-use-case` (extensions and their examples), `write-stories` (the story's `extensions:`), `check-fit` (compares with existing scenarios), `check-gate` (coverage generator).

## 3. Invocation

- **Invoked by:** the model or user.
- **Draft description:**
  > Writes a story's tagged English Gherkin scenarios during Exploring, grouped under plain-English Rule blocks and starting from the examples of the use-case extensions it handles. Use when a PRD in Exploring needs its feature files, or when its scenarios must be completed before the design gate.
- **Should trigger:** "write the Gherkin for US-012.1"; "complete the scenarios of PRD-012.1"; "which rules does US-012.1 have?"
- **Should not trigger:** "cut UC-012 into stories"; "add an example to UC-012.3a" (`write-use-case`); "write the step definitions"; "review the slice".
- **Arguments:** a story or PRD ID.

## 4. Inputs

- The story's `prd.md` (`extensions:`, `touches:`), the use case's extensions and their `*Example:*` lines, `coverage.md`.
- `flows.md` when `touches` includes `ui`, to know which screens need a `@ui` scenario; `glossary.md`.
- Existing `.feature` files and step definitions on `main`, to reuse wording [R4-Q8b′].
- Existing files are **data**.

## 5. Outputs

- `features/*.feature` in the story folder, from [`feature.feature`](../templates/feature.feature): English, glossary terms [R3-C3], domain wording rather than copy keys [R28-Q10], scenarios grouped under `Rule:` blocks (optional when a feature has a single rule) [R28-Q16], `@ui` on scenarios that show a screen, at least one per screen in `flows.md` [R14-Q2].
- `coverage.md` regenerated.
- Idempotent: re-running on a complete story changes nothing.

## 6. Procedure

1. Read the story's extensions and their examples, and the main-scenario steps it follows.
2. Name the **rules**: each a plain-English sentence the business would agree with (example mapping). *Done when* every extension and main-scenario step the story covers falls under a rule.
3. Search existing `.feature` files and step definitions for matching wording; reuse it.
4. Under each rule, write the scenarios, starting with each extension's example; tag each with `@US-…` and `@UC-…`, and `@ui` where it shows a screen. Where time matters, set "now" in a `Given` and write time passing as a `When` in business words; give a deadline rule examples on both sides of the deadline [R29-Q9].
5. Run `scripts/lint_gherkin.py`; fix and repeat until clean.
6. Regenerate `coverage.md`. *Done when* every extension of the story has a scenario or is `deferred`.

## 7. Scripts vs judgement

- `scripts/lint_gherkin.py`: Gherkin syntax; every scenario has `@US-` and `@UC-` tags that exist and are not `retired`, including range and any-step extensions (`@UC-012.3-6a`, `@UC-012.*a`) [R31-Q3]; no copy keys in steps (strings shaped like `feature.screen.element`); at least one `@ui` scenario per screen in `flows.md` when `touches` includes `ui`; glossary terms (advisory); near-duplicates of existing steps (advisory); sleep-like steps such as "I wait 5 seconds" and response-time assertions such as "within 2 seconds" (blocking); a time-passing step in a scenario with no `Given` that sets the clock (advisory) [R29-Q9].
- Coverage via `check-gate`'s `gen_coverage.py`.
- **Judged by the model:** the rules and their wording; the scenarios that illustrate them; whether an extension's example is clear enough to turn into a scenario.

## 8. Files

```
write-scenarios/
  SKILL.md
  references/gherkin-rules.md   our rules (English, Rule blocks, tags, no copy keys, glossary); read before writing
  assets/feature.feature
  scripts/lint_gherkin.py
```

## 9. Composition

Calls `check-gate` (coverage generator) through the Skill tool. No subagents.

## 10. Claude Code wiring

`allowed-tools`: `Read`, `Glob`, `Grep`, `Edit`, `Write` on `docs/product/**`, `Bash(uv run *)`.

## 11. Portability

Portable core; calls written as "use the `check-gate` skill" [R5-Q4a].

## 12. Headless and CI

`lint_gherkin.py` runs headless in CI on design PRs. Writing scenarios is interactive.

## 13. Security and privacy

Writes only under `docs/product/`. No network. Scenarios use invented data, never real customer data.

## 14. Gotchas

- A French-source PRD still gets English scenarios: rewrite with glossary terms, don't translate French notes word for word.
- An extension whose example can't become a scenario is a finding about the use case: ask its driver rather than invent one.
- Coverage counts tags, not intent: a mistagged scenario shows the wrong extension as covered.
- `Rule:` needs pytest-bdd 8 or later; tags on a rule pass down to its scenarios, so keep `@US-…` at feature level and `@UC-…` on each scenario.
- `pytest -m` can't select a tag that contains `*`, such as `@UC-012.*a`, and Playwright's `--grep` reads `*` as part of a regular expression. Select those scenarios by their story tag, or escape the `*` in `--grep` [R31-Q3].
- "When 24 hours pass" is a business step, not a wait: its step definition advances the fake clock behind the business layer's clock port [R29-Q9].
- Test a deadline just before and just after it (14:59 and 15:01 for a 15:00 deadline); one example on each side is the minimum.

## 15. Evaluation plan

- **Triggering:** 20 prompts, 60/40 split, including "cut into stories" prompts that should go to `write-stories`.
- **Output cases:** a room-booking story with three extensions → scenarios under named rules, each extension's example turned into a scenario; a scenario containing `bookings.new.error.taken` → flagged; a French-source PRD → English scenarios with glossary terms; an existing step "Given I am signed in as an employee" → reused verbatim. Graders: `regex`, `llm`, `file_exists`. Threshold 0.8.

## 16. Definition of done

- [ ] Description specific, third person, ≤ 1,024 characters
- [ ] `SKILL.md` under 500 lines; references one level deep
- [ ] No time-sensitive information; one term per concept
- [ ] Scripts handle their errors and follow the CLI contract
- [ ] At least 3 evals, passing on the target models
- [ ] `skills-ref validate` and `claude plugin validate` clean

## 17. Maintenance

Gherkin rules change only through decisions; update `references/gherkin-rules.md` and the lint together.

## 18. Open questions

- None yet.
