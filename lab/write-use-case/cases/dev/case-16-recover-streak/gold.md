---
id: UC-016
title: Recover a broken streak
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-016: Recover a broken streak

| Field | Value |
|---|---|
| **Primary actor** | Learner (free or premium subscriber) |
| **Supporting actors** | None |
| **Scope** | Language learning app |
| **Level** | User goal |
| **Trigger** | The Learner opens the app after a calendar day without a completed lesson and finds the streak broken. |
| **Preconditions** | The Learner's streak is marked broken: no lesson was completed before midnight in the Learner's registered time zone (BR-1). |
| **Minimal guarantees** | The streak is either restored with its cost taken once, or left broken with nothing taken; a streak broken for longer than the grace period is never restored (BR-2). |
| **Success guarantees** | The streak counter is back at its value before the lapse and the missed day is no longer marked lapsed; the cost of the chosen method is taken: the gems are deducted, the streak freeze is consumed, the month's subscription repair is used, or the repair lesson is recorded as passed (BR-3); the Learner's public profile and leaderboard show the active streak. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Learner | Keeps the streak, a motivator and a personal investment, after an occasional lapse; is never charged for a recovery that did not happen. |
| Product retention team | Occasional lapses are forgiven, so learners keep coming back daily, while a streak still means something: recovery has a cost and a time limit. |

## Main success scenario

1. (system) The system presents the broken streak and the recovery options the Learner is eligible for, given the account tier and inventory, each with its cost (BR-2, BR-3).
2. (actor) The Learner chooses a recovery method: spending gems, using an equipped streak freeze, or using the premium subscription's monthly repair.
3. (system) The system confirms the Learner can cover the chosen method and takes its cost (BR-3), restores the streak to its count before the lapse and clears the missed day, shows the active streak on the Learner's public profile and leaderboard, and celebrates the restored streak before taking the Learner to their current course.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 2 | n/a | yes: UC-016.3b | n/a | yes: UC-016.2b, UC-016.2c |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 1 | n/a | n/a | n/a | n/a | yes: UC-016.1a | n/a | n/a |
| 3 | n/a | yes: UC-016.3b | n/a | yes: UC-016.3c | yes: UC-016.3a | yes: UC-016.3a, UC-016.3b | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing the Learner's streak and learning history belongs to the account's own privacy use case, not to recovering a streak.

## Extensions

- **UC-016.1a** The streak broke longer ago than the grace period (BR-2):
  1. The system says the streak can no longer be restored.
  2. The system invites the Learner to start a new streak today, with a motivating target.
  3. The use case ends; the streak is not restored.

  *Example:* Kofi opens the app on Thursday evening; his 120-day streak broke at midnight on Monday, more than 48 hours ago, so the app invites him to start a new streak and aim for 7 days.
- **UC-016.2a** The Learner chooses a repair lesson instead of paying:
  1. The system starts a short review lesson on the Learner's recent weak vocabulary and grammar.
  2. The Learner completes the lesson with an accuracy at or above the passing threshold (BR-4).
  3. The system records the lesson as passed and returns to step 3, the passed lesson being the cost.

  *Example:* Mia, a free learner with no gems, takes a repair lesson on Spanish past tenses, scores 86 %, and her 45-day streak is restored.
- **UC-016.2b** The Learner fails the repair lesson or leaves it before the end:
  1. The system keeps the streak broken and takes nothing.
  2. The Learner retries the lesson (UC-016.2a) or chooses another method: returns to step 2.

  *Example:* Mia scores 65 % on the repair lesson, below the threshold; her streak stays broken and she spends 350 gems instead.
- **UC-016.2c** The Learner accepts the reset, or leaves without choosing:
  1. The system takes nothing. If the Learner accepted the reset, the system sets the streak to zero, and the next completed lesson starts a new streak. If the Learner left, the streak stays broken and the recovery options are offered again the next time the Learner opens the app within the grace period (BR-2).
  2. The use case ends.

  *Example:* Sam has 40 gems, not the 350 the recovery costs, and accepts the reset; his streak shows 0, and his next lesson makes it day 1.
- **UC-016.3a** The Learner does not have enough gems for the recovery:
  1. The system says how many gems are missing and takes nothing.
  2. The Learner buys gems (use case Buy Gems) and returns to step 3, takes a repair lesson (UC-016.2a), or accepts the reset (UC-016.2c).

  *Example:* Lena chooses to spend 350 gems on her 88-day streak but has 200; she buys a 500-gem pack and the streak is restored.
- **UC-016.3b** The streak was already restored, from another device or by a repeated request:
  1. The system takes no second cost and shows the restored streak.
  2. The use case ends in success.

  *Example:* Ravi restores his 30-day streak on his phone, then confirms the same recovery on his tablet; no more gems are taken and the tablet shows the 30-day streak.
- **UC-016.3c** The recovery cannot be completed in full:
  1. The system undoes what it did: the cost is not taken and the streak stays broken.
  2. The system says the recovery failed and keeps the Learner's choice, including a passed repair lesson.
  3. The Learner tries again: returns to step 3. Or the Learner leaves (UC-016.2c).

  *Example:* Ana spends 350 gems, the restore fails part way; her 350 gems are back, her streak is still broken, and her second try restores it.

## Technology and data variations

- 2: the recovery is paid with gems, with an equipped streak freeze, or with the premium subscription's monthly repair.

## Related information

- **Frequency:** Occasional: a few times a year per learner, whenever a streak breaks.
- **Business rules:** BR-1 a streak breaks when no lesson is completed before midnight in the Learner's registered time zone (Preconditions) · BR-2 a broken streak can be recovered for 48 hours after the lapse (step 1, UC-016.1a, UC-016.2c) · BR-3 the options depend on the account tier and inventory: gems, an equipped streak freeze, the premium subscription's monthly repair, or a repair lesson for any learner; each costs its gems, one streak freeze, the month's repair, or a passed repair lesson (steps 1 and 3) · BR-4 a repair lesson passes at an accuracy at or above the passing threshold (UC-016.2a, UC-016.2b).
- **Related use cases:** Buy Gems.
- **Open issues:** The passing threshold of the repair lesson: 80 % is given only as an example.
