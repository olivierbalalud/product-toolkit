---
id: UC-001
title: Order a meal
status: Draft
driver: lab
priority: unset
source_locale: en
inputs: []
stories: []
---

# UC-001: Order a meal

| Field | Value |
|---|---|
| **Primary actor** | Patron (an employee) |
| **Supporting actors** | Cafeteria Inventory System; cafeteria staff |
| **Scope** | Cafeteria Ordering System |
| **Level** | User goal |
| **Trigger** | The Patron asks to order a meal for a date. |
| **Preconditions** | The Patron is logged in. |
| **Minimal guarantees** | Until the order is accepted, nothing is kept, however the attempt ends: no order is saved, no item is reserved and no delivery slot is used up. |
| **Success guarantees** | The order is saved as accepted, the inventory shows its items as taken, a delivery takes one place in its window, and both the Patron and the cafeteria staff are told. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Patron | Gets the meal they chose, at the place and time they chose, without queuing, and is charged the right amount. |
| Cafeteria staff | Receive complete, unambiguous orders early enough to prepare them. |
| Cafeteria management | Inventory stays accurate; no window is ever promised more deliveries than it can take. |
| Payroll | Is asked only for deductions the Patron actually authorized. |

## Main success scenario

1. (actor) The Patron chooses a delivery date, or keeps the default date (BR-1).
2. (system) The system shows the menu for that date, including the daily special.
3. (actor) The Patron selects the food items for the meal, with a quantity for each.
4. (system) The system offers the delivery windows for the date that still have room (BR-3), and pickup at the cafeteria (BR-4).
5. (actor) The Patron chooses delivery, a delivery window and a delivery location.
6. (system) The system shows the summary: each item's price, the taxes, the delivery charge, the total, and payment by payroll deduction (BR-5, BR-7).
7. (actor) The Patron confirms the order.
8. (system) The system reserves the items with the Cafeteria Inventory System, saves the order as accepted, takes one place in the chosen window, notifies the cafeteria staff, and sends the Patron an order confirmation.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-001.1a | n/a | n/a | yes: `UC-001.*a` |
| 3 | yes: UC-001.3a | n/a | n/a | yes: `UC-001.*a` |
| 5 | yes: UC-001.5a | n/a | yes: UC-001.5b | yes: `UC-001.*a` |
| 7 | n/a | n/a | n/a | yes: `UC-001.*a` |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | n/a | n/a | n/a | n/a | yes: UC-001.4a | n/a | n/a |
| 6 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 8 | n/a | yes: UC-001.8a, UC-001.8b | yes: UC-001.8c | yes: UC-001.8c, UC-001.8e | yes: UC-001.8a, UC-001.8b | yes: UC-001.8d | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing a Patron's order history is a separate use case, not yet written.

## Extensions

- **UC-001.1a** The date can't be ordered for: its cutoff has passed, or the cafeteria is closed that day (BR-2):
  1. The system tells the Patron why the date can't be ordered for.
  2. The Patron picks another date and the use case returns to step 2, or stops and the use case ends.

  *Example:* At 11:30 Ana asks for today's menu, but today's cutoff was 10:30.
- **UC-001.3a** The Patron asks for more of an item than the cafeteria can supply (BR-6):
  1. The system tells the Patron the most it can supply of that item.
  2. The Patron changes the quantity; the use case returns to step 4.

  *Example:* Ben asks for 12 vegetable soups; the cafeteria can supply 8.
- **UC-001.4a** Every delivery window for the date is full (BR-3):
  1. The system offers only pickup.
  2. The use case continues at UC-001.5c.

  *Example:* Chloe orders for Friday, when all twelve lunch windows are already full.
- **UC-001.5a** The Patron chooses delivery, and an item in the order can't be delivered (BR-8):
  1. The system names the item that can't be delivered.
  2. The Patron takes the item out and the use case returns to step 6, or switches to pickup and the use case continues at UC-001.5c.

  *Example:* Dan chooses delivery with a soft-serve ice cream in his order.
- **UC-001.5b** The Patron chooses delivery but isn't registered for payroll deduction (BR-5):
  1. The system tells the Patron that delivery needs payroll deduction, and offers pickup or registering.
  2. The Patron chooses pickup and the use case continues at UC-001.5c, or goes off to register: the order is dropped, nothing is kept, and the use case ends.

  *Example:* Eva, who joined this week and hasn't registered for payroll deduction, chooses delivery to room 4.12.
