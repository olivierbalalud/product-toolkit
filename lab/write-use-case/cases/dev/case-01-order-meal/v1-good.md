- **ID / Name:** UC-01 — Order Meal
- **Scope:** Cafeteria Ordering System (black box) · **Level:** User goal (!)
- **Primary actor:** Patron (employee)
- **Supporting actors:** Cafeteria Inventory System, Cafeteria Staff (notified)
- **Stakeholders & interests:**
  - Patron — gets the chosen meal at the chosen place and time without queuing; is charged correctly.
  - Cafeteria Staff — receives complete, unambiguous orders early enough to prepare them.
  - Cafeteria management — inventory stays accurate; delivery capacity is never over-committed.
  - Payroll — only authorized deductions are requested.
- **Trigger:** Patron decides to order a meal for a given date.
- **Preconditions:** Patron is authenticated; Patron is registered for payroll deduction (required for delivery, see UC-05).
- **Minimal guarantees:** No order is stored, no food item is reserved and no delivery slot is consumed unless the Patron confirmed the order.
- **Success guarantees:** Order stored with status *Accepted*; inventory reflects the ordered items; remaining capacity of the delivery window is reduced; Patron and Cafeteria Staff are notified.

**Main success scenario**
1. Patron requests the menu for a delivery date.
2. System presents the available food items and the daily special for that date.
3. Patron selects food items.
4. System presents the order summary: item prices, taxes, delivery charge and total.
5. Patron confirms the order.
6. System presents the delivery windows still available for that date.
7. Patron chooses a delivery window, a delivery location and a payment method.
8. System accepts the order, reserves the items and the delivery slot, notifies Cafeteria Staff, and sends the Patron a confirmation.

**Extensions**
- \*a. At any time before step 8, Patron cancels: System discards the draft; use case ends.
- 1a. Order cutoff for that date has passed (BR-1): System says so; Patron picks another date (continue at step 2) or abandons (use case ends).
- 3a. Patron wants several identical meals: Patron gives the quantity.
  - 3a1. System cannot supply that quantity: System states the maximum; Patron adjusts the quantity or cancels.
- 5a. Patron wants to change the selection: continue at step 3.
- 5b. Patron wants to add another meal to the order: continue at step 2.
- 6a. No delivery window left for that date: System says so; Patron chooses pickup at the cafeteria (skip the location in step 7) or cancels (use case ends).

**Business rules:** BR-1 order cutoff time (default date is today before cutoff, otherwise next opening day) · BR-2 delivery windows are 15 minutes · BR-3 non-deliverable items cannot be ordered for delivery · BR-4 delivery requires payroll deduction registration.
**Technology & data variations:** payment by payroll deduction (delivery) or at the counter (pickup).
**Notes:** ~400 users, about one order each per day; peak 8:00–10:00.
**Related:** UC-02 Change Meal Order, UC-03 Cancel Meal Order, UC-05 Register for Payroll Deduction.
