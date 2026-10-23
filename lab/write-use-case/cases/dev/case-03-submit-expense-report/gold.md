---
id: UC-003
title: Submit an expense report
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-003: Submit an expense report

| Field | Value |
|---|---|
| **Primary actor** | Employee |
| **Supporting actors** | Approver (notified of the report at step 6; approving it is a separate use case); Expense administrator (receives a report for which no approver can be determined, UC-003.5b) |
| **Scope** | Expense management service |
| **Level** | User goal |
| **Trigger** | The Employee wants to claim business expenses, for example after a trip. |
| **Preconditions** | The Employee is authenticated; approval rules are configured for the Employee's organization. |
| **Minimal guarantees** | Entered expenses are never lost: they are kept in a draft report; a report that fails a mandatory policy check is never routed for approval; every status change of the report is recorded. |
| **Success guarantees** | The report is stored with its expenses and receipts under a unique number, with status *Pending approval*, and routed to the approver or approvers the approval rules determine (BR-3); the approver is notified; the decision is pending with the approver, and the Employee can follow the report's status until it is decided in Approve Expense Report. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Employee | Is reimbursed quickly and correctly with little effort. |
| Approver | Receives only complete reports that have passed the policy checks. |
| Finance | Only compliant expenses with their receipts reach payment. |
| Auditor / tax authority | Receipts are retained and every status change is traceable. |

## Main success scenario

1. (actor) The Employee starts an expense report and gives its business purpose.
2. (actor) The Employee records each expense with its date, category, amount and receipt.
3. (system) The system checks each expense against the expense policy (BR-1, BR-2) and shows the report total.
4. (actor) The Employee submits the report for approval.
5. (system) The system assigns the report a number, sets its status to *Pending approval* and routes it according to the approval rules (BR-3).
6. (system) The system notifies the approver and shows the Employee the report's number and status.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | n/a | n/a | n/a | yes: UC-003.1-4a |
| 2 | yes: UC-003.2a, UC-003.2b | out-of-scope: no rule against claiming the same expense twice is defined; the approver reviews each expense in Approve Expense Report | n/a | yes: UC-003.1-4a |
| 4 | yes: UC-003.4a | n/a | n/a | yes: UC-003.1-4a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 3 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | yes: UC-003.5b | n/a | n/a | n/a | n/a | n/a | n/a |
| 6 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing an Employee's expense data is its own use case; the legal retention of receipts for audit and tax limits erasure.

## Extensions

- **UC-003.1-4a** The Employee stops before submitting the report:
  1. The system keeps the report as *Draft*, with every expense entered so far.
  2. The use case ends.

  *Example:* Omar has recorded three of his five Berlin trip expenses when he is called into a meeting; his report stays a draft with the three expenses.
- **UC-003.2a** A receipt is missing for an expense that requires one (BR-1):
  1. The system flags the expense as missing its receipt.
  2. The Employee attaches the receipt or gives a justification.
  3. Returns to step 3.

  *Example:* Nadia records a €140 hotel night without a receipt; receipts are required above €25, so the system flags it and she attaches the hotel's invoice.
- **UC-003.2b** An expense exceeds its category limit (BR-2):
  1. The system flags the expense and states the limit.
  2. The Employee corrects the expense or, where the policy allows an exception for that category, adds a justification; where it does not, the Employee corrects or removes the expense.
  3. Returns to step 3.

  *Example:* Omar records a €95 client dinner against a €60 meals limit that allows exceptions; he explains that four clients attended, and the dinner stays in the report with his justification.
- **UC-003.4a** The Employee submits the report while an expense still fails a mandatory policy check (BR-1, BR-2):
  1. The system does not submit the report, keeps it as *Draft* and names the expenses to fix.
  2. Returns to step 2.

  *Example:* Nadia submits her Lisbon trip report with a €70 taxi fare above the €50 taxi limit, which allows no exception; the report stays a draft and the system points her to the taxi fare.
- **UC-003.5a** The report qualifies for automatic approval (BR-3):
  1. The system sets the report's status to *Approved* instead of *Pending approval*.
  2. Returns to step 6, where the system notifies the Employee instead of an approver.

  *Example:* Lea submits a report with one €18 parking ticket; reports under €50 are approved automatically, so it is set to *Approved* at once and she is told so.
- **UC-003.5b** No approver can be determined from the approval rules:
  1. The system routes the report to the expense administrator.
  2. Returns to step 6, where the system notifies the expense administrator.

  *Example:* Jonas's manager left the company last week and has no successor yet; his report goes to the expense administrator.

## Technology and data variations

- 1: the Employee starts a new report, or continues a draft kept from an earlier sitting (UC-003.1-4a).

## Related information

- **Frequency:** a few reports a month per Employee, typically after a trip or at month end.
- **Business rules:** BR-1 a receipt is required for an expense above a threshold (step 3, UC-003.2a, UC-003.4a) · BR-2 each expense category has a limit, and the policy says for which categories a justified exception is allowed (step 3, UC-003.2b, UC-003.4a) · BR-3 routing and automatic approval depend on the amount and the Employee's place in the hierarchy (step 5, UC-003.5a).
- **Related use cases:** Approve Expense Report, Reimburse Employee.
- **Open issues:** None
