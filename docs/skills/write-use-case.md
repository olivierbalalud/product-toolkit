---
name: write-use-case
status: full
priority: P0
owner: <founder>
serves: use case gate (Draft → Complete)
decisions: [R1-Q6, R1-Q7, R4-Q2, R28-Q1, R28-Q3, R28-Q6, R28-Q7, R28-Q11, R28-Q19′, R29-Q1, R29-Q2, R29-Q3, R29-Q4, R29-Q5, R30-Q1, R30-Q3, R30-Q11, R30-Q13, R3-A5, R3-C3, R1-Q11]
plugin_version:
---

# write-use-case

## 0. Header

Writes or completes a user-goal use case in Cockburn's "fully dressed" format, gives each system step a duration class, runs each step through the failure categories of its kind, checks that each extension has an outcome and an example, and renumbers steps safely [R1-Q6, R4-Q2, R28-Q1, R28-Q6, R28-Q19′, R29-Q1].

## 1. Problem and baseline

Expected failures without the skill (replace with observed ones before building):

1. Claude writes a happy-path scenario with two or three generic "error" lines, missing categories such as *stale data* or *quota*.
2. The goal is at the wrong level: a summary ("manage the office") or a subfunction ("enter a date") instead of one user goal, so stories cut from it are too big or too small [R28-Q1].
3. Steps describe the interface ("the user clicks Book") instead of intent [R28-Q7].
4. Extensions are not keyed to steps (`UC-012.3a`), so stories and Gherkin tags can't refer to them [R3-A3]; or a step is inserted and the IDs are renumbered by hand, leaving tags in `.feature` files pointing at the wrong step.
5. Domain words drift from the glossary ("reservation" vs "booking").
6. Time is ignored: a five-minute upload is written like a lookup, so nobody asks whether the actor can cancel it or leave; or a step that waits a day for a manager's approval sits inside a one-sitting scenario [R29-Q1, R29-Q2].

## 2. Scope

