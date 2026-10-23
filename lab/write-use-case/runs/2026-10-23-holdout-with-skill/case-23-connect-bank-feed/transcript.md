**Q1.** Boundary first. I'd set it up like this: the scope is the accounting app; the bank (or a bank-data provider we go through) is a supporting actor, reached for authentication, consent and the transactions; the precondition is that the business's books already exist with their bank accounts set up; and the daily feed of new transactions is its own time-triggered use case, so this one ends once the feed is scheduled. Is that right, and do we connect to banks directly or through a provider?

**A1.** Yes, with three corrections.

1. **Scope:** Yes. The scope is our small-business accounting service.
2. **Supporting actors:** Yes, but there are two outside parties, not one. The bank data aggregator hands the Owner over to the bank and relays the consent and transactions. The bank authenticates the Owner, records the consent and provides the transactions.
3. **Precondition:** Only partly right. The precondition is that the company's books already exist and the Owner is signed in with permission to manage bank accounts. The bank accounts are not set up beforehand. Linking each shared account to a bank account in the books is part of this use case.
4. **Daily feed:** Yes. It's a separate, time-triggered thing. This use case ends once the daily feed is scheduled.
5. **Direct or through a provider:** Both. Some banks are connected through the aggregator and others through the bank's own API. The steps are the same either way.

**Q2.** Stakeholders. Besides the Business Owner (wants the bank transactions in the books without typing them), I see: the company's accountant (imported transactions are complete, not duplicated, and the books reconcile with the bank), and whoever answers for data protection (only the accounts the Owner consented to are read, and the consent is recorded). Who should I add or drop, and what does each insist on?

**A2.** **Keep:**
- **Business Owner:** wants transactions to arrive without typing them in, with none missing and none entered twice.
- **Accountant:** wants the books' balance to match the bank statement from the start date on. Missing and duplicate transactions are the Owner's concern, not the accountant's.

**Add:**
- **Bank and bank data aggregator:** want access only with the account holder's consent. The service must never see the bank credentials.
- **Account holder:** wants only the accounts the Owner chose to share, and only for the period they consented to. The system records when the consent ends and lists the shared accounts. This covers your consent-scope concern.

**Not decided:** whether a separate data-protection stakeholder should be added. Nothing in the facts names one. The account holder's consent-scope requirement is the closest match. Use your recommendation.

**Q3.** Guarantees. Minimal (however it ends): no transaction is imported twice, and no consent or link is left half-set-up; an aborted connection leaves the books as they were. Success: each shared account is linked to a bank account in the books, its transactions since the start date are imported, its balance matches the bank's, the consent and its end date are recorded with the list of shared accounts, and the daily feed is scheduled. Is that right? What should I add or drop?

**A3.** Mostly right, with three corrections.

**Minimal (however it ends):**
- No transaction is imported twice: **yes.** Entries that match ones already in the books are marked as possible duplicates for reconciliation and never added a second time.
- No consent or link is left half-set-up: **yes.**
- "An aborted connection leaves the books as they were": **not quite.** Giving up before the import leaves nothing recorded. Cancelling during the import removes what that run imported but keeps the link. If the bank or aggregator goes silent mid-import, what came in so far is kept, the import is marked incomplete, and it retries in the background.

**Success:**
- Each shared account is linked to a bank account in the books: **yes.**
- Transactions since the start date are imported: **yes, with one exception.** If the bank provides less history, we import what it gives and show the date the import actually starts from.
- Balance matches the bank's: **no, that isn't guaranteed.** The balance is compared with the bank's. On a mismatch, the system shows the difference and the transactions it may come from, and flags the account for review. Change this to "balance is compared; any difference is shown and flagged."
- Consent and its end date are recorded with the list of shared accounts: **yes.**
- Daily feed is scheduled: **yes, even when the balance doesn't match.**

**Add:**
- The service never sees or stores the bank credentials. This applies in every outcome.
- Only the accounts the Owner chose are shared, and only for the consented period.
- The Owner sees the number of transactions imported and the closing balance comparison.
- The consent end date is shown on each linked account.

**Q4.** Main scenario, as I'd rewrite it: 1. The Owner chooses the bank and the start date. 2. The Owner authenticates at the bank and consents to share the selected accounts. 3. The system records the consent with its end date and presents the shared accounts (a few seconds). 4. The Owner links each shared account to a bank account in the books. 5. The system imports the transactions since the start date, showing progress: I'd class this as 'long' (over 10 seconds, the Owner stays and watches, and can cancel). 6. The system compares the closing balance with the bank's, schedules the daily feed, and shows the number of transactions imported and the balance comparison. Is that the right flow, and is the import 'long' rather than something the Owner leaves running in the background?

**A4.** Yes, the flow is right, with three corrections.

