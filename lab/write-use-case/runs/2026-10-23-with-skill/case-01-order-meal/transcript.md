**Q1.** Boundary first. I'd write this as: primary actor the Patron (an employee), goal 'Order a meal for delivery', scope the cafeteria ordering system, precondition 'the Patron is signed in'. The system accepts the order itself, so the use case ends once the order is accepted and the confirmation sent; preparing and delivering the meal is the cafeteria's own work, a separate use case. Agreed, and is anything else (e.g. changing or cancelling an order later) a separate task?

**A1.** **Yes, with three corrections:**

- **Goal:** the goal is one meal order for a given date. Delivery is the usual case and pickup is a variant, so the goal isn't specifically "for delivery."
- **Precondition:** the Patron must be signed in. Being registered for payroll deduction is not assumed. It only matters when delivery is chosen.
- **Ending:** the use case ends once the order is accepted. The order is saved, the inventory shows the items as taken, a delivery window is used up, and both the Patron and the staff are told.

**Separate tasks:** yes. Changing an order, cancelling an accepted order, and registering for payroll deduction are separate tasks, not part of this one. Changing or cancelling a draft before it's accepted is part of this use case.

**Not decided:** whether preparing and delivering the meal is a separate use case. Use your recommendation.

**Q2.** Supporting actors. I'd list: the payroll system (for payroll deduction) and a card payment service (for paying by card), with the cafeteria staff as the people told of the order. Which payment methods exist, and which of these are outside systems we call rather than build?

**A2.** **Payment methods:** Two exist. Delivery is paid by payroll deduction. Pickup is paid at the counter, with no delivery charge. Not decided: whether a card payment service exists or is needed. Use your recommendation.

**Outside systems we call rather than build:** The Cafeteria Inventory System is one, since we call it to reserve items and don't build it. The payroll system is also outside, since we ask it for deductions the Patron authorized. A card payment service isn't mentioned in the facts, so it's not decided.

**Cafeteria staff:** Yes, they are told about every accepted order. They are notified, not a system we call.

**Q3.** Stakeholders. I see: the Patron (gets the meal they chose at the time and place they chose, and pays exactly the total shown), the cafeteria staff (hear of every accepted order, and only get orders they can supply), and the payroll office (deducts only what the Patron authorized). Who else has a stake, and what would you add or drop?

**A3.** Add **cafeteria management**. They want inventory to stay accurate and never to promise more deliveries than a window can take.

Your other three are right, with two details to fix:
- **Patron:** correct.
- **Cafeteria staff:** they want complete, unambiguous orders early enough to prepare them. The "only orders they can supply" part belongs to management.
- **Payroll:** correct, they want only deductions the Patron authorized.

Drop nothing.

**Q4.** Minimal guarantee, true however it ends. I'd write: no order is half-accepted; no items or delivery window stay reserved without an accepted order, and no deduction is requested without one. Agreed, or does anything else hold on every exit (for example, a draft is kept)?

**A4.** **Partly.** Your first two clauses match the facts, with one caveat:

- **No half-accepted order:** Agreed. If the inventory system fails or only part reserves, the system releases what was reserved and saves nothing. Once accepted, the order is saved, the inventory is updated, the delivery slot is taken, and the Patron and staff are told. The caveat is that if telling the staff fails after acceptance, the order stands and that case is out of scope.
- **No items or window reserved without an accepted order:** Agreed. Nothing is kept until the order is accepted, however the attempt ends.
- **No deduction requested without an accepted order:** Not decided: that payroll is never asked without an accepted order. Use your recommendation. The facts only say payroll is asked for deductions the Patron actually authorized.

**Something else holds on every exit:** no draft is kept. If the Patron cancels or walks away, the draft is thrown away the same way, and nothing is kept.

**Q5.** Main scenario. I'd rewrite it as: 1. The Patron chooses a date. 2. The system presents that day's menu. 3. The Patron chooses the items and quantities. 4. The Patron chooses a delivery window and a location. 5. The system presents the total with taxes and the delivery charge. 6. The Patron confirms the order and authorizes the payroll deduction. 7. (a few seconds) The system reserves the items with the Cafeteria Inventory System, takes the delivery window, saves the order, and tells the Patron and the staff. I moved the window and location before the total, since the delivery charge depends on delivery, so the Patron confirms once. Pickup would be an alternative at step 4. Agreed?

**A5.** Mostly yes. The order you give matches the facts: the Patron chooses delivery or pickup before seeing the total, and delivery means a window, a place and payroll payment. Corrections:

- **Step 1:** If the Patron doesn't pick a date, it's today when they're before the cutoff, otherwise the next day the cafeteria is open.
- **Step 4:** Pickup is always offered next to delivery. Pickup means choosing a pickup time and paying at the counter, with no delivery charge.
- **Step 4, delivery:** Choosing delivery without payroll registration is a failure case. Tell the Patron delivery needs it, and offer pickup or registering. If they go off to register, this order is dropped and they order again afterwards.
- **Step 5:** The summary lists each item's price, the taxes, the delivery charge and the total. After seeing it, the Patron can go back and change items or add another meal from the menu. Your rewrite leaves that out.
- **Step 6:** The facts say payroll is asked only for deductions the Patron authorized, but they don't say where that authorization sits in the flow. Your placement at confirmation is a reasonable reading.
- **Step 7:** Drop "(a few seconds)". Everything the system does here is immediate, and the Patron never waits on it.

