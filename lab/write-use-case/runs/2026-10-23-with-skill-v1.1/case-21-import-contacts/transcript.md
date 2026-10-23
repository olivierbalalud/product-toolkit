**Q1.** Before the details: from your steps I see no outside party the system calls on during the import (everything happens inside our product), so Supporting actors would be None. For the ways the work is done, I see two variations: at step 1 the spreadsheet given as a CSV file or as an Excel file; and at step 2 the mapping proposed from the column headers or from a mapping saved at a previous import. (1) Continue with these, adding or dropping any, or (2) stop here and go back to product ideation first. I recommend 1. Which outside parties or variations should I add or drop?

**A1.** 1. **Outside parties:** None. Agreed. No outside system or other person takes part, so supporting actors would be None.
2. **Step 1 inputs:** Drop "Excel" and say "spreadsheet file", which covers it. Add rows pasted from the clipboard. The inputs are a CSV file, a spreadsheet file, or pasted rows.
3. **Step 2 mapping:** The system proposes the column mapping from the file's columns. If it can't recognise the email column, it asks the user which column holds the email address. Not decided: whether a mapping saved from a previous import can be reused. Use your recommendation.

**Q2.** Boundary facts, to confirm in one go: the primary actor is the Marketing Manager; the goal is 'Import contacts into an audience'; the scope is our email marketing platform as a whole; the precondition is that the Manager is signed in and the audience already exists (creating an audience is a separate use case, as is sending a campaign to the new contacts); and nothing waits on anyone else, so the use case ends when the import report is presented. Is that right, and is there any other task you consider separate?

**A2.** - **Primary actor:** Yes, the Marketing Manager starts the import and wants the list in.
- **Goal:** Yes, importing contacts into an audience.
- **Scope:** Yes, the system is our email marketing service.
- **Precondition:** Yes, the Manager is signed in with permission to manage the audience. Not decided: that the audience already exists, and that creating an audience is a separate use case. Use your recommendation.
- **Sending a campaign:** Yes, it's separate.
- **Nothing waits on anyone else:** Yes. No outside system or other person takes part.
- **Ending:** Nearly. The report shows straight away once the import is done. If the Manager has walked away, the import still finishes and the report is kept in the import history to read later.

Other tasks I consider separate: upgrading the plan, sending a campaign, and exporting or erasing a contact's personal data.

**Q3.** Stakeholders. Besides the Marketing Manager (gets the list in quickly without broken or duplicate contacts), I see: the imported contacts themselves (receive only email they agreed to, their data handled lawfully); the account owner who pays (the plan's contact limit is respected, no surprise charges); and our company as the sender (consent is recorded so a complaint can be answered, and sender reputation isn't damaged by unconsented lists). Who should I add or drop, and is each interest stated right?

**A3.** **Drop** "our company as the sender" and **add** the deliverability team. They're the stakeholder that doesn't want purchased lists or role addresses, because those bring spam complaints.

- **Marketing Manager:** right, but add that they want to be able to stop an import started by mistake.
- **Imported contacts:** partly right. They want email only if they agreed to it, and don't want their details duplicated or existing values wiped out with blanks. The file holds their personal data, so it's deleted when the import is over, whatever the outcome. "Handled lawfully" isn't stated.
- **Account owner:** right. They want to stay within the plan's contact limit and never get a surprise overage charge.
- **Deliverability team (replacing the sender):** the stated concern is spam complaints from purchased lists and role addresses. "Consent recorded so a complaint can be answered" isn't stated. Not decided: whether consent records must be kept so complaints can be answered. Use your recommendation.

**Q4.** Guarantees. Minimal (true however it ends): the uploaded file is deleted, no contact is duplicated, no existing value is overwritten with a blank, and the audience never goes over the plan's contact limit. Success: the new contacts are in the audience, tagged with this import, with the Manager's consent confirmation recorded (who and when); existing contacts are updated with the file's non-blank values; invalid rows are left out and listed; and the import report is kept in the import history. Agreed, or what should change?

