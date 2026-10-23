---
id: UC-021
title: Import contacts into an audience
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-021: Import contacts into an audience

| Field | Value |
|---|---|
| **Primary actor** | Marketing Manager |
| **Supporting actors** | None |
| **Scope** | Email marketing service |
| **Level** | User goal |
| **Trigger** | The Marketing Manager has a list of contacts to add to an audience, usually after an event. |
| **Preconditions** | The Marketing Manager is signed in with permission to manage the audience, and the audience exists. |
| **Minimal guarantees** | The uploaded file is deleted, whatever the outcome. No contact is duplicated, and no stored value is overwritten with a blank. The import starts only after the plan's contact limit has been checked. An import that is stopped or fails leaves the audience as it was. |
| **Success guarantees** | The new contacts are in the audience, tagged with this import, with the consent status the Marketing Manager chose and who confirmed it and when; contacts whose consent is unknown or from a purchased list are stored as non-subscribed (BR-1). Existing contacts are updated with the file's non-blank values only if the Marketing Manager chose to update them. Each skipped row is listed with its reason, and the import report is kept in the import history. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Marketing Manager | Gets the list into the audience quickly, without broken or duplicate contacts, and can stop an import started by mistake. |
| Imported contacts | Receive email only if they agreed to it; their details aren't duplicated and stored values aren't wiped out with blanks; the file holding their personal data is deleted when the import is over. |
| Account owner | Stays within the plan's contact limit and never gets a surprise overage charge. |
| Deliverability team | No purchased lists or role addresses get in, since they bring spam complaints. |

## Main success scenario

1. (actor) The Marketing Manager provides the spreadsheet and chooses the audience to import into (BR-2).
2. (system, wait) The system reads the spreadsheet and proposes a mapping of its columns to contact fields.
3. (actor) The Marketing Manager confirms the mapping, chooses the contacts' consent status (BR-1) and chooses whether existing contacts are updated.
4. (system, wait) The system checks the plan's contact limit (BR-4) and shows how many rows are new, existing or skipped (BR-3, BR-5).
5. (actor) The Marketing Manager starts the import.
6. (system, long) The system imports the rows and tags the new contacts with this import, showing progress.
7. (system) The system presents the import report, listing each skipped row with its reason, and keeps it in the import history.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-021.1a, UC-021.1b | yes: UC-021.1b | n/a | yes: UC-021.1-5a |
| 3 | yes: UC-021.3a, UC-021.3b | n/a | n/a | yes: UC-021.1-5a |
| 5 | n/a | n/a | n/a | yes: UC-021.1-5a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | yes: UC-021.2a | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | n/a | n/a | n/a | n/a | yes: UC-021.4a | n/a | n/a |
| 6 | n/a | yes: UC-021.6d | n/a | yes: UC-021.6b | out-of-scope: the contact limit is checked once, before the import starts; contacts added to the audience elsewhere during the import are not handled | out-of-scope: the counts shown at step 4 are not checked again; contacts added to the audience elsewhere during the import are not handled | yes: UC-021.6a |
| 7 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing a contact's personal data is a separate use case, not part of an import.

## Extensions

- **UC-021.1-5a** The Marketing Manager gives up before starting the import:
  1. The system discards the file and the mapping; the audience is untouched.
  2. The use case ends.

  *Example:* Lea Martin provides "salon-2026.csv", sees the proposed mapping, and leaves without starting the import; the "Trade fair leads" audience has the same 3,200 contacts as before.
- **UC-021.1a** The file can't be used: it is in a format the system doesn't read, has an unknown encoding, has no rows, or has more than 100,000 rows (BR-2):
  1. The system says what is wrong with the file and keeps nothing.
  2. The Marketing Manager provides another file: returns to step 1. Or gives up: the use case ends.

  *Example:* Lea provides "all-leads.csv" with 140,000 rows; the system says a file holds at most 100,000 rows, and Lea provides "leads-part-1.csv" with 70,000 rows instead.
- **UC-021.1b** Some rows hold a malformed address, a role address (BR-3), or an address already given in an earlier row of the file (BR-5):
  1. The system counts these rows as skipped at step 4 and leaves them out of the import.
  2. The import report lists each skipped row with its reason.
  3. Returns to step 2.

  *Example:* Lea's file has 500 rows, among them "tom.dupont@example" (malformed), "info@example.com" (role address) and a second row for "ana.silva@example.com"; step 4 shows 3 skipped rows, and the report lists each with its reason.
