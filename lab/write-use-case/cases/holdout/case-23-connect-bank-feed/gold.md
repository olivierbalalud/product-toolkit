---
id: UC-023
title: Connect a bank account to import transactions
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-023: Connect a bank account to import transactions

| Field | Value |
|---|---|
| **Primary actor** | Business Owner |
| **Supporting actors** | Bank data aggregator (hands the Business Owner over to the bank, relays the consent and the transactions); Bank (authenticates the Business Owner, records the consent, provides the transactions) |
| **Scope** | Small-business accounting service |
| **Level** | User goal |
| **Trigger** | The Business Owner wants the company's bank transactions in the books. |
| **Preconditions** | The Business Owner is signed in with permission to manage bank accounts; the company's books exist. |
| **Minimal guarantees** | The service never sees or stores the bank credentials; no transaction is imported twice; a connection that is not completed leaves no half-configured bank link. |
| **Success guarantees** | Each shared account is linked to a bank account in the books, with the consent's end date shown; the transactions since the start date are imported and ready to reconcile; a daily feed of new transactions is scheduled; the Business Owner sees the number of imported transactions and the closing balance compared with the bank's. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Business Owner | Transactions arrive without typing them in; none is missing, none is imported twice. |
| Accountant | The books' balance matches the bank statement from the start date. |
| Bank and bank data aggregator | Access only with the account holder's consent; the service never sees the bank credentials. |
| Account holder | Only the accounts the Business Owner chose are shared, and only for the consented period. |

## Main success scenario

1. (actor) The Business Owner chooses the bank to connect and the date from which transactions are imported (BR-2).
2. (system, wait) The system hands the Business Owner over to the bank, through the bank data aggregator, to authenticate and give consent.
3. (actor) The Business Owner authenticates at the bank and consents to share the selected accounts.
4. (system, wait) The system receives the consent, records its end date (BR-1) and lists the shared accounts.
5. (actor) The Business Owner links each shared account to a bank account in the books.
6. (system, long) The system imports the transactions since the start date, showing progress.
7. (system) The system presents the number of imported transactions and the closing balance compared with the bank's, shows the consent's end date on each linked account, and schedules the daily feed of new transactions.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-023.1a, UC-023.1b | n/a | n/a | yes: UC-023.1-5a |
| 3 | out-of-scope: the bank checks the credentials and the accounts chosen; the service never sees them | n/a | out-of-scope: the bank decides who may consent to share an account | yes: UC-023.1-5a |
| 5 | n/a | yes: UC-023.5a | n/a | yes: UC-023.1-5a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | yes: UC-023.2-4a | n/a | n/a | n/a | n/a |
| 4 | n/a | n/a | yes: UC-023.2-4a | n/a | n/a | n/a | n/a |
| 6 | n/a | yes: UC-023.6c | yes: UC-023.6b | yes: UC-023.6b | yes: UC-023.6d | n/a | yes: UC-023.6a |
| 7 | n/a | yes: UC-023.7a | n/a | n/a | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, the imported transactions and the consent hold personal data of the account holder and of the counterparties; disconnecting a bank and exporting or erasing its data is its own use case, and the legal retention of accounting records limits erasure.

## Extensions

- **UC-023.1-5a** The Business Owner abandons before the import starts: leaves, refuses consent at the bank, or does not complete authentication at the bank within 10 minutes:
  1. The system discards the pending connection and records no link.
  2. The use case ends.

  *Example:* Nadia chooses her bank and 1 March as the start date, reaches the bank's sign-in and declines to share her accounts; no bank link is recorded in the books.
- **UC-023.1a** The bank is not supported:
  1. The system says the bank cannot be connected and offers to import a statement file instead (Import Bank Statement File).
  2. The use case ends.

  *Example:* Nadia chooses Harbourside Credit Union, which the service cannot connect to, and is offered to import its statement file instead.
- **UC-023.1b** The start date is more than 12 months back (BR-2):
  1. The system says the earliest date from which it can import.
  2. Returns to step 1.

  *Example:* In October 2026 Nadia asks for transactions since 1 January 2025; the system says it can import from October 2025 and she chooses 1 November 2025.
- **UC-023.2-4a** The bank data aggregator or the bank does not answer before the import starts:
  1. The system records no link and tells the Business Owner that the bank cannot be reached and that the connection can be started again.
  2. The use case ends.

  *Example:* Omar chooses his bank, but the aggregator does not answer the hand-over; no link is recorded and he is told he can start the connection again.
- **UC-023.5a** A shared account is already linked to a bank account in the books:
  1. The system proposes to renew that link instead of creating a second one, and the Business Owner accepts.
  2. Returns to step 6; for that account, the system imports only the transactions after the last one already imported.

  *Example:* Omar shares his current account, linked since March; the system renews that link and imports only the transactions after 14 September, the last one already in the books.
- **UC-023.6a** The Business Owner cancels during the import:
  1. The system stops the import, removes the transactions imported in this run and keeps the link.
  2. The system tells the Business Owner that the import can be started again.
  3. The use case ends.

  *Example:* Nadia starts importing ten months of transactions, realises she picked the wrong start date and cancels at 40 %; the 520 transactions imported are removed and the link to her current account stays.
- **UC-023.6b** The bank or the bank data aggregator stops answering during the import:
  1. The system keeps the transactions imported so far, marks the import incomplete and retries in the background.
  2. The system tells the Business Owner that the import is incomplete and that they will be notified when it completes.
  3. The use case ends.

  *Example:* The bank stops answering after 300 of Omar's transactions; the 300 stay in the books, the import is marked incomplete, and he is notified when the remaining ones are in.
- **UC-023.6c** Some imported transactions match entries already in the books:
  1. The system marks them as possible duplicates for reconciliation instead of adding them a second time.
  2. The import continues at step 6.

  *Example:* Nadia had typed in the 1,200.00 rent payment of 2 June by hand; the imported payment of the same amount and date is marked as a possible duplicate instead of being added again.
- **UC-023.6d** The bank provides transactions only from a later date than the start date (BR-2):
  1. The system imports what the bank provides.
  2. Returns to step 7, where the system also states the date from which transactions were imported.

  *Example:* Omar asks for transactions since 1 January, but his bank provides only the last 90 days; the system imports them and states that the import starts on 25 July.
- **UC-023.7a** The closing balance differs from the bank's:
  1. The system shows the difference and the transactions it may come from, flags the account for review, and schedules the daily feed.
  2. The use case ends.

  *Example:* After the import, Nadia's books show 8,412.50 and the bank 8,462.50; the system shows the 50.00 difference, points to two card payments of 25.00 on 30 September, and flags the account for review.

## Technology and data variations

- 2: the connection goes through a bank data aggregator or through the bank's own API.

## Related information

- **Frequency:** a few times per company: once for each bank when the company starts using the service, and again when it opens an account at a new bank.
- **Business rules:** BR-1 consent expires after the period the bank sets and must then be renewed (step 4, step 7). BR-2 the import goes back at most 12 months, less if the bank provides less (step 1, UC-023.1b, UC-023.6d).
- **Duration:** the import takes from about 15 seconds to two minutes, depending on the bank and the period (step 6).
- **Related use cases:** Import Bank Statement File, Reconcile Transactions, Renew Bank Consent, Resume Interrupted Bank Import, Import Daily Bank Feed.
- **Open issues:** None
