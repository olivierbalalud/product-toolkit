# Answers: submit an expense report

## Actor, goal and scope

- The system is our expense management service.
- They start because they have business expenses to claim, typically after a trip.
- Before they start they're already signed in, and the approval rules for their organization are already set up.
- The approver takes part only by being told there's a report waiting; approving it is the approver's own job, done separately.
- The expense administrator takes part only when no approver can be worked out for a report.
- They can start a fresh report, or pick up a draft they left earlier.
- An employee submits a few reports a month, usually after a trip or at month end.
- Approving a report and paying the employee back are separate things, not part of this.

## Stakeholders and guarantees

- The employee wants to be paid back quickly and correctly, without much effort.
- The approver wants only complete reports that have already passed the policy checks.
- Finance wants only compliant expenses, with their receipts, to reach payment.
- Auditors and the tax authority want receipts kept and every status change traceable.
- Whatever happens, expenses they've entered are never lost; they stay in a draft report.
- A report that fails a mandatory policy check never goes to an approver.
- Every change to a report's status is recorded.
- When it works: the report is stored with its expenses and receipts, gets a unique number and the status pending approval, and goes to whoever the approval rules say; the approver is told. The decision then sits with the approver, and the employee can follow the report's status until it's decided.

## Main scenario

- When they start a report, they give its business purpose.
- Each expense has a date, a category, an amount and a receipt.
- The checks run against our expense policy, and the report total is shown.
- A receipt is required for an expense above a threshold.
- Each expense category has a limit, and the policy says for which categories an exception is allowed if it's justified.
- On submission the report gets a number, its status becomes pending approval, and it's routed by the approval rules.
- Routing and automatic approval depend on the amount and on the employee's place in the hierarchy.
- At the end the employee sees the report's number and status.

## What can go wrong

- A receipt is missing for an expense that needs one.
- An expense goes over its category limit.
- They try to submit while an expense still fails a mandatory check.
- They stop before submitting.
- No approver can be worked out from the approval rules.
- Not a failure, but it changes the path: a report small enough is approved automatically.
- Routing and notifying are all inside our service; there's no outside system that can be down or fail halfway.

## How each is handled

- Missing receipt: the expense is flagged, and they attach the receipt or give a justification; then the checks run again.
- Over the limit: the expense is flagged with the limit. They correct it, or add a justification if that category allows an exception; if it doesn't, they correct it or remove it. Then the checks run again.
- Submitting with a failing check: the report isn't submitted, it stays a draft, and the system names the expenses to fix.
- Stopping before submitting: the report stays a draft with everything entered so far.
- No approver found: the report goes to the expense administrator, who is told instead.
- Automatic approval: the report is marked approved straight away, and the employee is told instead of an approver.

## Durations

- Checking the expenses and showing the total is immediate.
- Numbering, setting the status and routing on submission is immediate.
- Telling the approver and showing the employee the status happens straight away.

## Out of scope

- The same expense being claimed twice: we have no rule against it at submission; the approver reviews each expense when deciding.
- Exporting or erasing an employee's expense data: that's a separate job, and we have to keep receipts for audit and tax, which limits erasing them.