- **UC-001.5c** The Patron chooses pickup at the cafeteria instead of delivery:
  1. The Patron chooses a pickup time.
  2. The system shows the summary with no delivery charge, and payment at the counter (BR-7).
  3. The use case returns to step 7; in step 8 no delivery window place is taken.

  *Example:* Farid orders a sandwich for pickup at 12:15 and pays at the counter.
- **UC-001.7a** After seeing the summary, the Patron changes what they picked or adds another meal from the menu:
  1. The use case returns to step 3, keeping what the Patron already chose.

  *Example:* Grace sees the summary, then adds a second meal for a colleague.
- **UC-001.8a** The chosen delivery window filled up after it was offered:
  1. The system reserves and saves nothing, and tells the Patron the window is no longer available.
  2. The use case returns to step 4, where the Patron picks another window.

  *Example:* Hugo confirms delivery at 12:00–12:15, but another order took the last place in that window a second earlier.
- **UC-001.8b** An item ran out, or fell below the quantity asked for, after it was shown:
  1. The system reserves and saves nothing, and tells the Patron which item is short and how many are left.
  2. The Patron lowers the quantity to what's left; the use case returns to step 6.

  *Example:* Iris confirms 3 lasagnas, but only 1 is left.
- **UC-001.8c** The Cafeteria Inventory System doesn't answer, or reserves only some of the items:
  1. The system releases whatever was reserved, saves nothing, and tells the Patron the order didn't go through.
  2. The system keeps everything the Patron chose.
  3. The Patron tries again and the use case returns to step 7, or gives up and the use case ends.

  *Example:* Jon confirms his order; the inventory system reserves the salad but not the soup, then stops answering.
- **UC-001.8d** The date's cutoff passed while the Patron was ordering (BR-2):
  1. The system reserves and saves nothing, and tells the Patron the cutoff has passed.
  2. The Patron picks another date and the use case returns to step 2, or stops and the use case ends.

  *Example:* Kim starts ordering at 10:25 and confirms at 10:32, after the 10:30 cutoff.
- **UC-001.8e** Notifying the cafeteria staff fails after the order is accepted: `out-of-scope`, the order stands and the staff see accepted orders anyway.
- **`UC-001.*a`** The Patron cancels, or walks away without finishing:
  1. The system throws the draft away the same way in both cases; nothing is kept.
  2. The use case ends.

  *Example:* Leo picks two items, then closes the app to go to a meeting.

## Technology and data variations

- Step 1: the Patron picks a date, or keeps the default date (BR-1).
- Step 3: several of the same item, by giving a quantity.
- Step 5: delivery (the usual case) or pickup at the cafeteria (UC-001.5c).

## Related information

- **Frequency:** about 400 Patrons, roughly one order each per day; most orders arrive between 8:00 and 10:00.
- **Business rules:**
  - BR-1: If the Patron doesn't pick a date, the date is today when it is before today's cutoff, otherwise the next day the cafeteria is open.
  - BR-2: A date can be ordered for only if the cafeteria is open that day and its cutoff hasn't passed.
  - BR-3: Delivery windows are 15 minutes long and each has a limited number of places; only windows with room left are offered, and each accepted delivery takes one place.
  - BR-4: Pickup at the cafeteria is always offered next to delivery, even when windows are free.
  - BR-5: Delivery requires the Patron to be registered for payroll deduction, and is paid by payroll deduction. Pickup is open to anyone logged in and is paid at the counter.
  - BR-6: The quantity of an item can't exceed what the cafeteria can supply.
  - BR-7: The summary lists each item's price, the taxes, the delivery charge (none for pickup) and the total. The Patron chooses delivery or pickup before seeing it, so the total they confirm is the real one.
  - BR-8: Some items can't be delivered; they can only be picked up.
- **Open issues:**
  - What is the cutoff time for a date, and is it the same every day?
  - How many deliveries can one window take?
  - How are the delivery charge and the taxes calculated?
  - Which items can't be delivered, and who maintains that list?
  - Which pickup times are offered, and is pickup capacity limited?
  - Can a Patron place more than one order for the same date?
  - Changing an order, cancelling an accepted order and registering for payroll deduction are separate use cases, not yet written.
