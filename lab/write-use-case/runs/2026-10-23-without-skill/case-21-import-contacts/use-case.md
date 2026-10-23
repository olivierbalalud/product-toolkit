---
id: UC-021
title: Import contacts into an audience
status: Draft
driver: lab
priority: TBD
source_locale: en
inputs: []
stories: []
---

# UC-021: Import contacts into an audience

| Field | Value |
|---|---|
| **Primary actor** | Marketing Manager |
| **Supporting actors** | None |
| **Scope** | The email marketing service |
| **Level** | User goal |
| **Trigger** | The Marketing Manager has a contact list exported from another tool, typically an event registration list, and asks to import it. |
| **Preconditions** | The Manager is signed in with permission to manage the account's audience. The target audience exists (it is created in another use case). |
| **Minimal guarantees** | The import is all-or-nothing: the audience is either changed by the whole import or left exactly as it was. No contact is stored as subscribed unless the Manager confirmed how the contacts consented. The uploaded file is deleted whatever the outcome, including when the Manager gives up before starting. Every started import, finished, cancelled or failed, is recorded in the import history. |
| **Success guarantees** | Every valid new row is added as a contact with its consent status and tagged with the import's name. If the Manager chose to update existing contacts, their non-blank values from the file are written and nothing is blanked; otherwise existing contacts are untouched. The audience is within the plan's contact limit as checked before the start. The import report (added, updated, skipped with reasons) is shown and kept in the import history. The uploaded file is deleted. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Marketing Manager | Gets an event's contacts into the audience quickly, without retyping, and knows exactly what was added, updated and skipped. Can walk away from a long import. |
| Contacts | Are emailed only if they agreed to it; their details are not duplicated; an existing value is never wiped out by a blank cell; an earlier unsubscribe is respected. |
| Deliverability team | No purchased lists and no role addresses such as info@ get subscribed, since they cause spam complaints. |
| Account owner | The audience stays within the plan's contact limit, with no surprise overage charge. |
| Compliance (data protection) | There is a record of how the imported contacts consented, and the uploaded file with its personal data is not kept. |

## Main success scenario

1. (actor) The Marketing Manager provides the contact list, as a CSV file, a spreadsheet file or rows pasted from the clipboard, and chooses the audience to import into.
2. (system, wait) The system reads the rows, proposes a mapping of columns to contact fields and shows it with a sample of rows.
3. (actor) The Manager confirms the mapping, states how the contacts consented (BR-3), chooses whether existing contacts are updated, and confirms the import's name.
4. (system, wait) The system checks the new contacts against the plan's contact limit and shows how many rows are new, existing (to be updated or skipped) and invalid, with the reason for each invalid row.
5. (actor) The Manager starts the import.
6. (system, background) The system adds the new contacts with their consent status, updates or skips the existing ones as chosen, and tags the new contacts with the import's name, showing progress and time remaining while the Manager watches.
7. (system) The system presents the import report, keeps it in the import history, deletes the uploaded file and, if the Manager has left, emails them that the import finished.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-021.1a, UC-021.1b | yes: UC-021.1b | yes: `UC-021.*a` | yes: UC-021.1-5a |
| 3 | yes: UC-021.3a | n/a | yes: `UC-021.*a` | yes: UC-021.1-5a |
| 5 | n/a | n/a | yes: `UC-021.*a` | yes: UC-021.1-5a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | yes: UC-021.2a | n/a | n/a | n/a | yes: UC-021.1a | n/a | n/a |
| 4 | yes: UC-021.4b | n/a | n/a | n/a | yes: UC-021.4a | n/a | n/a |
| 6 | n/a | yes: UC-021.6c, UC-021.6d | yes: UC-021.6b | yes: UC-021.6b | out-of-scope: the limit is checked once, before the start (UC-021.6e) | yes: UC-021.6d, UC-021.6e | yes: UC-021.6a |
| 7 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing a contact's personal data is a separate use case, not part of an import.

## Extensions

