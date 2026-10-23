**Q1.** What is the app (the system under design) and who is the Purchaser? For example, is it a personal portfolio-tracking app used by an individual investor, and must the Purchaser already be signed in and hold an account at the brokerage before starting?

**A1.** The app is our personal finance app, not specifically a portfolio tracker. It does keep a portfolio, which the purchase updates. The Purchaser is an app user who has decided to buy stocks. Yes, they must already be signed in to the app before they start.

Not decided: whether the Purchaser must already hold a brokerage account before starting. Use your recommendation.

**Q2.** Step 2 says the app connects to the brokerage 'while keeping control of the session'. What does keeping control mean in practice: does the Purchaser trade inside a window the app hosts and can return from at any time, and what must the app remember about the session (for example, which purchase it is waiting for)?

**A2.** Partly. The app connects either through an embedded session on the brokerage's site, which it hosts, or through the brokerage's API. So the buyer trades in a window the app hosts only in the embedded case. The app keeps control of the session so it can pick up what the brokerage sends back. If the buyer gives up before buying, the app closes the brokerage session if there is one.

Not decided: whether the buyer can return from the window at any time. Use your recommendation.

Not decided: what the app must remember about the session, including which purchase it is waiting for. Use your recommendation.

**Q3.** What happens if the brokerage cannot be reached, or the connection drops after the Purchaser has bought but before the app has captured the confirmation? Is there a way for the app to recover the confirmation later, and how should the Purchaser be told?

**A3.** **Brokerage can't be reached, before buying:** The app reports that the connection failed and advises what to do. The buyer can retry with the same brokerage or another, or give up. The portfolio stays as it was.

**Connection drops after buying, before the confirmation is captured:** Not decided: whether the app recovers the confirmation later. Most likely the app checks with the brokerage the next time it starts, as it would for a put-off or incomplete purchase, but that's still open. Whatever happens, we log enough to notice that the purchase went wrong and to ask the buyer for its details.

**How the buyer is told:** Not decided: the message for this case. Use your recommendation. The put-off message doesn't carry over, since the brokerage has not said the purchase is pending.

**Q4.** You mentioned put-off and incomplete purchases. What outcomes can the brokerage send back besides a completed purchase (for example: order pending because the market is closed, partly filled, rejected for insufficient funds), and how should the app handle each in the portfolio and with the Purchaser?

**A4.** - **Put off (e.g. pending because the market is closed): yes.** The app logs it as pending and leaves the portfolio alone. It tells the buyer the brokerage hasn't confirmed the purchase and that the app will ask them later how it turned out. Following up is a separate job.
- **Incomplete (the brokerage doesn't send back something needed to record it, such as the price):** the app logs what's missing and asks the buyer for it there and then. Once they give it, the purchase is recorded and the updated portfolio is shown.
- **Partly filled:** Not decided. Use your recommendation.
- **Rejected, e.g. for insufficient funds:** Not decided. Use your recommendation.

**Q5.** In step 1, what is a 'supported brokerage' and what happens if the Purchaser's brokerage isn't on the list? Also, can the Purchaser buy several stocks in one session at the brokerage, and should the app record each purchase separately?

**A5.** A supported brokerage is one the app works with. We only work with the brokerages on that list, and the buyer can name one that isn't on it.

If the buyer names a brokerage we don't support, the app says so and asks for another. They can pick another or cancel.

Not decided: whether the buyer can buy several stocks in one session at the brokerage. Use your recommendation.

Not decided: whether the app records each of those purchases separately. Use your recommendation.

**Q6.** When the app updates the portfolio and logs the transaction (step 5), what must be recorded (stock, quantity, price, fees, brokerage, time, order reference?), and what if the confirmation names a purchase that is already in the portfolio, or the portfolio update fails after the purchase is logged?

**A6.** **Recorded fields:** Not decided: the full list of fields. The price is required: if the brokerage doesn't send it, the app logs what's missing and asks the buyer for it before recording the purchase. Not decided: stock, quantity, fees, brokerage, time, and order reference. Use your recommendation.

**Confirmation for a purchase already in the portfolio:** Not decided. Use your recommendation.

**Portfolio update fails after the purchase is logged:** We log enough to notice that a purchase went wrong and to ask the buyer for its details. Not decided: how the portfolio update itself is retried or shown. Use your recommendation.

**Q7.** Who else cares how this goes (for example the brokerage, the company running the app, a regulator or auditor), and are there any rules or limits on purchases: amounts, number of brokerages per user, how long the app keeps the transaction log, or whether the Purchaser can ask to export or erase their transaction data?

**A7.** - **Who else cares:** The brokerage cares, since it wants complete information about the purchase. Regulator or auditor: Not decided. Use your recommendation.
- **Amount limits:** Not decided. Use your recommendation.
- **Brokerages per user:** Not decided: how many brokerages a user may connect. Use your recommendation. Only supported brokerages can be used.
- **Transaction log retention:** Not decided. Use your recommendation.
- **Export or erase of transaction data:** Not part of buying. Exporting or erasing holdings is a separate account privacy job.

**Q8.** If the Purchaser fails to sign in at the brokerage, or leaves the brokerage without buying anything, what should the app do and say? And roughly how often do you expect users to buy stocks through the app?

**A8.** If the connection can't be set up, including because sign-in fails, the app reports it with advice on what to do. The buyer can try again with the same brokerage or another, or give up. Sign-in itself is checked by the brokerage in its own session, so the app only handles the connection result.

If the buyer leaves without buying, the app closes the brokerage session if there is one, and the portfolio stays as it was. Not decided: the exact wording the app uses when they give up. Use your recommendation.

Users buy stocks through the app a few times a month each.

