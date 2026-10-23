# Answers: Edit an article

## Actor, goal and scope

- The person editing is a member, meaning a registered user; anonymous visitors don't edit.
- The system we're designing is the wiki as a whole.
- They can edit the whole article or just one section of it.
- Before they start, the article is already in front of them and editing is enabled on it; we don't check that again.
- Nobody else and no outside system takes part in an edit.
- It happens often: editing is the main thing people write in the wiki.

## Stakeholders and guarantees

- The member wants to edit quickly, see the result and compare it before saving, and never lose what they typed.
- Readers want articles that stay accurate and readable.
- People watching an article want to hear when it changes.
- Community moderators need to know who made every change and be able to undo it.
- Whatever happens, the published article is never left half-changed, and nothing unsaved ever goes live.
- When it works, the article is saved with the change and they see the updated version.
- Each save leaves a record of who edited, when, and their summary, and the previous version is kept, so watchers can be told and moderators can trace or revert it.

## Main scenario

- The edit summary comes pre-filled when they open the editor.
- When they submit, they also say whether they want to watch the article, and saving applies that choice.
- Saving records the edit and applies the watch choice; there is no other processing after that.
- A preview shows the content as it will look, with a warning that it isn't saved yet, and they carry on editing.
- Comparing shows what they changed against the latest saved version, and they carry on editing.

## What can go wrong

- They can give up and cancel at any point while editing or writing the summary.
- Their session may have expired by the time they submit.
- Someone else may have saved the same article since they started, so they've been working on an outdated version.
- The save can fail part way through.

## How each is handled

- If they cancel, their changes are thrown away and they see the article as it was.
- If their session expired, we keep what they submitted, ask them to sign in again, and then save it without them retyping anything.
- If someone else saved in the meantime, we don't save; we show them both versions so they can merge them, and they go back to editing.
- If the save fails part way, nothing is published, their text and summary are kept, and we tell them it wasn't saved so they can submit again.

## Durations

- Opening the content for editing is immediate; saving takes a few seconds and they wait for it.

## Out of scope

- An article deleted while someone is editing it: deleting is a moderator's job, and that use case decides what happens to edits in progress.
- Size limits: there is no size limit on articles, so there is nothing to hit.
- Losing edit rights mid-edit, for example the article gets protected or the member gets blocked: being allowed to edit is a given when they start, so we don't handle it here.
- Submitting without changing anything, or submitting twice: neither needs special handling.
- Nothing they type is rejected: there are no rules the content or the summary must meet.
- Exporting or erasing a member's contributions: the edit record does tie their name to the change, but that request belongs to a separate account privacy use case, and the content licence requires attribution, which limits erasure.
