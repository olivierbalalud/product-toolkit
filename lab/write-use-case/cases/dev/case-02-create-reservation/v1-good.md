- **ID / Name:** UC-001 — Create Reservation
- **Scope:** Property Management System (black box) · **Level:** User goal (!)
- **Primary actor:** Front Desk Clerk
- **Supporting actor:** Payment Service
- **Stakeholders & interests:**
  - Guest — gets the room type and dates asked for, at the quoted price, with a confirmation.
  - Front Desk Clerk — books quickly while the guest waits or is on the phone.
  - Revenue manager — no overbooking; deposit policy enforced.
  - Finance — no payment taken without a matching reservation.
- **Trigger:** A guest asks the front desk to book a room.
- **Preconditions:** Clerk is authenticated; room inventory and rates are configured.
- **Minimal guarantees:** No partial reservation is stored; room availability is unchanged; no payment is charged without a stored reservation.
- **Success guarantees:** Reservation stored with status *Confirmed*; availability updated for the reserved dates; confirmation sent to the guest.

**Main success scenario**
1. Clerk starts a new reservation and enters the guest's contact details.
2. Clerk enters the check-in and check-out dates.
3. System presents the room types available for those dates, with rates.
4. Clerk selects the room type the guest wants.
5. System presents the total price of the stay.
6. Clerk confirms the reservation with the guest's agreement.
7. System records the reservation, updates availability, gives the Clerk a confirmation number, and sends the guest a confirmation.

**Extensions**
- 1a. Contact details match an existing guest: System presents the existing profile; Clerk confirms or updates it; continue at step 2.
- 2a. Dates break a booking rule (BR-001, BR-002): System states the rule; Clerk corrects the dates (continue at step 2) or use case ends.
- 3a. No room available for those dates: System says so; Clerk changes the dates (continue at step 2) or use case ends.
- 5a. Guest declines the price: use case ends.
- 6a. Stay requires a deposit (BR-003): System requests payment details; Clerk provides them; System obtains authorization from the Payment Service; continue at step 7.
  - 6a1. Payment is declined: System says so; Clerk tries another payment method (continue at 6a) or use case ends.

**Business rules:** BR-001 minimum stay one night · BR-002 no booking more than 365 days ahead · BR-003 stays of 3+ nights require a 50% deposit.
