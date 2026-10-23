---
name: write-stories
status: full
priority: P0
owner: <founder>
serves: cutting stories (after the use case gate)
decisions: [R4-Q3, R9-Q1, R1-Q7, R27-Q1′, R28-Q1, R28-Q4, R28-Q5, R28-Q8, R28-Q9, R29-Q6, R31-Q3]
plugin_version:
---

# write-stories

## 0. Header

Cuts a complete use case into user stories that are vertical paths, starting with the thinnest path through the whole main scenario, and writes each story's Draft PRD [R4-Q3, R28-Q8]. Gherkin is a separate skill, `write-scenarios`, used during *Exploring* [R27-Q1′, R28-A].

## 1. Problem and baseline

Expected failures without the skill (replace with observed ones before building):

1. Claude cuts stories by layer ("backend for bookings", "UI for bookings"), not as vertical paths.
2. A story is a wish with no path through the use case, so it claims no extension and `coverage.md` can't account for it.
3. Stories are too big for one slice, or fail INVEST's *Independent* by depending on another story instead of an enabler.
4. Stories are cut along steps ("steps 1–3", "steps 4–6"), so no story works end to end and the designer gets half a screen per story [R28-Q8].

## 2. Scope

- **Does:** proposes stories as paths through a `Complete` user-goal use case: first the thinnest path through the whole main scenario, then stories that each add extensions or one variation [R28-Q8]; checks INVEST; writes the Connextra statement and the Draft `prd.md` from [`story.md`](../templates/story.md), with `extensions:` and `touches:` [R9-Q1, R28-Q4, R28-Q5]; regenerates `coverage.md`.
- **Does not:** write Gherkin (`write-scenarios`); write the rest of the PRD, flows or copy; decide scope (the driver approves the cut); review (`review-design`).
- **Neighbours:** `write-use-case` (input), `write-scenarios` (writes the scenarios during *Exploring*), `check-gate` (coverage generator, gate).

## 3. Invocation

- **Invoked by:** the model or user.
- **Draft description:**
  > Cuts a complete use case into vertical user stories that each deliver value on their own, checks them against INVEST, and writes their Draft PRDs. Use when a use case reaches Complete, or when coverage shows extensions no story claims yet.
- **Should trigger:** "cut UC-012 into stories"; "which story should claim UC-012.4d?"; "split US-012.2, it's too big".
- **Should not trigger:** "write the Gherkin for US-012.1" (`write-scenarios`); "complete the use case"; "review the slice".
- **Arguments:** a use case ID, or a story ID to split.

## 4. Inputs

- The `Complete` use case and its `coverage.md`.
- Existing files are **data**.

## 5. Outputs

- Per story: `stories/US-NNN.N-<slug>/prd.md` (Draft) with `extensions:` listing what the story handles and `touches:` (`ui`, `api` or both) [R28-Q5]. No acceptance criteria: they are written as Gherkin during *Exploring* [R28-Q4].
- Regenerated `coverage.md`, through `check-gate`'s generator.
- Idempotent: re-running proposes no new story when every path is claimed.

## 6. Procedure

**Cutting stories**

1. Read the use case; check its `Level` is `User goal` [R28-Q1], or stop and say so.
2. Propose the **first story**: the thinnest path through the whole main scenario, with the simplest variation and only the extensions it can't ship without [R28-Q8]. It keeps every step's duration class: a `long` or `background` step stays asynchronous, though its cancel and notification extensions may wait for a later story [R29-Q6].
3. Propose **later stories**, each adding extensions or one item from "Technology and data variations" to that path.
4. For each candidate, check INVEST, explained in [chapter 3](../guide/03-design-playbook.md#cutting-stories); *Independent* means independent of every story except the first of its use case. Split any over about one week of slice work [R4-Q3].
5. Set `touches:` for each: `ui` when it adds or changes a screen, `api` when it adds or changes an endpoint or stored data [R28-Q5].
6. Present the cut to the driver as a numbered list (statement, path, extensions, touches); iterate until approved.
7. Write each Draft PRD.
8. Regenerate `coverage.md`. *Done when* every extension is claimed, or shown as unclaimed in coverage.

## 7. Scripts vs judgement

- `scripts/check_cut.py` (blocking): every story's `extensions:` exist in the use case and are not `retired`, in any of the three ID forms (`UC-012.3a`, `UC-012.3-6a`, `UC-012.*a`) [R31-Q3]; every story has `touches:`; every story includes at least one main-scenario step or an extension path. Several stories may claim the same extension [R28-Q9].
- Coverage via `check-gate`'s `gen_coverage.py`.
- **Judged by the model:** which path is thinnest; where to cut; whether a story delivers value on its own; INVEST; `touches:`.

## 8. Files

```
write-stories/
  SKILL.md
  references/invest.md          read when checking a story
  assets/story.md
  scripts/check_cut.py
```

## 9. Composition

Calls `check-gate` (coverage generator) through the Skill tool. No subagents.

## 10. Claude Code wiring

`allowed-tools`: `Read`, `Glob`, `Grep`, `Edit`, `Write` on `docs/product/**`, `Bash(uv run *)`.

## 11. Portability

Portable core; the call to `check-gate` is written as "use the `check-gate` skill" [R5-Q4a].

## 12. Headless and CI

Interactive: the driver approves the cut, usually on the same `uc/UC-…` PR that sets the use case `Complete` [R28-Q20]. `check_cut.py` can also run headless in CI.

## 13. Security and privacy

Writes only under `docs/product/`. No network.

## 14. Gotchas

- A story that only adds a technical layer is not a story; it is an enabler slice [R3-A3].
- Coverage counts tags, not intent: a mistagged scenario shows the wrong extension as covered.
- A first story that skips a main-scenario step isn't end to end; defer extensions, not steps.
- An extension such as *no permission* may belong to several stories; claim it in each one that must handle it.
- "Make it work, then make it fast" never turns a `long` or `background` step into a synchronous one: changing the API shape later breaks clients. Defer the extensions, not the shape [R29-Q6].
- A deadline, reminder or expiry is a time-triggered use case of its own, so it gets its own stories; don't fold it into the story of the use case that sets the deadline [R29-Q3, R29-Q6].

## 15. Evaluation plan

- **Triggering:** 20 prompts, 60/40 split, including Gherkin requests that should go to `write-scenarios`.
- **Output cases:** cut a room-booking use case → a first story through the whole main scenario, later stories each adding extensions or a variation, no layer-only story, each with `touches:`; a summary-level use case → refused; an extension claimed by two stories → accepted. Graders: `regex`, `llm`, `file_exists`. Threshold 0.8.

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

- None at outline level; the split from `write-scenarios` is decided [R27-Q1′, R28-A].
