---
id: UC-004
title: Process a sale
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-004: Process a sale

| Field | Value |
|---|---|
| **Primary actor** | Cashier |
| **Supporting actors** | Tax calculator (works out the taxes); payment authorization service (authorizes card payments); accounting system and inventory system (receive each completed sale) |
| **Scope** | Point-of-sale application at the checkout |
| **Level** | User goal |
| **Trigger** | A customer comes to the checkout with items to buy, and the cashier starts a new sale. |
| **Preconditions** | The cashier is identified and signed in at the register. |
| **Minimal guarantees** | No sale is half-recorded. A sale is never recorded as paid unless the payment is confirmed, and a completed sale is never lost. A cancelled sale is thrown away: nothing is recorded as sold and nothing is sent to accounting or inventory. Card details go only to the payment authorization service. |
| **Success guarantees** | The sale is recorded with its items, taxes, discounts, payment authorization and the cashier's commission; accounting and inventory have it, or it is kept to be sent to them when they are back; the customer has the receipt. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Cashier | Fast, accurate entry; no payment mistakes they would have to cover; their commission credited. |
| Customer | Correct prices, quick service, the discounts they are entitled to, and a receipt as proof of purchase. |
| Store manager | Can step in quickly for an override. |
| Retailer | Every sale recorded accurately, payment authorizations recorded, no sale lost, and selling goes on when back-end services are down. |
| Tax authorities | Correct tax collected on each sale. |
| Payment authorization service | Authorization requests in the format it expects, and an accurate record of what it owes the store. |

## Main success scenario

1. (actor) The cashier enters each item and its quantity.
2. (system) The system presents each item's description and price, and the running total.
3. (actor) The cashier identifies the customer.
4. (system) The system gets the taxes from the tax calculator, applies the customer's discounts (BR-1) and presents the total due (BR-2).
5. (actor) The cashier enters the customer's card payment.
6. (system, wait) The system gets the payment authorized by the payment authorization service.
7. (system) The system records the sale with its items, taxes, discounts, payment authorization and the cashier's commission, sends it to accounting and inventory, and issues the receipt.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-004.1a | n/a | n/a | yes: UC-004.1-5a |
| 3 | yes: UC-004.3a | n/a | n/a | yes: UC-004.1-5a |
| 5 | yes: UC-004.5a | n/a | n/a | yes: UC-004.1-5a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | n/a | n/a | yes: UC-004.4a | n/a | n/a | n/a | n/a |
| 6 | n/a | n/a | yes: UC-004.6a | n/a | n/a | n/a | n/a |
| 7 | n/a | n/a | yes: UC-004.7a | yes: UC-004.7a | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing the personal data of a customer identified for a discount is a separate customer-data privacy use case, not part of the sale.

## Extensions

- **UC-004.1a** The system does not recognise the item entered:
  1. The system rejects the entry and says the item is not recognised; the running total is unchanged.
  2. Returns to step 1.

  *Example:* Maria enters a jar of honey whose code is not in the catalogue; the system rejects it, the total stays at 23.40, and she enters the item again.
- **UC-004.1b** The cashier notices a wrong item or quantity before the payment is entered:
  1. The cashier corrects the quantity or removes the item.
  2. The system updates the running total.
  3. Returns to step 1.

  *Example:* Maria entered 3 bottles of milk instead of 2; she corrects the quantity and the total drops from 31.20 to 30.10.
- **`UC-004.1-5a`** The customer or the cashier cancels the sale before the payment goes through:
  1. The system throws the sale away: nothing is recorded as sold and nothing is sent to accounting or inventory.
  2. The use case ends.

  *Example:* After 6 items, Tom realises he left his wallet at home; Maria cancels the sale and no stock leaves the inventory.
- **UC-004.3a** The system cannot find the customer:
  1. The system says the customer is not found and applies no customer discount.
  2. The cashier identifies the customer again: returns to step 3. Or the sale goes on without customer discounts: returns to step 4.

  *Example:* Tom gives a loyalty number with two digits swapped; the system finds no customer, and Maria enters the right number.
- **UC-004.3b** The customer does not want to be identified:
  1. The system applies no customer discounts.
  2. Returns to step 4.

  *Example:* Lena prefers not to give her name; her 18.75 total is presented without any customer discount.
- **UC-004.4a** The tax calculator does not answer:
  1. The system says it cannot work out the taxes and keeps the sale open with its items (BR-2).
  2. The cashier retries: returns to step 4. Or cancels the sale: continues as in `UC-004.1-5a`.

  *Example:* Maria finishes entering Lena's 4 items; the tax calculator does not answer, the sale stays open, and Maria retries a moment later and gets the total.
- **UC-004.5a** The payment authorization service declines the card:
  1. The system says the payment is not authorized; nothing is recorded as paid and the sale stays open.
  2. The cashier asks the customer for another way to pay: returns to step 5.

  *Example:* Tom's card is declined for 42.80; Maria asks him for another way to pay and he pays with a second card.
- **UC-004.5b** The customer pays cash:
  1. The cashier enters the amount of cash handed over.
  2. The system shows the change due; no authorization is needed.
  3. Returns to step 7.

  *Example:* Lena hands over 50.00 for a 42.80 total; the system shows 7.20 change due.
- **UC-004.6a** The payment authorization service does not answer:
  1. Continues as in UC-004.5a.

  *Example:* The authorization service does not answer for Tom's 42.80 card payment; nothing is recorded as paid, and Tom pays in cash instead.
- **UC-004.7a** Accounting, inventory or both cannot take the sale:
  1. The system keeps the sale at the register, issues the receipt, and sends the sale to accounting and inventory when they are back.
  2. The use case ends.

  *Example:* The inventory system is down at 17:05 when Lena's sale is recorded; she gets her receipt, and the sale reaches inventory when it is back at 17:20.
- **`UC-004.*a`** The store manager steps in for an override:
  1. The system switches to manager mode.
  2. The store manager does the override.
  3. The system switches back to the cashier, and the sale goes on from the step where the manager stepped in.

  *Example:* While Maria enters Tom's items, the store manager steps in, makes an override in manager mode, and hands the register back to Maria at the same item.

## Technology and data variations

- None.

## Related information

- **Frequency:** A sale every few minutes at each checkout, during opening hours.
- **Business rules:** BR-1 the retailer's discount rules decide the identified customer's discounts, applied to the total (step 4, UC-004.3a, UC-004.3b). BR-2 no sale without tax: a sale cannot be paid until its taxes are worked out (step 4, UC-004.4a).
- **Related use cases:** Export or erase a customer's personal data (privacy request).
- **Open issues:** None.