- **UC-021.2a** The system does not recognise which column holds the email address:
  1. The system asks the Marketing Manager which column holds the email address, keeping the rest of the proposed mapping.
  2. Returns to step 3.

  *Example:* Lea's file has its addresses in a column headed "Courriel"; the system asks which column holds the email address, and Lea points to "Courriel".
- **UC-021.3a** The Marketing Manager confirms without a column mapped to the email address, or without choosing a consent status:
  1. The system asks for the missing choice, keeping the rest of the mapping.
  2. Returns to step 3.

  *Example:* Lea confirms the mapping of "salon-2026.csv" without choosing a consent status; the system asks her to choose one, and she chooses "unknown".
- **UC-021.3b** The Marketing Manager chooses "purchased list" as the consent status:
  1. The system tells the Marketing Manager that a purchased list is not consent, and that the new contacts will be stored as non-subscribed and never emailed (BR-1).
  2. Returns to step 4.

  *Example:* Lea imports 2,000 contacts bought from a list broker and chooses "purchased list"; the system warns her, and the 2,000 new contacts are stored as non-subscribed.
- **UC-021.4a** The new contacts would take the audience over the plan's contact limit (BR-4):
  1. The system shows by how many contacts the limit would be exceeded, and offers no upgrade from here.
  2. The Marketing Manager cuts the file down and provides it again: returns to step 1. Or gives up: the file and the mapping are discarded, the audience is untouched, and the use case ends.

  *Example:* Lea's plan allows 10,000 contacts and her audience holds 9,600; her file has 700 new contacts, so the system says the import would exceed the limit by 300, and Lea provides a file with 400 rows.
- **UC-021.6a** The Marketing Manager stops the import while it runs:
  1. The system stops the import, removes the contacts it added in this run and puts back the values of the contacts it updated.
  2. The system confirms that the audience is unchanged and deletes the file.
  3. The use case ends.

  *Example:* Lea starts importing 40,000 rows into the wrong audience, notices it at 25% and stops; the 10,000 contacts already added are removed and the audience is as it was.
- **UC-021.6b** The import fails part-way because of a fault in the system:
  1. The system removes the contacts it added in this run and puts back the values of the contacts it updated.
  2. The system tells the Marketing Manager that the import failed, confirms that the audience is unchanged and deletes the file.
  3. The Marketing Manager starts a new import: returns to step 1. Or stops: the use case ends.

  *Example:* Lea's import of 20,000 rows fails at 60%; the 12,000 contacts added are removed, the system says the audience is unchanged, and Lea provides the file again.
- **UC-021.6c** The Marketing Manager leaves while the import runs:
  1. The system finishes the import and keeps the import report in the import history, where the Marketing Manager reads it later.
  2. The use case ends.

  *Example:* Lea starts importing 60,000 rows and goes to a meeting; when she comes back, the report in the import history shows 58,900 contacts imported and 1,100 skipped.
- **UC-021.6d** The audience is deleted, or the Marketing Manager loses permission to manage it, while the import runs:
  1. The system stops the import and removes the contacts it added in this run and puts back the values of the contacts it updated, as in UC-021.6b.
  2. The system tells the Marketing Manager that the import stopped because the audience no longer exists or is no longer theirs to manage, and deletes the file.
  3. The use case ends.

  *Example:* While Lea's import into "Trade fair leads" runs, her colleague Marc Petit deletes that audience; the import stops and Lea is told why.

## Technology and data variations

- 1: the Marketing Manager provides the contacts as a CSV file, as a spreadsheet file, or as rows pasted from the clipboard.

## Related information

- **Frequency:** A few times a month per account, usually after an event.
- **Business rules:**
  - BR-1 A purchased list is not consent: contacts imported with an unknown consent status or from a purchased list are stored as non-subscribed and never emailed (step 3, UC-021.3b).
  - BR-2 A file holds at most 100,000 rows; a bigger file is rejected as unusable (step 1, UC-021.1a).
  - BR-3 Role addresses, such as info@ or sales@, are skipped (step 4, UC-021.1b).
  - BR-4 The new contacts must fit within the plan's contact limit, checked once before the import starts (step 4, UC-021.4a).
  - BR-5 When an address appears in several rows of a file, the first row is imported and the later rows are skipped (step 4, UC-021.1b).
- **Related use cases:** Create an audience; Upgrade the plan; Send a campaign; Export or erase a contact's personal data.
- **Open issues:** None.
