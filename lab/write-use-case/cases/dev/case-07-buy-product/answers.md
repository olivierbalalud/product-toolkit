# Answers: buy a product

## Actor, goal and scope

- The system is our online store; the one doing the buying is the customer.
- It starts when the customer decides to buy one or more products.
- Before they start, the catalog is already published; that's someone else's job.
- Two outside parties take part: the payment provider, which authorizes the payment and handles the card issuer's extra authentication, and a notification service that sends the confirmation email.
- Customers can check out as guests or signed in.
- They can pay by card, digital wallet or bank transfer. By bank transfer we mean a payment they authorize with their bank during checkout, so it's authorized in seconds like a card; we don't take transfers that arrive days later.
- It happens many times a day; it's the store's main transaction, with peaks during sales.

## Stakeholders and guarantees

- The customer wants the right items at the price they were shown, delivered the way they chose, and never to be charged twice.
- The merchant wants to be paid and to have the order captured for fulfillment.
- Fulfillment needs complete shipping information.
- The payment provider wants to receive valid authorization requests.
- Whatever happens, a customer is never charged unless an order is recorded, and never charged twice for the same order.
- An order is never confirmed unless the payment is authorized.
- When it works: the order is recorded with its items, shipping details and full price, the payment for that price is authorized, the customer sees the confirmation and gets it by email, and the order is queued for fulfillment with complete shipping details.

## Main scenario

- Choosing the items and asking to check out is one move for the customer.
- The shipping details are the address and the delivery speed.
- The full price includes the items, the shipping for the chosen speed, and taxes.
- Giving the payment details is when the customer places the order; there's no separate review step after it.
- The payment is authorized for exactly the full price we showed.
- Once the payment is authorized, the order is recorded, queued for fulfillment and confirmed to the customer on the spot; the email follows.
- A returning customer who is signed in gets their stored shipping details and card proposed, with only the card's last four digits shown, along with the price. They accept or change any of it and place the order. If they change the shipping, they see the updated price before placing it.

## What can go wrong

- The shipping address is incomplete, or it's somewhere we don't deliver.
- An item went out of stock between choosing it and seeing the full price.
- The payment is declined: an expired card, wrong details, a refusal.
- The customer places the same order twice before it's confirmed.
- The card issuer asks for strong customer authentication.
- The payment provider doesn't answer, or we can't record the order after the payment was authorized.
- Someone else buys the last units of an item after we showed the customer the price and before their order goes through.
- The customer gives up before placing the order.

## How each is handled

- Bad address: we say what's missing or that we don't deliver there; they correct it or cancel.
- Out of stock at the price step: we say which item; they remove it or swap it, and see the price again.
- Declined payment: no order is recorded, we tell them it was declined, and they give other payment details or cancel. Cancelling leaves nothing recorded and nothing charged.
- Placed twice: we process and charge it once.
- Strong authentication: the customer completes the card issuer's challenge and the authorization carries on.
- Provider not answering, or the order not recorded after authorization: no order is recorded and we have the payment provider cancel any authorization, so they aren't charged. We tell them the order wasn't placed and keep their items and shipping details; they try again, pay another way, or cancel.
- Sold out at the last moment: we check stock before asking for authorization, so nothing is authorized or recorded; we say which item sold out, they remove or swap it, and see the price again.
- Giving up before placing the order: nothing is recorded and nothing is charged.

## Durations

- Showing the full price is immediate.
- Getting the authorization, recording and confirming the order takes a few seconds, while the customer waits.
- Handing the email to the notification service is immediate.

## Out of scope

- The confirmation email failing to go out: the order is already confirmed on screen, and delivering the email once it's handed over is the notification service's job.
- Permissions: anyone can buy, as a guest or signed in, so there's nothing to refuse.
- Limits on quantities or order size: we don't have any.
- Working out the price doesn't call any outside service.
- Exporting or erasing the customer's personal data: that's a separate account privacy job, and we have to keep order records for accounting, which limits erasure.
