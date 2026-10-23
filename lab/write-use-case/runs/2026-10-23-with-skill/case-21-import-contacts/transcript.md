**Q1.** A few boundary facts, which I'd settle as follows. (a) The scope is our email marketing platform, and no outside system is called during the import (supporting actors: none). (b) Preconditions: the manager is signed in and the audience already exists; creating an audience is a separate task. (c) The import itself (step 5) takes over 10 seconds for a normal large file and the manager stays and watches the progress, rather than leaving and being told later. Correct?

**A1.** (a) Yes. The system is our email marketing service, and no outside system or other person takes part, so supporting actors: none.

(b) Partly. The manager is signed in with permission to manage the audience, and the audience is the one the import goes into. Not decided: whether creating an audience is a separate task. Use your recommendation.

(c) Not quite. A few hundred rows go in within seconds. Thousands of rows take from about ten seconds to several minutes. The manager can stay and watch progress and time remaining, and can cancel. But they can also walk away: the import still finishes, and the report is kept in the import history to read later.

**Q2.** Stakeholders. Besides the marketing manager (wants the list in the audience quickly, without retyping or cleaning it by hand), I see: the people in the spreadsheet (only receive mail if they consented, and their existing data isn't overwritten wrongly); the account owner who pays for the plan (the contact limit is respected, no surprise overage); and whoever answers for data protection and sender reputation (consent is recorded for every imported contact, so bounces and complaints stay low). What would you add or drop?

**A2.** Keep the marketing manager, the contacts, and the account owner as you have them. For the account owner, the limit is checked before the import starts, and the import never offers an upgrade.

The fourth stakeholder should be the deliverability team, not data protection. Their concern is no purchased lists and no role addresses such as info@, because those bring spam complaints. Recording consent is how we handle contacts whose consent is unknown or purchased: they are stored as non-subscribed and never emailed.

Data protection is not a named stakeholder. The uploaded file is deleted when the import ends, whatever the outcome, and that is a guarantee rather than a stakeholder.

Not decided: whether bounces are a concern for anyone. Use your recommendation.

**Q3.** Guarantees. Minimal (true however it ends): the uploaded file is deleted when the import ends; no contact is ever stored as subscribed without confirmed consent; the plan's contact limit is never exceeded. Success: the new contacts are in the audience with their consent status recorded and the import tag, existing contacts are handled as decided, and the import report (new, updated, skipped and invalid rows) is kept in the import history. Is that right, and is anything missing?

**A3.** Mostly right, with one correction and some missing items.

- **File deletion:** Correct. The file is thrown away when the import ends, whatever the outcome.
- **Consent:** Correct. Unknown consent or a purchased list stores the new contacts as non-subscribed, and they're never emailed.
- **Contact limit:** Not right as stated. The limit is checked once, before the import starts, and not again while rows are written. A limit reached because contacts were added elsewhere during the import isn't handled. So "never exceeded" needs that qualification.
- **Success, new contacts:** Correct. They go in with their consent status and the import's name as a tag, and the tagging happens during the import.
- **Success, existing contacts:** Handled as the user chose at setup. A blank cell in the file never replaces a stored value.
- **Success, report:** It lists added, updated and skipped rows, and each skipped row has its reason. Invalid rows appear as skipped rows with a reason, not as a separate category. The facts say the report is kept in import history when the user walks away. Not decided: whether it's kept in history after a normal finish. Use your recommendation.

Missing from the list:

- **Cancelled or failed import:** The audience is exactly as it was before. Added contacts are removed and updated contacts are restored. This applies to both cancellation and service failure.
- **Every row accounted for:** Each row ends up added, updated, or skipped with a reason.
- **No duplicates:** When an address appears on more than one row, the first row is imported and the later ones are skipped.

**Q4.** Main scenario, rewritten: 1. The manager provides the spreadsheet and chooses the audience. 2. The system reads the file and proposes a mapping of columns to contact fields (a few seconds). 3. The manager confirms the mapping, chooses how existing contacts are handled, and states the contacts' consent. 4. The system checks the plan's contact limit against the new rows and presents how many rows will be added, updated and skipped (a few seconds). 5. The manager starts the import. 6. The system imports the rows, tagging new contacts with the import's name, with progress and time remaining; the manager may leave. 7. The system presents the report and keeps it in the import history. I'd offer two choices for existing contacts, 'update them' (default) or 'leave them unchanged', and three consent statements: 'they opted in' (stored as subscribed), 'unknown' and 'purchased list' (both stored as non-subscribed). Agreed?

**A4.** Yes, with these corrections:

- **Step 1, "chooses the audience":** Not decided: how the audience is chosen. Use your recommendation.
- **Step 3, existing contacts:** Yes, they choose whether existing contacts are updated. But existing contacts are updated only if they asked for that, so "update them" shouldn't be the default. Not decided: which option is pre-selected. Use your recommendation.
- **Step 4:** The check shows counts of new, existing and invalid rows, not added, updated and skipped. Existing rows are updated only if that option was chosen.
- **Consent:** Yes. "They opted in" is stored as subscribed. "Unknown" and "purchased list" are both stored as non-subscribed and never emailed. Choosing "purchased list" also makes the system tell them that it isn't accepted as consent.
- **Steps 5 to 7:** Yes. The import shows progress and time remaining, new contacts are tagged with the import's name during the import, the manager can leave, and the report is shown when the import finishes and kept in the import history.

**Q5.** What can go wrong at the manager's steps? I see: at step 1, the file is not a readable spreadsheet, is empty, or is over a size or row limit; at step 3, no column is mapped to the email address; within the file, rows with an invalid address, role addresses such as info@, and an address that appears on several rows; and the manager giving up any time before starting the import. Which of these are real, what limits apply (file size, rows), and what else can go wrong there?

**A5.** - **Unreadable file (step 1):** Real. Causes are a format we don't read, an unknown encoding, or no rows at all. The system says what's wrong, and they either provide another file or give up.
- **Over the row limit (step 1):** Real. The limit is 100,000 rows per file, and a larger file is treated like an unreadable one. Not decided: file size limit. Use your recommendation.
- **No email column (step 3):** Real. The system asks which column holds the email address, and they confirm the mapping and carry on.
- **Invalid addresses and role addresses such as info@:** Real. Those rows are skipped, each listed in the report with its reason, and they can go ahead with the rest.
- **Same address on several rows:** Real. The first row is imported and the later ones are skipped, each listed with its reason.
- **Giving up before starting:** Real. The file and mapping are thrown away and the audience is untouched.

Also possible before the import starts:
- **Consent unknown:** The new contacts are stored as non-subscribed and never emailed.
- **Purchased list:** Not accepted as consent. The system says so, and the new contacts are stored as non-subscribed and never emailed.
- **Over the plan's contact limit:** The system says how many new contacts fit. They cut the file down and start again, or give up. We don't offer an upgrade from here.

**Q6.** Now the system's steps. During the import (step 6) I see: the manager cancels part-way; the import fails part-way (service failure); another import into the same audience runs at the same time; a contact is edited or unsubscribes elsewhere while the import is writing it; and contacts added elsewhere after the check push the audience past the plan limit (which you said isn't handled). Which of these are real, and what else can go wrong at the mapping, the check or the import?

