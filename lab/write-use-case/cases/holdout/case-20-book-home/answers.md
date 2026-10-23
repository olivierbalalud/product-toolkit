# Answers: book a home for a trip

## Actor, goal and scope

- The system is our accommodation booking marketplace.
- They start once they've found a listing that suits their trip and decide to book it; finding the listing isn't part of this.
- Before they start they're already signed in.
- Payment goes through our payment provider, which charges the guest's payment method.
- The host is told about every reservation, and decides on the ones that can't be booked instantly.
- It happens all the time: booking is the main thing guests do on the marketplace, and a typical guest books a few stays a year.
- The host answering a request, cancelling a reservation, creating a listing and checking in are separate things, not part of this.

## Stakeholders and guarantees

- The guest wants a home for the trip's dates and party, wants to know the full price, the policies and the terms before committing, and wants to be charged once, and only for a stay that's confirmed.
- The host wants only reservations that fit the listing's calendar and limits, wants to hear about each one, and wants to decide on requests when the listing isn't open to instant booking.
- We, the marketplace, want every confirmed reservation paid and never two bookings on the same listing for the same dates.
- Whatever happens, the guest is never charged for something that isn't confirmed, and never charged twice for the same reservation.
- Whatever happens, the guest knows at the end whether they have a confirmed reservation, a request with the host, or nothing.
- When it works: the reservation is confirmed for their dates and party, they've paid the total they were shown, they can see the stay details, and the host knows about it.

## Main scenario

- Opening the listing isn't a step; they start by giving the dates and the number of guests.
- When the stay fits, the system shows the total price, the cancellation policy, the house rules and the reservation terms.
- The information a booking needs is a payment method and, when the host or we ask for it, identity information. They can confirm a payment method already on their account or add a new one.
- Submitting means accepting the price, the policies and the terms.
- On submit, the system checks the information, takes the payment, confirms the reservation, tells the host and shows them the confirmation with the stay details.
- Payment is taken only when a reservation is confirmed.

## What can go wrong

- Some of the dates are already booked or blocked by the host, or the party is bigger than the listing takes.
- The listing can't be booked instantly, because the host hasn't turned instant booking on or the guest doesn't meet the host's requirements for it.
- They submit the same booking twice, for example when their connection stalls.
- The payment details or the identity information are missing, or the payment method is declined.
- Someone else books the dates, or the host blocks them, between the moment they're shown as free and the submit.
- The payment provider doesn't answer, or the payment goes through but the reservation doesn't, or the other way round.
- They leave before submitting.

## How each is handled

- Dates taken or party too big: the system says which dates aren't free or how many guests the listing takes; they change the dates or the party, or pick another listing.
- No instant booking: they send a reservation request instead, with the same information. Nothing is charged; the system tells them the request is with the host and that they'll be notified of the host's answer. That's the end for the guest here; the host accepting or declining, and the guest looking elsewhere after a decline, belong to the host's side.
- Submitted twice: it's handled once, so one reservation and one charge.
- Missing information or declined payment: nothing is reserved or charged; the system says what's missing or that the payment method was declined, and they fix it and submit again, or stop.
- Dates gone between showing and submitting: nothing is charged or confirmed, the system says which dates are gone, and they pick other dates or another listing.
- Payment provider down or a half-done booking: any charge is reversed, nothing is confirmed, the system says the booking wasn't made and keeps what they entered, and they can try again or stop.
- Leaving before submitting: nothing is reserved or charged.
- Besides the host's decision, other conditions can leave a booking waiting for confirmation; we haven't pinned down which.

## Durations

- Checking availability and showing the price and terms is immediate.
- Taking the payment and confirming the reservation takes a few seconds.
- Sending a request to the host also takes a few seconds; the host's answer comes later, by notification.

## Out of scope

- The listing being removed while someone is booking it: that's decided by the host's own use case for removing a listing, not here.
- Exporting or erasing the guest's identity, payment and stay data: that's the account privacy job, not booking.
