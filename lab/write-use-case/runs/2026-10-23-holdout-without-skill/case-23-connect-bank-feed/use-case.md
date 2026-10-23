---
id: UC-023
title: Connect a bank feed
status: Draft
driver: lab
priority: TBD
source_locale: en
inputs: []
stories: []
---

# UC-023: Connect a bank feed

| Field | Value |
|---|---|
| **Primary actor** | Business Owner |
| **Supporting actors** | Bank data aggregator (hands the Business Owner over to the bank, relays the consent and the transactions); the bank (authenticates the Business Owner, records the consent, provides the transactions and the balance) |
| **Scope** | The small-business accounting service |
| **Level** | User goal |
| **Trigger** | The Business Owner asks to connect a bank to the company's books. |
| **Preconditions** | The Business Owner is signed in with permission to manage bank accounts, and the company's books exist. |
| **Minimal guarantees** | The service never sees the bank credentials. No bank link is recorded unless the bank's consent came back and at least one shared account was linked. No transaction is added to the books twice. A cancelled import leaves none of its transactions in the books. Every connection attempt, consent outcome, link and import run is logged with who did it, when and how it ended (recommendation). |
| **Success guarantees** | Each shared account the Business Owner chose is linked to exactly one bank account in the books, with its consent end date recorded and shown. The transactions since the start date are imported, and those that match existing entries are marked as possible duplicates. Each account's closing balance has been compared with the bank's, and any account that does not match is flagged for review. The daily feed of new transactions is scheduled for each linked account. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Business Owner | Gets the company's bank transactions into the books quickly, without retyping them or importing files, and knows when the bank consent ends. |
| Accountant | The books' balance matches the bank statement from the start date on; nothing is imported twice and closed periods are not changed. |
| Bank and aggregator | Access only with the account holder's consent; the service never sees the bank credentials. |
| Account holder | Only the accounts the Business Owner chose to share are read, and only for the period consented to. |
| Counterparties named in transactions | Their names in transaction details are personal data, used only for bookkeeping and kept only for the legal retention period (recommendation). |

## Main success scenario

1. (actor) The Business Owner chooses the bank and the date from which to import.
2. (system, wait) The system checks the start date against BR-1 and hands the Business Owner over to the bank through the aggregator.
3. (actor) The Business Owner authenticates at the bank and consents to share the selected accounts.
4. (system, wait) The system receives the consent through the aggregator, records its end date (BR-7), and lists the shared accounts, each with a suggested bank account in the books.
5. (actor) The Business Owner links each shared account to a bank account in the books (BR-2).
6. (system, long) The system imports the transactions since the start date for each linked account, showing progress, and marks those that match existing entries as possible duplicates (BR-3).
7. (system) The system compares each account's closing balance in the books with the bank's closing balance (BR-4).
8. (system) The system schedules the daily feed of new transactions for each linked account and reports, per account, the transactions imported, the possible duplicates, the balance check and the consent end date.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-023.1a, UC-023.1b | n/a | n/a | yes: `UC-023.1-5a` |
| 3 | out-of-scope: wrong credentials are handled by the bank; the service never sees them | n/a | yes: UC-023.3a | yes: UC-023.3a |
| 5 | yes: UC-023.5a | yes: UC-023.5b, UC-023.5c | n/a | yes: `UC-023.1-5a` |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | yes: `UC-023.2-4a` | n/a | yes: `UC-023.2-4a` | n/a | n/a |
| 4 | n/a | n/a | yes: `UC-023.2-4a` | n/a | yes: `UC-023.2-4a` | n/a | n/a |
| 6 | n/a | yes: UC-023.6d | yes: UC-023.6a | yes: UC-023.6a | yes: UC-023.6a | yes: UC-023.6b | yes: UC-023.6e, UC-023.6f |
| 7 | yes: UC-023.7b | n/a | n/a | yes: UC-023.7a | n/a | n/a | n/a |
| 8 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

**Privacy request:** no: exporting or erasing the personal data in imported transactions belongs to the separate "disconnect a bank" use case, and accounting records must be kept for the legal period regardless.

## Extensions

- **UC-023.1a** The start date is earlier than BR-1 allows:
  1. The system states the earliest date it can import from.
  2. Returns to step 1.

  *Example:* On 23 October 2026, Lea picks 1 June 2025; the system says the earliest date is 23 October 2025.
