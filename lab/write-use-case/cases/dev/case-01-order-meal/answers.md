# Answers: Order a meal

## Actor, goal and scope

- The person ordering is an employee; we call them the Patron.
- What we're designing is the Cafeteria Ordering System, seen from the outside.
- The goal is one meal order for a given date, done in one go.
- The only thing we assume beforehand is that the Patron is logged in. Being registered for payroll deduction is not assumed; it only matters for delivery.
- The Cafeteria Inventory System is a separate system we call to reserve the items; we don't build it.
- The cafeteria staff are told about every accepted order.
- About 400 people use it, roughly one order each per day, and most orders come in between 8:00 and 10:00.
- Changing an order, cancelling an accepted order and registering for payroll deduction are separate tasks, not part of this one.

## Stakeholders and guarantees

- The Patron wants the meal they chose, at the place and time they chose, without queuing, and to be charged the right amount.
- The cafeteria staff want complete, unambiguous orders early enough to prepare them.
- Cafeteria management wants the inventory to stay accurate and never to promise more deliveries than a window can take.
- Payroll wants to be asked only for deductions the Patron actually authorized.
- Until the order is accepted, nothing is kept: no order saved, no item reserved, no delivery slot used up, however the attempt ends.
- Once it's accepted, the order is saved as accepted, the inventory shows the items as taken, a delivery takes one place in its window, and both the Patron and the staff are told.

## Main scenario

- If the Patron doesn't pick a date, it's today when they're before the cutoff, otherwise the next day the cafeteria is open.
- The menu for a date includes the daily special.
- Delivery windows are 15 minutes long, and only windows with room left are offered.
- Pickup at the cafeteria is always offered next to delivery, even when windows are free.
- The Patron chooses delivery or pickup before seeing the total, so the total they confirm is the real one.
- Delivery means a window, a place to deliver to, and payment by payroll deduction.
- Pickup means choosing a pickup time and paying at the counter, with no delivery charge.
- The summary lists each item's price, the taxes, the delivery charge and the total.
- The usual case is delivery; pickup is the variant.
- A Patron can order several of the same item by giving a quantity.
- After seeing the summary, the Patron can go back and change what they picked, or add another meal from the menu.

## What can go wrong

- The date can't be ordered for: the cutoff has passed, or the cafeteria is closed that day.
- The Patron asks for more of an item than the cafeteria can supply.
- Every delivery window for the date is already full.
- Some items can't be delivered at all, and the Patron chooses delivery with one of them in the order.
- The Patron chooses delivery without being registered for payroll deduction. That's the only permission that matters; anyone logged in can order for pickup.
- Between being shown and the order going through, the chosen window can fill up or an item can run out, because other people are ordering at the same time.
- The inventory system may not answer, or only part of the items may get reserved.
- The cutoff can pass while the Patron is still ordering.
- The Patron can cancel, or just walk away without finishing.

## How each is handled

- Date can't be ordered for: we tell them why, and they pick another date or stop.
- Too many of an item: we tell them the most we can supply and they change the quantity.
- No delivery window left: we offer only pickup.
- Item that can't be delivered: we name it, and they either take it out or switch to pickup.
- Not registered for payroll deduction: we tell them delivery needs it and offer pickup or registering. If they go off to register, this order is dropped and they order again afterwards.
- Window filled or item ran out at the last moment: nothing is reserved or saved, we say what's gone, and they pick another window, or lower the quantity to what's left.
- Inventory system down or only part reserved: we release whatever was reserved, save nothing, tell them the order didn't go through, and keep everything they chose so they can try again or give up.
- Cutoff passed at the last moment: nothing is reserved or saved, we tell them, and they pick another date or stop.
- Cancelled or walked away: the draft is thrown away the same way in both cases, and nothing is kept.

## Durations

- Everything the system does here is immediate; the Patron never waits on it.

## Out of scope

- If telling the staff fails after the order is accepted, we don't handle it: the order stands, and the staff see accepted orders anyway.
- A Patron asking to export or erase their order history is a separate use case we haven't written yet, so it's not handled here.
