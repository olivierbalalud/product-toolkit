---
id: UC-023
title: Connect a bank feed
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-023: Connect a bank feed

| Field | Value |
|---|---|
| **Primary actor** | Business Owner |
| **Supporting actors** | Bank data aggregator (hands the Business Owner over to the bank, relays the consent and the transactions); Bank (authenticates the Business Owner, records the consent, provides the transactions) |
| **Scope** | Small-business accounting service |
| **Level** | User goal |
| **Trigger** | The Business Owner wants the company's bank transactions to come into the books. |
| **Preconditions** | The company's books exist, and the Business Owner is signed in with permission to manage bank accounts. |
| **Minimal guarantees** | The service never sees or stores the bank credentials. Only the accounts the Business Owner chose are shared, and only for the consented period. No transaction is imported twice. No consent or link is left half-set-up: giving up before the import records nothing; cancelling during the import removes what that run imported and keeps the link; an import interrupted by the bank or the aggregator keeps what came in, marked incomplete. |
| **Success guarantees** | Each shared account is linked to a bank account in the books, and its transactions since the start date (or since the earliest date the bank provides) are imported, none added twice. The consent is recorded with its end date and the list of shared accounts, and the end date is shown on each linked account. Each closing balance has been compared with the bank's; any difference is shown and the account flagged for review. The Business Owner has seen the number of transactions imported and the balance comparison. The daily feed is scheduled. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Business Owner | Transactions arrive without typing them in, with none missing and none entered twice. |
| Accountant | The books' balance matches the bank statement from the start date on. |
| Bank and bank data aggregator | Access only with the account holder's consent; the service never sees the bank credentials. |
| Account holder | Only the accounts the Business Owner chose are shared, and only for the consented period; the system records when the consent ends and lists the shared accounts. |

## Main success scenario

1. (actor) The Business Owner chooses the bank and the start date of the import (BR-1).
2. (actor) The Business Owner authenticates at the bank and consents to share the selected accounts.
3. (system, wait) The system receives the consent, records it with its end date and the shared accounts, and presents the shared accounts.
4. (actor) The Business Owner links each shared account to a bank account in the books.
5. (system, long) The system imports each linked account's transactions since the start date, showing progress.
6. (system) The system compares each account's closing balance with the bank's, schedules the daily feed, and presents the summary: the number of transactions imported, the balance comparison and the consent end date on each linked account.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-023.1a, UC-023.1b | n/a | n/a | yes: `UC-023.1-4a` |
| 2 | out-of-scope: the bank handles wrong credentials, and the service never sees them | n/a | n/a | yes: `UC-023.1-4a` |
| 4 | n/a | yes: UC-023.4a | n/a | yes: `UC-023.1-4a` |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 3 | n/a | n/a | yes: UC-023.3a | n/a | n/a | n/a | n/a |
| 5 | n/a | yes: UC-023.5c | yes: UC-023.5a | yes: UC-023.5a | yes: UC-023.5b | n/a | yes: UC-023.5d |
| 6 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing the personal data in the imported transactions belongs with disconnecting a bank, a separate use case, and accounting records must be kept for the legal period.

## Extensions

- **UC-023.1a** The start date is more than 12 months back (BR-1):
  1. The system says the earliest date it can import from.
  2. Returns to step 1.

  *Example:* On 23 October 2026, Nadia Okafor asks to import from 1 June 2025; the system says it can import from 23 October 2025 at the earliest, and she picks 1 November 2025.
- **UC-023.1b** The bank is not one the service can connect to:
  1. The system says so and offers to import a statement file instead.
  2. The use case ends.

  *Example:* Tomás Reyes chooses Harbour Mutual, a small local bank the service doesn't connect to; the system offers to import its statement file instead.
- **`UC-023.1-4a`** The Business Owner gives up before the import, refuses consent at the bank, or doesn't finish signing in at the bank within 10 minutes (BR-2):
  1. The system throws away the pending connection, including any consent received; no link is recorded.
  2. The use case ends.

  *Example:* Nadia starts connecting North Bank at 09:00, is called away at the bank's sign-in and doesn't return; at 09:10 the pending connection is thrown away and her books show no link to North Bank.
