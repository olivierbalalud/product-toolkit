# Answers: import contacts from a spreadsheet

## Actor, goal and scope

- The system is our email marketing service.
- They start because they have a contact list exported from another tool, typically an event registration list, and want it in the service.
- Before they start they're already signed in with permission to manage the audience.
- No outside system or other person takes part; the service does everything itself.
- The contacts can come as a CSV file, a spreadsheet file, or rows pasted from the clipboard.
- It happens a few times a month per account, usually after an event.
- Upgrading the plan and sending a campaign are separate things, not part of this.

## Stakeholders and guarantees

- The Marketing Manager wants the whole list in, mapped to the right fields, without retyping or cleaning it by hand, and wants to be able to stop an import started by mistake.
- The contacts want to be emailed only if they agreed to it, and don't want their details duplicated or wiped out with blanks.
- The account owner wants to stay within the plan's contact limit and never get a surprise overage charge.
- The deliverability team doesn't want purchased lists or role addresses, because they bring spam complaints.
- If an import is cancelled or fails, the audience is exactly as it was before.
- An existing contact's value is never replaced with an empty one.
- When an import runs, every row in it ends up somewhere: added, updated, or skipped with a reason.
- The uploaded file holds people's personal data, so it's thrown away when it's over, whatever the outcome.
- When it works: new contacts are in with their consent status and tagged with the import's name, existing ones are updated if they asked for that, and there's a report of what was added, updated and skipped, with the reason for each skipped row.

## Main scenario

- The system reads the file and shows a sample of rows along with the proposed column mapping.
- Along with the mapping and the consent, they choose whether contacts already in the audience get updated.
- A contact is identified by its email address; that's how we tell new from existing.
- The count of new, existing and invalid rows comes with the contact limit check, before they start.
- While importing, the system shows progress and the time remaining.
- Tagging the new contacts with the import's name happens during the import itself, not afterwards.
- When updating existing contacts, a blank cell in the file never replaces a value we already have.
- The report lists each skipped row with its reason.

## What can go wrong

- The file can't be used: a format we don't read, an unknown encoding, no rows at all, or more than 100,000 rows, which is our limit per file.
- Some rows have a malformed address, or a role address such as info@.
- The same address appears on more than one row of the file.
- None of the columns can be recognised as the email address.
- They don't know how the contacts consented.
- They say the contacts come from a purchased list.
- The import would take the audience over the plan's contact limit.
- They give up before starting the import.
- They cancel while the import is running.
- The service fails partway through the import.
- They walk away while the import is running, without cancelling.

## How each is handled

- Unusable file: the system says what's wrong with it, and they either provide another file or give up. A file over 100,000 rows is treated just like an unreadable one.
- Bad addresses and role addresses: those rows are skipped, each listed with its reason, and they can go ahead with the rest.
- Repeated address: the first row with it is imported and the later ones are skipped.
- No email column recognised: the system asks them which column holds the email address, and they carry on confirming the mapping.
- Consent unknown: the new contacts are stored as non-subscribed and never emailed.
- Purchased list: we don't accept that as consent. The system tells them so, and the new contacts are stored as non-subscribed and never emailed, same as unknown consent.
- Over the contact limit: the system says how many new contacts fit; they cut the file down and start again, or give up. We don't offer an upgrade from here.
- Giving up before starting: the file and the mapping are thrown away and the audience is untouched.
- Cancelling during the import: the system stops, removes the contacts it added in this run, puts back the ones it updated, and confirms the audience is unchanged.
- Service failure: same clean-up, removing what was added and putting back what was updated; then it tells them the audience is unchanged and they can start the import again.
- Walking away during the import: the import still finishes, and the report is kept in the import history so they can read it later.

## Durations

- Reading the file and proposing the mapping takes a few seconds.
- Checking the limit and counting the rows also takes a few seconds.
- The import itself: a few hundred rows go in within seconds, but thousands of rows take from about ten seconds to several minutes. They stay and watch it, and can cancel.
- The report shows up straight away once the import is done.

## Out of scope

- The contact limit being reached during the import because contacts were added elsewhere since the check: not handled; we check the limit once, before the import starts, and not again while rows are written.
- Exporting or erasing a contact's personal data: that's a separate job, not part of an import.
