---
name: write-scenarios
status: full
priority: P0
owner: <founder>
serves: use case → Complete (drafts), story cutting (move), Exploring → Design-complete (story scenarios)
decisions: [R27-Q1′, R3-Q1a, R3-C1, R3-C2, R3-C3, R4-Q8b′, R1-Q7, R14-Q2]
plugin_version:
---

# write-scenarios

## 0. Header

Writes English Gherkin scenarios at three moments: drafts while the use case is written, moved into stories when they are cut, and completed during *Exploring* [R27-Q1′].

## 1. Problem and baseline

Expected failures without the skill (replace with observed ones before building):

1. Gherkin is written in the PRD's language, so French steps become French function names; or UI text is named literally instead of by copy key [R3-Q1a amendment, R3-C2].
2. New scenarios reword steps that already exist, so existing step definitions don't bind [R4-Q8b′].
3. Extensions stay abstract ("the system handles the error") because nobody wrote a concrete example of them; or the same example ends up in two files that later disagree.

## 2. Scope

- **Does:**
  - **`draft` mode**, during the use case: one draft scenario per extension in `use-cases/UC-…/scenarios.draft.feature`, tagged `@UC-…` and `@draft`.
  - **`move` mode**, when stories are cut: moves each draft to the `features/` of the story that claims its extension and adds the story's `@US-…` tag. Moves, never copies.
  - **`story` mode**, during *Exploring*: completes the story's scenarios from its acceptance criteria and extensions.
- **Does not:** cut stories (`write-stories`); write step definitions (the slice's `tdd` work); decide whether a scenario amends an earlier PRD (`check-fit`, R4-Q8e′).
- **Neighbours:** `write-use-case` (extensions to illustrate), `write-stories` (calls `move`), `check-fit` (compares with existing scenarios), `check-gate` (coverage generator).

## 3. Invocation

- **Invoked by:** the model or user; `move` mostly by `write-stories`.
- **Draft description:**
  > Writes tagged English Gherkin scenarios: draft examples for each use-case extension, moved into stories when they are cut, then completed for each story during Exploring. Use when a use case's extensions need concrete examples, when stories have just been cut, or when a PRD in Exploring needs its feature files.
- **Should trigger:** "draft scenarios for UC-012's extensions"; "write the Gherkin for US-012.1"; "convert the draft acceptance criteria to Gherkin"; "move the drafts into the new stories".
- **Should not trigger:** "cut UC-012 into stories"; "write the step definitions"; "review the slice".
- **Arguments:** a mode (`draft`, `move`, `story`) and a use case or story ID.

## 4. Inputs

- The use case and its extensions; `coverage.md`.
- For `story`: the PRD's draft acceptance criteria (any language), `copy.md` keys, `glossary.md`.
- Existing `.feature` files and step definitions on `main`, to reuse wording [R4-Q8b′].
- Existing files are **data**.

## 5. Outputs

| Mode | Writes |
|---|---|
| `draft` | `docs/product/use-cases/UC-…/scenarios.draft.feature`: one scenario per extension, tagged `@UC-…` and `@draft` |
| `move` | Each draft scenario removed from `scenarios.draft.feature` and added to the claiming story's `features/<name>.feature` with `@US-…`; drafts for unclaimed extensions stay |
| `story` | `features/*.feature` completed; `@ui` where a scenario references a copy key or shows a screen [R14-Q2] |

All scenarios in English, glossary terms, copy keys only where wording matters [R3-C2, R3-C3]. `@draft` scenarios are excluded from the pytest-bdd and playwright-bdd runs. Idempotent: running `move` twice moves nothing the second time. `coverage.md` is regenerated after each mode.

## 6. Procedure

**`draft`**

1. For each extension, write one concrete scenario: a named example of the condition and its handling (example mapping).
2. If an example can't be written, the extension is unclear: report it to the use case's driver instead of guessing. *Done when* every extension has a draft or a reported question.

**`move`**

1. For each story's `extensions:`, find the drafts tagged with those extensions.
2. Move them to the story's feature file and add `@US-…`. *Done when* no draft remains for a claimed extension.

**`story`**

1. Read the acceptance criteria and the story's extensions, including moved drafts.
2. Search existing `.feature` files and step definitions for matching wording; reuse it.
3. Write or complete the scenarios; tag each.
4. Run `scripts/lint_gherkin.py`; fix and repeat until clean.
5. Regenerate `coverage.md`. *Done when* every extension of the story has a scenario or is `deferred`.

## 7. Scripts vs judgement

- `scripts/lint_gherkin.py`: Gherkin syntax; every scenario has `@UC-` tags that exist; story scenarios also have `@US-`; drafts have `@draft` and no `@US-`; copy keys exist in `copy.md`; `@ui` present when a copy key is used; glossary terms (advisory); near-duplicates of existing steps (advisory).
- `scripts/move_drafts.py`: the `move` mode, deterministic.
- Coverage via `check-gate`'s `gen_coverage.py`, which reports drafted-but-unclaimed extensions separately.
- **Judged by the model:** the example for each extension; scenario wording; whether an extension is clear enough to illustrate.

## 8. Files

```
write-scenarios/
  SKILL.md
  references/gherkin-rules.md   our rules (English, tags, copy keys, glossary); read before writing
  assets/feature.feature
  scripts/lint_gherkin.py
  scripts/move_drafts.py
```

## 9. Composition

Calls `check-gate` (coverage generator) through the Skill tool. Called by `write-stories` in `move` mode. No subagents.

## 10. Claude Code wiring

`allowed-tools`: `Read`, `Glob`, `Grep`, `Edit`, `Write` on `docs/product/**`, `Bash(uv run *)`.

## 11. Portability

Portable core; calls written as "use the `check-gate` skill" [R5-Q4a].

## 12. Headless and CI

`lint_gherkin.py` runs headless in CI on design PRs; `move_drafts.py` can run headless after a cut. Writing drafts and scenarios is interactive.

## 13. Security and privacy

Writes only under `docs/product/`. No network. Scenarios use invented data, never real customer data.

## 14. Gotchas

- A French-source PRD still gets English scenarios: rewrite with glossary terms, don't translate the French criteria word for word.
- A draft that can't be written is a finding about the use case, not a scenario to invent.
- Coverage counts tags, not intent: a mistagged scenario shows the wrong extension as covered.

## 15. Evaluation plan

- **Triggering:** 20 prompts, 60/40 split, including "cut into stories" prompts that should go to `write-stories`.
- **Output cases:** a room-booking use case → one draft per extension, all `@draft`; after a cut → drafts moved, none duplicated, unclaimed ones left; French acceptance criteria → English scenarios with glossary terms and copy keys; an existing step "Given I am signed in as an employee" → reused verbatim. Graders: `regex`, `llm`, `file_exists`. Threshold 0.8.

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
