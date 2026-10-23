**Q1.** Who is the Patron and what system is this? Who else has a stake in the order (cafeteria staff, payroll, delivery staff)?

**A1.** The Patron is an employee who is logged in and orders a meal. The system is the Cafeteria Ordering System, seen from the outside. The Cafeteria Inventory System is a separate system it calls to reserve items, and we don't build it.

Other stakeholders:
- **Cafeteria staff** want complete, unambiguous orders early enough to prepare them. They are told about every accepted order.
- **Cafeteria management** wants inventory to stay accurate and never to promise more deliveries than a window can take.
- **Payroll** wants to be asked only for deductions the Patron actually authorized.
- **Delivery staff:** Not decided: whether delivery staff have a stake. Use your recommendation.

**Q2.** What payment methods are offered (payroll deduction, card, other)? Are there external payment systems the ordering system calls, and are there limits on payroll deductions?

**A2.** - **Payment methods:** Delivery is paid by payroll deduction. Pickup is paid at the counter, with no delivery charge. Card and other methods: Not decided. Use your recommendation.
- **External payment systems:** The ordering system asks payroll for the deduction, and it calls the Cafeteria Inventory System to reserve items. Any other payment system: Not decided. Use your recommendation.
- **Limits on payroll deductions:** Not decided. Use your recommendation. The only requirement is that the Patron is registered for payroll deduction and has authorized the deduction.

**Q3.** How far ahead can a Patron order, and is there an ordering cutoff before a delivery window? How are delivery windows defined, and what limits how many orders a window can take?

**A3.** **How far ahead can a Patron order?** Not decided: how far ahead a Patron can order. Use your recommendation.

**Is there a cutoff before a delivery window?** Yes, but it applies to the whole date, not to a single window. Once the cutoff for a date has passed, that date can't be ordered for. Not decided: the cutoff time. Use your recommendation.

**How are delivery windows defined?** Each window is 15 minutes long, and only windows with room left are offered. Not decided: when the windows start. Use your recommendation.

**What limits how many orders a window can take?** Not decided: how many orders a window can take. Use your recommendation.

**Q4.** What happens if an item runs out between when the Patron selects it and when the order is placed (the inventory reservation fails for some or all items)? And what if the Cafeteria Inventory System is down?

**A4.** **Item runs out at the last moment (some or all items fail to reserve):** Nothing is reserved or saved. We tell the Patron what's gone and they either pick another delivery window or lower the quantity to what's left.

**Inventory system is down, or only some items get reserved:** We release whatever was reserved, save nothing, and tell the Patron the order didn't go through. We keep everything they chose so they can try again or give up.

**Q5.** When is the payroll deduction requested: at order acceptance, or later? What happens if the Patron is not registered for payroll deduction, or payroll refuses or is unreachable?

**A5.** - **When the deduction is requested:** Not decided: when the payroll deduction is requested (at order acceptance or later). Use your recommendation.
- **Patron not registered for payroll deduction:** We tell them delivery needs it and offer pickup or registering. If they go off to register, this order is dropped and they order again afterwards.
- **Payroll refuses the deduction:** Not decided: what happens if payroll refuses. Use your recommendation.
- **Payroll unreachable:** Not decided: what happens if payroll is unreachable. Use your recommendation.

**Q6.** What happens if the chosen delivery window fills up (another Patron takes the last place) between choosing it and placing the order? And what if the cutoff for the date passes while the Patron is still ordering?

**A6.** **Window filled:** Yes. Nothing is reserved or saved. We tell the Patron what's gone, and they either pick another window or lower the quantity to what's left.

**Cutoff passes:** Nothing is reserved or saved. We tell the Patron, and they pick another date or stop.

**Q7.** What locations can be chosen for delivery? Any limits on order size (items, quantity, total amount), or on how many orders a Patron can have per day or per window?

**A7.** **Delivery locations:** Not decided: which places can be chosen for delivery. Use your recommendation.

**Order size:** There is no fixed cap on items or quantity. The only limit is stock: if a Patron asks for more of an item than the cafeteria can supply, they're told the most available and change the quantity.

**Total amount:** Not decided: a maximum order total. Use your recommendation.

**Orders per day:** Not decided: how many orders a Patron can place per day. Use your recommendation.

**Orders per window:** No per-Patron limit is stated. Not decided: how many people a delivery window can hold beyond "it has room left or it's full." Use your recommendation.

**Q8.** How is the cafeteria notified of an accepted order, and what if that notification fails? How is the Patron's order confirmation delivered (in the app, email)?

**A8.** **Cafeteria notification:** The staff are told about every accepted order. Not decided: how they are told. Use your recommendation.

**If notification fails:** That's out of scope. The order stands, and the staff see accepted orders anyway.

**Patron confirmation:** The Patron is told when the order is accepted. Not decided: the channel, whether in the app, by email, or both. Use your recommendation.

**Q9.** What if the Patron abandons partway through (closes the app or the session expires)? Is anything kept, such as a saved cart? And what if a menu item or price changes while the Patron is ordering?

**A9.** **Abandoning:** Nothing is kept. If the Patron closes the app, the session expires, or they walk away, the draft is thrown away and nothing is saved, so there is no saved cart. Nothing is reserved or saved until the order is accepted.

**Menu or price changes while ordering:** Not decided: what happens if a menu item or price changes while the Patron is ordering. Use your recommendation.

**Q10.** If a Patron submits the same order twice (double submit or retry after an error), should the system detect the duplicate? And can a Patron order meals for someone else, or for several dates in one go?

**A10.** **Duplicate submits:** Not decided: whether the system detects a duplicate. Use your recommendation. Retries after a failed attempt are covered: nothing is reserved or saved, and the Patron keeps their choices to try again.

**Ordering for someone else:** Not decided: whether a Patron can order for another person. Use your recommendation.

**Several dates in one go:** No. An order is for one date, and the Patron picks that date (defaulting to today or the next open day).

**Q11.** Roughly how often is this used (orders per day)? And should a Patron be able to export or erase their order history and personal data?

**A11.** Roughly 400 orders per day: about 400 people use it, with roughly one order each per day, and most come in between 8:00 and 10:00.

Export or erase of order history and personal data is not handled here. It is a separate use case we haven't written yet.

**Q12.** Does the date's menu ever come back empty or the date have no open windows (holiday, closed cafeteria)? What does the Patron see then?

**A12.** **Menu coming back empty:** Not decided: whether the menu for a date can come back empty. Use your recommendation.

**Closed cafeteria (holiday or otherwise):** Yes. The date can't be ordered for. The Patron is told why and can pick another date or stop.

**No open delivery windows:** The Patron is not told the date is closed. Only the delivery windows are full, so they're offered pickup only.

**Q13.** How is the delivery charge set (flat per order, by location, by size)? And at step 3, if the Patron doesn't accept the total, can they go back and change items?

**A13.** **Delivery charge:** Not decided: how the delivery charge is set (flat, by location, or by size). Use your recommendation. The summary shows the delivery charge as its own line, and pickup has no delivery charge.

**Going back to change items:** Yes. After seeing the summary, the Patron can go back and change what they picked, or add another meal from the menu.

