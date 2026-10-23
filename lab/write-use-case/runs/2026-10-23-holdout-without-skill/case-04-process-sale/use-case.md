---
id: UC-004
title: Process a sale
status: Draft
driver: lab
priority: Not set
source_locale: en
inputs: []
stories: []
---

# UC-004: Process a sale

| Field | Value |
|---|---|
| **Primary actor** | Cashier |
| **Supporting actors** | Customer; Store manager; Tax calculator (external); Payment authorization service (external); Accounting system (external); Inventory system (external); Loyalty system (external, holds customer records) |
| **Scope** | The point-of-sale application at the checkout |
| **Level** | User goal |
| **Trigger** | A customer comes to the checkout with items to buy, and the cashier starts a new sale. |
| **Preconditions** | The cashier is identified and logged in at the checkout. The checkout holds a current copy of the product catalogue with prices. |
| **Minimal guarantees** | A sale is never recorded as paid unless the payment is confirmed. The customer's card is never charged without a recorded sale (BR-7). A completed sale is never lost (BR-3). Every item removal and manager override is logged (BR-6). An unfinished sale survives a restart of the checkout. |
| **Success guarantees** | The sale is recorded with its items, discounts, taxes, payment and authorization, and the cashier's commission. It has reached accounting and inventory, or is kept at the checkout until they can receive it. The customer has a receipt, and the change due for a cash payment has been shown. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Cashier | Quick, accurate entry, since shortages come out of their pay. The sale carries their commission. |
| Customer | Correct prices and discounts, a fast checkout, and a receipt as proof of purchase for returns. |
| Retailer | Accurate records, every payment captured, and completed sales reaching accounting and inventory, or kept until they can. Removals and overrides are traceable. |
| Store manager | Can step in for overrides at any moment without losing the sale in progress. |
| Tax authorities | Tax collected on every sale. |
| Payment authorization service | Requests in the format it expects, one request per payment. |
| Auditors | A complete trail of sales, removals and overrides (covered by the retailer's records and BR-6). |

## Main success scenario

1. (actor) The cashier starts a new sale.
2. (actor) The cashier enters an item identifier, with a quantity when there are several of the same item.
3. (system) The system finds the item in the catalogue, adds it to the sale, and shows its description, price and the running total. The cashier repeats steps 2 and 3 until all items are entered.
4. (actor) The cashier indicates that all items are entered.
5. (system, wait) The system applies any discount rules, gets the taxes from the tax calculator, and presents the total with taxes.
6. (actor) The customer pays by card, or hands over cash and the cashier enters the amount tendered.
7. (system, wait) For a card, the system gets the payment authorized by the payment authorization service. For cash, the system works out the change due.
8. (system) The system records the sale with its items, discounts, taxes, payment and authorization, and the cashier's commission, and passes it to the accounting and inventory systems.
9. (system) The system prints the receipt and, for cash, shows the change due.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | n/a | n/a | n/a | n/a |
| 2 | yes: UC-004.2a, UC-004.2b, UC-004.2c | yes: UC-004.2d | yes: UC-004.2b | yes: UC-004.1-6a |
| 4 | n/a | n/a | n/a | yes: UC-004.1-6a |
| 6 | yes: UC-004.6a | yes: UC-004.6b | n/a | yes: UC-004.1-6a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 3 | yes: UC-004.2a | n/a | n/a | n/a | n/a | yes: UC-004.3a | n/a |
| 5 | n/a | n/a | yes: UC-004.5a | n/a | n/a | n/a | n/a |
| 7 | n/a | n/a | yes: UC-004.7a | yes: `UC-004.*b` | n/a | n/a | n/a |
| 8 | n/a | n/a | yes: UC-004.8a | yes: UC-004.8b | n/a | n/a | n/a |
| 9 | n/a | n/a | yes: UC-004.9a | n/a | n/a | n/a | n/a |

**Privacy request:** no: the sale does not store the customer's identity (BR-8). Card data stays with the payment authorization service, and the checkout keeps only a masked card number and the authorization reference. Requests about loyalty data go to the loyalty system.

## Extensions

- **UC-004.2a** The identifier is invalid or not in the catalogue:
  1. The system flags the entry and rejects it. The running total is unchanged.
  2. Returns to step 2.

  *Example:* The cashier types item code 40071 with a digit missing; the system says no item has that code, and the cashier types it again.
- **UC-004.2b** The item has no price in the catalogue:
  1. The system rejects the entry and says the item has no price.
  2. The cashier calls the store manager, who enters the price as an override (`UC-004.*a`), or the customer leaves the item aside.
  3. Returns to step 2.

  *Example:* A new desk lamp scans but has no price yet; the manager enters 24.90 and the lamp is added at that price.
- **UC-004.2c** The quantity is not a whole number above zero:
  1. The system rejects the entry and asks for a valid quantity.
  2. Returns to step 2.

  *Example:* The cashier enters 0 as the quantity of notebooks; the system asks for a quantity of at least 1.
- **UC-004.2d** The cashier entered an item by mistake, or entered it twice:
  1. The cashier removes the item from the sale, before step 4.
  2. The system removes it, updates the running total, and logs the removal (BR-6).
  3. Returns to step 2.

  *Example:* The same bottle of water is scanned twice; the cashier removes one, and the total drops by 1.20.
- **UC-004.3a** The catalogue price of an item changes while the sale is open:
  1. The system keeps the price shown when the item was entered (BR-4). The new price applies from the next sale.
  2. Returns to step 3.

  *Example:* Coffee goes from 4.50 to 4.20 at noon while a sale with coffee entered at 11:59 is open; that sale keeps 4.50.
- **UC-004.4a** The customer has a loyalty card (an alternative, not a failure):
  1. Before step 4, the cashier enters the customer's loyalty card number.
  2. The system looks the customer up in the loyalty system and notes the discounts the customer is entitled to.
  3. Returns to step 2 or step 4. At step 5, the system applies the discount rules to the total (BR-5).

  *Example:* A member presents her loyalty card; at step 5 her 5% member discount is taken off the total before tax.
- **UC-004.4b** The loyalty card is not found, or the loyalty system does not answer within 5 seconds:
  1. The system says the customer could not be identified.
  2. The sale continues without the loyalty discount. Returns to step 2 or step 4.

  *Example:* The loyalty system is down; the cashier tells the customer and the sale goes on at the normal price.
- **UC-004.5a** The tax calculator is down, or does not answer within 10 seconds:
  1. The system says it can't work out the taxes, and keeps the sale open (BR-1).
  2. The cashier tries again (returns to step 5) or cancels the sale (UC-004.1-6a).

  *Example:* The tax calculator times out; the cashier retries and gets the total with taxes on the second attempt.
- **UC-004.6a** The cash tendered is less than the total:
  1. The system says the amount does not cover the total and asks for at least the total.
  2. Returns to step 6.

  *Example:* The total is 37.80 and the cashier enters 30.00; the system asks for at least 37.80.
- **UC-004.6b** The payment is submitted again while a card authorization is pending:
  1. The system ignores the repeat and sends only one authorization request.
  2. Returns to step 7.

  *Example:* The customer taps the card twice in quick succession; one authorization request goes out.
- **UC-004.6c** The customer wants to split the payment across card and cash: `deferred`, one payment method per sale in this version (see Open issues).
- **UC-004.1-6a** The cashier cancels the sale, for example because the customer leaves without paying:
  1. The use case ends. Cancelling a sale is its own use case; nothing is recorded as sold or paid.

  *Example:* A customer realises he forgot his wallet and leaves; the cashier cancels the sale.
- **UC-004.7a** The card is declined, or the payment authorization service does not answer within 30 seconds:
  1. The system says the payment isn't authorized. Nothing is recorded as paid.
  2. The cashier asks the customer for another way to pay. Returns to step 6.

  *Example:* The customer's card is declined; she pays the 37.80 in cash instead.
- **UC-004.8a** The accounting or inventory system cannot be reached:
  1. The system keeps the completed sale at the checkout and sends it when the system is back (BR-3).
  2. Continues at step 9. The cashier carries on as usual.

  *Example:* The inventory system is down for maintenance; the sale is kept and reaches inventory an hour later.
- **UC-004.8b** The sale cannot be recorded at the checkout after the card was authorized:
  1. The system cancels the authorization with the payment authorization service (BR-7) and says the sale was not completed.
  2. Returns to step 6.

  *Example:* The checkout's storage fails while recording a paid sale; the system cancels the 37.80 authorization and the cashier takes the payment again once recording works.
- **UC-004.9a** The receipt printer fails:
  1. The system says the receipt could not be printed. The sale stays recorded.
  2. The receipt is kept so it can be printed again once the printer works (reprinting a receipt is its own use case). The use case ends.

  *Example:* The printer is out of paper; the cashier reloads it and reprints the receipt.
- **`UC-004.*a`** The store manager steps in for an override, such as a price override:
  1. The system switches to manager mode. The manager does what is needed.
  2. The system logs the override with the manager and the time (BR-6), and switches back to the cashier.
  3. Returns to the step where the override started.

  *Example:* The manager overrides the price of a dented tin from 3.00 to 2.00, and the cashier carries on.
- **`UC-004.*b`** The checkout crashes or restarts in the middle of a sale:
  1. On restart, the system restores the open sale with the items entered so far.
  2. If a card authorization was pending, the system asks the payment authorization service for its outcome before marking the sale paid. If it was authorized, continues at step 8; if not, or the outcome is unknown, nothing is recorded as paid and returns to step 6.
  3. Otherwise, returns to the step where the sale stopped.

  *Example:* The checkout loses power during authorization; on restart the service confirms the 37.80 payment and the sale is recorded once.

## Technology and data variations

- Step 2: the item identifier is read by barcode scanner, typed on the keyboard, or read by camera.
- Step 2: one item at a time, or one item with a quantity.
- Step 6: card payment by physical card or mobile wallet; cash payment.
- Step 9: printed receipt; a digital receipt (for example by email) is a later variation and would bring personal data into this use case.

## Related information

- **Frequency:** All day during opening hours, a sale every few minutes at each checkout.
- **Business rules:**
  - BR-1: No sale is completed without taxes worked out by the tax calculator.
  - BR-2: A sale is recorded as paid only when the payment is confirmed: the card authorized, or cash tendered of at least the total.
  - BR-3: A completed sale is never lost. It is kept at the checkout until accounting and inventory have received it.
  - BR-4: The price charged for an item is the price shown when it was entered.
  - BR-5: Discount rules apply to the total when the customer is identified, before taxes are worked out.
  - BR-6: Every item removal and manager override is logged with who did it and when.
  - BR-7: The customer's card is never charged without a recorded sale. If the sale cannot be recorded after authorization, the authorization is cancelled.
  - BR-8: The customer's identity is not stored with the sale; only the discount applied is.
  - BR-9: The receipt shows the store, sale number, date and time, cashier, items with quantities and prices, discounts, taxes, total, payment method (masked card number and authorization reference, or cash tendered and change).
- **Open issues:**
  - Recommendations to confirm with the product owner (all "not decided" in the interview): kind of store and fixed checkout terminal; catalogue held at the checkout; item with no price handled by a manager override; cashier can remove items without the manager before step 4; price override as a manager override; loyalty card as the way to identify the customer, with customer records in an external loyalty system and discount rules in the point-of-sale application; customer identity not stored with the sale; receipt contents and printed-only delivery; printer failure handling; recovery of an unfinished sale after a restart.
  - Timeouts: 10 s for the tax calculator, 30 s for card authorization, 5 s for the loyalty system. Card authorization normally takes a few seconds, but a 30 s timeout means the worst case is a long step.
  - Split payment across card and cash (UC-004.6c).
  - Whether there is a limit on items or amount per sale; none is assumed.
  - Whether auditors are a stakeholder in their own right.
