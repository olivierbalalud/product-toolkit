**Q1.** What is the system under design, who uses this, and what outside parties are involved (e.g. a bank aggregator or open-banking provider)?

**A1.** The system under design is our small-business accounting service, and the Business Owner is the person who uses it to bring the company's bank transactions into the books.

The outside parties are:
- **A bank data aggregator**, which hands the Owner over to the bank and relays the consent and the transactions.
- **The bank itself**, which authenticates the Owner, records the consent, and provides the transactions.

**Q2.** What must already be true before the owner starts (company set up, bank accounts created in the books, role/permission needed)? And how far back can the start date go?

**A2.** Before they start, the Owner must be signed in with permission to manage bank accounts, and the company's books must already exist.

Not decided: whether the bank accounts must already be created in the books. Use your recommendation.

The start date can go back at most 12 months, or less if the bank provides less history.

**Q3.** Is the start date allowed to be before the books' opening date or inside a closed (locked) accounting period? What happens if it is?

**A3.** Not decided: whether the start date may be before the books' opening date, and what happens if it is. Use your recommendation.

Not decided: whether the start date may fall inside a closed (locked) accounting period, and what happens if it does. Use your recommendation.

The only start-date limit I have is that it can't be more than 12 months back. If it is, the system says the earliest date it can import from, and the Owner picks again.

**Q4.** What happens if the owner's bank is not in the list, the aggregator or bank is down, or the owner fails or cancels authentication at the bank or shares no accounts?

**A4.** - **Bank not in our list:** We say so and offer to import a statement file instead. That's the end of the connection attempt.
- **Aggregator or bank down before the import starts** (during hand-over or when consent should come back): No bank link is recorded. The Owner is told the bank can't be reached and can start the connection again.
- **Aggregator or bank stops answering mid-import:** We keep what came in so far, mark the import incomplete, retry in the background, and notify the Owner when it completes.
- **Owner fails or cancels at the bank:** If they leave, refuse consent, or don't finish signing in within 10 minutes, the pending connection is thrown away and no link is recorded. Wrong credentials are handled by the bank, since we never see them.
- **Owner shares no accounts:** Not decided: what happens when no accounts are shared. Use your recommendation.

**Q5.** In linking (step 3): can the owner create a new bank account in the books while linking, skip some shared accounts, and what if a shared account is already linked to a feed (in this company or another), or two shared accounts are linked to the same book account? What about currency mismatch?

**A5.** - **Create a new bank account in the books while linking:** Not decided: creating a new book account during linking. Use your recommendation.
- **Skip some shared accounts:** Not decided: skipping shared accounts during linking. Use your recommendation.
- **Shared account already linked in this company:** Yes. We propose renewing that existing link instead of making a second one, and the import brings in only the transactions after the last one already imported for that account.
- **Shared account already linked in another company:** Not decided: a shared account linked in another company. Use your recommendation.
- **Two shared accounts linked to the same book account:** Not decided: two shared accounts linked to the same book account. Use your recommendation.
- **Currency mismatch:** Not decided: currency mismatch between the bank account and the book account. Use your recommendation.

**Q6.** How long does the import in step 4 usually take, does the owner wait or may they leave, and how are duplicates handled (transactions already in the books, e.g. from an earlier statement file import)?

**A6.** **Duration:** About 15 seconds to two minutes, depending on the bank and the period.

**Waiting:** The Owner stays and watches the import, and can cancel it. Not decided: whether they may leave without cancelling. Use your recommendation.

**Duplicates:** Transactions that match entries already in the books, including ones from an earlier statement file import, are marked as possible duplicates for reconciliation. They're never added a second time, and the import carries on.

**Q7.** If the owner cancels the import mid-way, what happens to the transactions already imported and to the bank link and consent?

**A7.** Cancelling stops the import and removes the transactions that this run had already imported. The bank link is kept, and the Owner is told they can start the import again.

