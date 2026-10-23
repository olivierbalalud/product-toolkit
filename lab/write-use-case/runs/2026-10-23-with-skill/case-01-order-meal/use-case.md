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
| **Primary actor** | Patron (an employee) |
| **Supporting actors** | Cafeteria Inventory System (reserves the items); cafeteria staff (told of every accepted order) |
| **Scope** | Cafeteria ordering system |
| **Level** | User goal |
| **Trigger** | The Patron wants to order a meal for a given date. |
| **Preconditions** | The Patron is signed in. |
| **Minimal guarantees** | No order is half-accepted: no items or delivery window stay reserved, and no payroll deduction is authorized, without an accepted order. If the Patron cancels or walks away, the draft is discarded and nothing is kept. |
| **Success guarantees** | The order is saved for the date with the Patron's payroll deduction authorization; the Cafeteria Inventory System shows its items as taken; the delivery window has one place fewer; the Patron and the cafeteria staff are told the order is accepted. Preparing and delivering the meal is pending, as the cafeteria's own work. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Patron | Gets the meal they chose at the time and place they chose, and pays exactly the total shown. |
| Cafeteria staff | Get complete, unambiguous orders early enough to prepare them. |
| Cafeteria management | Inventory stays accurate, and a window is never promised more deliveries than it can take. |
| Payroll office | Deducts only what the Patron authorized. |

## Main success scenario

1. (actor) The Patron chooses the date of the meal (BR-1, BR-2).
2. (system) The system presents that day's menu.
3. (actor) The Patron chooses the items and their quantities (BR-3).
4. (actor) The Patron chooses delivery, a delivery window and a location (BR-4, BR-5, BR-6).
5. (system) The system presents each item's price, the taxes, the delivery charge and the total.
6. (actor) The Patron confirms the order and authorizes the payroll deduction for the total.
7. (system) The system reserves the items through the Cafeteria Inventory System, takes the delivery window, saves the order with the authorization, and tells the Patron and the cafeteria staff that the order is accepted.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-001.1a | n/a | n/a | yes: UC-001.1-6a |
| 3 | yes: UC-001.3a | n/a | n/a | yes: UC-001.1-6a |
| 4 | yes: UC-001.4b | n/a | yes: UC-001.4a | yes: UC-001.1-6a |
| 6 | n/a | n/a | n/a | yes: UC-001.1-6a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 7 | n/a | yes: UC-001.7b, UC-001.7c | yes: UC-001.7a | yes: UC-001.7a | yes: UC-001.7b, UC-001.7c | yes: UC-001.7b, UC-001.7c, UC-001.7d | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing the Patron's order history is a separate use case, not yet written.

## Extensions

- **UC-001.1-6a** The Patron cancels or walks away before confirming:
  1. The system discards the draft and keeps nothing.
  2. The use case ends.

  *Example:* Lena chooses two soups for Thursday, is called into a meeting and never comes back; no draft of her order remains.
- **UC-001.1a** The cafeteria is closed on the chosen date, or the date is today and the cutoff has passed (BR-1, BR-2):
  1. The system tells the Patron why the date can't be ordered for and proposes the next day the cafeteria is open.
  2. The Patron accepts that day or picks another date: returns to step 2. Or stops: the use case ends.

  *Example:* Omar picks Saturday; the cafeteria is closed on Saturdays, so the system proposes Monday, which he accepts.
- **UC-001.3a** The Patron asks for more of an item than the cafeteria can supply (BR-3):
  1. The system tells the Patron the most it can supply of that item.
  2. The Patron lowers the quantity to that amount or drops the item: returns to step 3.

  *Example:* Priya asks for six lasagnas for Tuesday; the cafeteria can supply four, so she takes four.
- **UC-001.4a** The Patron chooses delivery but is not registered for payroll deduction (BR-5):
  1. The system tells the Patron that delivery needs payroll deduction registration and offers pickup or registering.
  2. The Patron chooses pickup: continues as in UC-001.4c. Or goes off to register: the system discards the draft and the use case ends; the Patron orders again once registered.

  *Example:* Tom, who joined last week and never registered for payroll deduction, chooses delivery to room 2.14 and switches to pickup at 12:30.
