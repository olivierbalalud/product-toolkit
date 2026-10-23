---
id: UC-006
title: Edit an article
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-006: Edit an article

| Field | Value |
|---|---|
| **Primary actor** | Member (a registered user) |
| **Supporting actors** | None |
| **Scope** | Wiki system |
| **Level** | User goal |
| **Trigger** | The member asks to edit the whole article or one section of it. |
| **Preconditions** | An article with editing enabled is presented to the member. |
| **Minimal guarantees** | The published article is never partially modified; unsaved changes are never published. |
| **Success guarantees** | The article is saved with the member's change and its updated version is presented; an edit record names the member, the time and the edit summary, and the previous version is kept, so watchers can be informed and moderators can trace or revert the change; the member's choice to watch the article or not is applied. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Member | Edits quickly, can preview and compare before saving, and never loses work. |
| Readers | Articles stay accurate and readable. |
| Watchers | Are informed of changes to the articles they follow. |
| Community moderators | Every change is attributable and reversible. |

## Main success scenario

1. (system) The system presents the content to edit, the whole article or only the chosen section, with a pre-filled edit summary.
2. (actor) The member modifies the content until satisfied.
3. (actor) The member writes the edit summary, states whether to watch the article, and submits the edit.
4. (system, wait) The system saves the article, records the edit, applies the member's watch choice, and presents the updated article.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 2 | n/a | n/a | n/a | yes: UC-006.2-3c |
| 3 | n/a | n/a | yes: UC-006.4a | yes: UC-006.2-3c |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 1 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | out-of-scope: deleting an article is a moderator's use case, which decides what happens to edits in progress | yes: UC-006.4b | n/a | yes: UC-006.4c | out-of-scope: no size limit is defined for articles | yes: UC-006.4b | n/a |

**Privacy request:** yes: `deferred`, the edit record ties the member's name to the change for attribution; exporting or erasing a member's contributions belongs to a separate account privacy use case, and the content licence's attribution requirement limits erasure.

## Extensions

- **UC-006.2-3a** The member asks for a preview:
  1. The system shows the rendered content and warns that it is not saved yet.
  2. Returns to step 2.

  *Example:* Ana rewrites the "History" section of "Harbour Bridge", asks for a preview, and sees her new paragraph rendered with a notice that it is not saved yet.
- **UC-006.2-3b** The member asks to see the changes:
  1. The system shows the differences between the member's content and the latest saved version.
  2. Returns to step 2.

  *Example:* Ana asks to see her changes and sees that she removed the sentence on the 1932 opening and added two sentences on the 1998 repairs.
- **UC-006.2-3c** The member cancels the edit:
  1. The system discards the changes and presents the article unchanged.
  2. The use case ends.

  *Example:* Ana cancels after rewriting two paragraphs of "Harbour Bridge"; the article still shows its last saved version.
- **UC-006.4a** The member's session has expired:
  1. The system keeps the submitted content and asks the member to sign in again.
  2. Once the member has signed in, returns to step 4.

  *Example:* Ben submits his edit to "Tidal Mills" an hour after his session expired; he signs in again and his edit is saved without his retyping it.
- **UC-006.4b** Another member saved the article since this edit began:
  1. The system does not save the edit and shows both versions so the member can reconcile them.
  2. Returns to step 2.

  *Example:* Ana submits her edit to "Harbour Bridge" at 10:05, but Ben saved a change to the same article at 10:02; Ana sees both versions and works Ben's corrected date into her text.
- **UC-006.4c** The article cannot be saved in full:
  1. The system publishes nothing, keeps the submitted content, and tells the member the edit was not saved.
  2. Returns to step 3.

  *Example:* Ben submits his edit to "Tidal Mills", the save fails part way, the article still shows its previous version, and Ben's text and summary are kept for him to submit again.

## Technology and data variations

- 1: the member edits the whole article, or only one section of it.

## Related information

- **Frequency:** Frequent: editing is the wiki's main write action.
- **Open issues:** None
