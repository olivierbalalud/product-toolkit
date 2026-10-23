---
id: UC-001
title: Order a meal
status: Draft
driver: lab
priority: Not set
source_locale: en
inputs: []
stories: []
---

# UC-001: Order a meal

| Field | Value |
|---|---|
| **Primary actor** | Patron (an employee who orders a meal for themselves) |
| **Supporting actors** | Cafeteria Inventory System (reserves items; not built by us), Payroll system (authorizes deductions) |
| **Scope** | Cafeteria Ordering System |
| **Level** | User goal |
| **Trigger** | The Patron asks to order a meal. |
| **Preconditions** | The Patron is logged in. |
| **Minimal guarantees** | Nothing is half-saved: either the order is accepted with all its items reserved, its window slot taken and its payment settled, or nothing is reserved or saved and any partial reservation is released. Payroll is never asked to deduct an amount the Patron did not authorize. |
| **Success guarantees** | The order is saved as accepted for one date, delivery window and location. Its items are reserved in the Cafeteria Inventory System, its slot in the window is taken, and payroll has authorized the deduction for the total. Cafeteria staff are told about the order, and the Patron has a confirmation. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Patron | Gets the meal they chose, at the time and place they chose, for the total they confirmed, and is never charged for an order that didn't go through. |
| Cafeteria staff | Complete, unambiguous orders, early enough to prepare them; told about every accepted order. |
| Cafeteria management | Inventory stays accurate; a window is never promised more deliveries than it can take. |
| Payroll | Asked only for deductions the Patron actually authorized. |
| Delivery staff | Each delivery has a clear location and a window it fits in, with no window overbooked. |

## Main success scenario

1. (actor) The Patron picks a delivery date (BR-1, BR-2).
2. (system) The system shows that date's menu, with the items available and their prices.
3. (actor) The Patron selects the food items and quantities for the meal.
4. (system) The system shows a summary: the items, the taxes, the delivery charge as its own line, and the total (BR-5).
5. (actor) The Patron confirms the summary.
6. (system) The system offers the delivery windows of that date that still have room, the delivery locations and the payment methods (BR-3, BR-4, BR-9).
7. (actor) The Patron chooses a delivery window, a location and payroll deduction, authorizes the deduction, and places the order.
8. (system, wait) The system checks that the date is still open, reserves the items in the Cafeteria Inventory System, takes a slot in the window, asks payroll to authorize the deduction for the total, saves the order as accepted and notifies the cafeteria staff (BR-7).
9. (system) The system shows the Patron an order confirmation and sends it to them by email.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-001.1a | n/a | n/a | yes: `UC-001.*a` |
| 3 | yes: UC-001.3a | n/a | n/a | yes: `UC-001.*a` |
| 5 | n/a | n/a | n/a | yes: `UC-001.*a` |
| 7 | n/a | yes: UC-001.7c | yes: UC-001.7a | yes: `UC-001.*a` |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | yes: UC-001.1a | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 6 | yes: UC-001.6a | n/a | n/a | n/a | n/a | n/a | n/a |
| 8 | yes: UC-001.8a | yes: UC-001.8a | yes: UC-001.8b, UC-001.8e | yes: UC-001.8b | yes: UC-001.8a, UC-001.8c | yes: UC-001.8d | n/a |
| 9 | n/a | n/a | yes: UC-001.9a | n/a | n/a | n/a | n/a |

**Privacy request:** no: export and erasure of order history and personal data are handled by a separate use case, not yet written.

## Extensions

- **UC-001.1a** The date can't be ordered for: its cutoff has passed, it is beyond the ordering horizon, the cafeteria is closed that day, or its menu is empty:
  1. The system tells the Patron why the date can't be ordered for.
  2. The Patron picks another date and the use case returns to step 2, or stops and the use case ends.

  *Example:* Ana picks 25 December; the system tells her the cafeteria is closed that day, and she picks 27 December.
- **UC-001.3a** The Patron asks for more of an item than the cafeteria can supply:
  1. The system tells the Patron the most it can supply.
  2. The Patron lowers the quantity and the use case returns to step 4.

  *Example:* Ben asks for 3 lasagnas; only 2 are left, and he changes the quantity to 2.
- **UC-001.5a** The Patron wants to change the meal after seeing the summary (alternative, not a failure):
  1. The Patron goes back to change what they picked, or adds another meal from the menu.
  2. The use case returns to step 3.

  *Example:* After seeing the total, Ana removes the dessert and adds a soup.
- **UC-001.6a** No delivery window of the date has room left:
  1. The system tells the Patron that delivery windows are full and only pickup is available. The date is not shown as closed.
  2. The use case continues at UC-001.7b.

  *Example:* At 10:15 every delivery window for today is full, so Ben is offered pickup only.
- **UC-001.7a** The Patron is not registered for payroll deduction:
  1. The system tells the Patron that delivery needs payroll deduction, and offers pickup or registering.
  2. If the Patron chooses pickup, the use case continues at UC-001.7b. If the Patron goes off to register, the draft order is dropped and the use case ends; they order again afterwards.

  *Example:* Ana chooses delivery, is told she isn't registered for payroll deduction, and switches to pickup.
- **UC-001.7b** The Patron chooses pickup instead of delivery (alternative, not a failure):
  1. The system removes the delivery charge and shows the updated total.
  2. The Patron confirms it and places the order.
  3. The use case continues at step 8, without taking a delivery slot and without asking payroll; the Patron pays at the counter (BR-4).

  *Example:* Ben chooses pickup; his total drops by the delivery charge, and he pays at the counter.