**A4.** **Minimal guarantees:** Mostly agreed, with one correction.
- Uploaded file deleted: yes, whatever the outcome.
- No duplicate contacts: yes. A repeated address is imported once and the later rows are skipped.
- No existing value overwritten with blank: yes.
- Audience never over the plan's contact limit: needs changing. The limit is checked once, before the import starts. If contacts are added elsewhere during the import, that case is out of scope and not handled, so the guarantee can't be stated as "never." It should say the limit is checked before the import starts.

**Success guarantees:**
- New contacts in the audience, tagged with this import: yes. Tagging happens during the import.
- Consent confirmation recorded with who and when: Not decided: who and when the consent confirmation is recorded. Use your recommendation. The facts only say the consent status is chosen with the mapping, and that unknown or purchased-list consent stores the contacts as non-subscribed.
- Existing contacts updated with the file's non-blank values: yes, but only when the Manager chose to update existing contacts. Add that condition.
- Invalid rows left out and listed: yes, each with its reason.
- Import report kept in the import history: yes.

**Q5.** Here are your steps rewritten, with how long each feels to the Manager: 1 (actor) The Manager provides the spreadsheet and chooses the audience. 2 (system, a few seconds) The system reads the spreadsheet and proposes a mapping of its columns to contact fields. 3 (actor) The Manager confirms the mapping, chooses the contacts' consent status and whether existing contacts are updated. 4 (system, a few seconds) The system checks the plan's contact limit and shows how many rows are new, existing or invalid. 5 (actor) The Manager starts the import. 6 (system, background) The system imports the rows and tags the new contacts, showing progress; the Manager may leave. 7 (system) The system presents the import report and keeps it in the import history. I mark step 6 'background' (minutes, the Manager may leave) rather than 'long' (the Manager stays and watches), because you said the import finishes if the Manager walks away. Is the order right, and are the durations right?

**A5.** **Order:** Yes, steps 2 to 7 match. Step 1 says the Manager "chooses the audience," but nothing I know settles that. Not decided: which audience the Manager chooses. Use your recommendation.

**Step 6 label:** Keep it as the Manager staying and watching, which is the main scenario. The facts say they watch it and can cancel. Walking away is a branch: the import still finishes and the report goes to the import history. So step 6 is not "background" as the normal case.

**Durations:**
- Step 2 (read and propose mapping): a few seconds. Correct.
- Step 4 (limit check and row counts): a few seconds. Correct.
- Step 6 (import): not "minutes" in general. A few hundred rows finish within seconds. Thousands take about 10 seconds to several minutes.

**Q6.** Choices and rules at step 3. I'd write: the consent status is one of 'opted in', 'unknown' or 'purchased list', with no default so the Manager must choose; contacts imported with 'unknown' or 'purchased list' are stored as non-subscribed (a business rule); and 'update existing contacts' is off by default, so existing contacts are left untouched unless the Manager turns it on. Is that right? And does the business set any other rule the import enforces, such as a maximum file size or number of rows, or a rule about role addresses like info@ or sales@?

**A6.** Mostly yes, with one gap.

- **Consent choices:** Unknown and purchased list are the two cases we have. The Manager chooses the consent status along with the mapping. Whether there is a default is not decided: Not decided: whether consent has a default. Use your recommendation. Our terms don't use the label "opted in", but the agreed case is the one the consent choice covers.
- **Unknown or purchased list:** Yes. Those contacts are stored as non-subscribed and never emailed. We don't accept a purchased list as consent.
- **Update existing contacts:** Existing contacts are updated only if the Manager asks for it, so leaving it off leaves them untouched. Not decided: the default setting. Use your recommendation. A blank cell never replaces a value we already have.

Other rules the import enforces:
- **Row limit:** 100,000 rows per file. A bigger file is rejected as unusable.
- **File size:** Not decided: maximum file size in megabytes. Use your recommendation.
- **Role addresses:** Yes, addresses such as info@ are skipped and listed with a reason. sales@ is the same kind of address, so it is skipped too.
- **Other row rules:** Malformed addresses are skipped with a reason. When an address repeats, the first row is imported and later ones are skipped. The contact limit is checked once, before the import starts.