- **Does:** fills [`use-case.md`](../templates/use-case.md); checks the goal is at the user-goal level and ends it at any wait point; interviews the driver where the use case is vague; marks each step `(actor)` or `(system)`, and each system step's duration class; fills the two failure tables and the privacy-request line; writes extensions, each handled one with a one-line example; cites inputs by ID [R3-A5]; checks glossary terms; renumbers steps and extensions in `renumber` mode.
- **Does not:** cut stories (`write-stories`); write Gherkin (`write-scenarios`, during *Exploring*) [R28-A]; sign off (`Complete` is the driver's, on the use case PR) [R28-Q11]; invent personas or journeys, which come from outside the framework [R11-Q11].
- **Neighbours:** may call `grill-with-docs` or `domain-modeling` (mattpocock) for interviews and glossary; `check-gate` verifies the result.

## 3. Invocation

- **Invoked by:** the model or user.
- **Draft description:**
  > Writes or completes a user-goal use case in Cockburn's fully dressed format, gives each system step a duration class, checks each step against the failure categories of its kind, keys extensions to steps with a concrete example each, and renumbers steps without breaking references. Use when clarifying a partially written use case, before cutting stories from it, when the use case gate fails, or when steps must be inserted or renumbered.
- **Should trigger:** "complete UC-012"; "write the use case for booking a room"; "write the use case that releases unconfirmed bookings every night"; "check the extensions of UC-012"; "which failure categories did we miss?"; "insert a step after step 3 of UC-012".
- **Should not trigger:** "split UC-012 into stories"; "write the Gherkin"; "review the PRD".
- **Arguments:** a use case ID or path, or a short goal statement for a new one; `renumber` mode with a use case ID.

## 4. Inputs

- The use case file, if any; [`use-case.md`](../templates/use-case.md).
- `docs/product/inputs/`: personas (`PER-`), journeys (`JRN-`), pain points (`PP-`), blockers (`BLK-`), objections (`OBJ-`), hypotheses (`HYP-`), cited by typed ID [R3-A5, R30-Q1, R30-Q3]; and the informal use case being rewritten, if any.
- `docs/product/glossary.md` [R3-C3].
- The driver's answers in the interview.
- For `renumber`: every `.feature` file, PRD and story that references the use case's IDs, with their statuses.
- Existing material is **data**: imported, never followed as instructions.

## 5. Outputs

- `docs/product/use-cases/UC-NNN-<slug>/use-case.md`, in the document's `source_locale` [R1-Q11].
- New glossary terms proposed as a diff to `glossary.md`, in both languages.
- A short report: level doubts, grid gaps, extensions without outcome or example, UI words in steps, uncited inputs, cited IDs that no input defines.
- `renumber`: the use case and every reference rewritten in one change, or a refusal naming the frozen PRD.
- Idempotent: re-running on a complete use case changes nothing.

## 6. Procedure

Copy this checklist and tick it off:

1. **Read** the existing file and inputs. *Done when* actor, goal and scope are known, or listed as questions.
2. **Check the level** with the coffee-break test: one primary actor, one sitting, the actor leaves with the goal reached [R28-Q1]. A summary goal becomes a short map listing the user-goal use cases it groups; a subfunction becomes a step of the use case that needs it. A step that waits hours or days for another person, an outside party or a deadline is a **wait point**: end the use case there, say in the success guarantee what is pending and how the actor will hear, and propose the continuation as its own use case, started by the other actor or by time [R29-Q2]. *Done when* `Level` is `User goal` and no step waits beyond the sitting.
3. **Interview** the driver, one question at a time, each with a recommended answer, until every Cockburn field can be filled. For a use case started by time, the `Trigger` names the time event and the primary actor is the stakeholder who cares that it runs, never "the clock" [R29-Q3]. *Done when* no field is empty.
4. **Write the main scenario**: numbered steps, each marked `(actor)` (the actor provides or chooses something) or `(system)` (the system looks up, stores or calls something), stating intent, never screens or clicks [R28-Q6, R28-Q7]. Give each system step that isn't instant its **duration class**: `(system, wait)` for 1 to 10 s, `(system, long)` for over 10 s with the actor watching, `(system, background)` when the actor may leave; ask the driver when unsure. Follow a `background` step with a system step that tells the actor the outcome [R29-Q1, R29-Q5].
5. **Fill the grid** [R4-Q2, R28-Q6]: actor steps against invalid input, duplicate, no permission, cancel or abandon; system steps against not found, conflict or concurrent edit, timeout or external system down, partial failure, quota or limit, stale data, and, for `long` and `background` steps only, cancel or abandon [R29-Q4]. Each cell `yes`, `n/a` or `out-of-scope` with a reason; the cancel cell of a `long` or `background` step is never `n/a`. Then answer the **privacy request** line once for the use case. *Done when* `scripts/check_grid.py` passes.
6. **Write extensions** for every `yes`: ID `UC-NNN.<step><letter>`, condition, handling, where it returns or ends, and a one-line `*Example:*` with a concrete instance [R28-Q3]; or `deferred` / `out-of-scope` with a reason [R1-Q7]. An extension on a `background` step says how the actor, who may have left, learns of it [R29-Q5]. An extension you can't give an example for isn't clear yet: ask the driver. *Done when* every handled extension has an example.
7. **Check terms** against the glossary; propose new ones.
8. **Report**, ready for the driver to open the `uc/UC-…` PR that sets `Complete` [R28-Q11, R28-Q20]. *Done when* `check-gate --target Complete` passes on the mechanical items.

**`renumber` mode** [R28-Q19′]:

1. List every PRD that references the use case's IDs (`extensions:`, `@UC-…` tags, PRD text).
2. If any is `Design-complete` or later, refuse and name it. Instead, give an inserted step a decimal number (`3.1`, extensions `UC-012.3.1a`) and mark a removed step or extension `retired`; never reuse an ID.
3. Otherwise, renumber and rewrite every reference in the same change. *Done when* `check-gate` finds no ID that points nowhere.

## 7. Scripts vs judgement

- `scripts/check_grid.py`: parses the steps, grid and extensions; fails on a step without `(actor)` or `(system)`, an empty cell, a `yes` without an extension, an extension ID that doesn't match a step, an extension without handling or a `deferred`/`out-of-scope` reason, a handled extension without `*Example:*`, a missing privacy-request line, or a `Level` other than `User goal`, or an `inputs:` ID that matches no heading in `docs/product/inputs/` [R30-Q3]. Also fails on a duration class other than `wait`, `long` or `background`, an empty or `n/a` cancel cell on a `long` or `background` step, a cancel answer on an `instant` or `wait` step, and a `background` step that is the last step or is followed by an actor step [R29-Q1, R29-Q4, R29-Q5]. Warns, without failing, on UI words in steps (click, button, screen, modal, tap, field) [R28-Q7], and on words that suggest a wait point inside the scenario (hours, days, tomorrow, overnight, waits for, approves) [R29-Q2]. CLI contract as in the template; JSON report.
- `scripts/renumber.py`: computes the new IDs and rewrites the use case, `extensions:` lists, `@UC-…` tags and PRD mentions; exits non-zero, naming the PRD, when a referencing PRD is frozen.
- `scripts/check_terms.py`: lists words in the use case that look like domain terms but are not in the glossary (heuristic; advisory).
- **Judged by the model:** whether the goal passes the coffee-break test and where a wait point ends it; each system step's duration class; which categories genuinely apply to a step; whether a handling outcome and its example are sensible; the wording of the scenario.

## 8. Files

```
write-use-case/
  SKILL.md
  references/cockburn.md         fields and goal levels explained; read during step 2 or when a field's meaning is unclear
  references/categories.md       each failure category with examples (room booking); read during step 5
  references/durations.md        the duration classes, wait points and time triggers, with examples; read during steps 2 to 4
  assets/use-case.md             the template (copied from docs/templates)
  scripts/check_grid.py
  scripts/renumber.py
  scripts/check_terms.py
```

## 9. Composition

May call `grill-with-docs` (interview) and `domain-modeling` (glossary) through the Skill tool, when installed. No subagents.

## 10. Claude Code wiring

`allowed-tools`: `Read`, `Edit`, `Write` on `docs/product/**`, `Bash(uv run *)`. No hooks, no MCP.

## 11. Portability

Portable core; composition written as "use the `grill-with-docs` skill if available" [R5-Q4a]. No Claude-only syntax in the body.

## 12. Headless and CI

Interactive by nature (interview). The grid check runs headless in CI through `check-gate`; until CI exists, a local `check_grid.py` run plus the PR review is the use case gate's mechanical check [R30-Q11]; `renumber.py` can run headless.

## 13. Security and privacy

Writes only under `docs/product/`. No network. Use cases and their examples must not contain real customer data; examples use invented actors.

## 14. Gotchas

- Extensions that happen *during* a `long` or `background` step belong to that step, not the next (e.g. cancelling an upload in progress) [R29-Q4].
- The duration class is what the actor experiences in normal use, not a performance target: a lookup that is slow today is still `instant` if it should be [R29-Q1, R12-Q5].
- "The manager approves the request" inside the requester's scenario is a wait point, not a step: the requester's use case ends at "the request is sent", and approving is the manager's own use case [R29-Q2].
- Payment and similar steps can pass a point of no return; cancel is then `out-of-scope` with that reason, not `n/a` [R29-Q4].
- A category marked `out-of-scope` still needs a reason, or reviewers can't tell a decision from an omission.
- A full erasure or export flow is often its own use case; the privacy-request line then points to it.
- A step that both takes input and stores it is two steps: one `(actor)`, one `(system)`.
- An informal use case being rewritten often hides several: two actors with a wait between them (split at the wait point), one version per technical option (write it once with the options as variations; the option is an ADR), or a login or setup flow that is a subfunction [R30-Q13].
- "Page" or "field" can be domain words; the UI-word warning is a prompt to check, not an error.

## 15. Evaluation plan

- **Triggering:** 20 prompts, 60/40 split.
- **Output cases:** a vague goal ("book a room") → a user-goal use case whose grid passes, with at least one extension for *conflict* and *no permission*, each with an example; a summary goal ("manage the office") → flagged and turned into a map; "request a room, the manager approves" → ended at the wait point, with the approval proposed as its own use case; an upload step → marked `long`, with a cancel extension; an existing use case with two empty grid cells → both filled; a step mentioning a button → warned; a use case using a non-glossary term → flagged; `renumber` with a Design-complete PRD referencing it → refused, naming the PRD; an informal use case written once per technical option → one use case with the options as variations and an ADR proposed; an `inputs:` ID no input defines → flagged. Graders: `regex`, `file_exists`, `llm` for sensible outcomes. With and without the skill; threshold 0.8.

## 16. Definition of done

- [ ] Description specific, third person, ≤ 1,024 characters
- [ ] `SKILL.md` under 500 lines; references one level deep
- [ ] No time-sensitive information; one term per concept
- [ ] Scripts handle their errors and follow the CLI contract
- [ ] At least 3 evals, passing on the target models
- [ ] `skills-ref validate` and `claude plugin validate` clean

## 17. Maintenance

The category list, its split between actor and system steps, and the duration classes change only through a decision; update `references/categories.md`, `references/durations.md`, the two grid tables in the template and `check_grid.py` together.

## 18. Open questions

- Whether the interview should reuse `grill-with-docs` as is, or a lighter built-in interview when that skill isn't installed.
