---
id: UC-011
title: Pay contractors off-cycle
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-011: Pay contractors off-cycle

| Field | Value |
|---|---|
| **Primary actor** | Payroll Administrator (or Finance Lead) |
| **Supporting actors** | Payment clearinghouse (receives the batch and the debit of the employer's bank account); accounting software (receives the journal entries) |
| **Scope** | Payroll service (payroll and disbursements) |
| **Level** | User goal |
| **Trigger** | An unscheduled or milestone-based contractor invoice must be paid outside the standard monthly pay schedule. |
| **Preconditions** | The employer's business bank account is connected to the payroll service and verified; the Payroll Administrator is signed in with permission to pay contractors. |
| **Minimal guarantees** | No money moves and nothing is debited unless the batch is submitted at step 5; a batch the clearinghouse does not accept leaves no debit, voucher or journal entry behind; every authorization is recorded with the Payroll Administrator and the time. |
| **Success guarantees** | The run is locked and the off-cycle batch is queued with the payment clearinghouse for the settlement date; the employer's bank account carries an ACH debit for the exact total; each paid contractor has a payment voucher; the journal entries are generated and synced with the accounting software, so each payment is on record for year-end contractor tax filing. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Payroll Administrator | Pays the contractors quickly, outside the schedule, and sees the fees and debit dates before authorizing. |
| Contractors | Receive accurate, timely direct deposits without surprise deductions. |
| Corporate treasury | Sees the debit on the bank account and its date right away, to prevent overdrafts. |
| Tax and regulatory authorities | Accurate accounting records for the year-end 1099-NEC filings. |

## Main success scenario

1. (actor) The Payroll Administrator chooses the contractors to pay, from those eligible (BR-1), and the settlement date.
2. (actor) The Payroll Administrator gives, for each contractor, the payment amount, the hours or deliverables it covers, and the project cost center.
3. (system) The system validates the total against the instant payroll limit (BR-2) and the settlement date against the banking calendar and the daily ACH cutoff (BR-3), and presents the reconciliation summary: gross disbursements, processing fees and ACH debit dates.
4. (actor) The Payroll Administrator confirms and authorizes the payment run.
5. (system, wait) The system locks the run, records the authorization, submits the batch to the payment clearinghouse with the ACH debit of the exact total from the employer's bank account, creates a payment voucher for each contractor, sends the journal entries to the accounting software, and confirms the submission to the Payroll Administrator.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-011.1a | n/a | n/a | yes: UC-011.1-4a |
| 2 | yes: UC-011.2a | out-of-scope: a second payment for the same invoice is not detected; the run carries no invoice reference, and the Payroll Administrator checks the payment history | n/a | yes: UC-011.1-4a |
| 4 | n/a | n/a | n/a | yes: UC-011.1-4a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 3 | n/a | n/a | n/a | n/a | yes: UC-011.3a | n/a | n/a |
| 5 | n/a | n/a | yes: UC-011.5a, UC-011.5b | yes: UC-011.5b | out-of-scope: the instant payroll limit is checked once, at step 3, and not again at submission | yes: UC-011.5c, UC-011.5d | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing a contractor's payment and bank data is its own use case, and the duty to keep tax records limits erasure.

## Extensions

- **UC-011.1-4a** The Payroll Administrator abandons the run before authorizing it:
  1. The system discards the run; nothing is debited or paid.
  2. The use case ends.

  *Example:* Rosa has entered amounts for five of her nine contractors when she learns the milestone was not signed off; she abandons the run and no money moves.
- **UC-011.1a** The settlement date is a federal banking holiday or past the daily ACH cutoff (BR-3):
  1. When it validates the date (step 3), the system calculates the earliest available settlement date and asks the Payroll Administrator to accept it.
  2. The Payroll Administrator accepts: the summary shows that date and the use case continues at step 4. Or the Payroll Administrator gives another date: returns to step 3.

  *Example:* Rosa picks Thursday 25 December as the settlement date; the system proposes Friday 26 December, the earliest banking day, and she accepts it.
- **UC-011.2a** An amount is missing or not above zero, or a contractor has no project cost center:
  1. The system names each contractor concerned and what is missing.
  2. Returns to step 2.

  *Example:* Rosa enters 0 for Malik Haddad's milestone payment; the system flags it and she enters $4,800.
- **UC-011.3a** The total exceeds the instant payroll limit (BR-2):
  1. The system halts direct ACH processing for the run and says that it needs wire funding or a 4-day ACH processing hold.
  2. The Payroll Administrator accepts the 4-day hold: the system presents the summary with the later debit and deposit dates, and the use case continues at step 4. Or the Payroll Administrator chooses wire funding: the system presents the summary with wire funding, and the use case continues at step 4, then as in UC-011.5e. Or the Payroll Administrator reduces the batch: returns to step 1.

  *Example:* Rosa pays 14 contractors $186,000 for a launch milestone against a $150,000 instant payroll limit; she accepts the 4-day hold, and the deposit date moves from Tuesday to the following Monday.
- **UC-011.5a** The payment clearinghouse does not answer, or does not accept the batch:
  1. The system debits nothing, creates no voucher or journal entry, and unlocks the run with the Payroll Administrator's entries kept.
  2. The system tells the Payroll Administrator that the payment was not submitted.
  3. The Payroll Administrator tries again: returns to step 4. Or the Payroll Administrator stops: the run is discarded and the use case ends.

  *Example:* Rosa authorizes a $38,000 run while the clearinghouse is not answering; nothing is debited or paid, and her second attempt goes through.
- **UC-011.5b** The accounting software does not answer once the batch is submitted:
  1. The system completes the payment run and keeps the journal entries.
  2. The system tells the Payroll Administrator that the contractors are paid and that the journal entries will be sent to the accounting software as soon as it answers; the run history shows when they are synced.
  3. The use case ends.

  *Example:* Rosa's run is submitted while the accounting software is down for maintenance; she is told the 12 journal entries are pending, and the run history later shows them synced.
- **UC-011.5c** The daily ACH cutoff passed after the summary was presented (BR-3):
  1. The system submits nothing, calculates the earliest available settlement date and asks the Payroll Administrator to accept it.
  2. The Payroll Administrator accepts: returns to step 4. Or the Payroll Administrator stops: the run is discarded and the use case ends.

  *Example:* Rosa sees a Tuesday deposit at 15:50 and authorizes at 16:05, after the 16:00 cutoff; nothing is submitted, she accepts Wednesday and authorizes again.
- **UC-011.5d** A contractor's bank details have been flagged as invalid by their bank:
  1. The system leaves that contractor out of the direct deposit batch and tells the Payroll Administrator.
  2. The Payroll Administrator chooses a manual paper check for that contractor, which the system records with its voucher, or skips that contractor.
  3. The system continues step 5 for the other contractors.

  *Example:* Ines Ferreira's bank has flagged her account as closed; Rosa chooses a paper check for Ines's $2,300, and the other six contractors are paid by direct deposit.
- **UC-011.5e** The run is funded by wire (UC-011.3a):
  1. The system locks the run, records the authorization and presents the wire instructions for the exact total.
  2. The system tells the Payroll Administrator that the batch will be submitted once the wire is received, and that they will be notified when it is.
  3. The use case ends; the batch is pending receipt of the wire.

  *Example:* Rosa chooses to fund her $186,000 run by wire; the system shows the wire instructions and tells her she will be notified when the batch is submitted.

## Technology and data variations

- 2: a payment covers hours worked or a delivered milestone.

## Related information

- **Frequency:** a few times a month per company, when a milestone or unscheduled invoice comes in.
- **Business rules:** BR-1 only contractors with an active profile, a completed W-9 verification and verified direct deposit details can be paid (step 1) · BR-2 a total above the company's uncollateralized instant payroll limit cannot go by direct ACH with standard timing; it needs wire funding or a 4-day ACH processing hold (step 3, UC-011.3a) · BR-3 a settlement date must be a banking day, reachable before the daily ACH cutoff (step 3, UC-011.1a, UC-011.5c).
- **Related use cases:** Submit a wire-funded payment run.
- **Open issues:** None