**Q7.** What can go wrong at the Manager's steps (1 provide the spreadsheet, 3 confirm mapping and consent, 5 start). I see: (a) the file can't be used at all: unreadable, empty, or over 100,000 rows; (b) some rows are invalid: a malformed address, a role address, or an address repeated earlier in the file; (c) the email column isn't recognised, so the system asks which column holds the address; (d) the Manager confirms without mapping any column to the email address, or without choosing a consent status; (e) the Manager gives up at any point before starting the import. I'd treat importing the same file again as harmless (its contacts just count as existing). What should I add or drop?

**A7.** Yes, mostly. Here is each item:

- **(a)** Yes. The file can't be used if it's in a format we don't read, has an unknown encoding, has no rows, or has more than 100,000 rows. The system says what's wrong, and they either provide another file or give up.
- **(b)** Yes, with one correction. For a repeated address, the first row is imported and the later rows are skipped. Malformed and role addresses are skipped too, each listed with its reason.
- **(c)** Yes. The system asks which column holds the email address, and they then confirm the mapping.
- **(d)** Confirming without an email column is the same case as (c): they must map the email column before going on. Not decided: whether they can confirm without choosing a consent status. Use your recommendation. Note that "we don't know how they consented" is a valid choice, and it stores the new contacts as non-subscribed.
- **(e)** Yes. Giving up before starting throws away the file and the mapping, and the audience is untouched.

**Add:**
- **Purchased list** at step 3. We don't accept it as consent. The system tells them, and the new contacts are stored as non-subscribed and never emailed.
- **Over the contact limit**, which the pre-start check reveals before step 5. They either cut the file down and start again, or give up. No upgrade is offered from here.

**Drop:** nothing from your list. The cancel, service-failure and walk-away cases happen during the import, after step 5, so they belong to a later step.

On re-importing the same file: contacts are matched by email, so they count as existing. They're updated only if the Manager chose to update existing contacts, and a blank cell never replaces a stored value.

**Q8.** Now the system's steps (2 propose mapping, 4 limit check and counts, 6 import, 7 report). Besides the unrecognised email column at 2 and the contact limit at 4, I see at step 6: (a) the Manager stops the import while it runs; (b) the import fails part-way because of a fault on our side; (c) the Manager walks away and the import finishes without them; (d) contacts are added to the audience elsewhere during the import, out of scope as you said; (e) someone else deletes the audience, or the Manager loses permission on it, while the import runs. Nothing else at 2, 4 or 7. What should I add or drop?

**A8.** **(a) Stop during the import:** Already covered. Cancelling stops the import, removes the contacts it added in this run, puts back the ones it updated, and confirms the audience is unchanged. Keep it.

**(b) Service fails partway:** Already covered. The same clean-up runs, the audience is confirmed unchanged, and they can start the import again. Keep it.

**(c) Walks away during the import:** Already covered. The import still finishes, and the report is kept in the import history. Keep it.

**(d) Contacts added elsewhere during the import:** Yes, out of scope. The limit is checked once, before the import starts, and not again while rows are written. Keep it as an out-of-scope note.

**(e) Audience deleted, or the Manager loses permission, during the import:** Not decided: how this case is handled. Use your recommendation.

Your list also misses some cases that apply to steps 2, 4 and 7:

- **Step 2:** If they don't know how the contacts consented, or say the list was purchased, the new contacts are stored as non-subscribed and never emailed.
- **Step 4:** If they give up before starting, the file and mapping are discarded and the audience is untouched.
- **Step 7:** Bad or role addresses and repeated addresses are skipped, and the report lists each skipped row with its reason.

**Q9.** Last points. Frequency: how often does a Manager import contacts, and how large is a typical file? And for privacy, I'd mark a contact's request to export or erase their data as deferred to the separate use case you named, since this import handles names and addresses. Agreed?

**A9.** A Manager imports a few times a month per account, usually after an event.

Not decided: typical file size. Use your recommendation. The limit is 100,000 rows per file.

Yes, agreed. Exporting or erasing a contact's personal data is a separate job, not part of an import.

