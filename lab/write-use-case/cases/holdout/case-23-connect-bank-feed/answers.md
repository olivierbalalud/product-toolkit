# Answers: connect a bank account to import transactions

## Actor, goal and scope

- The system is our small-business accounting service.
- The Business Owner starts because they want the company's bank transactions in the books without typing them in.
- Before they start, they're signed in with permission to manage bank accounts, and the company's books already exist.
- Two outside parties take part: a bank data aggregator, which hands the Owner over to the bank and relays the consent and the transactions, and the bank itself, which authenticates the Owner, records the consent and provides the transactions.
- Some banks are connected through the aggregator, others through the bank's own API; what happens is the same either way.
- It happens a few times per company: once for each bank when the company starts using the service, and again when it opens an account at a new bank. That's our estimate.
- Importing a statement file, reconciling transactions and renewing a bank's consent are separate things, not part of this.
- The daily feed of new transactions, once scheduled, runs on its own; that's a separate thing too.
- When an interrupted import is retried later, that retry is a separate thing as well.

## Stakeholders and guarantees

- The Owner wants transactions to arrive without typing them in, with none missing and none in twice.
- The accountant wants the books' balance to match the bank statement from the start date on.
- The bank and the aggregator want access only with the account holder's consent, and the service must never see the bank credentials.
- The account holder wants only the accounts the Owner chose to be shared, and only for the period they consented to.
- Whatever happens, the service never sees or stores the bank credentials, no transaction gets imported twice, and a connection that isn't completed leaves no half-set-up bank link behind.
- When it works: each shared account is linked to a bank account in the books and shows when the consent ends, the transactions since the start date are in and ready to reconcile, the daily feed is scheduled, and the Owner sees how many transactions came in and how the closing balance compares with the bank's.

## Main scenario

- Along with the bank, the Owner chooses the date from which transactions are imported. We go back at most 12 months, less if the bank provides less.
- The system hands the Owner over to the bank, through the aggregator, to sign in and give consent there.
- When the consent comes back, the system notes when it ends and lists the accounts the Owner shared.
- Consent expires after the period the bank sets and then has to be renewed.
- The import shows its progress while it runs.
- At the end, the system shows how many transactions came in and compares the closing balance with the bank's, shows the consent end date on each linked account, and schedules the daily feed.

## What can go wrong

- The bank isn't one we support.
- The Owner picks a start date more than 12 months back.
- The Owner gives up before the import starts: they leave, refuse consent at the bank, or don't finish signing in at the bank within 10 minutes.
- The aggregator or the bank doesn't answer during the hand-over or when the consent should come back.
- One of the shared accounts is already linked to an account in the books.
- The Owner cancels while the import is running.
- The bank or the aggregator stops answering in the middle of the import.
- Some imported transactions match entries already in the books, for example ones typed in by hand.
- The bank provides less history than the start date asks for.
- The closing balance doesn't match the bank's.

## How each is handled

- Unsupported bank: the system says so and offers to import a statement file instead; that's the end of it.
- Start date too far back: the system says the earliest date it can import from, and the Owner picks again.
- Giving up before the import: the pending connection is thrown away and no link is recorded.
- Aggregator or bank not answering before the import: no link is recorded, and the Owner is told the bank can't be reached and they can start the connection again.
- Account already linked: we propose renewing that link instead of making a second one; the import then brings in only what came after the last transaction already imported for that account.
- Cancelling during the import: the system stops, removes what this run imported, keeps the link, and tells the Owner they can start the import again.
- Bank or aggregator going silent mid-import: we keep what came in so far, mark the import incomplete and retry in the background. The Owner is told it's incomplete and gets a notification when it completes.
- Matching entries already in the books: they're marked as possible duplicates for reconciliation, never added a second time, and the import carries on.
- Less history than asked: we import what the bank gives and, at the end, say the date the import actually starts from.
- Balance mismatch: the system shows the difference and the transactions it may come from, and flags the account for review. The daily feed is still scheduled.

## Durations

- Handing the Owner over to the bank takes a few seconds.
- Receiving the consent and listing the shared accounts takes a few seconds too.
- The import takes from about 15 seconds to two minutes, depending on the bank and the period. The Owner stays and watches it, and can cancel.
- The summary at the end shows up straight away.

## Out of scope

- Wrong credentials or a wrong account selection at the bank: the bank handles that; we never see the credentials.
- Whether the person signing in at the bank may share a given account: the bank decides that, not us.
- Exporting or erasing the personal data in the imported transactions: that belongs with disconnecting a bank, which is a separate job, and we have to keep accounting records for the legal period anyway.
