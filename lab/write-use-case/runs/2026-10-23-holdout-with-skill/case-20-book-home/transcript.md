**Q1.** Step 5 says the reservation is either confirmed or needs further approval. I read that as two kinds of listing: some book instantly, others need the host to accept the request later. I'd end this use case at the hand-over: for an instant listing it ends with the booking confirmed; for the others it ends with the request sent and pending the host's answer, and the host's decision is the host's own use case ('Respond to a booking request'). Agreed? And how long does the host have to answer, and how does the guest hear the outcome?

**A1.** Mostly yes, with one correction: a booking can wait for confirmation for reasons other than a listing lacking instant booking. Besides the host's decision, other conditions can leave a booking waiting, and we haven't pinned down which ones. So the hand-over ends the use case for instant listings (booking confirmed) and for requests (pending the host's answer), but the other waiting conditions still need defining.

Not decided: how long the host has to answer. Use your recommendation.

The guest hears the outcome by notification. When they send a request, the system tells them it's with the host and that they'll be notified of the host's answer.

**Q2.** Boundary facts, to confirm in one go: (a) the guest is already signed in when they start (signing in and creating an account are separate); (b) payment goes through an outside payment provider, which charges the guest when the booking is confirmed (for a request, the payment is only authorised and charged if the host accepts); (c) the 'required information' at step 4 is the payment method and a message to the host; (d) searching for a listing is a separate task, so this use case starts with the guest on a listing. Correct, and what would you change?

**A2.** **(a) Yes.** The guest is already signed in when they start. Signing in and creating an account are not part of this.

**(b) Mostly yes, with one correction.** Payment goes through our payment provider, which charges the guest's payment method, and payment is taken only when the reservation is confirmed. For a request, nothing is charged when it is sent. Whether the payment is authorised at that point is not decided. Use your recommendation.

**(c) No.** The required information is a payment method, plus identity information when the host or we ask for it. A message to the host is not part of it.

**(d) Yes.** Finding the listing is a separate task. The guest starts on the listing by giving the dates and the number of guests.

**What I would change:** in (b), state that a request charges nothing when sent. In (c), replace "a message to the host" with "identity information when the host or we ask for it."

**Q3.** Stakeholders: I see the guest (a stay at a known total price, no surprise charges, no double charge), the host (no double booking of their dates, only stays that fit their rules, paid for confirmed stays), and the platform (its service fee collected, payment and identity data protected). Who should I add or drop, and what would each insist on?

**A3.** **Guest:** Close, but the wording differs. They want the full price, the policies and the terms shown before they commit, to be charged once, and to be charged only for a confirmed stay. Whatever happens, they should know at the end whether they have a confirmed reservation, a request with the host, or nothing.

**Host:** Partly right. The host wants only reservations that fit their calendar and limits, wants to hear about each one, and wants to decide on requests when the listing isn't open to instant booking. Not decided: whether the host insists on being paid for confirmed stays. Use your recommendation.

**Marketplace:** Use "marketplace" rather than "platform." It wants every confirmed reservation paid and never two bookings on the same listing for the same dates. Not decided: whether the service fee is a guarantee for this use case. Use your recommendation. Payment and identity data protection is not a booking guarantee here. Exporting or erasing that data belongs to the account privacy job.

**Add or drop:** The stakeholders are the guest, the host and the marketplace. Not decided: whether the payment provider should be a stakeholder. It charges the guest's payment method, but no guarantees are stated for it. Use your recommendation.

**Q4.** Guarantees. Minimal (however it ends): the guest is charged at most once and only for a confirmed reservation; the listing's dates are never held without a reservation; the guest knows whether they have a confirmed reservation, a request with the host, or nothing. Success (instant): the reservation is confirmed for the dates and guests, the dates are blocked on the listing's calendar, the guest is charged the total once, and both guest and host are notified. Success (request): the request is recorded with the host, nothing is charged, the host is notified, and the guest is told they will be notified of the host's answer. Agreed? Anything to add or remove?

**A4.** Mostly agreed, with three gaps:

- **Minimal:** Agreed. The guest is charged at most once and only for a confirmed reservation, the guest always knows whether they have a confirmed reservation, a request, or nothing, and failed attempts reserve and charge nothing.
- **Instant success:** Agreed for the reservation, the dates and guests, the single total charge, and the host being notified. The guest is shown the confirmation and stay details on screen, not sent a notification. Not decided: whether the dates are explicitly blocked on the listing's calendar. Use your recommendation.
- **Request success:** Agreed. The request goes to the host, nothing is charged, the host is notified, and the guest is told they'll hear the host's answer.

**Add:** Not decided: whether a pending request holds the dates. That bears on the minimal guarantee that dates are never held without a reservation. Use your recommendation.

**Remove:** Nothing.

**Q5.** Here is the main scenario I propose: 1. (actor) The guest gives the stay dates and the number of guests on the listing. 2. (system) The system presents the total price with its breakdown, the house rules and the cancellation policy for that stay. 3. (actor) The guest gives a payment method, and any identity information asked for, and submits the booking. 4. (system, wait: a few seconds) The system charges the total through the payment provider, confirms the reservation, blocks the dates and notifies the host, and shows the guest the confirmation. The request path (listing not open to instant booking) would be an alternative at step 4. Which rules does step 1 enforce: are there per-listing limits like a maximum number of guests or a minimum and maximum number of nights? Anything wrong in the steps?

**A5.** **Which rules step 1 enforces:** The dates must be free and the party must fit the listing. If either fails, the system says which dates aren't free or how many guests the listing takes. The listing's calendar and limits are the host's, and the maximum number of guests is one of them.

Not decided: minimum and maximum nights. Use your recommendation.

**What's wrong in the steps:**

- **Step 3** should also say that submitting means accepting the price, the policies and the reservation terms.
- **Step 4 order:** You charge before confirming. Payment is taken only when the reservation is confirmed, so confirm first, then charge. If the charge fails, the reservation isn't confirmed.
- **Step 4 is missing a re-check.** The dates can be booked or blocked between step 2 and submit. If so, nothing is charged or confirmed, and the system says which dates are gone.
- **Step 4 is missing duplicate submits.** A double submit must produce one reservation and one charge.
- **Step 4 is missing failures.** If information is missing or the payment is declined, nothing is reserved or charged, and the system says what's missing or that the payment was declined. The guest can fix it and submit again, or stop. If the payment provider doesn't answer, or the charge and reservation don't both succeed, any charge is reversed, nothing is confirmed, and the guest keeps what they entered.

**The request path at step 4:** Yes, that's the right alternative. If the listing isn't open to instant booking, the guest sends a request with the same information. Nothing is charged, and the system tells them the request is with the host and that they'll be notified of the answer.

**Q6.** Conditions so far: dates not free or party too large (step 1); information missing or payment declined (step 3); double submit (step 3); dates taken between step 2 and submit (step 4); payment provider not answering, or charge and reservation not both succeeding (step 4); listing not open to instant booking (step 4, the request path). Other candidates I'd add only if real: the guest already has a reservation overlapping those dates; the guest is not allowed to book this listing (for example the host requires verified identity and the guest declines to give it); the price changes between step 2 and submit; the guest gives up before submitting. Which of these are real, and what else can go wrong?

**A6.** **Already in your list, and real:**
- Dates not free or party too large (step 1)
- Information missing or payment declined (step 3)
- Double submit (step 3)
- Dates taken or blocked between showing and submit (step 4)
- Payment provider not answering, or charge and reservation not both succeeding (step 4)
- Listing not open to instant booking (request path)

**Candidates you proposed:**
- **Guest already has an overlapping reservation:** Not decided: whether this can happen or what happens then. Use your recommendation.
- **Guest not allowed to book, for example declining identity verification:** Yes, real. If the host or we ask for identity and the guest doesn't give it, that's missing information: nothing is reserved or charged, the system says what's missing, and the guest either supplies it and submits again or stops.
- **Price changes between step 2 and submit:** Not decided: whether the price can change, and what happens if it does. Use your recommendation.
- **Guest gives up before submitting:** Yes, real. Nothing is reserved or charged.

**Other things that can go wrong:**
- A booking can be left waiting for confirmation for reasons other than the host's decision. Not decided: which reasons. Use your recommendation.
- The listing being removed while someone is booking it is out of scope. It belongs to the host's listing-removal use case.

**Q7.** Handling at submit, to confirm: (a) dates taken meanwhile: nothing charged or confirmed, the system says which dates are gone and keeps the payment method and party; the guest picks other dates (back to step 1) or stops. (b) provider not answering or charge and reservation not both succeeding: any charge reversed, nothing confirmed, the guest keeps what they entered and can submit again (back to step 3) or stop. (c) double submit: the second submit is matched to the first, and the guest sees the single reservation or request it produced. (d) the request path also re-checks the dates and handles (a) and (b) the same way, and a pending request does not hold the dates. Correct?

**A7.** (a) Partly. Nothing is charged or confirmed, and the system says which dates are gone. The guest then picks other dates or another listing. Not decided: whether the payment method and party are kept, and whether they can stop here. Use your recommendation.

(b) Mostly. Any charge is reversed, nothing is confirmed, the system says the booking wasn't made and keeps what they entered, and they can try again or stop. Not decided: which step they return to when they try again. Use your recommendation.

(c) Yes. A double submit is handled once, so there is one reservation and one charge, and the guest learns the outcome.

(d) Nothing is charged on the request path, and the host decides on the request. Not decided: whether the request path re-checks the dates. Use your recommendation. Not decided: whether a pending request holds the dates. Use your recommendation. Not decided: how a payment or provider failure is handled on the request path. Use your recommendation.

**Q8.** Last one: how often does this happen? I'd write the frequency as 'several times a year per guest; continuous across the marketplace', unless you have a figure.

**A8.** Yes. A typical guest books a few stays a year, and it happens all the time across the marketplace, since booking is the main thing guests do here. I'd drop "several" and say "a few", since that's the wording we use.

