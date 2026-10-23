* **Use Case ID:** UC-B2B-03
* **Level:** Sea-Level (User Goal)
* **Primary Actor:** Payroll Administrator / Finance Lead
* **Scope:** Gusto SaaS Platform (Payroll & Disbursements)
* **Stakeholders & Interests:**
  * *Contractors (1099):* Expect accurate, timely direct deposit funds without surprise deductions.
  * *Corporate Treasury:* Needs immediate visibility into bank account debit liabilities to prevent overdrafts.
  * *Tax & Regulatory Authorities:* Mandates accurate accounting records for end-of-year 1099-NEC filings.
* **Preconditions:**
  1. The employer's primary business checking account is connected via Plaid/ACH and verified with positive balance standing.
  2. Target contractors have active profiles with completed W-9 verification and verified direct deposit routing.
* **Success Guarantees (Postconditions):**
  1. An off-cycle disbursement batch is queued for payment clearing.
  2. Employer's bank account receives an ACH debit reservation for the exact total amount.
  3. Digital payment vouchers (pay stubs) are created in contractor accounts.
  4. General ledger journal entries are synchronized with connected ERP/accounting software (e.g., QuickBooks Online, NetSuite).
* **Trigger:** An unscheduled or milestone-based invoice requires immediate settlement outside the standard monthly pay schedule.

**Main Success Scenario (MSS):**
1. Actor selects an off-cycle payment run and chooses the subset of contractors eligible for disbursement.
2. Actor enters payment amounts, hours/deliverables, and allocates project cost centers for each payee.
3. System verifies that aggregate pay amounts do not exceed the company’s uncollateralized instant payroll limit.
4. System confirms that the employer’s banking rails and recipient bank clearing networks are open for the chosen disbursement date.
5. System displays a pre-submission reconciliation summary detailing gross disbursements, processing fees, and ACH pull dates.
6. Actor confirms and digitally authorizes the payroll execution.
7. System locks the run, submits the batch to the payment clearinghouse, and generates accounting journal lines.

**Extensions (Alternate & Failure Paths):**
* **3a. Total disbursement exceeds the instant settlement risk threshold:**
  * 3a1. System halts automated direct ACH processing.
  * 3a2. System informs Actor that a wire transfer or an extended 4-day ACH processing hold is required.
  * 3a3. Actor accepts the adjusted timeline or reduces the batch size to proceed.
* **4a. Target settlement date coincides with a federal banking holiday or passes the daily ACH cutoff window:**
  * 4a1. System recalculates the earliest available settlement date.
  * 4a2. System presents the adjusted deposit date to the Actor for explicit sign-off before proceeding.
* **6a. A selected contractor’s banking credentials are flagged as invalidated by their financial institution:**
  * 6a1. System excludes the compromised contractor from the direct deposit batch.
  * 6a2. System offers the Actor the choice to issue a manual paper check or bypass that payee while processing the remainder.
