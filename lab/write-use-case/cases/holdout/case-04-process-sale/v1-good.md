- **ID / Name:** UC-1 — Process Sale
- **Scope:** POS application (black box) · **Level:** User goal (!)
- **Primary actor:** Cashier
- **Supporting actors:** Payment Authorization Service, Tax Calculator, Accounting system, Inventory system
- **Stakeholders & interests:**
  - Cashier — fast, accurate entry; no payment mistakes (shortages come out of their pay).
  - Customer — fast checkout, correct prices, proof of purchase for returns.
  - Retailer — accurate records, payments captured, sales still possible when back-end services are down.
  - Store manager — can perform overrides quickly.
  - Tax authorities — tax collected on every sale.
  - Payment Authorization Service — requests in the expected format.
- **Trigger:** A customer arrives at checkout with goods.
- **Preconditions:** Cashier is identified and authenticated.
- **Minimal guarantees** *(added)*: A sale is never recorded as paid without confirmed payment; completed sales are never lost.
- **Success guarantees:** Sale saved; tax correctly calculated; accounting and inventory updated; commissions recorded; receipt generated; payment authorization recorded.

**Main success scenario**
1. Cashier starts a new sale.
2. Cashier enters an item identifier.
3. System records the line item and presents its description, price and the running total. *Cashier repeats steps 2–3 until all items are entered.*
4. System presents the total with taxes calculated.
5. Customer pays and System handles the payment.
6. System records the completed sale and sends the sale and payment information to the Accounting and Inventory systems.
7. System presents the receipt.

**Extensions**
- \*a. At any time, Manager requests an override: System enters manager-authorized mode; Manager performs the operation; System returns to Cashier mode.
- 2a. Invalid identifier: System signals the error and rejects the entry; continue at step 2.
- 2b. Several units of the same item: Cashier enters the quantity.
- 4a. Customer is eligible for a discount: Cashier identifies the customer; System applies the discount rules.
- 5a. Customer pays cash: Cashier enters the amount tendered; System presents the change due.
- 5b. Customer pays by card: System requests authorization from the Payment Authorization Service.
  - 5b1. Payment declined: System signals the denial; Cashier asks for another payment method; continue at step 5.
- 6a. Accounting or Inventory system unavailable: System stores the sale locally and forwards it when the service is back.

**Technology & data variations:** item entry by barcode, keyboard or camera; payment by card reader, contactless or mobile wallet.
