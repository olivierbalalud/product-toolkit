---
id: UC-001
title: Order a meal
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-001: Order a meal

| Field | Value |
|---|---|
| **Primary actor** | Patron (employee) |
| **Supporting actors** | Cafeteria Inventory System (reserves the items); Cafeteria Staff (notified of each accepted order) |
| **Scope** | Cafeteria Ordering System |
| **Level** | User goal |
| **Trigger** | The Patron decides to order a meal for a given date. |
| **Preconditions** | The Patron is authenticated. |
| **Minimal guarantees** | No order is stored, no food item is reserved and no delivery slot is consumed unless the order is accepted at step 8. |
| **Success guarantees** | The order is stored with status *Accepted*; the inventory reflects the ordered items; for a delivery, the remaining capacity of the delivery window is reduced; the Patron and the Cafeteria Staff are notified. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Patron | Gets the chosen meal at the chosen place and time without queuing; is charged correctly. |
| Cafeteria Staff | Receives complete, unambiguous orders early enough to prepare them. |
| Cafeteria management | Inventory stays accurate; delivery capacity is never over-committed. |
| Payroll | Only authorized deductions are requested. |

## Main success scenario

1. (actor) The Patron asks for the menu for a date (BR-1 gives the default date).
2. (system) The system presents the food items available for that date and the daily special.
3. (actor) The Patron selects food items.
4. (system) The system presents the delivery windows (BR-2) still available for that date, and pickup at the cafeteria.
5. (actor) The Patron chooses delivery: a delivery window, a delivery location and payment by payroll deduction.
6. (system) The system presents the order summary: item prices, taxes, delivery charge and total.
7. (actor) The Patron confirms the order.
8. (system) The system reserves the items with the Cafeteria Inventory System and the delivery slot, stores the order as *Accepted*, notifies the Cafeteria Staff and sends the Patron a confirmation.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-001.1a | n/a | n/a | yes: UC-001.1-7a |
| 3 | yes: UC-001.3b | n/a | n/a | yes: UC-001.1-7a |
| 5 | yes: UC-001.5b | n/a | yes: UC-001.5c | yes: UC-001.1-7a |
| 7 | n/a | n/a | n/a | yes: UC-001.1-7a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | n/a | n/a | n/a | n/a | yes: UC-001.4a | n/a | n/a |
| 6 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 8 | n/a | yes: UC-001.8a | yes: UC-001.8b | yes: UC-001.8b | yes: UC-001.8a | yes: UC-001.8a, UC-001.8c | n/a |

**Privacy request:** yes: `deferred`, a Patron's request to export or erase their order history is its own use case, not written yet.

## Extensions

- **UC-001.1a** No ordering is possible for that date: the order cutoff has passed (BR-1) or the cafeteria is closed that day:
  1. The system says why no order can be placed for that date.
  2. The Patron gives another date: returns to step 2. Or the Patron stops: the use case ends.

  *Example:* On Thursday at 10:20 Lena asks for Thursday's menu; the cutoff was 10:00, so she asks for Friday's instead.
- **UC-001.3a** The Patron asks for several identical meals:
  1. The Patron gives the quantity of that item.
  2. Returns to step 3, with that quantity in the selection.

  *Example:* Tomás orders three chicken curries for himself and two colleagues.
- **UC-001.3b** The system cannot supply the quantity the Patron gave:
  1. The system states the maximum quantity it can supply.
  2. Returns to step 3, where the Patron adjusts the quantity.

  *Example:* Tomás asks for 12 vegetable lasagnes; the system can supply 8, and he lowers his order to 8.
- **UC-001.4a** No delivery window is left for that date:
  1. The system says no delivery window is left and offers only pickup at the cafeteria.
  2. The Patron chooses pickup: continues as in UC-001.5a.

  *Example:* Marco orders at 9:30 for today; every delivery window is full, so he will pick his meal up at the cafeteria at 12:30.
