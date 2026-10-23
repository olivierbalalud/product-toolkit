---
id: UC-021
title: Import contacts from a spreadsheet
status: Draft
driver: lab
priority: TBD
source_locale: en
inputs: []
stories: []
---

# UC-021: Import contacts from a spreadsheet

| Field | Value |
|---|---|
| **Primary actor** | Marketing Manager |
| **Supporting actors** | None |
| **Scope** | Email marketing service |
| **Level** | User goal |
| **Trigger** | The Marketing Manager has a contact list exported from another tool, typically an event registration list, and asks to import it into an audience. |
| **Preconditions** | The Marketing Manager is signed in with permission to manage the audience. |
| **Minimal guarantees** | If the import is abandoned, cancelled or fails, the audience is exactly as it was before. An existing contact's value is never replaced with an empty one (BR-3). The uploaded file is discarded when the use case ends, whatever the outcome (BR-8). |
| **Success guarantees** | Every row in the import has been added, updated or skipped with a reason (BR-9). New contacts are in the audience with their consent status and tagged with the import's name. Existing contacts are updated only if the Manager asked for it. A report lists what was added, updated and skipped, with the reason for each skipped row. The audience stays within the plan's contact limit. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Marketing Manager | Gets the whole list in, mapped to the right fields, without retyping or cleaning it by hand; can stop an import started by mistake. |
| Contacts | Are emailed only if they agreed to it; their details are not duplicated or wiped out with blanks. |
| Account owner | Stays within the plan's contact limit and never gets a surprise overage charge. |
| Deliverability team | Keeps purchased lists and role addresses out, because they bring spam complaints. |

## Main success scenario

1. (actor) The Marketing Manager provides the contact list and chooses the audience to import it into.
2. (system, wait) The system reads the list and shows a sample of rows with a proposed mapping of columns to contact fields.
3. (actor) The Marketing Manager confirms the mapping, states how the contacts consented, and chooses whether contacts already in the audience get updated.
4. (system, wait) The system checks the plan's contact limit and shows how many rows are new, existing or invalid, telling new from existing by email address (BR-1).
5. (actor) The Marketing Manager starts the import.
6. (system, long) The system adds the new contacts with their consent status, tagged with the import's name, and updates existing contacts if asked, never replacing a value with a blank cell (BR-3); it shows progress and the time remaining.
7. (system) The system presents the import report: contacts added, contacts updated, and each skipped row with its reason; it discards the uploaded file (BR-8).

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-021.1a, UC-021.1c | yes: UC-021.1b | n/a | yes: UC-021.1-5a |
| 3 | yes: UC-021.3a, UC-021.3b | n/a | n/a | yes: UC-021.1-5a |
| 5 | n/a | n/a | n/a | yes: UC-021.1-5a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | yes: UC-021.2a | n/a | n/a | n/a | yes: UC-021.1a | n/a | n/a |
| 4 | n/a | n/a | n/a | n/a | yes: UC-021.4a | n/a | n/a |
| 6 | n/a | n/a | n/a | yes: UC-021.6c | out-of-scope: the contact limit is checked once before the import starts and not again while rows are written (BR-7) | out-of-scope: same reason, contacts added elsewhere after the check are not rechecked (BR-7) | yes: UC-021.6a, UC-021.6b |
| 7 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

**Privacy request:** no: exporting or erasing a contact's personal data is a separate job, not part of an import. The uploaded file, which holds personal data, is discarded when the use case ends, whatever the outcome (BR-8).

## Extensions

- **UC-021.1a** The list can't be used: a format the system doesn't read, an unknown encoding, no rows at all, or more than 100,000 rows (BR-2):
  1. The system says what is wrong with the list.
  2. The Marketing Manager provides another list: returns to step 2. Or the Manager gives up: the use case ends, as in UC-021.1-5a.

  *Example:* Ana provides a registration export of 120,000 rows; the system tells her the limit is 100,000 rows per file.
- **UC-021.1b** The same email address appears on more than one row:
  1. The system imports the first row with that address and skips the later ones (BR-5), each listed in the report as a duplicate in the file.
  2. Returns to the step in progress.

  *Example:* ben@example.com appears on rows 12 and 340; row 12 is imported and row 340 is skipped as a duplicate.
