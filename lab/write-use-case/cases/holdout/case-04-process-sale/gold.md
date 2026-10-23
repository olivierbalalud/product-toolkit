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
| **Supporting actors** | Customer (pays); Payment authorization service (authorizes card payments); Tax calculator (calculates the taxes); Accounting system and Inventory system (receive each completed sale); Store manager (performs overrides) |
| **Scope** | Point-of-sale application |
| **Level** | User goal |
| **Trigger** | A Customer arrives at the checkout with goods to buy. |
| **Preconditions** | The Cashier is identified and authenticated. |
| **Minimal guarantees** | A sale is never recorded as paid without a confirmed payment; a completed sale is never lost. |
| **Success guarantees** | The sale is recorded with its line items, correctly calculated taxes, its payment and payment authorization, and the Cashier's commission; the Accounting system and the Inventory system have received it, or it is stored to be forwarded to them; the Customer has a receipt. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Cashier | Fast, accurate entry; no payment mistakes, since shortages come out of their pay. |
| Customer | Fast checkout, correct prices, proof of purchase for returns. |
| Retailer | Accurate records, payments captured, sales still possible when back-end services are down. |
| Store manager | Can perform overrides quickly. |
| Tax authorities | Tax collected on every sale. |
| Payment authorization service | Receives authorization requests in the expected format. |

## Main success scenario

1. (actor) The Cashier starts a new sale.
2. (actor) The Cashier enters an item identifier.
3. (system) The system records the line item and presents its description, its price and the running total. Steps 2 and 3 repeat until the Cashier has entered every item.
4. (system) The system calculates the taxes with the Tax calculator (BR-1) and presents the total due.
5. (actor) The Customer pays by card.
6. (system, wait) The system gets the payment authorized by the Payment authorization service (BR-3).
7. (system) The system records the completed sale, with its payment, its payment authorization and the Cashier's commission, and sends the sale and payment information to the Accounting system and the Inventory system.
8. (system) The system presents the receipt.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | n/a | n/a | n/a | yes: UC-004.1-5a |
| 2 | yes: UC-004.2a | n/a | n/a | yes: UC-004.1-5a |
| 5 | n/a | n/a | n/a | yes: UC-004.1-5a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 3 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | n/a | n/a | yes: UC-004.4b | n/a | n/a | n/a | n/a |
| 6 | n/a | n/a | yes: UC-004.6a | n/a | n/a | n/a | n/a |
| 7 | n/a | n/a | yes: UC-004.7a | yes: UC-004.7a | n/a | n/a | n/a |
| 8 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, the sale holds personal data only when a Customer is identified for a discount, and card details go only to the Payment authorization service; exporting or erasing a Customer's data is its own use case, not written yet.

## Extensions

- **`UC-004.*a`** The Store manager asks for an override:
  1. The system switches to manager-authorized mode.
  2. The Store manager performs the operation.
  3. The system switches back to the Cashier's mode and returns to the step where the override was asked for.

  *Example:* During Tom's sale, the store manager Ms Haddad overrides the price of a dented kettle from €40.00 to €30.00, then hands the checkout back to Tom.
- **UC-004.1-5a** The Customer leaves without paying, or the Cashier cancels the sale, before the payment is authorized:
  1. The system discards the sale: nothing is recorded as sold and nothing is sent to the Accounting system or the Inventory system.
  2. The use case ends.

  *Example:* Leo has entered four items when his customer finds she left her wallet in the car and walks out; Leo cancels the sale and nothing is recorded as sold.
- **UC-004.2a** The item identifier is not valid:
  1. The system signals the error and rejects the entry.
  2. Returns to step 2.

  *Example:* Tom types 40012 for a bag of apples; no item has that identifier, so the system rejects it and Tom enters 40021, the right one.
- **UC-004.2b** The Customer buys several units of the same item:
  1. The Cashier enters the quantity with the item identifier.
  2. Returns to step 3, which records the line item with that quantity.

  *Example:* A customer buys six bottles of water; Tom enters the item once with a quantity of 6 and the line shows 6 × €0.90.
- **UC-004.4a** The Customer is eligible for a discount:
  1. The Cashier identifies the Customer.
  2. The system applies the discount rules (BR-2) and presents the new total due.
  3. Returns to step 5.

  *Example:* Rosa, who works at the store, is identified as an employee, and the employee discount takes €4.50 off her €45.00 total.
- **UC-004.4b** The Tax calculator does not answer:
  1. The system signals that the taxes cannot be calculated, and keeps the sale open (BR-1).
  2. The Cashier tries again: returns to step 4. Or the Cashier cancels the sale: continues as in UC-004.1-5a.

  *Example:* At 17:42 the Tax calculator does not answer for Mia's sale of three items; she tries again and the total with tax appears.
- **UC-004.5a** The Customer pays cash:
  1. The Cashier enters the amount tendered.
  2. The system presents the change due.
  3. Continues at step 7.

  *Example:* Ines pays €50.00 in cash for a €37.85 basket, and the system shows €12.15 change due.
- **UC-004.6a** The card payment is declined, or the Payment authorization service does not answer:
  1. The system signals that the payment is not authorized; nothing is recorded as paid (BR-3).
  2. The Cashier asks the Customer for another payment method: returns to step 5.

  *Example:* Sam's card is declined for €84.20, so he pays in cash instead.
- **UC-004.7a** The Accounting system or the Inventory system does not receive the sale:
  1. The system stores the sale locally and forwards it to the system that missed it once that system is available again.
  2. Continues at step 8.

  *Example:* At 21:00 the Inventory system is down for maintenance; Tom's sale is stored, the receipt is presented, and the sale reaches the Inventory system when it is back up.

## Technology and data variations

- 2: the item identifier is read from a barcode, typed on a keyboard, or read by a camera.
- 5: the card is read by a card reader, paid contactless, or paid from a mobile wallet.

## Related information

- **Frequency:** Continuous during opening hours: a sale every few minutes at each checkout.
- **Business rules:** BR-1 taxes are calculated on every sale (step 4, UC-004.4b) · BR-2 the discount rules set the discount an eligible Customer gets (UC-004.4a) · BR-3 a sale is recorded as paid only once the cash is received or the card payment is authorized (step 6, UC-004.6a).
- **Open issues:** None
