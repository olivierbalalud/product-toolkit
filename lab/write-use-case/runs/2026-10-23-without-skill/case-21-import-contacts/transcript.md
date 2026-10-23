**Q1.** What is the system under design, and who is the Marketing Manager importing for? What happens before this use case starts (e.g. must the audience already exist, must the Manager be signed in with a given role)?

**A1.** **System under design:** our email marketing service. No outside system or other person takes part; the service does everything itself.

**Who the Marketing Manager imports for:** the contacts go into the account's audience. Not decided: whether the Manager imports for anyone beyond that account. Use your recommendation.

**Before the use case starts:**
- The Manager is already signed in with permission to manage the audience. The facts don't name a specific role.
- Not decided: whether the audience must already exist before the import starts. Use your recommendation.
- The Manager already has a contact list exported from another tool, typically an event registration list.

**Q2.** What file formats and size limits does the spreadsheet have (CSV, XLSX, max rows or MB)? What happens if the file is unreadable, empty, or too big?

**A2.** **Formats:** The contacts can come as a CSV file, a spreadsheet file, or rows pasted from the clipboard. Not decided: which spreadsheet file types are read (for example, XLSX). Use your recommendation.

**Size limit:** 100,000 rows per file. Not decided: a limit in megabytes. Use your recommendation.

**Unreadable file:** The system says what's wrong with it, and the user either provides another file or gives up.

**Empty file (no rows):** Handled the same way as an unreadable file.

**Too big (over 100,000 rows):** Treated the same way as an unreadable file.

**Q3.** On the column mapping: how does the system propose it (from header names?), what fields are required (is email mandatory?), can the Manager skip columns or create new custom fields, and what if no column maps to email?

**A3.** The system proposes a mapping and shows it with a sample of rows. Not decided: how the mapping is proposed, such as whether it uses header names. Use your recommendation.

Email is effectively mandatory. A contact is identified by its email address, so the import can't match or add contacts without one. Not decided: whether any other field is required. Use your recommendation.

Not decided: whether the Manager can skip columns. Use your recommendation.

Not decided: whether the Manager can create custom fields. Use your recommendation.

If no column can be recognised as the email address, the system asks which column holds it. They then carry on confirming the mapping.

**Q4.** On consent: what exactly does the Manager confirm (that all contacts opted in to marketing email?), is it recorded, and what if the Manager can't confirm? Are contacts who previously unsubscribed or bounced in this account treated specially?

**A4.** Consent is chosen with the column mapping, before the import starts. The Manager's confirmation does not have to be that all contacts opted in, because the exact wording is not decided. Not decided: the exact wording of what the Manager confirms. Use your recommendation.

New contacts are stored with their consent status. Not decided: whether the Manager's confirmation itself is recorded. Use your recommendation.

If the Manager can't say how the contacts consented, the import still goes ahead, and the new contacts are stored as non-subscribed and never emailed. A purchased list is not accepted as consent, and those contacts get the same treatment.

Not decided: whether contacts who previously unsubscribed or bounced in this account are treated specially. Use your recommendation.

**Q5.** On the plan's contact limit: what happens if the new contacts would exceed it? Can the Manager import part, upgrade the plan, or must they cancel? Does the limit count all contacts or only subscribed ones?

**A5.** - **Over the limit:** The system tells them how many new contacts fit. They can cut the file down and start again, or give up. Nothing is imported in that case.
- **Import part:** Yes, by cutting the file down to the number that fits and starting again. There's no option to import a selection from this screen.
- **Upgrade the plan:** Not from here. Upgrading is a separate task, outside the import.
- **Cancel:** They can give up before starting. The file and mapping are discarded and the audience is untouched.
- **Counting:** Not decided: whether the limit counts all contacts or only subscribed ones. Use your recommendation.

**Q6.** For rows that match an existing contact by email: are they updated (overwrite fields, fill blanks only) or skipped? Does the Manager choose? And what about the same email appearing twice in the file?

**A6.** Matching rows are updated if the Manager chose that option. Otherwise they are skipped. When updating, a non-blank cell in the file overwrites the existing value, but a blank cell never replaces a value we already have. So it's not fill-blanks-only.

Yes, the Manager chooses whether existing contacts get updated, along with the column mapping and the consent setting.

For an email that appears more than once in the file, the first row is imported and the later rows are skipped. Each skipped row is listed in the report with its reason.

**Q7.** When updating an existing contact, can the import change their subscription status, e.g. resubscribe someone who unsubscribed? And what makes a row invalid (malformed email, other checks)? Are invalid rows skipped and the rest imported?

**A7.** **Subscription status of existing contacts:** Not decided: whether an import can change the subscription status of an existing contact, including resubscribing someone who unsubscribed. Use your recommendation.