1. **Steps 1–3:** Correct. The Owner picks the bank and start date (at most 12 months back), signs in and consents at the bank, and the system records the consent end date and lists the shared accounts in a few seconds.
2. **Step 4:** Linking each shared account to a bank account in the books is part of the outcome. Where it sits relative to the import is not decided. Use your recommendation.
3. **Step 5:** Yes, the import is long: about 15 seconds to two minutes. The Owner stays and watches it and can cancel. Cancelling removes what this run imported and keeps the link. It only moves to the background if the bank or aggregator stops responding mid-import. Then it's marked incomplete, retried in the background, and the Owner is notified when it completes.
4. **Step 6:** Correct, with one addition. The end-of-import summary also shows the consent end date on each linked account. If the closing balances don't match, the account is flagged for review, and the daily feed is still scheduled.

**Q5.** Conditions at the Owner's steps. At step 1 I see: a start date more than 12 months back or in the future, the bank isn't one we can connect to, and the bank is already connected for this company. At step 2: authentication fails at the bank, the Owner refuses consent or shares no account, and the Owner gives up at the bank. At step 4: a shared account is already linked in the books by an earlier feed, the Owner links two shared accounts to the same book account, or a shared account has no matching bank account in the books yet. And at any step before the import, the Owner gives up. What should I add or drop?

**A5.** **Step 1**
- Start date more than 12 months back: keep. The system says the earliest date it can import from, and the Owner picks again.
- Start date in the future: Not decided: a start date in the future. Use your recommendation.
- Bank not supported: keep. The system says so and offers to import a statement file instead, and that ends it.
- Bank already connected for this company: Not decided: a bank already connected for this company. Use your recommendation.

**Step 2**
- Authentication fails at the bank: drop. The bank handles wrong credentials, and we never see them.
- Owner refuses consent: keep, as giving up before the import. The pending connection is thrown away and no link is recorded.
- Owner shares no account: Not decided: the Owner shares no account. Use your recommendation.
- Owner gives up at the bank: keep. If they don't finish signing in within 10 minutes, the pending connection is thrown away and no link is recorded.

**Step 4**
- Shared account already linked by an earlier feed: keep. We propose renewing that link instead of making a second one. The import then brings in only what came after the last transaction already imported for that account.
- Two shared accounts linked to the same book account: Not decided: two shared accounts linked to the same book account. Use your recommendation.
- Shared account with no matching bank account in the books yet: Not decided: a shared account with no matching bank account in the books. Use your recommendation.

**Any step before the import**
- Owner gives up: keep. The pending connection is thrown away and no link is recorded.

**Q6.** Conditions at the system's steps. You've given me, at the import: the bank or aggregator stops responding mid-import, the bank provides less history than asked, imported entries match ones already in the books, and the Owner cancels; and at the comparison: the closing balances differ. I'd add: at step 3, the bank or aggregator doesn't answer when the system fetches the consent and the shared accounts; at step 5, a limit on the number of accounts or transactions per connection; and at step 6, scheduling the daily feed fails. Which of these three are real, and is anything else missing?

**A6.** - **Step 3, bank or aggregator not answering when the consent and shared accounts come back: real.** No link is recorded, the Owner is told the bank can't be reached, and they can start the connection again.
- **Step 5, a limit on accounts or transactions per connection: Not decided. Use your recommendation.**
- **Step 6, scheduling the daily feed fails: Not decided. Use your recommendation.**
- **Anything else missing: Not decided. Use your recommendation.**

**Q7.** Handling at the import when the bank or aggregator stops responding: I'd keep what came in, mark the import incomplete, tell the Owner it will finish in the background, schedule the daily feed and end the sitting there; when the background retry completes, the system compares the balances and notifies the Owner with the summary. Is that right, how is the Owner notified (in the app, by email), and what happens if the retries keep failing?

**A7.** Mostly yes. We keep what came in so far, mark the import incomplete, and retry in the background. The Owner is told the import is incomplete and gets a notification when it completes. The completion notice then shows the transaction count and how the closing balance compares with the bank's.

Not decided: whether the daily feed is scheduled while the import is incomplete. Use your recommendation.

Not decided: how the Owner is notified (in the app or by email). Use your recommendation.

Not decided: what happens if the retries keep failing. Use your recommendation.

**Q8.** Two leftovers. Frequency: I'd guess each company does this once per bank at setup, plus a renewal when consent ends; how often does it happen? Privacy: the imported transactions name people (payees, payers), so an Owner or account holder could ask to export or erase them; I'd mark that deferred to a separate account privacy use case, and withdrawing consent as its own use case too. Agreed?

**A8.** **Frequency:** Partly. It's a few times per company, not just at setup. It happens once for each bank when the company starts using the service, and again when it opens an account at a new bank. That's our estimate. Renewing consent when it expires is separate and not part of this use case.

**Privacy:** Partly. Exporting or erasing the personal data in the imported transactions is out of scope here. It belongs with disconnecting a bank, which is a separate job, and we have to keep accounting records for the legal period anyway. Not decided: withdrawing consent as its own use case. Use your recommendation.

