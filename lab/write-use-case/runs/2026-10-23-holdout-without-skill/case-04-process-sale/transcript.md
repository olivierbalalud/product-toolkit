**Q1.** Who uses this system and in what setting: what kind of store, and is the cashier at a fixed checkout terminal? What is the system under design: the point-of-sale application only, or also the accounting and inventory back ends?

**A1.** **Users and setting:** The cashier is the main user. They are already identified and logged in at the checkout. The customer takes part when paying, and the store manager steps in for overrides. The system runs all day during opening hours, with a sale every few minutes at each checkout.

- **Kind of store:** Not decided: what kind of store. Use your recommendation.
- **Fixed terminal:** Not decided: whether the cashier works at a fixed checkout terminal. Use your recommendation.

**System under design:** Only the point-of-sale application at the checkout. Accounting and inventory are external systems that receive every completed sale, so they are not part of the design. The payment authorization service and the tax calculator are also external.

**Q2.** How does the cashier enter an item (scan a barcode, type a code, quantity)? What happens if an item code is not recognised or has no price? Can the cashier remove an item already entered, and does that need the manager?

**A2.** The cashier enters one item identifier at a time, by barcode, by typing it on the keyboard, or by camera read. For several of the same item, the cashier enters the quantity with the item.

Not decided: what happens when an item has no price. Use your recommendation.

Not decided: whether the cashier can remove an item already entered, and whether that needs the manager. Use your recommendation. (Cancelling the whole sale is possible, but that's a separate case.)

**Q3.** What happens when an entered identifier is not found in the catalogue? And how are taxes computed: is the external tax calculator called once at the total, and what happens if it is down or slow?

**A3.** **Unknown identifier:** Yes, this is the invalid-identifier case. The system flags it and rejects the entry, and the cashier enters the item again.

**Taxes:** Yes, the tax calculator is called once, when all the items are in, to work out the taxes for the total.

**Calculator down:** The system says it can't work out the taxes and keeps the sale open. The cashier either tries again or cancels the sale. We don't sell without tax.

**Calculator slow:** Not decided: how a slow calculator that still answers is handled. Use your recommendation.

**Q4.** Which payment methods are accepted (cash, card, other), and can the customer split payment across methods? For card payments, what happens when authorization is declined, and when the payment service is down or times out?

**A4.** Two methods are accepted: card and cash. Mobile wallet is a way of paying by card, not a separate method, and no other method is mentioned.

Not decided: whether the customer can split payment across methods. Use your recommendation.

If the card is declined, the system says the payment isn't authorized, nothing is recorded as paid, and the cashier asks for another way to pay.

If the payment service doesn't answer, it's handled the same way as a decline: the system says the payment isn't authorized, nothing is recorded as paid, and the cashier asks for another way to pay.

**Q5.** For cash: does the system compute change from the amount tendered, and what if the amount is less than the total? Also, how long may card authorization take before it counts as not answering?

**A5.** Yes, for cash the cashier enters the amount handed over and the system shows the change due.

Not decided: what happens when the amount tendered is less than the total. Use your recommendation.

Not decided: how long card authorization may take before it counts as not answering. Normally it takes a few seconds. Use your recommendation.

**Q6.** After payment is authorized, what happens if accounting or inventory cannot be reached when the sale is recorded? Is the sale still completed and sent later, and must the customer's card never be charged without a recorded sale?

**A6.** Yes. The sale is still completed. The system keeps it locally and sends it to accounting and inventory when they are back. The cashier carries on and gives the receipt as usual.

Not decided: whether the card may be charged without a recorded sale. Use your recommendation.

**Q7.** What does the receipt contain, is it printed or can it be sent digitally (e.g. by email, which would involve personal data), and what happens if the printer fails? When exactly does the store manager step in for overrides, for example price overrides or discounts?

**A7.** - **Receipt contents:** Not decided: receipt contents. Use your recommendation.
- **Printed or digital:** Not decided: printed or digital delivery, and whether email is used. Use your recommendation.
- **Printer failure:** Not decided: what happens if the printer fails. Use your recommendation.
- **When the store manager steps in:** At any moment the manager can step in for an override. The system switches to manager mode, the manager does what's needed, and then the system switches back to the cashier.
- **Price overrides and discounts:** Discounts are not a manager step. The cashier identifies the customer, and the system applies the discount rules to the total. Whether a price override is handled the same way as other overrides is not decided. Use your recommendation.

**Q8.** How does the cashier identify the customer for discounts (loyalty card, phone number, ID?), where do customer data and discount rules come from, and what if the customer is not found? Is the customer's identity stored with the sale?

**A8.** - **How the cashier identifies the customer (loyalty card, phone number, or ID):** Not decided: how the cashier identifies the customer. Use your recommendation.
- **Where customer data and discount rules come from:** Not decided: where customer data and discount rules come from. Use your recommendation.
- **What happens if the customer is not found:** Not decided: what happens when the customer is not found. Use your recommendation.
- **Whether the customer's identity is stored with the sale:** Not decided: whether the customer's identity is stored with the sale. Use your recommendation. The sale is saved with its items, taxes, payment and authorization, and the cashier's commission, and the customer is not among those.

**Q9.** What should happen if the checkout terminal crashes or restarts in the middle of a sale: is the open sale recovered? And who else cares about the outcome (for example the cashier for their commission, auditors, tax authority), and what do they need protected?

**A9.** **Is the open sale recovered?** Not decided: whether an unfinished sale is recovered after a crash or restart. Use your recommendation. Two facts do bound it: a completed sale is never lost, and a sale is never recorded as paid unless the payment is confirmed. So a crash during card authorization must not leave the sale marked as paid.

**Who else cares, and what they need protected:**
- **Cashier:** the sale must carry their commission, and entries must be accurate, since shortages come out of their pay.
- **Customer:** correct prices, and proof of purchase in case they return something (the receipt).
- **Retailer:** accurate records, every payment captured, and completed sales reaching accounting and inventory, or kept until they can.
- **Tax authorities:** tax collected on every sale.
- **Payment authorization service:** requests in the format it expects.
- **Auditors:** Not decided: whether auditors are a stakeholder and what they need protected. Use your recommendation.

**Q10.** Is the product catalogue with prices held by the point-of-sale application itself or by an external system, and what happens if it cannot be reached while items are being entered? Is there any limit on items or amount per sale?

**A10.** Not decided: where the product catalogue with prices is held. Use your recommendation.

Not decided: what happens if the catalogue cannot be reached while items are being entered. Use your recommendation.

Not decided: whether there is any limit on items or amount per sale. Use your recommendation.