**What makes a row invalid:** A row is skipped if its email address is malformed or is a role address such as info@. A row is also skipped if its address repeats one from an earlier row in the same file; the first row is imported and the later ones are skipped. Not decided: any other checks beyond these. Use your recommendation.

**Skipping:** Yes. Invalid rows are skipped, each one is listed in the report with its reason, and the rest of the file is imported.

**Q8.** How long does the import itself take for a large file (seconds, minutes)? Must the Manager stay and watch, or can they leave and be notified (how)? Can they cancel it midway, and if so what happens to rows already imported?

**A8.** **Duration:** A few hundred rows go in within seconds. Thousands of rows take from about ten seconds to several minutes. Not decided: the exact time for the largest files (up to 100,000 rows). Use your recommendation.

**Staying and watching:** They don't have to stay. The system shows progress and time remaining while they watch, but if they walk away, the import still finishes and the report is kept in the import history for them to read later. Not decided: how they are notified when it finishes. Use your recommendation.

**Cancelling midway:** Yes, they can cancel. The system stops and removes the contacts it added in that run. It puts back the existing contacts it had updated, then confirms the audience is unchanged. No rows from a cancelled import remain.

**Q9.** What if the import fails midway because of a system error? Is it all-or-nothing (rolled back like a cancel) or are imported rows kept? And what happens if someone else edits or deletes a contact in the audience, or another import runs on the same audience, while this one is running?

**A9.** **Service failure:** It's all-or-nothing. Imported rows are not kept. The system removes the contacts it added in this run and restores the contacts it updated, the same clean-up as a cancel. It then tells them the audience is unchanged and they can start the import again.

**Someone else edits or deletes a contact while the import runs:** Not decided: what happens when someone else edits or deletes a contact during the import. Use your recommendation.

**Another import runs on the same audience:** Not decided: how a concurrent import on the same audience is handled. The contact limit is checked only once, before the import starts, and contacts added elsewhere in the meantime are not handled. Use your recommendation.

**Q10.** About the tag and report: what tag is applied to new contacts (automatic like the file name and date, or chosen by the Manager)? Are updated contacts tagged too? What does the report contain, and can the Manager download the skipped rows?

**A10.** - **Tag:** New contacts are tagged with the import's name, and the tag is added during the import itself.
  - Not decided: whether the name is set automatically or chosen by the Manager. Use your recommendation.
- **Updated contacts:** Not decided: whether updated contacts get the tag. Use your recommendation.
- **Report:** It shows what was added, updated and skipped, with the reason for each skipped row.
- **Download of skipped rows:** Not decided: whether the Manager can download the skipped rows. Use your recommendation.

**Q11.** Which stakeholders besides the Marketing Manager care about this import, and what do they need protected (e.g. the contacts themselves, deliverability, the account owner paying for the plan, compliance)? Also, how often do imports happen, and is the uploaded file kept after the import?

**A11.** **Other stakeholders and what they need protected:**
- **The contacts:** they're emailed only if they agreed to it, their details aren't duplicated, and an existing value is never wiped out with a blank.
- **The deliverability team:** no purchased lists and no role addresses such as info@, since they cause spam complaints.
- **The account owner:** the audience stays within the plan's contact limit, with no surprise overage charge.
- **Compliance:** Not decided: whether compliance is a stakeholder. Use your recommendation. The file is deleted after the import, whatever the outcome.

**How often:** a few times a month per account, usually after an event.

**Is the file kept?** No. The uploaded file is thrown away when the import is over, whatever the outcome. It's also thrown away if they give up before starting.

**Q12.** What happens if the Manager's session expires or they lose permission partway through (before starting, or while the import runs)? And can a contact later ask to have the data from this import exported or erased, or is that handled elsewhere?

**A12.** **Session expiry or lost permission before starting:** Not decided: what happens if the session expires or permission is lost before the import starts. Use your recommendation.

**Session expiry or lost permission while the import runs:** Not decided: what happens if the session expires or permission is lost while the import runs. Use your recommendation.

**Contact export or erasure:** Exporting or erasing a contact's personal data is a separate job, not part of an import, so this import doesn't handle it.

**Q13.** After seeing the counts of new, existing and invalid rows, can the Manager go back and change the mapping, consent or update option before starting? And what if every row is invalid or already exists (nothing new to add)?

**A13.** **Going back to change the mapping, consent or update option after the counts:** Not decided: whether they can go back and change these before starting. Use your recommendation. What the facts do give: they can give up before starting, which throws away the file and mapping and leaves the audience untouched. If the file is over the contact limit, they cut it down and start again with a new file.

**Every row invalid or already existing:** Not decided: what happens when there are no new contacts to add. Use your recommendation.