**A6.** - **Manager cancels part-way:** Real. The system stops, removes the contacts it added in this run, puts back the ones it updated, and confirms the audience is unchanged.
- **Import fails part-way (service failure):** Real. The same clean-up runs, the system tells them the audience is unchanged, and they can start the import again.
- **Another import into the same audience at the same time:** Not decided: how two concurrent imports into one audience interact. Use your recommendation.
- **Contact edited or unsubscribes elsewhere while the import writes it:** Not decided: how a concurrent edit or unsubscribe is resolved. Use your recommendation. An existing value is never replaced with a blank, but nothing else is settled.
- **Contacts added elsewhere push the audience past the plan limit:** Real, and not handled. The limit is checked once before the import starts, not again while rows are written.

Other things that can go wrong:

- **File (before mapping):** A format we don't read, an unknown encoding, no rows, or more than 100,000 rows. The system says what's wrong, and they either provide another file or give up.
- **Mapping:** If no column is recognised as the email address, the system asks which column holds it, and they confirm the mapping. If consent is unknown or the contacts come from a purchased list, the new contacts are stored as non-subscribed and never emailed. For a purchased list, the system also tells them we don't accept that as consent.
- **Check:** If the import would go over the contact limit, the system says how many new contacts fit. They cut the file down and start again, or give up. Giving up before starting throws away the file and mapping, and the audience is untouched.
- **Import:** Malformed addresses and role addresses (such as info@) are skipped, each with its reason. A repeated address is imported on its first row and skipped on later ones. If they walk away, the import still finishes and the report stays in the import history.

**Q7.** Handling during the import, as I'd write it: (a) cancel: the system rolls back and confirms the audience is unchanged; the use case ends. (b) service failure: the same roll-back; since the file is deleted when the import ends, the manager starts again by providing the file anew; the failed run is recorded in the import history. (c) a manager who left learns the outcome, success or failure, from the import history only, with no email. (d) a second import into an audience that already has one running is refused when the manager starts it, and can be started once the first finishes. (e) a contact who unsubscribes elsewhere during the import stays unsubscribed; the import never resubscribes them. Correct?

**A7.** Not quite. Parts (a), (b), and the file deletion in (b) match the facts. Parts (c), (d), and (e) and the rest of (a) and (b) are not settled.

- **(a) Cancel:** Yes. The system stops, removes the contacts added in this run, puts back the updated ones, and confirms the audience is unchanged. Not decided: whether the use case ends there. Use your recommendation.
- **(b) Service failure:** Yes for the roll-back and the restart. The system cleans up the same way and tells them the audience is unchanged. The file is thrown away when the import is over, whatever the outcome, and they can start the import again. Not decided: whether the failed run is recorded in the import history. Use your recommendation.
- **(c) Manager who left:** The report is kept in the import history so they can read it later. Not decided: whether an email is sent, and whether a failed run's outcome appears there. Use your recommendation.
- **(d) Second import while one is running:** Not decided. Use your recommendation.
- **(e) Unsubscribe during the import:** Not decided. Use your recommendation.

**Q8.** Last two points. How often do imports happen (roughly, per account or overall)? And the contacts' personal data: I'd mark a request by a contact to export or erase their data as deferred, handled by a separate contact privacy use case, not here. Agreed?

**A8.** **How often:** A few times a month per account, usually after an event. Overall: Not decided. Use your recommendation.

**Personal data requests:** Agreed, it's out of scope for this import. Exporting or erasing a contact's personal data is a separate job, not part of an import. I haven't named a separate use case for it, so that part is yours to decide.

