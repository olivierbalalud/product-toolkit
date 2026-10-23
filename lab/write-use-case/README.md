# write-use-case lab

This is where `write-use-case` is built and tested before it ships to the monorepo [R31-Q6]. The spec is [`docs/skills/write-use-case.md`](../../docs/skills/write-use-case.md) and the quality rubric is [`docs/research/use-case-quality.md`](../../docs/research/use-case-quality.md). The decisions are round 31 of the [grilling log](../../docs/grilling-log.md).

## Rules

- **Only this folder holds a skill.** It is the one exception to "no skills in this repo". Nothing here is installed as a project skill: runs load `skill/` by path [R31-Q6].
- **Cases may come from other products**, in their own language. They are exempt from the English and neutral-domain rules, but never contain content from the product monorepo. Replace real people's names and personal data with invented ones before committing [R31-Q7].
- **Lessons go back to `docs/` in the neutral domain**, meeting room booking. A change to a rule, as opposed to the skill's wording, starts as a new round in the grilling log.
- **The held-out cases stay unseen.** They are never read while the skill is tuned (see [Held-out cases](#held-out-cases)) [R31-Q8].

## Layout

```
lab/write-use-case/
  README.md                this file
  cases/
    manifest.md            one row per case: shape, language, split
    dev/                   cases used to build and tune the skill
      case-01-<slug>/
        v1-good.md         given: the near-correct version, never edited
        v2-bad.md          given: the badly written version, never edited
        v3-short.md        given: the summary in 6 steps or fewer, never edited
        inputs/            given, optional: the documents the use case was written from
        gold.md            made in the lab: v1 in the current template, reviewed by the driver
        answers.md         made in the lab: the driver's answers to the interview
    holdout/               about 4 cases, same layout, unseen until the final test
  skill/                   the draft skill, in the layout of spec §8 (SKILL.md, references/, assets/, scripts/)
  tests/                   unit tests of skill/scripts/ (check_grid.py first)
  runs/                    one folder per run: <date>-<label>/<case>/ with the output and its grading
  evals/                   claude plugin eval cases and the 20 triggering prompts
```

## Where to put your use cases

For each use case, create one folder named `case-NN-<slug>`, numbered from `01`, with a slug of two or three words (`case-03-book-room`). Put it in `cases/dev/`, or straight in `cases/holdout/` if it is held out. In the folder:

| File | What to put in it |
|---|---|
| `v1-good.md` | Version 1, the near-correct one, as you have it. Any format. |
| `v2-bad.md` | Version 2, the badly written one. |
| `v3-short.md` | Version 3, the summary in 6 steps or fewer. |
| `inputs/` (optional) | The documents the use case came from, such as a brief, notes or a transcript, in Markdown or plain text. |

Then add a row to `cases/manifest.md`. Leave `gold.md` and `answers.md` to the lab.

**Which cases to hold out.** About four, picked by you, so that together they cover different shapes: one with a wait point, one with a `long` or `background` step, one started by time, and one with many extensions. A case that has none of these can stay in `dev/`. Put each one directly in `cases/holdout/` so it is never read in a tuning session.

## What each version is for

| Version | Used as | Measures |
|---|---|---|
| `v1-good.md` → `gold.md` | The expected output of every run | How close a run comes to what you would sign off |
| `v2-bad.md` | The input of **repair** runs; a case `check_grid.py` must fail; the list of failures for the rubric check (rubric §7) | Whether the skill finds and fixes what is wrong |
| `v3-short.md` + `answers.md` | The input of **write** runs | Whether the skill asks the questions that lead from v3 to the gold version, and no more |

`gold.md` is v1 brought to the current [`use-case.md`](../../docs/templates/use-case.md) template: actor and system marks, duration classes, the failure grid, an example per extension. Its ID is `UC-0NN`, from the case number. A session drafts it from v1, and you correct it. Where v1 is silent, the gap is a question for you, not something to invent.

`answers.md` is what you would say in the interview: one bullet per fact that v3 doesn't contain and the gold version does. Every run reads it instead of interviewing you, so runs can be compared. The live interview is tested later, on the product's first use case (onboarding note, §5 step 10).

## The loop

1. **Import.** You add the cases; the lab drafts `gold.md` and `answers.md` for the `dev/` cases, and you review them.
2. **Check the rubric** against the v1 and v2 pairs (rubric §7): tag each difference with a criterion or `none`, and tally. The tally sets the order of the interview and the weights of the grader.
3. **Baseline.** A fresh session without the skill writes each `dev/` case from `v3-short.md`, `answers.md` and the template, and repairs each `v2-bad.md`. Outputs go to `runs/<date>-baseline/`.
4. **`check_grid.py`, test first** in `tests/`: every `gold.md` passes, every `v2-bad.md` fails, and each rule of spec §7 has a unit test.
5. **Draft `skill/`** from the spec, the rubric and the failures seen in the baseline.
6. **Run with the skill**, in a fresh session each time, and compare with the baseline and the gold version (`skill-creator` runs both arms).
7. **Iterate.** Each gap from the gold version gets one fix: a rule, an example, a script check or a gotcha. Stop when `check_grid.py` passes, you would accept the outputs with wording changes only, and two runs in a row agree.
8. **Generalise** with the spec §15 cases as small fixtures in `evals/`, threshold 0.8.
9. **Held-out test.** Freeze `skill/`, then follow [Held-out cases](#held-out-cases).
10. **Ship** [R31-Q9]. You copy `skill/` to the monorepo's marketplace, `plugins/<plugin>/skills/write-use-case/`. From then on the monorepo copy is the source; `skill/` is removed here, and the cases, tests, runs and evals stay.

## Held-out cases

A deny rule in `.claude/settings.local.json` keeps Claude's file tools out of `cases/holdout/`. It is a guard, not a lock: a shell command can still read the folder, so no tuning session is asked to. For the final test:

1. Commit the frozen `skill/`.
2. Remove the deny rule.
3. In a fresh session, draft each held-out `gold.md` and `answers.md`, and review them.
4. In another fresh session, run the frozen skill on each held-out case.
5. Grade the outputs. A failure there is a finding: it goes into the spec's gotchas or the evals, and the skill is re-tuned on `dev/` cases only.
