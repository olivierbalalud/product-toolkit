---
id: UC-021
title: Import contacts from a spreadsheet into an audience
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-021: Import contacts from a spreadsheet into an audience

| Field | Value |
|---|---|
| **Primary actor** | Marketing manager |
| **Supporting actors** | None |
| **Scope** | Email marketing service |
| **Level** | User goal |
| **Trigger** | The marketing manager has a spreadsheet of contacts, usually from an event, to add to an audience. |
| **Preconditions** | The marketing manager is signed in with permission to manage the audience. |
| **Minimal guarantees** | The uploaded file is thrown away when the import ends or the manager gives up, whatever the outcome. A cancelled or failed import leaves the audience exactly as it was: the contacts it added are removed and the contacts it updated are restored. No new contact is stored as subscribed unless the manager stated they opted in. A blank cell never replaces a stored value. |
| **Success guarantees** | The new contacts are in the audience with their consent status, tagged with the import's name. Existing contacts are updated only if the manager chose that. Every row is accounted for as added, updated, or skipped with its reason, in an import report kept in the import history. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Marketing manager | Gets the list into the audience quickly, without retyping or cleaning it by hand. |
| Contacts in the spreadsheet | Receive mail only if they consented; their existing data isn't overwritten wrongly. |
| Account owner | The plan's contact limit is respected and checked before the import starts; the import never pushes an upgrade. |
| Deliverability team | No purchased lists and no role addresses (such as info@), which bring spam complaints. |

## Main success scenario

1. (actor) The marketing manager provides the spreadsheet and chooses the audience to import into (BR-1).
2. (system, wait) The system reads the spreadsheet and proposes a mapping of its columns to contact fields.
3. (actor) The marketing manager confirms the mapping, chooses whether existing contacts are updated, and states the contacts' consent (BR-3).
4. (system, wait) The system checks the new rows against the plan's contact limit (BR-2) and presents how many rows are new, existing and invalid.
5. (actor) The marketing manager starts the import.
6. (system, background) The system imports the rows with their consent status, updates existing contacts as chosen (BR-6), tags the new contacts with the import's name, and shows progress and time remaining (BR-4, BR-5, BR-7).
7. (system) The system presents the import report and keeps it in the import history.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-021.1a, UC-021.1b | yes: UC-021.1b | n/a | yes: UC-021.1-5a |
| 3 | n/a | n/a | n/a | yes: UC-021.1-5a |
| 5 | n/a | n/a | n/a | yes: UC-021.1-5a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | yes: UC-021.2a | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | n/a | n/a | n/a | n/a | yes: UC-021.4a | n/a | n/a |
| 6 | n/a | yes: UC-021.6c, UC-021.6d | n/a | yes: UC-021.6b | out-of-scope: the contact limit is checked once before the import starts; contacts added elsewhere while rows are written are not re-checked | out-of-scope: the counts and the limit check are not repeated while rows are written; contacts added elsewhere since step 4 are not re-checked | yes: UC-021.6a |
| 7 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing a contact's personal data is a separate job, not part of an import.

## Extensions

- **UC-021.1a** The spreadsheet can't be read: a format the system doesn't read, an unknown encoding, no rows, or more than 100,000 rows (BR-1):
  1. The system says what is wrong and keeps nothing.
  2. The marketing manager provides another file: returns to step 1. Or gives up: the use case ends.

  *Example:* Lena provides a 140,000-row export of her trade-fair badge scans; the system says a file can hold at most 100,000 rows.
- **UC-021.1b** Some rows have a malformed address or a role address (BR-4), or repeat an address from an earlier row (BR-5):
  1. The system counts these rows as invalid at step 4 and skips them at step 6; the report lists each skipped row with its reason.
  2. Returns to step 2.

  *Example:* Lena's file has 1,200 rows; row 48 reads "ana@@example.com", row 311 is "info@hotel-example.com", and row 640 repeats Ben Ortiz's address from row 12. Rows 48, 311 and 640 are skipped and listed with their reasons; row 12 is imported.
- **UC-021.2a** No column is recognised as the email address:
  1. The system asks which column holds the email address.
  2. The marketing manager names the column: returns to step 3.

  *Example:* Lena's file heads its address column "Courriel"; the system asks which column holds the email address, and she names "Courriel".
