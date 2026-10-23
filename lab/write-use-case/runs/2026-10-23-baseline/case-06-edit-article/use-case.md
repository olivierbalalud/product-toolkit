---
id: UC-006
title: Edit an article
status: Draft
driver: lab
priority: unset
source_locale: en
inputs: []
stories: []
---

# UC-006: Edit an article

| Field | Value |
|---|---|
| **Primary actor** | Member (a registered user; anonymous visitors don't edit) |
| **Supporting actors** | None |
| **Scope** | The wiki |
| **Level** | User goal |
| **Trigger** | The member asks to edit an article, or one section of it. |
| **Preconditions** | The article is in front of the member and editing is enabled on it for them. |
| **Minimal guarantees** | The published article is never left half-changed, and nothing unsaved ever goes live (BR-1). If the save does not happen because of a failure, an expired session or a conflict, the member's text, summary and watch choice are kept, so nothing they typed is lost. |
| **Success guarantees** | The article is saved as a new version with the change; the previous version is kept; the edit is recorded with who made it, when, and their summary, so watchers can be told and moderators can trace or revert it (BR-2); the member's watch choice is applied; the member sees the updated article. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Member | Edit quickly, see and compare the result before saving, and never lose what they typed. |
| Readers | Articles that stay accurate and readable. |
| Watchers of the article | Hear when the article changes. |
| Community moderators | Know who made every change and be able to undo it. |

## Main success scenario

1. (actor) The member asks to edit the article, or one of its sections.
2. (system) The system presents the current content of the article or section for editing, with the edit summary pre-filled.
3. (actor) The member changes the content.
4. (actor) The member completes the edit summary, chooses whether to watch the article, and submits the edit.
5. (system, wait) The system checks the edit is based on the latest saved version (BR-3), saves the new version while keeping the previous one, records the edit with who, when and the summary (BR-2), and applies the watch choice.
6. (system) The system shows the updated article.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | n/a | n/a | out-of-scope: being allowed to edit is a precondition | n/a |
| 3 | out-of-scope: no rules the content must meet, and no size limit (BR-4) | n/a | out-of-scope: losing edit rights mid-edit (protection, block) is not handled; edit rights are a given at the start | yes: UC-006.3-4a |
| 4 | out-of-scope: no rules the summary must meet (BR-4); submitting without changes needs no special handling | out-of-scope: submitting twice needs no special handling | yes: UC-006.4a (session expired); losing edit rights is out-of-scope, as for step 3 | yes: UC-006.3-4a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | out-of-scope: an article deleted during the edit is decided by the moderators' delete use case | yes: UC-006.5a | n/a | yes: UC-006.5b | out-of-scope: articles have no size limit (BR-4) | yes: UC-006.5a | n/a |
| 6 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`. The edit record ties the member's name to the change, but exporting or erasing a member's contributions belongs to a separate account privacy use case, and the content licence requires attribution, which limits erasure.

## Extensions

- **UC-006.3a** The member previews the edit:
  1. The system shows the content as it will look, with a warning that it is not saved yet (BR-1).
  2. Returns to step 3.

  *Example:* Ana rewrites the "Booking rules" section of the "Meeting rooms" article and previews it to check the table of opening hours renders correctly.
- **UC-006.3b** The member compares their changes:
  1. The system shows what the member changed against the latest saved version of the article.
  2. Returns to step 3.

  *Example:* Before submitting, Ana compares her edit and sees she removed the line about room 3's projector by mistake.
- **UC-006.3-4a** The member cancels while editing or writing the summary:
  1. The system discards the member's changes.
  2. The system shows the article as it was.
  3. The use case ends.

  *Example:* Ana starts editing the "Meeting rooms" article, changes her mind, and cancels; the article is unchanged.
- **UC-006.4a** The member's session has expired when they submit:
  1. The system keeps the submitted content, summary and watch choice.
  2. The system asks the member to sign in again.
  3. The member signs in.
  4. Returns to step 5, without the member retyping anything.

  *Example:* Ana spends an hour on the "Booking rules" section, her session expires, and after she signs in again her edit is saved as submitted.
- **UC-006.5a** Someone else saved the article after the member started, so the member's edit is based on an outdated version:
  1. The system does not save the edit (BR-3).
  2. The system shows both the member's version and the latest saved version so the member can merge them.
  3. Returns to step 3.

  *Example:* Ana and Ben both edit the "Meeting rooms" article; Ben saves first, so when Ana submits she is shown Ben's version next to hers to merge.
- **UC-006.5b** The save fails part way through:
  1. The system publishes nothing; the article stays as it was (BR-1).
  2. The system keeps the member's text, summary and watch choice.
  3. The system tells the member the edit was not saved.
  4. Returns to step 4.

  *Example:* Ana submits her edit, the save fails while storing the new version, and she is told it was not saved, with her text and summary still there to submit again.

## Technology and data variations

- Step 1: the member edits the whole article, or a single section of it.

## Related information

- **Frequency:** Often; editing is the main thing people write in the wiki.
- **Business rules:**
  - BR-1: The published article is never left half-changed, and nothing unsaved ever goes live.
  - BR-2: Each save keeps the previous version and records who edited, when, and their summary.
  - BR-3: An edit is saved only if it is based on the latest saved version of the article; otherwise it is never saved over the newer one.
  - BR-4: There are no rules the content or the edit summary must meet, and no size limit on articles.
- **Open issues:** None.