Not decided: whether the bank consent itself is kept on cancel. Use your recommendation.

**Q8.** In step 5, which balances exactly are compared, what tolerance, and what happens when they don't match? Does the bank always provide a balance?

**A8.** The system compares the books' closing balance with the bank's closing balance.

Not decided: tolerance. Use your recommendation.

If they don't match, the system shows the difference and the transactions it may come from, and flags the account for review. The daily feed is still scheduled.

Not decided: whether the bank always provides a balance. Use your recommendation.

**Q9.** About the daily feed in step 6: how long does the bank consent last, and what does the owner learn about expiry? Is the daily feed itself (and its failures) part of this use case or a separate one?

**A9.** **Consent length:** Not decided: how many days or months the consent lasts. Use your recommendation. The bank sets that period, and the consent has to be renewed when it ends.

**What the owner learns about expiry:** At the end of the import, the owner sees the consent end date on each linked account. When the consent comes back, the system also records when it ends.

**Daily feed:** It is a separate use case. This one schedules the daily feed at the end, but the feed itself and its failures are not part of this use case. Renewing the bank's consent is also separate.

**Q10.** Are there limits: number of bank connections or accounts per company or plan, aggregator call quotas or rate limits, maximum number of transactions per import?

**A10.** Not decided: number of bank connections or accounts per company or plan. Use your recommendation.

Not decided: aggregator call quotas or rate limits. Use your recommendation.

Not decided: maximum number of transactions per import. Use your recommendation. The only limit I can state is on the period: the import goes back at most 12 months from the chosen start date, or less if the bank provides less.

**Q11.** Who else cares about this (accountant, the bank, the aggregator, counterparties named in transactions), and what is logged or kept for audit? Can someone ask to export or erase the personal data in imported transactions?

**A11.** **Who else cares:**
- **Accountant:** the books' balance must match the bank statement from the start date on.
- **Bank and aggregator:** they want access only with the account holder's consent. The service must never see the bank credentials.
- **Account holder:** only the accounts the Owner chose to share, and only for the period they consented to.
- **Counterparties named in transactions:** Not decided: whether counterparties have any stake in this. Use your recommendation.

**What is logged or kept for audit:** Not decided: what is logged for audit during the connection itself. Use your recommendation. What is kept: the bank records the consent, each linked account shows when its consent ends, and accounting records are kept for the legal period.

**Export or erasure:** Not in this use case. Exporting or erasing personal data in imported transactions belongs to disconnecting a bank, which is a separate job. Accounting records must be kept for the legal period regardless.

**Q12.** What if two people in the same company connect the same bank account at the same time, or the owner's session expires during the flow? And how often is this done?

**A12.** **Same bank account connected by two people at the same time:** Not decided: what happens when both connections run at the same moment. Use your recommendation. If the account is already linked when the second connection comes back, we propose renewing that existing link instead of making a second one. The import then brings in only transactions after the last one already imported, so nothing is imported twice.

**Owner's session expiring during the flow:** Not decided: what happens when the session expires mid-flow. Use your recommendation. The closest rule: if the Owner leaves before the import starts, the pending connection is thrown away and no link is recorded.

**How often:** A few times per company. It happens once for each bank when the company starts using the service, and again each time it opens an account at a new bank. That's our estimate.

**Q13.** When the import is interrupted and retried in the background, how long do retries go on before giving up, how is the owner notified, and is the daily feed scheduled even though the import is incomplete? Also, if several accounts are linked and only one fails, do the others complete normally?

**A13.** - **Retry duration:** Not decided: how long the background retries go on before giving up. Use your recommendation.
- **Notification:** The Owner is told the import is incomplete, and gets a notification when it completes.
- **Daily feed:** Not decided: whether the daily feed is scheduled while the import is incomplete. Use your recommendation.
- **Other accounts:** Not decided: whether the other linked accounts complete normally when one of them fails. Use your recommendation.