- **UC-023.1b** The Business Owner's bank is not in the list the aggregator supports:
  1. The system says the bank cannot be connected and offers to import a statement file instead.
  2. The use case ends.

  *Example:* Lea looks for a small regional cooperative bank that the aggregator does not cover and is offered the statement file import.
- **`UC-023.1-5a`** The Business Owner leaves, or the session expires, before the import starts:
  1. The system throws away the pending connection; no bank link is recorded.
  2. The use case ends.

  *Example:* Lea has shared two accounts but closes the browser before linking them; next time she starts from the beginning.
- **`UC-023.2-4a`** The aggregator or the bank cannot be reached, or refuses calls because of a rate limit, before the import starts:
  1. The system records no bank link and tells the Business Owner the bank cannot be reached right now.
  2. The use case ends; the Business Owner can start the connection again.

  *Example:* The aggregator does not answer when Lea's consent should come back; she is told to try again later.
- **UC-023.3a** The Business Owner refuses consent, cancels at the bank, shares no accounts, or does not finish within 10 minutes (BR-5):
  1. The system throws away the pending connection; no bank link is recorded.
  2. The use case ends; the Business Owner can start the connection again.

  *Example:* Lea opens the bank's consent page, gets a phone call and comes back 15 minutes later; the pending connection is gone.
- **UC-023.5a** The chosen book account cannot take the link: its currency differs from the bank account's, it is already chosen for another shared account, or it is already linked to another bank account (BR-2):
  1. The system says why and keeps the shared account unlinked.
  2. Returns to step 5.

  *Example:* Lea links her USD account to the "Main EUR" book account; the system says the currencies differ.
- **UC-023.5b** A shared account is already linked in this company:
  1. The system proposes renewing the existing link instead of making a second one.
  2. On acceptance, the system renews the link with the new consent; the import in step 6 brings in only the transactions after the last one already imported for that account.
  3. Returns to step 5 for the remaining accounts.

  *Example:* Lea reconnects her bank after the consent ended; her current account's link is renewed and only the transactions since 2 September are imported.
- **UC-023.5c** A shared account is already linked in another company's books (recommendation):
  1. The system warns that the account already feeds another company's books and asks the Business Owner to confirm.
  2. On confirmation, the link is made; otherwise the shared account stays unlinked.
  3. Returns to step 5.

  *Example:* Lea's personal-company account already feeds her other company's books; she confirms she wants it in both.
- **UC-023.5d** The Business Owner creates a new bank account in the books while linking (recommendation; an alternative, not a failure):
  1. The system creates the book account with the bank account's name and currency, which the Business Owner can change.
  2. Returns to step 5.

  *Example:* Lea has no book account for her new savings account yet and creates one while linking.
- **UC-023.5e** The Business Owner skips a shared account (recommendation; an alternative, not a failure):
  1. The system leaves it unlinked and imports nothing from it.
  2. Returns to step 5; if no account at all is linked, the use case continues as `UC-023.1-5a`.

  *Example:* Lea shares her current and savings accounts but links only the current account.
- **UC-023.6a** The aggregator or the bank stops answering, or rate-limits calls, during the import of an account:
  1. The system keeps the transactions imported so far for that account, marks its import incomplete, and tells the Business Owner.
  2. The other linked accounts complete normally (recommendation).
  3. The system retries in the background for up to 24 hours (BR-6, recommendation), then notifies the Business Owner of the outcome.
  4. When the retry completes, the system runs steps 7 and 8 for that account. If it gives up, the account stays incomplete, the daily feed is not scheduled for it, and the Business Owner can restart the import (recommendation).

  *Example:* The bank stops responding after 400 of Lea's 1,200 transactions; she is told the import is incomplete and gets a notification an hour later that it finished.
- **UC-023.6b** The bank provides less history than the chosen start date (recommendation):
  1. The system imports from the earliest date the bank provides and tells the Business Owner the actual start date.
  2. Continues at step 7.

  *Example:* Lea asks for 12 months, but her bank only gives 90 days; the report says transactions start on 25 July 2026.