- **UC-001.4b** The Patron chooses delivery, and the order contains an item that can't be delivered (BR-6):
  1. The system names the item that can't be delivered.
  2. The Patron removes it: returns to step 5. Or switches to pickup: continues as in UC-001.4c.

  *Example:* Ines orders a salad and a soft-serve ice cream for delivery; the system names the ice cream, and she removes it.
- **UC-001.4c** The Patron chooses pickup instead of delivery:
  1. The Patron chooses a pickup time.
  2. The system presents each item's price, the taxes and the total, with no delivery charge, to be paid at the counter (BR-5).
  3. The Patron confirms the order.
  4. Returns to step 7, where no delivery window is taken and no payroll deduction is authorized.

  *Example:* Marc orders a curry for today, chooses pickup at 12:15 and sees a total without a delivery charge, to pay at the counter.
- **UC-001.4d** No delivery window has room left on the chosen date (BR-4):
  1. The system offers only pickup.
  2. Continues as in UC-001.4c.

  *Example:* Sara orders for Friday at 11:00; every Friday delivery window is full, so only pickup is offered and she picks 13:00.
- **UC-001.5a** After seeing the total, the Patron wants to change the items or add another meal from that day's menu:
  1. The system keeps the choices made so far.
  2. Returns to step 3.

  *Example:* Ali sees his total of 9.40 for one pasta and adds a second meal for a colleague's lunch from the same menu.
- **UC-001.7a** The Cafeteria Inventory System does not answer, or reserves only some of the items:
  1. The system releases whatever was reserved, saves nothing and keeps the Patron's choices.
  2. The Patron retries: returns to step 6. Or gives up: the use case ends.

  *Example:* Julia confirms her order for Wednesday; the inventory system reserves the soup but not the bread, so the soup is released and she retries a moment later.
- **UC-001.7b** The chosen delivery window filled up after it was offered (BR-4):
  1. The system reserves nothing, saves nothing and tells the Patron the window is full.
  2. The Patron picks another window: returns to step 4. Or lowers the quantity: returns to step 3.

  *Example:* Ken confirms delivery in the 12:00 to 12:30 window; a colleague took its last place a second earlier, so Ken picks 12:30 to 13:00.
- **UC-001.7c** An item ran out after it was shown (BR-3):
  1. The system reserves nothing, saves nothing and tells the Patron which item is gone and how many are left.
  2. The Patron lowers the quantity to what is left: returns to step 3.

  *Example:* Nora confirms three quiches for today; only one is left by then, so she lowers her order to one.
- **UC-001.7d** The cutoff passed while the Patron was ordering for today (BR-1):
  1. The system reserves nothing, saves nothing and tells the Patron the cutoff has passed.
  2. The Patron picks another date: returns to step 1. Or stops: the use case ends.

  *Example:* Paul starts ordering for today just before the cutoff, confirms a minute after it, and picks tomorrow instead.
- **UC-001.7e** Telling the cafeteria staff fails after the order is accepted: `out-of-scope`, the order stands; the driver put this case out of scope.

## Technology and data variations

- 1: the Patron takes the default date (today before the cutoff, otherwise the next day the cafeteria is open) or picks another date.

## Related information

- **Frequency:** about 400 orders a day (about 400 Patrons, roughly one order each), peaking between 8:00 and 10:00.
- **Business rules:**
  - BR-1 a same-day order must be placed before the daily cutoff; after it, orders go to the next day the cafeteria is open (step 1, UC-001.1a, UC-001.7d).
  - BR-2 no order can be placed for a day the cafeteria is closed (step 1, UC-001.1a).
  - BR-3 a Patron can't order more of an item than the cafeteria can supply (step 3, UC-001.3a, UC-001.7c).
  - BR-4 a delivery window takes deliveries only while it has room; full windows aren't offered (step 4, UC-001.4d, UC-001.7b).
  - BR-5 delivery requires payroll deduction registration and is paid by payroll deduction; pickup needs only a signed-in Patron and is paid at the counter, with no delivery charge (step 4, UC-001.4a, UC-001.4c).
  - BR-6 items that can't be delivered can't be in a delivery order (step 4, UC-001.4b).
- **Related use cases:** Prepare and deliver a meal order (cafeteria staff); Change an accepted order; Cancel an accepted order; Register for payroll deduction; Export or erase the Patron's order history.
- **Open issues:** None
