# Answers: process a sale

## Actor, goal and scope

- The system is our point-of-sale application at the checkout.
- It starts when a customer comes to the checkout with goods to buy.
- Before they start, the cashier is already identified and logged in.
- Outside the application, it relies on a payment authorization service for cards, a tax calculator, and our accounting and inventory systems, which get every completed sale.
- The customer takes part when paying, and the store manager steps in for overrides.
- Items can be entered by barcode, typed on a keyboard, or read by a camera.
- Cards can go through the card reader, contactless, or a mobile wallet.
- It runs all day during opening hours: a sale every few minutes at each checkout.

## Stakeholders and guarantees

- The cashier wants fast, accurate entry and no payment mistakes, because shortages come out of their pay.
- The customer wants a quick checkout, correct prices, and proof of purchase in case they return something.
- The retailer wants accurate records, every payment captured, and to keep selling when back-end services are down.
- The store manager wants to be able to do overrides quickly.
- The tax authorities want tax collected on every sale.
- The payment authorization service wants requests in the format it expects.
- Whatever happens, a sale is never recorded as paid unless the payment is confirmed, and a completed sale is never lost.
- When it works: the sale is saved with its items, the right taxes, the payment and its authorization, and the cashier's commission; accounting and inventory have it, or it's kept to be sent to them; and the customer gets a receipt.

## Main scenario

- The cashier enters one item identifier at a time; for each one the system shows the description, the price and the running total.
- The tax calculator works out the taxes once all the items are in.
- Card is the usual way to pay; cash is the other one.
- Recording the sale includes the payment authorization and the cashier's commission.

## What can go wrong

- The item identifier isn't valid.
- The customer leaves without paying, or the cashier cancels the sale, before the payment goes through.
- The tax calculator doesn't answer.
- The card is declined, or the payment authorization service doesn't answer.
- The accounting or inventory system can't take the sale.
- Not failures, but other paths: the customer buys several of the same item, the customer qualifies for a discount, the customer pays cash, and the store manager can step in at any moment for an override.

## How each is handled

- Invalid identifier: the system flags it and rejects the entry, and the cashier enters the item again.
- Cancelled or abandoned sale: the sale is thrown away; nothing is recorded as sold and nothing goes to accounting or inventory.
- Tax calculator not answering: the system says it can't work out the taxes and keeps the sale open; the cashier tries again or cancels the sale. We don't sell without tax.
- Card declined or the service not answering: same handling for both. The system says the payment isn't authorized, nothing is recorded as paid, and the cashier asks for another way to pay.
- Accounting or inventory unavailable: the system keeps the sale locally and sends it on when that system is back; the cashier carries on and gives the receipt as usual.
- Several of the same item: the cashier enters the quantity with the item.
- Discount: the cashier identifies the customer and the system applies the discount rules to the total.
- Cash: the cashier enters the amount handed over and the system shows the change due.
- Override: the system switches to manager mode, the manager does what's needed, then it switches back to the cashier.

## Durations

- Recording each item and showing the running total is immediate.
- Working out the total with taxes is immediate.
- Getting a card payment authorized takes a few seconds.
- Recording the sale, sending it to accounting and inventory, and producing the receipt are immediate; the cashier never waits on the back-end systems.

## Out of scope

- What the customer hands over at payment isn't checked as a separate case: a card problem shows up as a declined payment, and cash is counted by the cashier.
- Entering the same item twice isn't a mistake case; it just adds another unit.
- The customer's right to export or erase their data is a separate job; the only personal data here is the customer identified for a discount and the card details, which go only to the payment authorization service.