**Q6.** Business rules. I see: BR-1 a same-day order must be placed before the daily cutoff; BR-2 each delivery window takes a limited number of deliveries; BR-3 delivery requires payroll deduction registration. What is the cutoff time, what is a window's capacity, and is there any other rule (for example how far ahead a date can be chosen, or a limit on meals or spend per order)?

**A6.** **BR-1:** Yes. A same-day order must be placed before the cutoff. Otherwise the order goes to the next day the cafeteria is open. Cutoff time: Not decided: cutoff time. Use your recommendation.

**BR-2:** Yes. A delivery window takes deliveries only while it has room, and full windows aren't offered. Window capacity: Not decided: window capacity. Use your recommendation.

**BR-3:** Yes. Delivery requires payroll deduction registration. Pickup needs only a logged-in Patron.

**Other rules:**
- A date can't be ordered for if the cafeteria is closed that day.
- A Patron can't order more of an item than the cafeteria can supply.
- Items that can't be delivered can't be in a delivery order. The Patron must remove them or switch to pickup.
- How far ahead a date can be chosen: Not decided: how far ahead a date can be chosen. Use your recommendation.
- Limit on meals or spend per order: Not decided: limit on meals or spend per order. Use your recommendation.

**Q7.** Payroll. I'd have the system only record the Patron's authorization with the accepted order at step 7, and not call the payroll system during this use case; the actual deduction is passed to payroll later, outside this use case. So payroll isn't called in this use case. Agreed?

**A7.** Not decided: whether payroll is called in this use case, and whether the authorization is recorded with the accepted order at step 7. Use your recommendation.

**Q8.** Conditions at the Patron's steps. I see: at step 1, a date when the cafeteria is closed, or today after the cutoff; at step 3, a quantity above what the cafeteria can supply; at step 4, delivery without payroll registration, and items in the order that can't be delivered; at any step before confirming, the Patron gives up. Could the Patron already have an order for that date, and is that a problem? What else can go wrong at these steps?

**A8.** Yes, your reading matches, with two details. For payroll, the Patron is offered pickup or registering, and if they go off to register, this order is dropped and they order again afterwards. For giving up, the draft is thrown away and nothing is kept, whether they cancel or walk away.

**Existing order for that date:** Not decided: whether a Patron may already have an order for that date, and whether that is a problem. Use your recommendation.

**Other things that can go wrong at these steps:**
- **Date:** the cutoff can pass while the Patron is still ordering. Nothing is reserved or saved. We tell them, and they pick another date or stop.
- **Quantity:** an item can run out between being shown and the order going through. Nothing is reserved or saved. We say what's gone, and they lower the quantity to what's left.
- **Delivery window:** if no window is left for the date, we offer only pickup. If the chosen window fills at the last moment, nothing is reserved or saved, and they pick another window or lower the quantity.
- **Items:** if an order includes an item that can't be delivered and they choose delivery, we name it, and they either remove it or switch to pickup.
- **Confirmation:** the inventory system may not answer, or only some items may be reserved. We release whatever was reserved, save nothing, and keep their choices so they can retry or give up.

**Q9.** Handling at steps 1 and 3. I'll handle these as follows: a closed date: the system says the cafeteria is closed that day and proposes the next open day; the Patron accepts it or picks another date. Today after the cutoff: the system says the cutoff has passed and proposes the next open day, same choice. A quantity above supply: the system says how many are available, and the Patron lowers the quantity or drops the item. Correct?

**A9.** Partly. Here is each part against what's decided:

- **Closed date:** Yes, the system tells the Patron the cafeteria is closed that day, and they pick another date or stop. Not decided: whether the system proposes the next open day. Use your recommendation.
- **Cutoff passed today:** Yes, the system tells them why, and they pick another date or stop. Not decided: whether the system proposes the next open day. Use your recommendation.
- **Quantity above supply:** Yes, the system tells them the most it can supply, and they change the quantity to that. Not decided: whether they can drop the item instead. Use your recommendation.

**Q10.** How often does this happen: roughly how many meal orders a day, and is there a peak?

**A10.** About 400 people use it, roughly one order each per day, so about 400 orders a day. Most orders come in between 8:00 and 10:00, which is the peak.

**Q11.** Privacy. The order holds personal data (the Patron's name, delivery location, order history, payroll authorization). I'd mark the export or erasure request as deferred to a separate account privacy use case, not handled here. Agreed?

**A11.** Yes, with one correction: the facts don't say the Patron's name, delivery location, order history or payroll authorization are personal data, and they don't mention a privacy use case. They only say that exporting or erasing the Patron's order history is a separate use case we haven't written yet, so it isn't handled here. Deferring it to that use case is correct.

