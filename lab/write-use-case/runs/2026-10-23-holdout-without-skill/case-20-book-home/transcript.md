**Q1.** Who exactly is the guest at the start: must they already have a signed-in account, and is anything else (verified identity, saved payment method) assumed before they open the listing, or does the booking flow handle sign-in and verification itself?

**A1.** Yes, they must already be signed in; the flow doesn't handle sign-in. Nothing else is assumed up front. They can use a payment method already on their account or add a new one during booking. Identity information is requested only when the host or we ask for it, and if it's missing, the system says what's missing.

**Q2.** Step 5 says the system either confirms or says approval is needed. What decides which: is it a per-listing setting (instant booking versus request to book), and when it's a request, how long does the host have to answer and how does the guest learn the outcome?

**A2.** **What decides:** Whether the listing is set to instant booking, which is the host's setting. The guest also has to meet the host's requirements for instant booking. If either fails, the system sends a reservation request instead. Other conditions can also leave a booking waiting for confirmation, but we haven't pinned down which.

**Host's time to answer:** Not decided. Use your recommendation.

**How the guest learns the outcome:** The guest is notified of the host's answer. Nothing is charged at the request stage, and the system tells the guest the request is with the host.

**Q3.** For an instant booking, when is the guest charged: in full at submission, partly now and partly later, or only a hold? And for a request, is the payment method validated or a hold placed at submission, then charged when the host accepts?

**A3.** **Instant booking:** The guest is charged the full total in one payment, at submission, as part of confirming the reservation. It isn't split, and there's no hold. Payment is taken only when the reservation is confirmed.

**Request:** Nothing is charged at submission. The charge happens when the host accepts and the reservation is confirmed. Not decided: whether the payment method is validated or a hold is placed at submission. Use your recommendation.

**Q4.** If the dates are taken by someone else, or the host blocks them, between the guest choosing them and submitting, what should happen? Is anything held for the guest while they fill in the checkout?

**A4.** If the dates are gone when the guest submits, nothing is charged or confirmed. The system says which dates are no longer free, and the guest picks other dates or another listing.

Nothing is held for the guest during checkout. Dates aren't reserved until submit, and if the guest leaves before submitting, nothing is reserved or charged.

**Q5.** What limits apply when the guest picks dates and guests (minimum or maximum nights, maximum guests, advance notice, check-in day rules, pets or children), and what does the system do when a choice breaks one?

**A5.** **Maximum guests:** The listing takes a set number of guests. If the party is bigger, the system says how many the listing takes, and the guest changes the party or picks another listing.

**Dates already booked or blocked by the host:** The system says which dates aren't free, and the guest changes the dates or picks another listing.

Not decided: minimum or maximum nights. Use your recommendation.

Not decided: advance notice. Use your recommendation.

Not decided: check-in day rules. Use your recommendation.

Not decided: pets. Use your recommendation.

Not decided: children. Use your recommendation.

**Q6.** If the price or the policies change after the guest reviewed them but before they submit (host edits the nightly rate, fees or cancellation policy), what happens at submission?

**A6.** Not decided: what happens at submission when the nightly rate, fees or cancellation policy change after the guest reviewed them. Use your recommendation.

**Q7.** Step 4 says the guest provides the required information. What exactly is required (message to the host, trip purpose, guest names, phone, ID), and must the guest explicitly accept the house rules and cancellation policy?

**A7.** **Required from the guest:**
- **Payment method:** required. They can confirm one already on their account or add a new one.
- **Identity information:** required only when the host or the marketplace asks for it.
- **Message to host, trip purpose, guest names, phone:** Not decided: message to host, trip purpose, guest names, phone. Use your recommendation.

**Acceptance:** Yes, but not as a separate step. Submitting the booking means accepting the price, the policies (including the cancellation policy and house rules) and the reservation terms.

**Q8.** If the payment is declined, needs extra authentication from the bank (e.g. 3-D Secure), or the payment provider doesn't respond, what should the guest see and what state is the booking left in?

**A8.** - **Declined payment:** Nothing is reserved or charged. The guest sees that the payment method was declined. They can fix it and submit again, or stop.
- **Payment provider doesn't respond:** Any charge is reversed and nothing is confirmed. The guest sees that the booking wasn't made. Their entered details are kept, and they can try again or stop.
- **Extra bank authentication (3-D Secure):** Not decided: what the guest sees and what state the booking is left in. Use your recommendation.

**Q9.** What should prevent duplicates: if the guest submits twice (double-click, retry after a timeout), or already has an overlapping reservation or pending request for the same listing, what happens?

**A9.** **Double submit:** Yes. The booking is handled once, so the guest gets one reservation and one charge.

**Overlapping reservation:** If the dates are already booked or blocked by the host, the system says which dates aren't free, and the guest changes the dates or party, or picks another listing.

**Overlapping pending request:** Not decided: whether a pending request holds the dates against other bookings. Use your recommendation.

**Q10.** Can a guest be barred from booking at all (suspended account, blocked by this host, under the minimum age), and what are the host's instant-booking requirements a guest might fail? What does the guest see in each case?

**A10.** **Barred from booking:**
- Suspended account: Not decided. Use your recommendation.
- Blocked by this host: Not decided. Use your recommendation.
- Under the minimum age: Not decided. Use your recommendation.

**Host's instant-booking requirements a guest might fail:** Yes, a guest can fail them. The listing then can't be booked instantly. The specific requirements are not decided. Use your recommendation.

**What the guest sees when they fail instant booking:** They send a reservation request instead, with the same information. Nothing is charged. The system tells them the request is with the host and that they'll be notified of the host's answer.

**What the guest sees when barred:** Not decided. Use your recommendation.

**Q11.** When identity information is required (step 4), how is it checked: is verification instant, or does it take minutes or days, and does the booking wait for it or proceed?

**A11.** **Verification speed:** Not decided: how long identity verification takes (instant, minutes or days). Use your recommendation.

**Wait or proceed:** The booking doesn't proceed without it. If identity information is missing, nothing is reserved or charged. The system says what's missing, and the guest either supplies it and submits again or stops.

**Q12.** Who else must be told when the reservation is confirmed or the request sent (host, guest by email or push), and what does the confirmation give the guest (confirmation code, address, check-in details)?

**A12.** - **Host:** Yes. The host is told about every reservation. For a request, the host is the one who decides it, so they are told about it too.
- **Guest by email or push:** Not decided: whether the guest is told by email or push. Use your recommendation. For a request, the system tells the guest on screen that it is with the host and that they'll be notified of the answer.
- **What the guest gets on confirmation:** They see a confirmation with the stay details. Not decided: whether it includes a confirmation code, the address, or check-in details. Use your recommendation.

**Q13.** Can the guest ask to export or erase the personal data captured here (payment details, identity info, messages), and is that handled in this flow or elsewhere? Also, roughly how often does this use case run, and is there anything in scope I haven't asked about, like coupons, gift cards, currencies or long-stay discounts?

**A13.** **Export or erase of identity, payment and stay data:** Handled elsewhere. It's the account privacy job, not booking.

**Messages:** Not decided: whether messages are covered by the privacy job or this flow. Use your recommendation.

**How often it runs:** All the time. Booking is the main thing guests do on the marketplace, and a typical guest books a few stays a year.

**Other scope (coupons, gift cards, currencies, long-stay discounts):** Not decided: whether these are in scope. Use your recommendation.

