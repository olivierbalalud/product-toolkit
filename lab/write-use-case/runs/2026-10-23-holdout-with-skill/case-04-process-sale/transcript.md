**Q1.** First, the boundary. I'd set it as follows: the system under design is the point-of-sale system at the register; the payment authorization service, the accounting system and the inventory system are outside systems it calls (supporting actors); the customer is a stakeholder who hands over the payment but doesn't use the system; and the only precondition is that the cashier is signed in at an open register. Agreed, or what would you change?

**A1.** Mostly agreed, with three corrections:

- **System under design:** Yes, the point-of-sale application at the checkout.
- **Outside systems:** Yes for the payment authorization service, accounting, and inventory. You left out the **tax calculator**, which is also an outside system the sale depends on.
- **Customer:** Partly. The customer takes part when paying, and the cashier identifies them for discounts. Whether the customer ever operates the system directly is not decided. Use your recommendation.
- **Precondition:** Partly. The cashier is already identified and logged in before the sale starts. Whether the register must be "open" is not decided. Use your recommendation.

**Q2.** When does the sale end for the cashier? I'd say once the payment is authorized, the sale is recorded and the receipt is issued, all while the customer is at the counter; accounting and inventory are updated by the system in the same step without the cashier waiting on them (if either is unreachable, the system keeps the update and sends it later). Nothing waits for another person. Agreed?

**A2.** Mostly yes, with two corrections:

1. The sale also ends for the cashier when it is cancelled or abandoned before the payment goes through. It is thrown away and nothing is recorded or sent on.
2. "Nothing waits for another person" is not quite right. The store manager can step in at any moment for an override, and then the system switches to manager mode until the manager is done. That is an interruption, not part of the main path.

The rest is right. Recording includes the payment authorization and the cashier's commission, and accounting and inventory are never waited on: if either is unavailable, the system keeps the sale and sends it when that system is back.

**Q3.** Stakeholders. My candidates: the cashier (fast, accurate entry; no payment mistakes they'd have to cover; their commission credited); the customer (correct prices, quick service, a receipt as proof of purchase, discounts they're entitled to); the store manager (can step in quickly for an override); the company (every sale recorded accurately, payment authorizations recorded, no sale lost when accounting or inventory is down); the tax authorities (correct tax collected on each sale); the payment authorization service (requests it can process, and an accurate record of what it owes the store). Which would you add or drop, or change?

**A3.** Nothing to add or drop. Change one name and one wording:

- **Company** should be **retailer**. Add that it wants to keep selling when back-end services are down. Your wording covers only that no sale is lost.
- **Cashier, customer, store manager, tax authorities:** yes, as written.
- **Payment authorization service:** requests in the format it expects, yes. Not decided: an accurate record of what it owes the store. Use your recommendation.

**Q4.** Guarantees. Minimal (however it ends): no sale is half-recorded, and a sale cancelled before payment leaves nothing recorded or sent on. Success: the sale is recorded with its items, taxes, payment authorization and the cashier's commission; accounting and inventory have it, or have it queued to send when they are back; the customer has the receipt. Correct?

**A4.** Yes for the success case and the cancelled sale. Whatever happens, a sale is never recorded as paid unless the payment is confirmed, and a completed sale is never lost. A cancelled sale is thrown away, with nothing recorded as sold and nothing sent to accounting or inventory.

Not decided: that no sale is half-recorded. Use your recommendation.

**Q5.** Here is the main scenario as I'd write it. Trigger: a customer comes to the checkout with items to buy, and the cashier starts a new sale.
1. (actor) The cashier enters each item and its quantity.
2. (system) The system presents each item's description and price, and the running total.
3. (actor) The cashier identifies the customer, for the discounts they are entitled to.
4. (system, wait: a few seconds) The system gets the taxes from the tax calculator, applies the customer's discounts and presents the total due.
5. (actor) The cashier enters the customer's payment.
6. (system, wait) The system gets the payment authorized, records the sale with the authorization and the cashier's commission, sends it on to accounting and inventory, and issues the receipt.
Does that match, in particular the place of the customer identification (before the total) and the durations?

**A5.** **Partly.** Identifying the customer before the discount is applied to the total matches. The durations don't match.

- **Customer identification:** The discount rules apply to the total, so the customer has to be identified before that. Your order does this. The facts don't say when the total is first shown, so step 4 can stay as written.
- **Step 4 wait:** Remove "a few seconds." Working out the total with taxes is immediate. The wait applies only to card authorization, in step 6.
- **Step 6 wait:** Only the authorization takes a few seconds. Recording the sale, sending it to accounting and inventory, and producing the receipt are immediate. The cashier never waits on those back-end systems.

**Q6.** Payment. I'd write card payment as the main path (authorization takes a few seconds), and cash as an alternative at step 5: the cashier enters the cash handed over, the system works out the change and skips the authorization. Which payment methods does the sale accept: card and cash only, or others too (cheque, gift card, splitting one sale across two methods)?

**A6.** **Card and cash only, as far as the facts go.** Card is the usual way to pay and cash is the other.

- **Cheque and gift card:** Not decided: cheque and gift card. Use your recommendation.
- **Splitting one sale across two methods:** Not decided: splitting one sale across two methods. Use your recommendation.
- **Cash at the payment step:** Yes. The cashier enters the amount handed over and the system shows the change due.
- **Skipping authorization for cash:** Not decided: whether cash skips the payment authorization. Use your recommendation.

