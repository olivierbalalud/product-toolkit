# Held-out test: skill v1 vs no skill on cases 04, 15, 20, 23 (2026-10-23)

Same protocol as the [dev comparison](../2026-10-23-comparison/summary.md): both arms start from `v3-short.md` and interview the simulated product owner; the skill was frozen at commit ea5fd1b; the held-out gold versions were drafted by fresh subagents after that commit. A grader that didn't know which arm wrote which compared each draft with gold (`grades.md`; letters unblinded in `grading-key.json`).

| Case | Questions (without / with) | `check_grid.py` | Coverage /10 | Invented (count) | Quality /10 |
|---|---|---|---|---|---|
| 04 Process sale | 10 / 11 | both pass | 8 / 8 | 18 / 3 | 6 / 7 |
| 15 Schedule post | 14 / 9 | both pass | 9 / 8 | 12 / 1 | 7 / 8 |
| 20 Book a home | 13 / 8 | both pass | 9 / 8 | 15 / 1 | 6.5 / 8 |
| 23 Bank feed | 13 / 8 | both pass | 9 / 8.5 | 13 / 2 | 7 / 8.5 |

**Reading.** The held-out results match the dev ones: the skill wins every case on invented content (1 to 3 items instead of 12 to 18) and quality, with fewer questions in three cases of four. It loses up to one point of coverage: it leaves out things the product owner didn't volunteer, such as a supporting actor (the host in 20) and the technology and data variations (20, as in dev case 21). Without the skill, runs also answered the privacy line "no" every time where gold says `deferred`.
