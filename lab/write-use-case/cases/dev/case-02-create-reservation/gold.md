---
id: UC-002
title: Create a reservation
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-002: Create a reservation

| Field | Value |
|---|---|
| **Primary actor** | Front Desk Clerk |
| **Supporting actors** | Payment service (authorizes deposits) |
| **Scope** | Property management system |
| **Level** | User goal |
| **Trigger** | A guest asks the front desk to book a room, at the desk or by phone. |
| **Preconditions** | The Clerk is signed in; room inventory and rates are configured. |
| **Minimal guarantees** | No partial reservation is stored; room availability is unchanged; no payment is taken without a stored reservation, and a deposit authorization obtained for a reservation that is not stored is released. |
| **Success guarantees** | The reservation is stored with status *Confirmed* at the price the guest agreed to; availability is updated for the reserved dates; a deposit, where BR-3 requires one, is authorized; the Clerk has the confirmation number and the guest has been sent a confirmation. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Guest | Gets the room type and dates asked for, at the quoted price, with a confirmation. |
| Front Desk Clerk | Books quickly while the guest waits at the desk or on the phone. |
| Revenue manager | No overbooking; the deposit policy is enforced. |
| Finance | No payment is taken without a matching reservation. |

## Main success scenario

1. (actor) The Clerk gives the guest's contact details.
2. (actor) The Clerk gives the check-in and check-out dates.
3. (system) The system presents the room types available for those dates, with their rates.
4. (actor) The Clerk chooses the room type the guest wants.
5. (system) The system presents the total price of the stay.
6. (actor) The Clerk confirms the reservation with the guest's agreement.
7. (system) The system stores the reservation as *Confirmed* at the price presented, updates availability for the dates, gives the Clerk the confirmation number and sends the guest a confirmation.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-002.1b | yes: UC-002.1a | n/a | yes: UC-002.1-6a |
| 2 | yes: UC-002.2a | out-of-scope: a guest may hold several reservations for the same dates, one per room, so an overlapping reservation is not treated as a duplicate | n/a | yes: UC-002.1-6a |
| 4 | n/a | n/a | n/a | yes: UC-002.1-6a |
| 6 | n/a | n/a | n/a | yes: UC-002.1-6a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 3 | n/a | n/a | n/a | n/a | yes: UC-002.3a | n/a | n/a |
| 5 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 7 | n/a | yes: UC-002.7a | out-of-scope: the reservation stands even if the guest's confirmation is not delivered; following up a failed delivery is not part of booking | yes: UC-002.7b | yes: UC-002.7a | yes: UC-002.7a | n/a |

**Privacy request:** yes: `deferred`, the guest's contact details are personal data; exporting or erasing a guest profile is its own use case, not part of booking.

## Extensions

- **UC-002.1a** The contact details match an existing guest:
  1. The system presents the existing guest profile.
  2. The Clerk confirms the profile or updates it with the guest.
  3. Returns to step 2.

  *Example:* Clerk Tom enters "Maria Okafor, maria.okafor@example.com"; the system finds her profile from last year's stay, and Tom updates her phone number.
- **UC-002.1b** The contact details give no usable way to send the guest the confirmation:
  1. The system says which detail is missing or malformed.
  2. The Clerk corrects the details with the guest; returns to step 1.

  *Example:* Tom types "j.berg@@mail.example" for Jonas Berg; the system flags the address, Jonas spells it again, and Tom corrects it.
- **UC-002.2a** The dates break a booking rule (BR-1, BR-2):
  1. The system states the rule that is broken.
  2. The Clerk gives corrected dates: returns to step 2. Or the guest gives up: the use case ends (UC-002.1-6a).

  *Example:* Priya Nair asks to arrive on 5 March 2028, more than 365 days ahead; Tom tells her the limit and she asks for 5 March 2027 instead.
- **UC-002.3a** No room is available for those dates:
  1. The system says no room type is available for those dates.
  2. The Clerk gives other dates: returns to step 2. Or the guest gives up: the use case ends (UC-002.1-6a).

  *Example:* Jonas Berg asks for the weekend of the city marathon; every room is booked, so he moves his stay one week later.
- **UC-002.6a** The stay requires a deposit (BR-3):
  1. The system asks for payment details for the deposit.
  2. The Clerk gives the guest's payment details.
  3. The system obtains authorization for the deposit from the payment service.
  4. Returns to step 7.

  *Example:* Maria Okafor books four nights at 120 a night; the system asks for a deposit of 240, and the payment service authorizes it on her card.
- **UC-002.6b** The payment service declines the deposit, or does not answer:
  1. The system takes no payment and says the deposit was not authorized.
  2. The Clerk gives another payment method or tries again: returns to step 2 of UC-002.6a. Or the guest gives up: nothing is stored and the use case ends.

  *Example:* Priya Nair's first card is declined for the 300 deposit; she gives a second card, and its authorization succeeds.
- **UC-002.7a** The last room of the chosen type was booked by someone else after the system presented it:
  1. The system stores nothing, releases any deposit authorization, and says the room type is no longer available.
  2. Returns to step 3, with current availability.

  *Example:* Tom and another clerk both book the last sea-view double for 12 to 14 June; the other clerk confirms first, so Tom is shown the room types still free.
- **UC-002.7b** The reservation cannot be stored in full:
  1. The system stores nothing, leaves availability unchanged, releases any deposit authorization, and tells the Clerk the reservation was not made.
  2. The Clerk tries again: returns to step 7. Or the guest gives up: the use case ends.

  *Example:* Tom confirms Jonas Berg's three-night stay, the save fails, the system releases Jonas's 180 deposit authorization, and Tom's retry a minute later succeeds.
- **UC-002.1-6a** The guest declines the price, or abandons the booking, before the Clerk confirms it:
  1. The system discards the draft reservation; nothing is stored and availability is unchanged.
  2. The use case ends.

  *Example:* Tom tells a caller the total for two nights is 410; she says it is over her budget and hangs up, and nothing is stored.

## Technology and data variations

- None.

## Related information

- **Frequency:** tens of reservations a day at a busy front desk.
- **Business rules:** BR-1 the minimum stay is one night (UC-002.2a) · BR-2 no booking more than 365 days ahead (UC-002.2a) · BR-3 stays of three or more nights require a deposit of 50% of the total price (UC-002.6a).
- **Open issues:** None
