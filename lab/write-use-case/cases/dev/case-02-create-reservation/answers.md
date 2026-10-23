# Answers: create a reservation

## Actor, goal and scope

- The system is our hotel property management system.
- It starts when a guest asks the front desk to book a room, either standing at the desk or on the phone.
- Before they start, the clerk is already signed in, and the room inventory and rates have been set up.
- The only outside party is the payment service, which authorizes deposits.
- It happens tens of times a day at a busy front desk.
- Exporting or erasing a guest's profile is a separate job, not part of booking.

## Stakeholders and guarantees

- The guest wants the room type and dates they asked for, at the price they were quoted, and a confirmation.
- The clerk wants to book quickly, because the guest is waiting at the desk or on the line.
- The revenue manager wants no overbooking and the deposit policy enforced.
- Finance wants no payment taken unless there's a matching reservation.
- However it ends, there's never a half-stored reservation and availability is left as it was.
- If a deposit was authorized and the reservation doesn't get stored, that authorization is released.
- When it works, the reservation is stored as confirmed at the price the guest agreed to, availability is updated for those dates, any deposit required is authorized, the clerk has a confirmation number, and the guest has been sent a confirmation.

## Main scenario

- The contact details and the stay dates are given separately: details first, then check-in and check-out.
- The available room types come with their rates.
- After the room type is chosen, the system shows the total price for the whole stay.
- The clerk only confirms once the guest has agreed.
- On confirmation the clerk gets a confirmation number to give the guest.
- The reservation keeps the price the guest was shown, even if rates are changed in the meantime.
- Booking rules: the minimum stay is one night, and nobody can book more than 365 days ahead.
- A stay of three nights or more needs a deposit of half the total price.

## What can go wrong

- The guest is already in the system from an earlier stay.
- The contact details don't give us a usable way to send the confirmation, for example a missing or mistyped email address.
- The dates break one of the booking rules.
- There's no room available for those dates.
- The guest turns down the price.
- The guest gives up or hangs up before the clerk confirms.
- The stay needs a deposit.
- The payment service declines the deposit, or doesn't answer.
- Someone else books the last room of that type between it being shown and the clerk confirming.
- The reservation fails to save properly.

## How each is handled

- Returning guest: the system shows their existing profile, the clerk confirms it or updates it with the guest, and carries on with the dates.
- Unusable contact details: the system says which detail is missing or wrong, and the clerk corrects it with the guest.
- Dates breaking a rule: the system says which rule, and the clerk gives new dates or the guest gives up.
- Nothing available: the system says so, and the clerk tries other dates or the guest gives up.
- Guest turning down the price, giving up or hanging up before confirmation: the draft is thrown away, nothing is stored and availability isn't touched.
- Deposit needed: the system asks for payment details, the clerk gives the guest's, and the system gets the deposit authorized by the payment service before storing the reservation.
- Deposit declined or no answer from the payment service: nothing is taken, the system says the deposit wasn't authorized, and the clerk tries again or uses another payment method; if the guest gives up, nothing is stored.
- Last room taken by someone else: nothing is stored, any deposit authorization is released, the system says that room type is gone, and the clerk is shown what's available now.
- Save failure: nothing is stored, availability is unchanged, any deposit authorization is released, the clerk is told the reservation wasn't made and can try again or the guest gives up.

## Durations

- Showing the available room types and showing the total price are immediate.
- Getting the deposit authorized by the payment service takes a few seconds.
- Storing the reservation and giving the confirmation number is immediate; the guest's confirmation goes out at the same time.

## Out of scope

- The same guest booking overlapping dates is not a duplicate: a guest can hold several reservations for the same dates, one per room.
- Any signed-in clerk can make a reservation; there's no extra permission check.
- If the guest's confirmation doesn't get delivered, the reservation still stands; chasing a failed delivery isn't part of booking.