- **UC-023.3a** The bank or the aggregator doesn't answer when the consent and the shared accounts come back:
  1. The system records no link and tells the Business Owner the bank can't be reached.
  2. The Business Owner starts the connection again: returns to step 1. Or stops: the use case ends.

  *Example:* Tomás consents at North Bank, but the aggregator doesn't answer when the system asks for his shared accounts; he is told North Bank can't be reached and tries again ten minutes later.
- **UC-023.4a** A shared account is already linked to a bank account in the books by an earlier feed:
  1. The system proposes renewing that link instead of making a second one.
  2. The Business Owner accepts; at step 5 the import brings in only the transactions after the last one already imported for that account.
  3. Returns to step 4.

  *Example:* Nadia reconnects North Bank; her current account is already linked to "North Bank current" with transactions up to 30 September 2026; the system renews that link and imports from 1 October only.
- **UC-023.4b** A shared account has no matching bank account in the books yet:
  1. The Business Owner creates a bank account in the books for it, named after the shared account.
  2. Returns to step 4.

  *Example:* Tomás shares his new North Bank savings account; the books have only a current account, so he creates "North Bank savings" and links the savings account to it.
- **UC-023.5a** The bank or the aggregator stops responding during the import:
  1. The system keeps the transactions imported so far, marks the import incomplete, schedules the daily feed, and tells the Business Owner the import is incomplete and will finish in the background.
  2. The system retries the import in the background; when it completes, the system compares the closing balances and notifies the Business Owner with the number of transactions imported and the balance comparison. While the retries fail, the account stays marked incomplete.
  3. The use case ends.

  *Example:* At 40% of Nadia's import, North Bank stops answering; 1,200 of 3,000 transactions are kept, the import is marked incomplete, and at 14:30 she is notified that it completed with 3,000 transactions and matching balances.
- **UC-023.5b** The bank provides less history than the start date asks for:
  1. The system imports what the bank gives.
  2. Continues at step 6; the summary shows the date the import actually starts from.

  *Example:* Tomás asks for transactions from 1 January 2026, but North Bank provides only 90 days; the import starts from 25 July 2026, and the summary says so.
- **UC-023.5c** An imported transaction matches one already in the books:
  1. The system marks it as a possible duplicate for reconciliation and does not add it a second time.
  2. Returns to step 5.

  *Example:* Nadia typed in a 450.00 rent payment of 2 October by hand; the imported 2 October rent payment of 450.00 is marked as a possible duplicate instead of being added again.
- **UC-023.5d** The Business Owner cancels the import while it runs:
  1. The system removes what this run imported and keeps the link.
  2. The use case ends.

  *Example:* Tomás cancels his import at 30%, after 600 transactions; the 600 are removed, and his North Bank account stays linked.
- **UC-023.6a** A closing balance differs from the bank's:
  1. The system shows the difference and the transactions it may come from, flags the account for review, and still schedules the daily feed.
  2. The use case ends.

  *Example:* Nadia's imported closing balance is 12,480.00 but North Bank reports 12,530.00; the system shows the 50.00 difference, points to a 50.00 transfer marked as a possible duplicate, and flags the account for review.

## Technology and data variations

- 2 to 5: the bank is reached through the bank data aggregator, or through the bank's own API; the steps are the same.

## Related information

- **Frequency:** A few times per company: once for each bank when the company starts using the service, and again when it opens an account at a new bank (the product owner's estimate).
- **Business rules:**
  - BR-1 the import starts at most 12 months back (step 1, UC-023.1a).
  - BR-2 a pending connection is thrown away if the Business Owner doesn't finish signing in at the bank within 10 minutes (step 2, `UC-023.1-4a`).
- **Related use cases:** Import the daily bank transactions (time-triggered, scheduled at step 6); Import a bank statement file (UC-023.1b); Renew a bank consent when it ends; Disconnect a bank (withdraws the consent, and handles exporting or erasing the imported personal data).
- **Open issues:** None