- **UC-021.1a** The file is unreadable, has no rows, or is over the size limit (100,000 rows or 50 MB, BR-1):
  1. The system says what is wrong with the file.
  2. The Manager provides another file and the use case returns to step 2, or gives up and the use case ends with the audience untouched and the file deleted.

  *Example:* Mia uploads a 140,000-row export of every past attendee; the system says the limit is 100,000 rows per file.
- **UC-021.1b** Some rows are invalid: the email address is malformed, is a role address such as info@, or repeats an address from an earlier row in the same file (BR-2):
  1. The system counts these rows as invalid at step 4, with the reason for each.
  2. The import skips them at step 6, imports the rest, and lists each skipped row with its reason in the report.

  *Example:* Of 320 registrations, row 41 has "jane.doe@@acme.com", row 88 is "info@acme.com" and row 203 repeats row 17's address; all three are skipped and listed.
- **UC-021.1-5a** The Manager gives up before starting the import:
  1. The system discards the file, the mapping and the choices.
  2. The use case ends with the audience untouched.

  *Example:* Mia sees the mapping, realises she exported the wrong event, and gives up.
- **UC-021.2a** No column can be recognised as the email address:
  1. The system asks the Manager which column holds the email address.
  2. The Manager picks the column and the use case returns to step 3.

  *Example:* The export labels the address column "Contact"; the system asks which column holds the email and Mia picks "Contact".
- **UC-021.3a** The Manager's mapping leaves no column mapped to the email address:
  1. The system says that email is required because it identifies a contact.
  2. Returns to step 3.

  *Example:* Mia sets the email column to "Don't import"; the system asks her to map a column to email.
- **UC-021.3b** The Manager can't say how the contacts consented, or the list was purchased (alternative):
  1. The system records the consent choice and continues; the new contacts will be stored as non-subscribed and never emailed (BR-3).
  2. Returns to step 4.

  *Example:* Mia imports a list her colleague bought from a trade-show organiser; the 500 new contacts are stored as non-subscribed.
- **UC-021.4a** The new contacts would take the audience over the plan's contact limit:
  1. The system says how many new contacts fit and does not offer to start the import.
  2. The Manager cuts the file down and the use case returns to step 1, or gives up and the use case ends with nothing imported. Upgrading the plan is a separate task.

  *Example:* The plan allows 2,000 contacts, the audience has 1,900 and the file has 250 new rows; the system says 100 fit.
- **UC-021.4b** No row would add or update a contact (every row is invalid, or every valid row already exists and updating is off):
  1. The system says the import would change nothing and does not offer to start it.
  2. The Manager changes the update option (back to step 3), provides another file (back to step 1), or gives up and the use case ends.

  *Example:* Mia re-imports last week's attendee list with updating off; all 320 rows already exist.
- **UC-021.4c** The Manager wants to change the mapping, the consent choice or the update option after seeing the counts (alternative):
  1. The use case returns to step 3, and step 4 recomputes the counts.

  *Example:* Mia sees 300 "existing, to skip" and switches updating on to refresh their company names.
- **UC-021.6a** The Manager cancels the import while it runs:
  1. The system stops, removes the contacts it added in this run and restores the existing contacts it updated.
  2. The system confirms the audience is unchanged, records the cancelled import in the history and deletes the file.
  3. The use case ends.

  *Example:* Halfway through 60,000 rows Mia notices the wrong audience was chosen and cancels; none of the 30,000 already added remain.
- **UC-021.6b** The service fails during the import:
  1. The system removes the contacts it added in this run and restores the existing contacts it updated, as for a cancel.
  2. The system tells the Manager (by email if they have left) that the audience is unchanged and they can start the import again, records the failed import in the history and deletes the file.
  3. The use case ends.

  *Example:* A server failure at row 12,000 of 40,000; the audience is put back and Mia is told to start again.
