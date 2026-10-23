# Answers: recover a broken streak

## Actor, goal and scope

- The system is our language learning app.
- The learner can be on the free tier or a premium subscriber; both can recover a streak, with different options.
- It starts when the learner opens the app after a calendar day with no completed lesson and finds the streak broken.
- By then the streak is already marked broken: a streak breaks when no lesson is completed before midnight in the learner's registered time zone. Something else does that marking; this is only about getting the streak back.
- No outside system or other person takes part; the app does everything itself.
- The currency is gems. A learner can pay with gems, with a streak freeze they have equipped, with the premium subscription's monthly repair, or by passing a repair lesson.
- It happens occasionally, a few times a year per learner, whenever a streak breaks.
- Buying gems is its own thing; we only link to it from here.

## Stakeholders and guarantees

- The learner cares about the streak as a motivator and something they've invested in, and wants to keep it after an occasional lapse.
- The learner must never be charged for a recovery that didn't happen.
- The retention team wants to forgive the odd lapse so people keep coming back every day, without making a streak meaningless: recovering always costs something and only works for a limited time.
- However it ends, the streak is either restored with its cost taken once, or still broken with nothing taken.
- Once the grace period is over, a streak is never restored.
- When it works: the counter is back at what it was before the lapse, the missed day no longer counts as lapsed, the cost has been taken, and the public profile and leaderboard show the streak as active.

## Main scenario

- The options shown depend on the account tier and what the learner has, and each one shows its cost.
- Choosing the repair lesson is an alternative to paying, open to any learner.
- Taking the cost, restoring the streak and updating the profile and leaderboard happen together, as one action.
- The missed day is cleared as part of the restore.
- After the restore the app celebrates the restored streak and takes the learner on to their current course.

## What can go wrong

- The streak broke more than 48 hours ago, so it's past the grace period.
- The learner fails the repair lesson or leaves it before the end.
- The learner decides to accept the reset, or just leaves without choosing anything.
- The learner chose to pay with gems but doesn't have enough, including when the balance dropped since the options were shown.
- The streak was already restored, from another device or because the same request came in twice.
- The recovery only goes through partly, for example gems taken but the streak not restored.

## How each is handled

- Past the grace period: the app says the streak can't be restored any more, invites them to start a new streak today with a motivating target, and that's the end of it.
- Repair lesson: a short review of the learner's recent weak vocabulary and grammar; passing it counts as the cost, and the streak is restored the same way as when paying.
- To pass, the learner needs an accuracy at or above the passing threshold. We've been using 80 % as an example, but the actual threshold isn't settled.
- Failed or abandoned lesson: the streak stays broken, nothing is taken, and they can retry the lesson or pick another way to pay.
- Accepting the reset: nothing is taken, the streak goes to zero, and the next lesson they complete starts a new one.
- Leaving without choosing: nothing changes, and the options come back the next time they open the app, as long as they're still within the grace period.
- Not enough gems: the app says how many are missing and takes nothing; they can buy gems and carry on, take a repair lesson, or accept the reset.
- Already restored: no second cost is taken, they just see the restored streak, and it counts as a success.
- Partial failure: everything is undone, so nothing is taken and the streak stays broken; the app says it failed, keeps their choice, including a lesson they already passed, and they can try again or leave.

## Durations

- Showing the broken streak and the options is immediate.
- Taking the cost and restoring the streak is immediate too.
- The repair lesson itself takes a few minutes, and the learner is doing it the whole time.

## Out of scope

- Picking an option they aren't entitled to, such as the monthly repair on the free tier, can't happen: only the options they're eligible for are offered.
- There's no outside service involved in recovering a streak, so nothing to time out.
- Exporting or erasing a learner's streak and learning history belongs to the account's privacy handling, not here.
