**Use case ID:** B2C-03

**Name:** Book a home for a trip

- **Primary actor:** Airbnb guest.
- **Goal:** Reserve accommodation for specified dates and receive confirmation of the reservation.
- **Trigger:** The guest finds a suitable listing and decides to book it.
- **Preconditions:**
  - The guest can access Airbnb and has an account set up as required.
  - The listing is available for the requested dates or can accept a reservation request.
  - The guest has the required booking and payment information.

**Main success scenario**

1. The guest opens the selected accommodation listing.
2. The guest specifies the stay dates and number of guests.
3. Airbnb presents the available booking option and applicable booking information.
4. The guest reviews the price, applicable policies, and reservation terms.
5. The guest supplies or confirms the required information and submits the booking or reservation request.
6. Airbnb processes the booking and communicates whether the reservation is confirmed or awaiting the host's response.

**Alternative and exception flows**

- If the listing supports Instant Book and the guest meets its requirements, the reservation can be confirmed without waiting for host approval.
- If the listing requires a reservation request, the guest submits the request and waits for the host's decision.
- If the dates are unavailable, the guest changes the dates or selects another listing.
- If payment or required identity information is incomplete, the guest provides the missing information before confirmation can be completed.
- If the host declines a reservation request, the guest can look for another accommodation option.

**Postconditions**

- **Success:** A reservation is confirmed, with the stay details accessible to the guest.
- **Pending:** A reservation request has been submitted but awaits the required decision or other confirmation conditions.
- **Failure:** No confirmed reservation is established, and the guest can correct the issue or select another listing.

**Scope boundary:** This use case covers the guest booking interaction, not the host's listing creation, check-in, cancellation management, or the overall travel itinerary.
