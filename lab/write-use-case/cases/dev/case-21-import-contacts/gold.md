---
id: UC-021
title: Import contacts from a spreadsheet
status: Draft
driver: lab
priority:
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
| **Trigger** | The Marketing Manager wants to add a contact list exported from another tool, such as an event registration list. |
| **Preconditions** | The Marketing Manager is signed in with permission to manage the audience. |
| **Minimal guarantees** | A cancelled or failed import leaves the audience as it was; an existing contact is never overwritten with empty values; every row of an import that runs is accounted for; the uploaded file, which holds the contacts' personal data, is discarded when the use case ends, however it ends. |
| **Success guarantees** | New contacts are added with their consent status and tagged with the import's name; existing contacts are updated if the Marketing Manager chose so; an import report lists the rows added, updated and skipped, each skipped row with its reason. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Marketing Manager | Gets the whole list in, mapped to the right fields, without retyping or cleaning it by hand; can stop an import started by mistake. |
| Contacts | Are emailed only if they consented; their details are not duplicated or overwritten with blanks. |
| Account owner | Stays within the plan's contact limit; no surprise overage charge. |
| Deliverability team | No purchased lists or role addresses that raise spam complaints. |

## Main success scenario

1. (actor) The Marketing Manager provides the contact file and chooses the audience to import into.
2. (system, wait) The system reads the file (BR-2) and proposes a mapping of its columns to contact fields, with a sample of rows.
3. (actor) The Marketing Manager confirms the mapping, states how the contacts gave consent, and chooses whether existing contacts are updated.
4. (system, wait) The system checks the import against the plan's contact limit and presents the number of new, existing and invalid rows (BR-1).
5. (actor) The Marketing Manager starts the import.
6. (system, long) The system imports the rows, showing progress and the time remaining: it adds the new contacts with their consent status (BR-3) and tags them with the import's name, and updates the existing contacts if the Marketing Manager chose so, never replacing a value with a blank.
7. (system) The system presents the import report: the rows added, updated and skipped, each skipped row with its reason.

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
| 6 | n/a | n/a | yes: UC-021.6b | yes: UC-021.6b | out-of-scope: the limit is checked at step 4 and not again while the rows are written | n/a | yes: UC-021.6a, UC-021.6c |
| 7 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, erasing or exporting a contact's data is its own use case and is not part of an import.

## Extensions

- **UC-021.1-5a** The Marketing Manager abandons before starting the import:
  1. The system discards the file and the mapping; the audience is unchanged.
  2. The use case ends.

  *Example:* Lena sees the proposed mapping, realises she exported last year's list, and leaves without starting the import; the audience still holds its 2,140 contacts.
- **UC-021.1a** The file cannot be used: unsupported format, unknown encoding, no rows, or more than 100,000 rows (BR-2):
  1. The system says what is wrong with the file.
  2. The Marketing Manager provides another file and the use case returns to step 2, or abandons (UC-021.1-5a).

  *Example:* Lena provides `open-day.numbers`, a format the system does not read; she exports it as CSV and provides that instead.
- **UC-021.1b** Some rows are invalid (a malformed address, or a role address such as info@) or repeat an address that an earlier row of the file already holds (BR-1):
  1. When it checks the import (step 4), the system counts those rows as invalid and lists each one as skipped, with its reason; the first row with a repeated address is kept.
  2. Returns to step 5.

  *Example:* Of Lena's 1,200 rows, `info@northwind.example` is a role address, `tom@@mail.example` is malformed and `ana@example.com` appears on rows 18 and 640; the system lists three rows as skipped: the role address, the malformed one, and row 640.
- **UC-021.2a** No column can be mapped to the email address:
  1. The system asks the Marketing Manager to choose the column that holds the email address (BR-1).
  2. Returns to step 3.

  *Example:* Lena's file has the columns "Name", "Company" and "Contact"; the system asks which one holds the email address and she chooses "Contact".
- **UC-021.3a** The Marketing Manager cannot state how the contacts consented:
  1. The system records that the new contacts will be stored as non-subscribed (BR-3).
  2. Returns to step 4.

  *Example:* Lena imports badge scans from a trade fair and does not know how the visitors consented; the 412 new contacts will be stored as non-subscribed and never emailed.
- **UC-021.3b** The Marketing Manager states that the contacts come from a purchased list:
  1. The system says that a purchased list is not consent (BR-4) and records that the new contacts will be stored as non-subscribed (BR-3).
  2. Returns to step 4.

  *Example:* Lena states that the 3,000 contacts were bought from a lead vendor; the system tells her this is not consent, and the 3,000 will be stored as non-subscribed and never emailed.
- **UC-021.4a** The import would exceed the plan's contact limit:
  1. The system states how many new contacts fit within the limit.
  2. The Marketing Manager reduces the file and the use case returns to step 1, or abandons (UC-021.1-5a).

  *Example:* Lena's plan allows 5,000 contacts and the audience holds 4,600; her file has 750 new contacts, so the system says 400 fit.
- **UC-021.6a** The Marketing Manager cancels while the import runs:
  1. The system stops the import, removes the contacts added in this run and restores the contacts it updated.
  2. The system confirms that the audience is unchanged.
  3. The use case ends.

  *Example:* Lena starts importing 8,000 rows into the wrong audience and cancels at 30 %; the system removes the 2,100 contacts added, restores the 300 it updated, and confirms the audience still holds its 2,140 contacts.
- **UC-021.6b** The import is interrupted by a service failure:
  1. The system removes the contacts added in this run and restores the contacts it updated.
  2. The system tells the Marketing Manager that the audience is unchanged and that the import can be started again.
  3. The use case ends.

  *Example:* The service fails after 5,000 of Lena's 12,000 rows; the system removes those 5,000 contacts and tells her she can start the import again.
- **UC-021.6c** The Marketing Manager leaves while the import runs, without cancelling it:
  1. The system completes the import.
  2. The system keeps the import report in the import history, where the Marketing Manager can read it later.
  3. The use case ends.

  *Example:* Lena starts importing 9,000 rows and closes her laptop to catch a train; the import completes, and later she reads its report in the import history.

## Technology and data variations

- 1: the contacts come as a CSV file, a spreadsheet file, or rows pasted from the clipboard.

## Related information

- **Frequency:** a few times a month per account, typically after an event.
- **Business rules:** BR-1 a contact is identified by its email address · BR-2 files have up to 100,000 rows · BR-3 contacts without stated consent are stored as non-subscribed and never emailed · BR-4 a purchased list is not consent.
- **Duration:** a few hundred rows import in seconds; files of thousands of rows take minutes, from about ten seconds to several minutes for large files (step 6).
- **Related use cases:** Upgrade Plan, Send Campaign.
- **Open issues:** None
