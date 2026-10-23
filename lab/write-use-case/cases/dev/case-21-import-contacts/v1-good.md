- **ID / Name:** UC-21 — Import Contacts from a Spreadsheet
- **Scope:** Email marketing service (black box) · **Level:** User goal (!)
- **Primary actor:** Marketing Manager
- **Stakeholders & interests:**
  - Marketing Manager — gets the whole list in, mapped to the right fields, without retyping or cleaning it by hand; can stop an import started by mistake.
  - Contacts — are emailed only if they consented; their details are not duplicated or overwritten with blanks.
  - Account owner — stays within the plan's contact limit; no surprise overage charge.
  - Deliverability team — no purchased lists or role addresses that raise spam complaints.
- **Trigger:** Marketing Manager has a contact list exported from another tool, such as an event registration list.
- **Preconditions:** Marketing Manager is signed in with permission to manage the audience.
- **Minimal guarantees:** A cancelled or failed import leaves the audience as it was; an existing contact is never overwritten with empty values; every row of the file is accounted for.
- **Success guarantees:** New contacts are added with their consent status and tagged with the import's name; existing contacts are updated if the Manager chose so; an import report lists the rows added, updated and skipped, each skipped row with its reason.

**Main success scenario**
1. Marketing Manager provides the spreadsheet file and chooses the audience to import into.
2. System reads the file and proposes a mapping of its columns to contact fields, with a sample of rows.
3. Marketing Manager confirms the mapping, states how the contacts gave consent, and chooses whether existing contacts are updated.
4. System checks the file against the plan's contact limit and presents the number of new, existing and invalid rows.
5. Marketing Manager starts the import.
6. System imports the rows, showing progress and the time remaining (from about ten seconds to several minutes for large files).
7. System presents the import report and tags the new contacts with the import's name.

**Extensions**
- 2a. File cannot be read (unsupported format, unknown encoding, no rows): System says what is wrong; Marketing Manager provides another file (continue at step 2) or abandons (use case ends).
- 2b. No column can be mapped to the email address: System asks the Manager to choose it; continue at step 3.
- 3a. Marketing Manager cannot state how the contacts consented: System will import them as non-subscribed (BR-3); continue at step 4.
- 4a. Import would exceed the plan's contact limit: System states how many contacts fit; Marketing Manager reduces the file (continue at step 1) or abandons (use case ends).
- 4b. Some rows are invalid (malformed address, role address such as info@) or appear twice in the file: System lists them as skipped; continue at step 5.
- 6a. Marketing Manager cancels while the import runs: System stops, removes the contacts imported in this run, and confirms the audience is unchanged; use case ends.
- 6b. The import is interrupted by a service failure: System removes the contacts imported in this run and tells the Manager the import can be started again; use case ends.

**Business rules:** BR-1 a contact is identified by its email address · BR-2 files up to 100,000 rows · BR-3 contacts without stated consent are stored as non-subscribed and never emailed.
**Technology & data variations:** CSV or spreadsheet file; rows pasted from the clipboard.
**Notes:** a few hundred rows import in seconds; files of thousands of rows take minutes.
**Related:** Upgrade Plan, Send Campaign.