- **UC-001.7c** The Patron places the same order twice (a double submit, or a resubmit while the first is still being processed):
  1. The system recognizes the same draft order and does not create a second order.
  2. The system shows the confirmation of the order already accepted; the use case ends.

  *Example:* Ana's connection hangs and she places the order again; she gets one confirmation and one deduction.
- **UC-001.8a** An item, or the chosen window, no longer has enough left (another Patron took it, or an item was withdrawn from the menu):
  1. The system releases anything it reserved and saves nothing.
  2. The system tells the Patron what is gone and the most still available.
  3. The Patron lowers the quantity (the use case returns to step 4) or picks another window (the use case returns to step 6).

  *Example:* Ben places an order for the 12:15 window, but another Patron took its last slot a second earlier; he picks 12:30.
- **UC-001.8b** The Cafeteria Inventory System is unreachable, or only some items could be reserved:
  1. The system releases whatever was reserved and saves nothing.
  2. The system tells the Patron the order didn't go through, keeping everything they chose.
  3. The Patron tries again (the use case returns to step 8) or gives up (the use case ends).

  *Example:* The inventory system times out after reserving the salad but not the soup; the salad is released and Ana retries a minute later.
- **UC-001.8c** The cutoff for the date passes before the order is accepted:
  1. The system saves nothing and releases anything it reserved.
  2. The system tells the Patron the date is now closed for orders.
  3. The Patron picks another date (the use case returns to step 2) or stops (the use case ends).

  *Example:* Ben places his order for today at 10:31, one minute after the cutoff; he is told today is closed and orders for tomorrow.
- **UC-001.8d** A price on the menu changed after the summary was shown:
  1. The system reserves nothing and saves nothing.
  2. The system shows the updated summary and the use case returns to step 4, so the Patron confirms the new total.

  *Example:* The price of the curry rises from 8.50 to 9.00 while Ana is choosing a window; she sees the new total and confirms it.
- **UC-001.8e** Payroll refuses the deduction, or is unreachable:
  1. The system releases the items and the window slot, and saves nothing.
  2. The system tells the Patron the deduction could not be authorized, keeping everything they chose.
  3. The Patron chooses pickup (UC-001.7b), tries again (the use case returns to step 8), or gives up (the use case ends).

  *Example:* Payroll refuses Ben's deduction; he switches to pickup and pays at the counter.
- **UC-001.8f** The cafeteria staff notification fails: `out-of-scope`, the order stands and the staff see accepted orders anyway.
- **UC-001.9a** The confirmation email can't be sent:
  1. The order stands; the Patron still sees the confirmation on screen.
  2. The use case ends.

  *Example:* The mail service is down at 9:05; Ana sees her confirmation on screen but gets no email.
- **`UC-001.*a`** The Patron abandons (closes the app, walks away, or the session expires) before the order is accepted:
  1. The system throws the draft away; nothing is reserved or saved, and no cart is kept.
  2. The use case ends.

  *Example:* Ben picks his items, then closes the app before choosing a window; next time he starts from an empty order.

## Technology and data variations

- Step 7: delivery to a location, paid by payroll deduction, or pickup at the counter, paid there with no delivery charge (UC-001.7b).
- Step 1: the date defaults to today, or to the next open day when today can't be ordered for.
- Step 9: confirmation on screen and by email.
- Step 8: the cafeteria staff see the order in their list of accepted orders.

## Related information

- **Frequency:** About 400 orders per day (about 400 users, roughly one order each), most of them between 8:00 and 10:00.
- **Business rules:**
  - **BR-1** An order is for one date only. The date defaults to today or the next open day. A Patron can order up to 7 days ahead (recommendation).
  - **BR-2** Each date has one ordering cutoff, at 10:30 on the date itself (recommendation). After it, the date can't be ordered for.
  - **BR-3** Delivery windows are 15 minutes long, from 11:30 to 13:30 (recommendation). Each window takes a number of deliveries set by cafeteria management, 20 by default (recommendation). Only windows with room left are offered.
  - **BR-4** Delivery is paid by payroll deduction: the Patron must be registered for it and authorize it for each order. Pickup is paid at the counter. No card or other payment method (recommendation). The deduction is authorized when the order is accepted (recommendation).
  - **BR-5** The delivery charge is a flat amount per order (recommendation), shown as its own line. Pickup has no delivery charge.
  - **BR-6** Quantity is limited only by stock. No cap on order total or on orders per Patron per day (recommendation).
  - **BR-7** Nothing is reserved or saved until the order is accepted. Reserving all items, taking the window slot and authorizing the deduction succeed together or not at all.
  - **BR-8** A Patron orders only for themselves (recommendation).
  - **BR-9** Delivery locations are picked from a list maintained by cafeteria management; no free-text addresses (recommendation).
- **Open issues:**
  - Confirm the recommendations marked in BR-1 to BR-9, and the handling recommended in UC-001.7c, UC-001.8d and UC-001.8e.
  - Does pickup need a pickup time, and is pickup capacity limited?
  - The summary at step 4 includes a delivery charge before the Patron chooses delivery or pickup at step 7. Should delivery or pickup be chosen earlier?
  - How cafeteria staff are notified (recommendation: their list of accepted orders).
