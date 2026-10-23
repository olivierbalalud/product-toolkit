- **ID / Name:** UC-EXP-01 — Submit Expense Report
- **Scope:** Expense management service (black box) · **Level:** User goal (!)
- **Primary actor:** Employee
- **Supporting actor:** Approver (notified only; approving is a separate use case)
- **Stakeholders & interests:**
  - Employee — reimbursed quickly and correctly with little effort.
  - Approver — receives complete, policy-checked reports only.
  - Finance — only compliant, receipted expenses reach payment.
  - Auditor / tax authority — receipts retained and every status change traceable.
- **Trigger:** Employee wants to claim business expenses (e.g. after a trip).
- **Preconditions:** Employee is authenticated; approval rules are configured for the Employee's organization.
- **Minimal guarantees:** Entered expenses are never lost (kept as draft); a report that fails a mandatory policy check is never routed for approval; every status change is recorded.
- **Success guarantees:** Report stored with a unique number and status *Pending approval*, routed to the approver(s) determined by the approval rules; approver notified; Employee can track status.

**Main success scenario**
1. Employee starts an expense report for a business purpose.
2. Employee records each expense with its date, category, amount and receipt.
3. System checks each expense against the expense policy and shows the report total.
4. Employee reviews the report and submits it for approval.
5. System assigns a report number, sets the status to *Pending approval*, and routes the report according to the approval rules.
6. System notifies the approver and shows the Employee the report's status.

**Extensions**
- 2a. Receipt missing where required (BR-1): System flags the expense; Employee attaches the receipt or gives a justification; continue at step 3.
- 3a. Expense exceeds a policy limit (BR-2): System flags it; Employee corrects the expense or, where policy allows, adds a justification; continue at step 3. If policy does not allow an exception, the expense must be removed before step 4.
- 4a. Employee stops before submitting: System keeps the report as *Draft*; use case ends.
- 5a. Report qualifies for automatic approval (BR-3): System marks it *Approved*; continue at step 6 (Employee notified instead of an approver).
- 5b. No approver can be determined *(added)*: System routes the report to the expense administrator; continue at step 6.

**Business rules:** BR-1 receipt required above a threshold · BR-2 per-category limits · BR-3 routing and auto-approval by amount and hierarchy.
**Out of scope:** Approve Expense Report (Approver's goal), Reimburse Employee.
