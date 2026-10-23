- **ID / Name:** UC-23 — Connect a Bank Account to Import Transactions
- **Scope:** Small-business accounting service (black box) · **Level:** User goal (!)
- **Primary actor:** Business Owner
- **Supporting actors:** Bank data aggregator, Bank
- **Stakeholders & interests:**
  - Business Owner — transactions arrive without typing them in; none missing, none twice.
  - Accountant — the books' balance matches the bank statement from the start date.
  - Bank and aggregator — access only with the account holder's consent; the service never sees bank credentials.
  - Account holder's privacy — only the accounts the Owner chose are shared, for the consented period only.
- **Trigger:** Business Owner wants the company's bank transactions in the books.
- **Preconditions:** Business Owner is signed in with permission to manage bank accounts; the company's books exist.
- **Minimal guarantees:** Bank credentials are never seen or stored by the service; no transaction is imported twice; a connection that is not completed leaves no half-configured bank link.
- **Success guarantees:** Each shared account is linked to a bank account in the books, with the consent's end date shown; transactions since the start date are imported and ready to reconcile; a daily feed of new transactions is scheduled; the Owner sees the imported count and the balance compared with the bank's.

**Main success scenario**
1. Business Owner chooses the bank to connect and the date from which transactions are imported.
2. System hands the Owner over to the bank, through the aggregator, to authenticate and give consent.
3. Business Owner authenticates at the bank and consents to share the selected accounts.
4. System receives the consent and lists the shared accounts.
5. Business Owner links each shared account to a bank account in the books.
6. System imports the transactions since the start date, showing progress (from about 15 seconds to two minutes, depending on the bank and the period).
7. System presents the number of imported transactions, compares the closing balance with the bank's, and schedules the daily feed.

**Extensions**
- 1a. Bank not supported: System says so and offers to import a statement file instead; use case ends.
- 3a. Business Owner refuses consent or abandons at the bank: System records no link; use case ends.
- 3b. Authentication at the bank is not completed within 10 minutes: System discards the pending connection; use case ends.
- 5a. A shared account is already linked: System proposes to renew that link rather than create a second one; continue at step 6, importing only after the last imported transaction.
- 6a. Business Owner cancels during the import: System stops, removes the transactions imported in this run and keeps the link; the Owner can start the import again later; use case ends.
- 6b. The bank or the aggregator stops answering during the import: System keeps the transactions imported so far, marks the import incomplete and retries in the background; the Owner is notified when it completes; use case ends.
- 6c. Some imported transactions match entries already in the books: System marks them as possible duplicates for reconciliation instead of adding them twice; continue at step 6.
- 7a. Closing balance differs from the bank's: System shows the difference and the transactions it may come from; the account is flagged for review; use case ends.

**Business rules:** BR-1 consent expires after the period the bank sets and must then be renewed · BR-2 import goes back at most 12 months, less if the bank provides less.
**Technology & data variations:** connection through an aggregator or through the bank's own API.
**Related:** Import Bank Statement File, Reconcile Transactions, Renew Bank Consent.
