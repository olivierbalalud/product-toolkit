# Skill v1 vs no skill: interview runs on dev cases 01, 08, 21 (2026-10-23)

Both arms started from `v3-short.md` and interviewed a simulated product owner (`evals/ask_driver.py`, answering from `answers.md`). The without-skill arm had the template; the with-skill arm followed `skill/SKILL.md`. A grader that didn't know which arm wrote which compared each draft with the case's gold version (`grades.md`; the letters are unblinded in `grading-key.json`).

| Case | Questions (without / with) | `check_grid.py` | Coverage of gold /10 | Invented content (count) | Quality /10 |
|---|---|---|---|---|---|
| 01 Order meal | 13 / 11 | both pass | 7 / 9 | 14 / 2 | 6 / 9 |
| 08 Buy stocks | 8 / 9 | both pass | 8 / 9 | 13 / 2 | 6 / 9 |
| 21 Import contacts | 13 / 8 | both pass | 9 / 8 | 15 / 4 | 6 / 8 |

**Reading.** The template alone already gets the form right, so `check_grid.py` doesn't separate the arms. The skill's gain is in substance: without it, a run fills every gap the product owner leaves open with its own rules, extensions and variations (13 to 15 invented items per case); with it, 2 to 4, and quality rises from 6 to 8–9 with similar coverage and no more questions. Gaps the skill still left, in case 21: the import-method variation (CSV, spreadsheet or pasted rows) and the "manager leaves, the import completes" extension.