- **UC-021.1c** Some rows have a malformed email address or a role address such as info@ (BR-4):
  1. The system counts those rows as invalid at step 4 and skips them at step 6, each listed in the report with its reason.
  2. The Marketing Manager can go ahead with the rest: returns to the step in progress.

  *Example:* Of 800 rows, "carla@@example" is skipped as malformed and "info@example.com" as a role address; the other 798 are imported.
- **UC-021.2a** No column can be recognised as the email address:
  1. The system asks which column holds the email address.
  2. The Marketing Manager chooses the column.
  3. Returns to step 3.

  *Example:* The export labels the email column "Courriel"; the system asks, and Ana points it to that column.
- **UC-021.3a** The Marketing Manager doesn't know how the contacts consented:
  1. The system records that the new contacts will be stored as non-subscribed and never emailed (BR-6).
  2. Returns to step 4.

  *Example:* Ana inherited a list from a former colleague with no record of consent; its 300 new contacts are stored as non-subscribed.
- **UC-021.3b** The Marketing Manager says the contacts come from a purchased list:
  1. The system tells the Manager that a purchased list is not accepted as consent.
  2. The system records that the new contacts will be stored as non-subscribed and never emailed (BR-6).
  3. Returns to step 4.

  *Example:* Ana selects "purchased list" for a trade show list she bought; the system tells her this isn't consent and stores the contacts as non-subscribed.
- **UC-021.4a** The import would take the audience over the plan's contact limit:
  1. The system says how many new contacts fit within the limit. It does not offer a plan upgrade.
  2. The Marketing Manager cuts the list down and provides it again: returns to step 1. Or the Manager gives up: the use case ends, as in UC-021.1-5a.

  *Example:* The plan allows 5,000 contacts, the audience has 4,600 and the list holds 700 new ones; the system says 400 fit.
- **UC-021.1-5a** The Marketing Manager gives up before starting the import:
  1. The system discards the uploaded list and the mapping; the audience is untouched.
  2. The use case ends.

  *Example:* Ana notices she chose the wrong audience after seeing the counts and leaves; nothing is imported.
- **UC-021.6a** The Marketing Manager cancels while the import is running:
  1. The system stops the import, removes the contacts it added in this run and puts back the ones it updated.
  2. The system confirms that the audience is unchanged and discards the uploaded file (BR-8).
  3. The use case ends.

  *Example:* Ana starts importing 20,000 rows into the newsletter audience instead of the event audience and cancels at 30%; the 6,000 contacts added so far are removed.
- **UC-021.6b** The Marketing Manager walks away while the import is running, without cancelling:
  1. The system finishes the import.
  2. The system keeps the report in the import history so the Manager can read it later, and discards the uploaded file (BR-8).
  3. The use case ends.

  *Example:* Ana starts a 50,000-row import and closes her laptop; the next morning she reads the report in the import history.
- **UC-021.6c** The service fails partway through the import:
  1. The system removes the contacts it added in this run and puts back the ones it updated.
  2. The system tells the Marketing Manager that the audience is unchanged and that they can start the import again, and discards the uploaded file (BR-8).
  3. The use case ends.

  *Example:* The service fails after writing 4,000 of 10,000 rows; the 4,000 are rolled back and Ana is told she can run the import again.

## Technology and data variations

- Step 1: the contacts come as a CSV file, a spreadsheet file, or rows pasted from the clipboard.
- Step 3: existing contacts are updated, or left as they are.
- Step 6: a few hundred rows go in within seconds; thousands of rows take from about ten seconds to several minutes.

## Related information

- **Frequency:** A few times a month per account, usually after an event.
- **Business rules:**
  - BR-1: A contact is identified by its email address; that is how new contacts are told from existing ones.
  - BR-2: A file holds at most 100,000 rows; a larger file is treated as unusable.
  - BR-3: When an existing contact is updated, a blank cell in the file never replaces a value already held.
  - BR-4: Rows with a malformed email address or a role address (such as info@) are skipped, each with its reason.
  - BR-5: When an email address appears on several rows, the first row is imported and the later ones are skipped.
  - BR-6: A purchased list is not consent. New contacts whose consent is unknown or who come from a purchased list are stored as non-subscribed and never emailed.
  - BR-7: The plan's contact limit is checked once, before the import starts, and not again while rows are written.
  - BR-8: The uploaded file is discarded when the use case ends, whatever the outcome.
  - BR-9: Every row in an import that runs ends up added, updated, or skipped with a reason.
- **Open issues:** None. Upgrading the plan and sending a campaign are separate use cases.
