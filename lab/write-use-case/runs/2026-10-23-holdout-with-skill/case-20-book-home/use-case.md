---
id: UC-020
title: Book a stay
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-020: Book a stay

| Field | Value |
|---|---|
| **Primary actor** | Guest |
| **Supporting actors** | Payment provider (charges the guest's payment method) |
| **Scope** | Accommodation marketplace |
| **Level** | User goal |
| **Trigger** | The guest wants to stay at a listing they have found. |
| **Preconditions** | The guest is signed in. |
| **Minimal guarantees** | The guest is charged at most once, and only for a confirmed reservation; a failed attempt reserves and charges nothing; the guest knows whether they have a confirmed reservation, a request with the host, or nothing. |
| **Success guarantees** | The reservation is confirmed for the dates and the party, the dates are blocked on the listing's calendar, the guest is charged the total once, the host is notified, and the guest has the confirmation and the stay details. When the listing is not open to instant booking (UC-020.4c), the request is with the host instead: nothing is charged, the host is notified, and the guest will be notified of the host's answer. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Guest | Sees the full price, the policies and the terms before committing; is charged once, and only for a confirmed stay; knows at the end whether they have a confirmed reservation, a request with the host, or nothing. |
| Host | Gets only reservations that fit their calendar and limits; hears about each one; decides on requests when the listing is not open to instant booking. |
| Marketplace | Every confirmed reservation is paid; never two bookings on the same listing for the same dates. |

## Main success scenario

1. (actor) The guest gives the stay dates and the number of guests for the listing (BR-1).
2. (system) The system presents the total price with its breakdown, the house rules and the cancellation policy for that stay.
3. (actor) The guest gives a payment method and any identity information asked for, and submits the booking, accepting the price, the policies and the reservation terms.
4. (system, wait) The system confirms the dates are still free, confirms the reservation and charges the total through the payment provider (BR-2), blocks the dates on the listing's calendar, notifies the host and shows the guest the confirmation and the stay details.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-020.1a | n/a | n/a | yes: `UC-020.1-3a` |
| 3 | yes: UC-020.3a | yes: UC-020.3b | yes: UC-020.3a | yes: `UC-020.1-3a` |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | out-of-scope: a listing removed while a guest is booking it belongs to the host's listing-removal use case | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | out-of-scope: a listing removed while a guest is booking it belongs to the host's listing-removal use case | yes: UC-020.4a | yes: UC-020.4b | yes: UC-020.4b | n/a | yes: UC-020.4a | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing the guest's booking, payment and identity data belongs to the account privacy use case.

## Extensions

- **UC-020.1a** Some of the dates are not free, or the party is larger than the listing takes (BR-1):
  1. The system says which dates are not free, or how many guests the listing takes.
  2. Returns to step 1.

  *Example:* Lea asks for 12 to 15 March for five guests at a flat that takes four; the system says the listing takes at most four guests.
- **`UC-020.1-3a`** The guest gives up before submitting:
  1. The system reserves and charges nothing.
  2. The use case ends.

  *Example:* Tom sees the total for a weekend in Lyon, finds it too high and leaves without submitting; the dates stay free and his card is not charged.
- **UC-020.3a** Information is missing, including identity information the host or the marketplace asked for and the guest did not give, or the payment provider declines the payment:
  1. The system reserves and charges nothing, says what is missing or that the payment was declined, and keeps what the guest entered.
  2. The guest supplies what is missing or another payment method: returns to step 3. Or stops: the use case ends.

  *Example:* The host of a cabin asks for identity information; Sara submits without it, the system says identity information is required, and she adds it and submits again.
- **UC-020.3b** The guest submits the same booking twice:
  1. The system handles the booking once: one reservation, or one request, and at most one charge.
  2. Returns to step 4, which shows the guest the outcome of that single booking.

  *Example:* Omar submits his booking for 2 to 4 May and submits again a second later; he has one reservation and one charge of 340 euros.
- **UC-020.4a** The dates were booked or blocked after the system presented the price:
  1. The system confirms nothing and charges nothing, says which dates are gone, and keeps the number of guests.
  2. The guest picks other dates: returns to step 1. Or stops, for example to look at another listing: the use case ends.

  *Example:* Nina is shown the price for 8 to 10 June; before she submits, another guest books 9 June, and on submit the system says 9 June is no longer free.
- **UC-020.4b** The payment provider does not answer, or the charge and the reservation do not both succeed:
  1. The system reverses any charge, confirms nothing, says the booking was not made, and keeps what the guest entered.
  2. The guest tries again: returns to step 3. Or stops: the use case ends.

  *Example:* Paul submits a booking for 1 to 3 July; the reservation cannot be recorded after his card is charged 210 euros, so the charge is reversed and he is told the booking was not made.
- **UC-020.4c** The listing is not open to instant booking:
  1. The system confirms the dates are still free (as in UC-020.4a), records the request with the host without charging anything and without holding the dates, and notifies the host.
  2. The system tells the guest the request is with the host and that they will be notified of the host's answer.
  3. The use case ends.

  *Example:* Ines asks to stay at a farmhouse from 20 to 23 August; the listing takes requests only, so the host is notified, nothing is charged, and Ines is told she will hear the host's answer.
- **UC-020.4d** The booking is left waiting for confirmation for a reason other than the host's decision: `deferred`, the driver has not yet decided which conditions can leave a booking waiting.

## Technology and data variations

- None.

## Related information

- **Frequency:** A typical guest books a few stays a year; bookings happen all the time across the marketplace.
- **Business rules:**
  - BR-1 a stay must fit the listing's calendar and the limits the host sets, including the maximum number of guests (step 1, UC-020.1a).
  - BR-2 payment is taken only when the reservation is confirmed; a request charges nothing when it is sent (step 4, UC-020.4b, UC-020.4c).
- **Related use cases:** Respond to a booking request (host, continues UC-020.4c); Find a listing; Sign in; Remove a listing (host); the account privacy use case (export or erase personal data).
- **Open issues:** Which conditions, other than the host's decision on a request, can leave a booking waiting for confirmation (UC-020.4d).
