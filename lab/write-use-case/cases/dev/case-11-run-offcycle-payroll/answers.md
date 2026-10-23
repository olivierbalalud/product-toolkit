# Answers: pay contractors off-cycle

## Actor, goal and scope

- The person doing this is the Payroll Administrator; in smaller companies it's the Finance Lead.
- The system is our payroll service, the part that handles payroll and disbursements.
- They start because a contractor invoice, unscheduled or tied to a milestone, has to be paid now rather than in the standard monthly pay run.
- Before they start, the company's business bank account is already connected to the service and verified, and they're signed in with permission to pay contractors.
- We don't assume the account has enough money in it; the debit happens later, at clearing.
- Two outside parties take part: the payment clearinghouse, which receives the batch and the debit of the company's account, and the company's accounting software, which receives the journal entries.
- A payment can cover hours worked or a delivered milestone.
- It happens a few times a month per company, whenever a milestone or unscheduled invoice comes in.
- Paying by wire means the batch only goes out once the wire arrives; sending the batch at that point is a separate job, not part of this.

## Stakeholders and guarantees

- The Payroll Administrator wants to pay the contractors quickly, outside the schedule, and to see the fees and debit dates before authorizing anything.
- Contractors want accurate, timely direct deposits with no surprise deductions.
- Corporate treasury wants to see the debit on the bank account and its date straight away, so the account never goes overdrawn.
- Tax and regulatory authorities need accurate accounting records for the year-end 1099-NEC filings.
- Whatever happens, no money moves and nothing is debited unless the batch is actually submitted.
- If the clearinghouse doesn't take the batch, there's no debit, no voucher and no journal entry left over.
- Every authorization is recorded with who gave it and when.
- When it works: the run is locked, the batch is queued with the clearinghouse for the settlement date, the company's account carries a debit for the exact total, each paid contractor has a payment voucher, and the journal entries are in the accounting software, which gives us the record for year-end contractor tax filing.

## Main scenario

- Along with the contractors, they choose the settlement date.
- Only contractors with an active profile, a completed W-9 verification and verified direct deposit details can be picked.
- For each contractor they give the amount, the hours or deliverables it covers, and the project cost center.
- The limit we check against is the company's uncollateralized instant payroll limit.
- The settlement date has to be a banking day that can still be reached before the daily ACH cutoff.
- On authorization the system locks the run, so it can't be changed or sent twice.
- After submitting, the system confirms the submission to them.

## What can go wrong

- The settlement date falls on a federal banking holiday or is already past the daily ACH cutoff.
- An amount is missing or zero, or a contractor has no cost center.
- The total is over the instant payroll limit.
- They give up before authorizing.
- The clearinghouse doesn't answer, or doesn't accept the batch.
- The accounting software doesn't answer after the batch has gone out.
- The daily cutoff passes between seeing the summary and authorizing.
- A contractor's bank has flagged their bank details as invalid; we find out when we submit.
- They choose to fund the run by wire.

## How each is handled

- Holiday or past cutoff: the system works out the earliest date that works and asks them to accept it before going on; they can pick another date instead.
- Missing or zero amount, or no cost center: the system names each contractor concerned and what's missing, and they fix it.
- Over the limit: we stop direct ACH processing for the run and tell them it needs a wire or a 4-day ACH processing hold. They accept the 4-day hold and see the later dates in the summary, choose the wire, or cut the batch down and pick again.
- Giving up before authorizing: the run is thrown away and nothing is paid. We don't keep drafts.
- Clearinghouse doesn't answer or refuses the batch: nothing is debited, no voucher or journal entry is created, the run is unlocked with their entries kept, and they're told it wasn't submitted. They can authorize again or drop the run.
- Accounting software down: the payment still goes out. The journal entries are kept and sent as soon as the software answers, and they're told so; the run history shows when the entries are synced.
- Cutoff passes before authorizing: nothing is submitted; the system offers the earliest date that works, and they accept it and authorize again, or drop the run.
- Flagged bank details: that contractor is taken out of the direct deposit batch and they're told. They either issue that contractor a manual paper check, which we record with its voucher, or skip that contractor; the rest are paid as normal.
- Wire funding: on authorization we lock the run, record the authorization and show the wire instructions for the exact total. The batch goes out only once the wire is received, and they're notified when it does. For them, it's over at that point.

## Durations

- Checking the limit and the date and showing the summary is immediate.
- Submitting the batch, creating the vouchers and sending the journal entries takes a few seconds; they stay for the confirmation.

## Out of scope

- Paying the same invoice twice: we don't detect it. The run has no invoice reference, so it's up to them to check the payment history.
- The limit being used up between the check and the submission: not handled; we check the limit once, before the summary.
- Another administrator editing the same run at the same time: not a case we handle; one person prepares a run.
- Exporting or erasing a contractor's payment and bank data: a separate job, and we have to keep tax records anyway.
