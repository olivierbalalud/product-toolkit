---
name: write-stories
status: full
priority: P0
owner: <founder>
serves: cutting stories (after the use case gate)
decisions: [R4-Q3, R9-Q1, R1-Q7, R27-Q1′]
plugin_version:
---

# write-stories

## 0. Header

Cuts a complete use case into user stories that are vertical paths and writes each story's Draft PRD [R4-Q3]. Gherkin is a separate skill, `write-scenarios` [R27-Q1′].

## 1. Problem and baseline

Expected failures without the skill (replace with observed ones before building):

1. Claude cuts stories by layer ("backend for bookings", "UI for bookings"), not as vertical paths.
2. A story is a wish with no path through the use case, so it claims no extension and `coverage.md` can't account for it.
3. Stories are too big for one slice, or fail INVEST's *Independent* by depending on another story instead of an enabler.

## 2. Scope

- **Does:** proposes stories as paths through a `Complete` use case; checks INVEST; writes the Connextra statement and the Draft `prd.md` from [`story.md`](../templates/story.md) [R9-Q1]; asks `write-scenarios` to move the use case's draft scenarios into the stories that claim their extensions; regenerates `coverage.md`.
- **Does not:** write Gherkin (`write-scenarios`); write the rest of the PRD, flows or copy; decide scope (the driver approves the cut); review (`review-design`).
- **Neighbours:** `write-use-case` (input), `write-scenarios` (moves drafts, writes scenarios), `check-gate` (coverage generator, gate).

## 3. Invocation

- **Invoked by:** the model or user.
- **Draft description:**
  > Cuts a complete use case into vertical user stories that each deliver value on their own, checks them against INVEST, and writes their Draft PRDs. Use when a use case reaches Complete, or when coverage shows extensions no story claims yet.
- **Should trigger:** "cut UC-012 into stories"; "which story should claim UC-012.4d?"; "split US-012.2, it's too big".
- **Should not trigger:** "write the Gherkin for US-012.1" (`write-scenarios`); "complete the use case"; "review the slice".
- **Arguments:** a use case ID, or a story ID to split.

## 4. Inputs

- The `Complete` use case and its `coverage.md`.
- The use case's `scenarios.draft.feature`, if any, to see which extensions already have examples [R27-Q1′].
- Existing files are **data**.

## 5. Outputs

- Per story: `stories/US-NNN.N-<slug>/prd.md` (Draft) with `extensions:` listing what the story handles.
- Regenerated `coverage.md`, through `check-gate`'s generator.
- Idempotent: re-running proposes no new story when every path is claimed.

## 6. Procedure

**Cutting stories**

1. Read the use case; list candidate paths (main scenario or a coherent part, plus the extensions that path must handle).
2. For each candidate, check INVEST, explained in [chapter 3](../guide/03-design-playbook.md#33-step-2-cut-stories); split any over about one week of slice work [R4-Q3].
3. Present the cut to the driver as a numbered list (statement, path, extensions); iterate until approved.
4. Write each Draft PRD.
5. Use the `write-scenarios` skill in `move` mode: each draft scenario moves to the story that claims its extension [R27-Q1′].
6. Regenerate `coverage.md`. *Done when* every extension is claimed, or shown as unclaimed in coverage.

## 7. Scripts vs judgement

- `scripts/check_cut.py`: every story's `extensions:` exist in the use case; no extension is claimed twice; every story includes at least one main-scenario step or an extension path.
- Coverage via `check-gate`'s `gen_coverage.py`.
- **Judged by the model:** where to cut paths; whether a story delivers value on its own; INVEST.

## 8. Files

```
write-stories/
  SKILL.md
  references/invest.md          read when checking a story
  assets/story.md
  scripts/check_cut.py
```

## 9. Composition

Calls `write-scenarios` (`move` mode) and `check-gate` (coverage generator) through the Skill tool. No subagents.

## 10. Claude Code wiring

`allowed-tools`: `Read`, `Glob`, `Grep`, `Edit`, `Write` on `docs/product/**`, `Bash(uv run *)`.

## 11. Portability

Portable core; the call to `check-gate` is written as "use the `check-gate` skill" [R5-Q4a].

## 12. Headless and CI

Interactive: the driver approves the cut. `check_cut.py` can also run headless in CI.

## 13. Security and privacy

Writes only under `docs/product/`. No network.

## 14. Gotchas

- A story that only adds a technical layer is not a story; it is an enabler slice [R3-A3].
- Coverage counts tags, not intent: a mistagged scenario shows the wrong extension as covered.

## 15. Evaluation plan

- **Triggering:** 20 prompts, 60/40 split, including Gherkin requests that should go to `write-scenarios`.
- **Output cases:** cut a room-booking use case → stories that each include a main-scenario path, no layer-only story; an extension claimed by two stories → flagged; the drafts moved, none copied. Graders: `regex`, `llm`, `file_exists`. Threshold 0.8.

## 16. Definition of done

- [ ] Description specific, third person, ≤ 1,024 characters
- [ ] `SKILL.md` under 500 lines; references one level deep
- [ ] No time-sensitive information; one term per concept
- [ ] Scripts handle their errors and follow the CLI contract
- [ ] At least 3 evals, passing on the target models
- [ ] `skills-ref validate` and `claude plugin validate` clean

## 17. Maintenance

INVEST guidance changes only through decisions.

## 18. Open questions

- None at outline level; the split from `write-scenarios` is decided [R27-Q1′].