- **UC-023.6c** Imported transactions match entries already in the books, including ones from an earlier statement file import (an alternative, not a failure):
  1. The system marks them as possible duplicates for reconciliation and does not add them a second time (BR-3).
  2. The import carries on.

  *Example:* Lea imported a March statement file last month; those March transactions are marked as possible duplicates.
- **UC-023.6d** Another user connects the same bank account at the same time (recommendation):
  1. The first link recorded wins; the second connection is offered renewal as in UC-023.5b.
  2. If an import is already running for that account, the system says so and does not start a second one; the link is renewed and the account will be updated by the running import and the daily feed.

  *Example:* Lea and her co-founder Sam both connect the company's current account within the same minute; Sam is told Lea's import is already running.
- **UC-023.6e** The Business Owner cancels the import:
  1. The system stops the import and removes the transactions this run had already imported.
  2. The bank link and the consent are kept (recommendation); the daily feed is not scheduled.
  3. The system tells the Business Owner they can start the import again. The use case ends.

  *Example:* Lea realises she picked the wrong start date and cancels at 30%; no transactions remain, and she restarts the import.
- **UC-023.6f** The Business Owner leaves without cancelling, or the session expires, during the import (recommendation):
  1. The import continues in the background.
  2. The system runs steps 7 and 8 and notifies the Business Owner of the outcome.

  *Example:* Lea closes her laptop at 60%; she later receives a notification that the import is complete and the balance matches.
- **UC-023.7a** The closing balances do not match:
  1. The system shows the difference and the transactions it may come from, and flags the account for review.
  2. Continues at step 8; the daily feed is still scheduled.

  *Example:* The books show 12,480.00 EUR and the bank 12,530.00 EUR; the system shows a 50.00 EUR difference and a refund that matched an existing entry.
- **UC-023.7b** The bank provides no closing balance (recommendation):
  1. The system tells the Business Owner the balance could not be checked and flags the account for review.
  2. Continues at step 8.

  *Example:* Lea's savings account returns transactions but no balance; the report says "balance not verified".

## Technology and data variations

- Step 4: consent end date returned by the bank, or a default when the bank returns none (BR-7).
- Step 5: link to an existing book account, create a new book account (UC-023.5d), or renew an existing link (UC-023.5b).
- Step 6: one linked account or several imported in the same run.
- Step 8: summary shown at once, or sent as a notification after a background import (UC-023.6a, UC-023.6f).
- UC-023.1b: statement file import instead of a bank feed (a separate use case).

## Related information

- **Frequency:** A few times per company: once per bank when the company starts using the service, and again each time it opens an account at a new bank (product owner's estimate).
- **Business rules:**
  - **BR-1** The start date can be at most 12 months back. The earliest start date is also no earlier than the books' opening date and the day after the last closed accounting period (recommendation, so that closed books are never changed).
  - **BR-2** A shared bank account is linked at most once per company; a book bank account has at most one bank link; the currencies must match (recommendation, except renewal of an existing link, which is the product owner's rule).
  - **BR-3** A transaction that matches an entry already in the books is marked as a possible duplicate and never added a second time.
  - **BR-4** The balances must match exactly, to the smallest currency unit (recommendation).
  - **BR-5** A pending connection is thrown away if the Business Owner has not finished signing in and consenting within 10 minutes.
  - **BR-6** After an interrupted import, background retries go on for up to 24 hours (recommendation).
  - **BR-7** The consent lasts as long as the bank sets; the system records its end date and shows it on each linked account. If the bank returns no end date, the system assumes 90 days (recommendation).
- **Open issues:**
  - Confirm the recommendations marked above: start date vs. opening date and closed periods (BR-1), currency and one-link rules (BR-2), zero tolerance (BR-4), 24-hour retry (BR-6), default consent length (BR-7), creating and skipping accounts during linking (UC-023.5d, UC-023.5e), accounts linked in another company (UC-023.5c), concurrent connections (UC-023.6d), keeping the consent on cancel (UC-023.6e), leaving during the import (UC-023.6f), and a missing bank balance (UC-023.7b).
  - Limits per plan on bank connections or accounts, aggregator quotas, and a maximum number of transactions per import are not decided; none is assumed here beyond the 12-month period.
  - What exactly is logged for audit during the connection is not decided; the minimal guarantees state a recommendation.
  - The daily feed, renewing the consent, and disconnecting a bank (including export and erasure of personal data) are separate use cases.