**Q7.** Business rules the sale enforces. I have one so far: the retailer's discount rules decide the customer's discounts, applied to the total (step 4). Are there others the steps apply, for example what needs a manager override (a price change, removing an item, a refund), a limit on quantity, or an amount above which cash isn't accepted?

**A7.** Yes, the discount rule is as you describe. The cashier identifies the customer, and the system applies the discount rules to the total. The facts don't number the steps.

Other rules the steps apply:
- **No sale without tax:** if the tax calculator doesn't answer, the sale stays open. We don't sell without tax.
- **Never paid unless confirmed:** nothing is recorded as paid unless the payment is confirmed.
- **No lost sales:** a completed sale is never lost. If accounting or inventory is unavailable, the system keeps it locally and sends it when they're back.
- **Cash change:** the cashier enters the amount handed over and the system shows the change due.

On your specific questions:
- **Manager override:** the store manager can step in at any moment for an override, and the system switches to manager mode. Which actions require one is not decided: price change, removing an item, and refund. Use your recommendation.
- **Quantity limit:** the cashier enters the quantity with the item. A maximum quantity is not decided. Use your recommendation.
- **Cash cap:** a maximum amount above which cash isn't accepted is not decided. Use your recommendation.

**Q8.** Conditions at the cashier's steps. I see: at item entry, an item the system doesn't recognise, and the cashier noticing a wrong item or quantity before paying; at customer identification, a customer the system can't find, or one who doesn't want to be identified; at payment, a card declined by the authorization service, or cash handed over that is less than the total; at any of these steps until the payment goes through, the customer or cashier cancelling the sale; and the manager stepping in for an override at any moment. What else can go wrong or differ there, and which of these can't happen?

**A8.** **Item entry**
- Unrecognised item: yes. The system flags it and rejects the entry, and the cashier enters the item again.
- Wrong item or quantity noticed before paying: Not decided: how to correct a wrong item or quantity. Use your recommendation. Entering the same item twice isn't a mistake case; it just adds another unit. The cashier can cancel the whole sale (see below).

**Customer identification**
- Customer the system can't find: Not decided: what happens when the customer can't be found. Use your recommendation.
- Customer who doesn't want to be identified: Not decided: whether a customer can refuse identification. Use your recommendation. Identification only matters for a discount, where the cashier identifies the customer and the system applies the discount rules.

**Payment**
- Card declined by the authorization service: yes. The system says the payment isn't authorized, nothing is recorded as paid, and the cashier asks for another way to pay.
- Cash less than the total: this isn't handled as a separate case. The cashier counts the cash, and the system only shows the change due for the amount handed over.

**Cancellation before the payment goes through**
- Yes, from the customer or the cashier. The sale is thrown away, nothing is recorded as sold, and nothing goes to accounting or inventory.

**Manager override at any moment**
- Yes. The system switches to manager mode, the manager does what's needed, and then it switches back to the cashier.

**Other things that can go wrong or differ there**
- The tax calculator doesn't answer once the items are in: the system says it can't work out the taxes and keeps the sale open. The cashier retries or cancels. We don't sell without tax.
- The authorization service doesn't answer: handled the same way as a declined card.
- Several of the same item: the cashier enters the quantity with the item.
- A discount: applied to the total after the customer is identified.

**What can't happen**
- A declined card or a cancelled sale can't be recorded as paid or sold, because a sale is never recorded as paid unless the payment is confirmed.
- A cancelled sale can't reach accounting or inventory.
- A sale can't be completed without tax.

**Q9.** Conditions at the system's steps. Besides the tax calculator and the authorization service not answering, and accounting or inventory being unavailable when the sale is recorded (kept and sent later), I see three candidates: the receipt can't be produced (say the printer is out of paper) after the sale is recorded; the payment is authorized but the sale can't be recorded at the register; and an item's price changing in the catalogue while the sale is open. Which of these can happen, and is there anything else at those steps?

**A9.** - **Receipt can't be produced after the sale is recorded (e.g. printer out of paper):** Not decided: whether this can happen and how it's handled. Use your recommendation. A completed sale is never lost, and producing the receipt is immediate.
- **Payment authorized but the sale can't be recorded at the register:** Not decided: whether this can happen and how it's handled. Use your recommendation. A completed sale is never lost, and a sale is never recorded as paid unless the payment is confirmed.
- **An item's catalogue price changes while the sale is open:** Not decided. Use your recommendation.
- **Anything else at those steps:** Not decided. Use your recommendation.

**Q10.** How often does this happen: roughly how many sales per register or per store in a day, and is there a peak?

**A10.** A sale every few minutes at each checkout, during opening hours.

Not decided: sales per store per day. Use your recommendation.

Not decided: whether there is a peak. Use your recommendation.

**Q11.** Privacy. Identifying the customer links them to their purchases, which is personal data. I'd say the customer can ask to export or erase it, but that request is handled by a separate customer-data privacy use case, not during the sale. Agreed?

**A11.** Yes, the export and erase right is a separate job, not part of this sale. The only personal data in this use case is the customer identified for a discount and the card details, and the card details go only to the payment authorization service.

