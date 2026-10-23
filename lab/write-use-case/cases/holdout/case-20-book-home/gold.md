---
id: UC-020
title: Book a home for a trip
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-020: Book a home for a trip

| Field | Value |
|---|---|
| **Primary actor** | Guest |
| **Supporting actors** | Payment provider (charges the guest's payment method); Host (informed of each reservation; decides on a reservation request, UC-020.2a) |
| **Scope** | Accommodation booking marketplace |
| **Level** | User goal |
| **Trigger** | The guest has found a listing that suits the trip and decides to book it. |
| **Preconditions** | The guest is signed in. |
| **Minimal guarantees** | The guest is charged only for a confirmed reservation, and never twice for the same one (BR-2); no listing is booked twice for the same dates; however the use case ends, the guest is told whether the reservation is confirmed, requested or not made. |
| **Success guarantees** | The reservation is confirmed for the guest's dates and party; the guest is charged the total presented; the stay details are available to the guest; the host is informed of the reservation. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Guest | Secures a home for the trip's dates and party; knows the full price, the policies and the terms before committing; is charged once, and only for a confirmed stay. |
| Host | Gets only reservations that fit the listing's calendar and limits; is informed of each reservation; decides on requests when the listing can't be booked instantly. |
| Marketplace operator | Every confirmed reservation is paid; no listing is booked twice for the same dates. |

## Main success scenario

1. (actor) The guest gives the stay dates and the number of guests for the listing.
2. (system) The system confirms the listing is available for that stay and presents the booking option with its total price, the cancellation policy, the house rules and the reservation terms (BR-1, BR-3).
3. (actor) The guest supplies or confirms the information the booking requires (BR-4), accepts the price, policies and terms, and submits the booking.
4. (system, wait) The system checks the required information, charges the guest's payment method through the payment provider, confirms the reservation, informs the host, and presents the confirmation with the stay details.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-020.1a | n/a | n/a | yes: UC-020.1-3a |
| 3 | yes: UC-020.3b | yes: UC-020.3a | n/a | yes: UC-020.1-3a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | out-of-scope: removing a listing is the host's use case, which decides what happens to bookings in progress | yes: UC-020.4a | yes: UC-020.4b | yes: UC-020.4b | n/a | yes: UC-020.4a | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing the guest's identity, payment and stay data is part of a separate account privacy use case, not of booking.

## Extensions

- **UC-020.1-3a** The guest leaves before submitting the booking:
  1. The system reserves nothing and charges nothing.
  2. The use case ends.

  *Example:* Mia looks at the price of the Porto apartment for 12–15 June, decides it is too much, and leaves; nothing is reserved and her card is not charged.
- **UC-020.1a** The listing can't take the stay as given: some of the dates are already booked or blocked by the host, or the party is larger than the listing accepts (BR-3):
  1. The system says which dates are not available, or how many guests the listing accepts.
  2. The guest gives other dates or a smaller party: returns to step 2. Or the guest chooses another listing: the use case ends.

  *Example:* Jonas asks for the Annecy chalet for 2–9 August, but 6 August is already booked; he picks 9–16 August instead.
- **UC-020.2a** The listing can't be booked instantly: the host has not enabled instant booking, or the guest doesn't meet the host's requirements for it (BR-1):
  1. The system presents the booking as a reservation request that the host accepts or declines.
  2. The guest supplies or confirms the information the booking requires, accepts the price, policies and terms, and submits the request.
  3. The system checks the required information (UC-020.3b applies), sends the request to the host, charges nothing (BR-2), and tells the guest the request is pending and that they will be notified of the host's decision.
  4. The use case ends. The host's decision is the use case Respond to a Reservation Request.

  *Example:* Clara requests the Ghent loft for 3–5 May, a listing whose host reviews each booking; the system tells her the request is with the host and that she will be notified of the answer.
- **UC-020.3a** The guest submits the same booking again before the first submission is answered:
  1. The system handles the booking once: one reservation and one charge.
  2. Returns to step 4.

  *Example:* Mia's connection stalls and she submits her booking of the Lisbon flat for 1–4 March a second time; she gets one reservation and one charge of €640.
- **UC-020.3b** The payment details or the identity information the booking requires are missing, or the payment provider declines the payment method:
  1. The system reserves nothing, charges nothing, and names the missing information or the declined payment method.
  2. The guest provides the missing information or another payment method: returns to step 4. Or the guest stops: the use case ends.

  *Example:* Jonas books the Annecy chalet without having added the identity document the host requires; he adds it and the booking is confirmed.
- **UC-020.4a** Another guest booked some of the dates, or the host blocked them, after the system presented the listing as available:
  1. The system charges nothing, confirms no reservation, and says which dates are no longer available.
  2. The guest gives other dates: returns to step 2. Or the guest chooses another listing: the use case ends.

  *Example:* Clara and Tom both submit a booking for the Bruges cottage for 20–22 October; Tom's is confirmed first, so Clara is told those dates are gone and picks 27–29 October.
- **UC-020.4b** The payment provider does not answer, or only one of the charge and the reservation succeeds:
  1. The system reverses any charge, confirms no reservation, and tells the guest the booking was not made, keeping their entries.
  2. The guest submits again: returns to step 4. Or the guest stops: the use case ends.

  *Example:* Mia submits her booking at 21:10 while the payment provider is down; nothing is charged or reserved, and her retry at 21:15 is confirmed.

## Technology and data variations

- 3: the guest confirms a payment method already on the account, or adds a new one.

## Related information

- **Frequency:** Frequent: booking is the marketplace's core guest action; a typical guest books a few stays a year.
- **Business rules:** BR-1 a listing can be booked instantly only if its host enabled instant booking and the guest meets the host's requirements for it; otherwise the guest sends a reservation request that the host accepts or declines (step 2, UC-020.2a) · BR-2 the guest is charged only when a reservation is confirmed (step 4, UC-020.2a, UC-020.3b, UC-020.4a, UC-020.4b) · BR-3 a stay must fit the listing's calendar and the number of guests it accepts (step 2, UC-020.1a) · BR-4 a booking requires a payment method and, where the host or the marketplace asks for it, identity information (step 3, UC-020.3b).
- **Related use cases:** Respond to a Reservation Request, Cancel a Reservation, Create a Listing, Check In.
- **Open issues:** Which conditions, besides the host's decision on a request, can leave a reservation awaiting confirmation.