- **UC-001.5a** The Patron chooses pickup at the cafeteria instead of delivery:
  1. The Patron gives a pickup time.
  2. Returns to step 6; the summary has no delivery charge and shows payment at the counter.

  *Example:* Priya will collect her lunch at 12:40 and pay at the counter, so her total has no delivery charge.
- **UC-001.5b** The Patron chooses delivery for an order that contains an item that cannot be delivered (BR-3):
  1. The system names the items that cannot be delivered.
  2. The Patron removes them: returns to step 3. Or the Patron chooses pickup: continues as in UC-001.5a.

  *Example:* Lena's order includes a soft-serve ice cream, which cannot be delivered; she removes it and chooses the 12:00–12:15 delivery again.
- **UC-001.5c** The Patron chooses delivery but is not registered for payroll deduction (BR-4):
  1. The system says delivery requires payroll deduction registration, and offers pickup or registering.
  2. The Patron chooses pickup: continues as in UC-001.5a. Or the Patron leaves to register (use case Register for Payroll Deduction): the draft order is discarded and the use case ends.

  *Example:* Jonas, hired last week and not yet registered for payroll deduction, chooses delivery to his desk; he switches to pickup at 12:15.
- **UC-001.7a** The Patron asks to change the selection:
  1. Returns to step 3.

  *Example:* Priya reads the summary and swaps the fish soup for a Caesar salad.
- **UC-001.7b** The Patron asks to add another meal to the order:
  1. Returns to step 2.

  *Example:* Priya, ordering her Friday lunch, adds a second meal for a visitor from the same menu.
- **UC-001.8a** The chosen delivery window filled up, or an item ran out, after the system presented it:
  1. The system reserves nothing, stores no order and says which window or item is no longer available.
  2. For a window, returns to step 4. For an item, the system states the quantity it can still supply and returns to step 3.

  *Example:* Marco and Ana both choose the last place in the 12:15–12:30 window; Ana's order is accepted first, so Marco is shown the windows still free.
- **UC-001.8b** The system cannot reserve the items: the Cafeteria Inventory System does not answer, or only part of the reservation succeeds:
  1. The system releases anything it reserved and stores no order.
  2. The system tells the Patron the order was not placed and keeps the Patron's choices.
  3. The Patron tries again: returns to step 8. Or the Patron cancels: the draft order is discarded and the use case ends.

  *Example:* Priya confirms her order at 9:05 while the Cafeteria Inventory System is down; nothing is reserved, and her retry at 9:07 is accepted.
- **UC-001.8c** The order cutoff for that date passed before the order was accepted (BR-1):
  1. The system reserves nothing, stores no order and says the cutoff for that date has passed.
  2. The Patron gives another date: returns to step 2. Or the Patron stops: the use case ends.

  *Example:* Ana starts her order for Thursday at 9:55 on Thursday and confirms at 10:01; the cutoff was 10:00, so she orders for Friday instead.
- **UC-001.1-7a** The Patron cancels the order, or walks away from it, before it is accepted:
  1. The system discards the draft order; nothing is stored or reserved.
  2. The use case ends.

  *Example:* Tomás has selected two meals, is called into a meeting and never comes back; his draft is discarded and nothing is reserved.

## Technology and data variations

- 5: delivery (delivery window, delivery location, payment by payroll deduction) or pickup (pickup time, payment at the counter, no delivery charge).

## Related information

- **Frequency:** about 400 users, about one order each per day; peak 8:00–10:00.
- **Business rules:** BR-1 order cutoff time; the default date is today before the cutoff, otherwise the next opening day (step 1, UC-001.1a, UC-001.8c). BR-2 delivery windows are 15 minutes (step 4). BR-3 items that cannot be delivered cannot be ordered for delivery (UC-001.5b). BR-4 delivery requires payroll deduction registration (UC-001.5c).
- **Related use cases:** Change Meal Order, Cancel Meal Order, Register for Payroll Deduction.
- **Open issues:** None