- **UC-021.6c** Another import into the same audience is already running when the Manager starts this one:
  1. The system does not start the import and says that one import at a time can run per audience (BR-6).
  2. The Manager starts it again once the other import finishes (back to step 4, which rechecks the limit and counts), or gives up and the use case ends.

  *Example:* Mia and Leo each import their event list into the same audience; Leo started first, so Mia is asked to wait.
- **UC-021.6d** Someone else edits or deletes a contact in the audience while the import runs:
  1. The system matches each row against the audience as it is when the row is written, not as counted at step 4: a contact deleted meanwhile is added as new, and one edited meanwhile gets the file's non-blank values if updating is on.
  2. The report shows what was actually done, which may differ from the step-4 counts.

  *Example:* Leo deletes ana@acme.com while Mia's import runs; Ana's row is added back as a new contact and counted as added.
- **UC-021.6e** Contacts added elsewhere (forms, manual entry) after step 4 push the audience over the plan's contact limit: `out-of-scope`, the product owner decided the limit is checked once, before the import starts; see Open issues.
- **`UC-021.*a`** The Manager's session expires or their permission to manage the audience is removed:
  1. Before step 5: the system discards the file and choices, the audience is untouched, and the use case ends; the Manager signs in and starts again.
  2. From step 6: the import was authorised when it started, so it runs to the end; the report is kept in the import history and the Manager is emailed the outcome.

  *Example:* Mia's session times out while she reviews the mapping; after signing in again she has to upload the file again.

## Technology and data variations

- 1: the list comes as a CSV file, an XLSX spreadsheet file, or rows pasted from the clipboard.
- 2: the mapping is proposed from header names, then from sample values (for example, a column of addresses with "@").
- 3: an unmapped column becomes a new custom field instead of being skipped.
- 6: matching existing contacts are also tagged with the import's name, so the whole event list can be emailed.
- 7: the skipped rows can be downloaded as a CSV file from the report.

## Related information

- **Frequency:** a few times a month per account, usually after an event. Files range from a few hundred rows (seconds) to tens of thousands (ten seconds to several minutes).
- **Business rules:**
  - **BR-1** A file holds at most 100,000 rows. Recommended: at most 50 MB.
  - **BR-2** A contact is identified by its email address, so email is the only required field. A row is invalid if its address is malformed or is a role address such as info@. When an address appears more than once in a file, the first row is imported and later ones are skipped.
  - **BR-3** The Manager states how the contacts consented. Recommended choices: "They opted in to marketing email from us (for example, on an event registration form)", stored as subscribed; or "Not sure, they didn't opt in, or the list was purchased", stored as non-subscribed and never emailed. A purchased list is never accepted as consent. Recommended: the choice, who made it, when, and the import's name are recorded with the contacts as proof of consent.
  - **BR-4** When updating an existing contact, a non-blank cell overwrites the existing value; a blank cell never replaces a value. Recommended: an import never changes an existing contact's subscription status, so an unsubscribed or bounced contact stays so.
  - **BR-5** The plan's contact limit is checked once, before the import starts. Recommended: it counts every contact stored in the audience, subscribed or not.
  - **BR-6** Recommended: one import at a time per audience.
  - **BR-7** Recommended: the import's name defaults to the file name and date, and the Manager may change it at step 3. Only new contacts get the tag, which is what lets a cancel or failure identify them.
  - **BR-8** The uploaded file is deleted when the import ends, whatever the outcome, and when the Manager gives up before starting.
- **Open issues:**
  - Does the plan's contact limit count all stored contacts or only subscribed ones (recommended: all)?
  - Contacts added elsewhere during a long import can push the audience over the limit (UC-021.6e). Is a possible overage acceptable, or should the limit be rechecked as rows are written?
  - Should matched existing contacts also get the import tag (variation at step 6)?
  - The skipped rows hold personal data; if they can be downloaded (variation at step 7), how long is the report kept?
  - Can a Manager import into an audience of an account other than their own? Recommended: no.
  - Target duration for a 100,000-row import (recommended: under 10 minutes) and the wording of the "finished" email.
