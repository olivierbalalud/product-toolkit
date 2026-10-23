---
id: UC-007
title: Buy a product
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-007: Buy a product

| Field | Value |
|---|---|
| **Primary actor** | Customer |
| **Supporting actors** | Payment provider (authorizes the payment, including the card issuer's strong customer authentication); Notification service (sends the confirmation email) |
| **Scope** | Online store |
| **Level** | User goal |
| **Trigger** | The Customer decides to buy one or more products. |
| **Preconditions** | The catalog is published. |
| **Minimal guarantees** | The Customer is never charged without a recorded order, nor twice for the same order; an order is never confirmed without an authorized payment. |
| **Success guarantees** | The order is recorded with its items, shipping details and full price; the payment for that full price is authorized; the order is confirmed to the Customer and the confirmation is emailed; the order is queued for fulfillment with complete shipping details. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Customer | Gets the right items at the price shown, delivered as chosen; is never charged twice. |
| Merchant | Is paid, and the order is captured for fulfillment. |
| Fulfillment | Receives complete shipping information. |
| Payment provider | Receives valid authorization requests. |

## Main success scenario

1. (actor) The Customer selects the items to buy from the catalog and asks to check out.
2. (actor) The Customer provides the shipping details: the address and the delivery speed.
3. (system) The system presents the full price: the items, shipping for the chosen delivery speed, and taxes.
4. (actor) The Customer provides payment details and places the order.
5. (system, wait) The system obtains the payment provider's authorization for the full price presented, records the order, queues it for fulfillment, and confirms the order to the Customer.
6. (system) The system has the notification service email the order confirmation to the Customer.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | n/a | n/a | n/a | yes: UC-007.1-4a |
| 2 | yes: UC-007.2b | n/a | n/a | yes: UC-007.1-4a |
| 4 | yes: UC-007.4a | yes: UC-007.4b | n/a | yes: UC-007.1-4a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 3 | n/a | n/a | n/a | n/a | n/a | yes: UC-007.3a | n/a |
| 5 | n/a | yes: UC-007.5c | yes: UC-007.5b | yes: UC-007.5b | n/a | yes: UC-007.5c | n/a |
| 6 | n/a | n/a | out-of-scope: the order is already confirmed to the Customer at step 5; delivering the email once handed over is the notification service's job | n/a | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, the order holds the Customer's address and, for a returning customer, stored shipping and card details; exporting or erasing them belongs to a separate account privacy use case, and the obligation to keep order records for accounting limits erasure.

## Extensions

- **UC-007.2a** The Customer is signed in and has stored shipping and card details:
  1. The system proposes the stored shipping details and the stored card, showing only its last four digits, with the full price.
  2. The Customer accepts them, or changes any of them, and places the order; if the shipping details changed, the system first presents the updated full price.
  3. Returns to step 5.

  *Example:* Ben, signed in, is offered his home address, standard delivery and the card ending 4242 for a total of €58.90; he accepts them and places the order.
- **UC-007.2b** The shipping address is incomplete, or the store does not deliver there:
  1. The system says what is missing or that it does not deliver to that address.
  2. Returns to step 2, where the Customer corrects the shipping details; or the Customer cancels (UC-007.1-4a).

  *Example:* Chloé gives her street and city but no postcode; the system asks for the postcode, and she adds 69003.
- **UC-007.3a** An item went out of stock since the Customer selected it:
  1. The system says which item is out of stock.
  2. The Customer removes or replaces it: returns to step 3.

  *Example:* Marta selected a blue and a white linen shirt; when she reaches the full price the blue one has sold out, and she replaces it with a grey one.
- **UC-007.4a** The payment provider declines the payment, for example because the card has expired or the details are wrong:
  1. The system records no order and says the payment was declined.
  2. Returns to step 4, where the Customer provides other payment details; or the Customer cancels and the use case ends with no order recorded and nothing charged.

  *Example:* Tom's card ending 1881 has expired; the payment is declined, and he pays with his digital wallet instead.
- **UC-007.4b** The Customer places the same order again before it is confirmed:
  1. The system processes the order only once and charges it once.
  2. Returns to step 5 for the first placement.

  *Example:* Ana places her €42.50 order twice in a row on a slow connection; she gets one order and one charge.
- **UC-007.5a** The card issuer requires strong customer authentication:
  1. The system has the Customer complete the card issuer's challenge.
  2. Returns to step 5.

  *Example:* Léa's bank sends her a one-time code for her €120 payment; she enters it, and the order is confirmed.
- **UC-007.5b** The payment provider does not answer, or the order cannot be recorded after the payment was authorized:
  1. The system records no order and has the payment provider cancel any authorization it obtained, so the Customer is not charged.
  2. The system tells the Customer the order was not placed, keeping the selected items and shipping details.
  3. Returns to step 4, where the Customer places the order again or provides other payment details; or the Customer cancels and the use case ends.

  *Example:* The payment provider does not answer within 10 seconds when Omar places his €75 order at 18:03; no order is recorded, nothing is charged, and his second try at 18:05 is confirmed.
- **UC-007.5c** An item sold out after the full price was presented, because another customer bought the last units:
  1. The system obtains no authorization, records no order, and says which item sold out.
  2. The Customer removes or replaces it: returns to step 3.

  *Example:* Marta and Jon both place orders for the last copy of a framed print; Jon's is recorded first, so Marta is told it sold out and removes it from her order.
- **UC-007.1-4a** The Customer cancels or abandons the purchase before placing the order:
  1. The system records no order and charges nothing.
  2. The use case ends.

  *Example:* Ben selects three books and gives his address, then leaves the store and does not come back; no order is recorded and nothing is charged.

## Technology and data variations

- 1-4: guest checkout, or signed-in checkout.
- 4: payment by card, digital wallet or bank transfer, each authorized while the Customer waits.

## Related information

- **Frequency:** Many times a day; buying is the store's main transaction, with peaks during sales.
- **Business rules:** None
- **Open issues:** None