- **UC-021.3a** The marketing manager states that the contacts' consent is unknown, or that they come from a purchased list:
  1. For a purchased list, the system tells the manager that a purchased list is not accepted as consent.
  2. The system will store the new contacts as non-subscribed, never emailed (BR-3).
  3. Returns to step 4.

  *Example:* Lena states her 800 contacts come from a purchased list of venue managers; the system tells her that isn't consent, and the 800 new contacts are stored as non-subscribed.
- **UC-021.1-5a** The marketing manager gives up before starting the import:
  1. The system throws away the file and the mapping; the audience is untouched.
  2. The use case ends.

  *Example:* Lena sees that 300 of her 1,200 rows are invalid and gives up to clean the file first; the audience is as it was.
- **UC-021.4a** The new rows would take the account past the plan's contact limit (BR-2):
  1. The system says how many new contacts fit, and offers no upgrade.
  2. The marketing manager cuts the file down and starts again: returns to step 1. Or gives up: the system throws away the file and the mapping, and the use case ends.

  *Example:* The plan allows 5,000 contacts and the account holds 4,600; Lena's file has 700 new rows, and the system says 400 new contacts fit.
- **UC-021.6a** The marketing manager cancels the import while it runs:
  1. The system stops, removes the contacts this run added, restores the contacts it updated, and throws away the file.
  2. The system confirms the audience is unchanged.
  3. The use case ends.

  *Example:* Lena starts importing 40,000 rows, cancels at 35% after spotting the wrong audience, and the audience is back to its 2,100 contacts.
- **UC-021.6b** The import fails part-way:
  1. The system removes the contacts this run added, restores the contacts it updated, and throws away the file.
  2. The system records the failed run in the import history and tells the manager the audience is unchanged; a manager who left reads this in the import history.
  3. The marketing manager provides the file again: returns to step 1. Or stops: the use case ends.

  *Example:* Lena's import of 25,000 rows fails at 60% while she is in a meeting; the import history shows the run failed and the audience unchanged, and she starts again with the same file.
- **UC-021.6c** Another import into the same audience is already running when the manager starts this one (BR-7):
  1. The system refuses to start and says an import into this audience is running; it keeps the file and the mapping.
  2. The marketing manager starts again once the running import finishes: returns to step 5. Or gives up: continues as in UC-021.1-5a.

  *Example:* Lena starts importing her fair contacts into "Customers" while Omar's newsletter-signup import into "Customers" is at 70%; the system refuses until Omar's import finishes.
- **UC-021.6d** A contact the import is writing is edited or unsubscribes elsewhere during the import:
  1. An unsubscribe stands: the import never resubscribes the contact.
  2. For other values, the import's values apply only if the manager chose to update existing contacts, and never as a blank (BR-6).
  3. Returns to step 6.

  *Example:* While Lena's import runs, Carla Diaz unsubscribes from a newsletter; Lena's file lists Carla as opted in, and Carla stays unsubscribed.

## Technology and data variations

- None.

## Related information

- **Frequency:** A few times a month per account, usually after an event.
- **Business rules:**
  - BR-1 a spreadsheet holds at most 100,000 rows (step 1, UC-021.1a).
  - BR-2 the new contacts must fit within the plan's contact limit, checked once before the import starts; the import never offers an upgrade (step 4, UC-021.4a).
  - BR-3 only contacts the manager states opted in are stored as subscribed; unknown consent or a purchased list stores the new contacts as non-subscribed, never emailed, and a purchased list is not consent (step 3, UC-021.3a).
  - BR-4 rows with a malformed address or a role address such as info@ are skipped, each with its reason (step 6, UC-021.1b).
  - BR-5 an address that appears on several rows is imported from its first row only; later rows are skipped (step 6, UC-021.1b).
  - BR-6 existing contacts are updated only if the manager chose that, and a blank cell never replaces a stored value (step 6, UC-021.6d).
  - BR-7 one import at a time runs into an audience (step 6, UC-021.6c).
- **Related use cases:** Create an audience (separate task); Export or erase a contact's personal data (separate job).
- **Open issues:** None.
