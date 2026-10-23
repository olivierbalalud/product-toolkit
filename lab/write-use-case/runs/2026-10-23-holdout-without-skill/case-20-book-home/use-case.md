---
id: UC-020
title: Book a stay at a listing
status: Draft
driver: lab
priority: high
source_locale: en
inputs: []
stories: []
---

# UC-020: Book a stay at a listing

| Field | Value |
|---|---|
| **Primary actor** | Guest |
| **Supporting actors** | Payment provider; Host (notified of every reservation and request); notification service (email and push) |
| **Scope** | The accommodation marketplace (booking flow) |
| **Level** | User goal |
| **Trigger** | The guest opens a listing and wants to stay there on given dates. |
| **Preconditions** | The guest is signed in to an adult account (sign-in and age are handled at sign-up, not here). |
| **Minimal guarantees** | Nothing is reserved or charged unless a reservation is confirmed; a charge taken without a recorded reservation is reversed. Each submission yields at most one reservation or request and at most one charge. The guest's entered details are kept after a failed submission. The attempt is logged. |
| **Success guarantees** | **Instant booking:** the reservation is confirmed, the full total is charged once, the dates are no longer available to others, the guest sees a confirmation and the host is notified. **Request to book (wait point):** a pending request is recorded, nothing is charged, the dates are held for the host's response window (BR-7), the host is notified, and the guest is told the request is with the host and that they will be notified of the answer. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Guest | Gets the stay they chose at the price and policies they reviewed; is never charged for a stay that isn't confirmed, or charged twice; knows clearly whether the stay is booked or pending. |
| Host | Receives only bookings that respect the listing's rules and their instant-booking requirements; is told of every reservation and request; is not double-booked. |
| Marketplace operator | Converts bookings reliably; collects payment correctly; keeps trust and safety (suspended accounts can't book, identity checks when needed). |
| Data protection | Payment and identity data are collected only when needed and handled under the account privacy process. |

## Main success scenario

1. (actor) The guest chooses the stay dates and the number of guests on a listing.
2. (system) The system checks that the dates are free and that the party and dates fit the listing's rules (BR-6), and shows the price breakdown, the cancellation policy, the house rules, and whether the stay can be booked instantly or needs the host's approval.
3. (actor) The guest reviews the details, confirms a saved payment method or adds a new one, supplies any identity information the host or the marketplace asks for (BR-9), optionally writes a message to the host, and submits the booking, which accepts the price, policies and terms (BR-1).
4. (system) The system rechecks that the dates are still free, that the price and policies match what the guest reviewed (BR-8), that the required information is complete, and that the stay can be booked instantly (BR-2).
5. (system, wait) The system charges the full total to the payment method and records the confirmed reservation as one outcome: both happen or neither does (BR-3, BR-10).
6. (system) The system shows the guest a confirmation with the stay details and a confirmation code, sends it to the guest by email and push, and notifies the host.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-020.1a, UC-020.1b | n/a | n/a | yes: UC-020.1-3a |
| 3 | yes: UC-020.3a, UC-020.3d | yes: UC-020.3b, UC-020.3c | yes: UC-020.3e | yes: UC-020.1-3a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | yes: UC-020.2a | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | yes: UC-020.2a | yes: UC-020.1b | n/a | n/a | n/a | yes: UC-020.4a | n/a |
| 5 | n/a | yes: UC-020.1b | yes: UC-020.5a | yes: UC-020.5a | n/a | n/a | n/a |
| 6 | n/a | n/a | yes: UC-020.6a | n/a | n/a | n/a | n/a |

**Privacy request:** no: export and erasure of identity, payment, stay data and messages are handled by the account privacy use case, not by booking.

## Extensions

- **UC-020.1a** The party or the dates break a listing rule (more guests than the listing takes, stay shorter or longer than the host allows, too little advance notice, a check-in day the host doesn't accept, pets where they aren't allowed):
  1. The system says which rule is broken and what the listing allows, e.g. how many guests it takes.
  2. Returns to step 1 (the guest changes the party or dates, or picks another listing).

  *Example:* Ana asks for 6 guests at a flat that takes 4; the system says the listing takes up to 4 guests.
- **UC-020.1b** Some of the chosen dates are not free (already booked, held by a pending request, or blocked by the host), whether found at step 2 or taken by someone else before the reservation is recorded at step 4 or 5:
  1. Nothing is reserved or charged; any charge already taken is reversed.
  2. The system says which dates are no longer free.
  3. Returns to step 1 (the guest picks other dates or another listing).

  *Example:* Ana submits for 12 to 15 June, but Ben's instant booking for 14 June was recorded a second earlier; the system says 14 June is no longer free.
- **UC-020.2a** The listing is no longer bookable (removed or unlisted by the host):
  1. The system says the listing is no longer available.
  2. The use case ends.

  *Example:* Ana opens a saved listing that the host unlisted yesterday; the system says it can no longer be booked.
- **UC-020.1-3a** The guest leaves before submitting:
  1. Nothing is reserved, held or charged (BR-5).
  2. The use case ends.

  *Example:* Ana reviews the price for 12 to 15 June, closes the app and books nothing.
- **UC-020.3a** Required identity information is missing:
  1. Nothing is reserved or charged.
  2. The system says what is missing; the guest supplies it (identity verification is its own use case) or stops.
  3. Returns to step 3.

  *Example:* The host requires verified identity; Ana hasn't verified hers, so the system says a verified ID is needed before she can submit.
- **UC-020.3b** The guest submits the same booking twice (double submit, or a retry after an unclear outcome):
  1. The system handles the submission once and returns the result of the first one.
  2. The use case continues from where the first submission is.

  *Example:* Ana taps submit twice on a slow connection; she gets one reservation and one charge.
- **UC-020.3c** The guest already has a pending request for this listing on overlapping dates:
  1. The system says a request for these dates is already with the host and doesn't record a second one.
  2. The use case ends.

  *Example:* Ana sent a request for 12 to 15 June an hour ago and submits again for 13 to 16 June; the system points her to the pending request.
- **UC-020.3d** The payment is declined:
  1. Nothing is reserved or charged.
  2. The system says the payment method was declined; the guest's details are kept.
  3. Returns to step 3 (the guest fixes or changes the payment method and submits again, or stops).

  *Example:* Ana's card is refused for insufficient funds; she adds another card and submits again.
- **UC-020.3e** The guest's account is suspended:
  1. Nothing is reserved or charged.
  2. The system says booking is not available for this account and points to account support, without giving the reason.
  3. The use case ends.

  *Example:* Ben's account is suspended after a trust review; his submission is refused and he is pointed to support.
- **UC-020.4a** The price, fees or policies changed after the guest reviewed them:
  1. Nothing is reserved or charged.
  2. The system shows what changed (old and new total, or the new cancellation policy).
  3. Returns to step 3 (the guest reviews and submits again, or stops).

  *Example:* The host raises the nightly rate from 120 to 140 while Ana is on the review; on submit the system shows the new total of 420 instead of 360.
- **UC-020.4b** The listing isn't set to instant booking, or the guest doesn't meet the host's instant-booking requirements (BR-2):
  1. (system, wait) The system checks the payment method with the payment provider, without charging it or placing a hold (BR-4).
  2. (system) The system records a pending request with the guest's details and message, holds the dates for the host's response window (BR-7), and notifies the host.
  3. (system) The system tells the guest that the request is with the host, that nothing has been charged, and that they will be notified of the host's answer. The use case ends at this wait point; the host's decision is a separate use case.

  If the payment method is declined, UC-020.3d applies; if the provider doesn't respond, UC-020.5a applies.

  *Example:* Ana requests 12 to 15 June at a listing that needs host approval; she sees "Request sent, nothing charged, the host has 24 hours to answer."
- **UC-020.5a** The payment provider doesn't respond, or the charge succeeds but the reservation can't be recorded:
  1. Any charge is reversed; nothing is confirmed.
  2. The system says the booking wasn't made; the guest's details are kept.
  3. Returns to step 3 (the guest tries again or stops).

  *Example:* The provider times out after Ana submits; she sees "Your booking wasn't made, you haven't been charged" and tries again.
- **UC-020.5b** The guest's bank asks for extra authentication (e.g. 3-D Secure):
  1. The system asks the guest to complete the bank's authentication; nothing is confirmed meanwhile.
  2. If it succeeds, returns to step 5. If it fails or the guest abandons it, nothing is reserved or charged, the details are kept, and the use case returns to step 3.

  *Example:* Ana's bank asks her to approve the 360 payment in her banking app; she approves and the reservation is confirmed.
- **UC-020.6a** The email or push notification can't be sent:
  1. The reservation stands; the guest still sees the confirmation on screen and in their trips.
  2. The system retries sending to the guest and the host.
  3. The use case ends.

  *Example:* The email service is down when Ana's reservation is confirmed; she sees it on screen and receives the email when the service recovers.

## Technology and data variations

- Step 3: payment method saved on the account, or a new one added during booking.
- Step 3: identity information required by the host, by the marketplace, or not at all.
- Step 4: instant booking (main scenario) or request to book (UC-020.4b).
- Step 2: price shown in the guest's chosen currency.

## Related information

- **Frequency:** Continuous; booking is the main thing guests do on the marketplace, and a typical guest books a few stays a year.
- **Business rules:**
  - **BR-1** Submitting the booking accepts the price, the cancellation policy, the house rules and the reservation terms; there is no separate acceptance step.
  - **BR-2** A stay is booked instantly only when the listing is set to instant booking and the guest meets the host's instant-booking requirements; otherwise the guest sends a request with the same information. Recommended requirements a host can set: verified identity, and a history of past stays without reported issues.
  - **BR-3** For an instant booking, the full total is charged in one payment when the reservation is confirmed; no split payment and no hold.
  - **BR-4** For a request, nothing is charged at submission; the payment method is checked without a charge or hold (recommendation); the charge happens when the host accepts.
  - **BR-5** Nothing is held while the guest is in checkout; dates are reserved only on submission.
  - **BR-6** The party must not exceed the listing's maximum guests (adults and children count; pets only where the listing allows them). Recommended host-set rules: minimum and maximum nights, advance notice, and accepted check-in days.
  - **BR-7** The host has 24 hours to answer a request (recommendation); a pending request holds the dates against other bookings for that window (recommendation).
  - **BR-8** The guest is never charged a price, or bound by a policy, they didn't review (recommendation).
  - **BR-9** Identity information is required only when the host or the marketplace asks for it; without it the booking doesn't proceed.
  - **BR-10** One submission yields at most one reservation and one charge.
- **Open issues:**
  - Which other conditions can leave a booking waiting for confirmation besides instant booking being off or unmet (owner unsure).
  - Recommendations not yet confirmed by the owner: host response window (24 h), whether a pending request holds the dates, payment-method check without hold for requests, 3-D Secure handling, price or policy change at submission, listing rules beyond maximum guests, pets and children, suspended accounts, instant-booking requirements, guest notification by email and push, confirmation content (code, address, check-in details).
  - Whether a host can block specific guests: not decided; not covered here.
  - Identity verification speed: recommended as its own use case, so this one only checks whether it's done.
  - Whether messages to the host fall under the account privacy job (recommended yes).
  - Coupons, gift cards and long-stay discounts: recommended out of scope for this version.
