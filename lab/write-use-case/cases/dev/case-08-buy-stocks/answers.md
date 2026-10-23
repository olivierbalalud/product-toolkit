# Answers: buy stocks over the web

## Actor, goal and scope

- The system is our personal finance app; the brokerage is outside it.
- The person buying is an app user, and they start simply because they've decided to buy stocks.
- Before they start they're already signed in to the app.
- The brokerage is the one outside party involved: they buy at it, and it confirms the purchase or puts it off.
- We only work with the brokerages the app supports; they can name one we don't.
- The app can connect either through an embedded session on the brokerage's site or through the brokerage's API.
- It happens a few times a month per user.
- Following up on a purchase the brokerage hasn't confirmed yet is a separate job, not part of buying.

## Stakeholders and guarantees

- The buyer wants their stocks to show up in their portfolio without typing them in.
- The brokerage wants complete information about the purchase.
- Whatever happens, we log enough to notice that a purchase went wrong and to ask the buyer for its details.
- When it works: the brokerage has confirmed the purchase, it's in the log and the portfolio, and the buyer has seen the updated portfolio.

## Main scenario

- The buyer names the brokerage at the same time as asking to buy.
- The app stays in control of the brokerage session so it can pick up what the brokerage sends back.
- Logging the purchase, updating the portfolio and showing it all happen together once the confirmation comes in.

## What can go wrong

- They name a brokerage we don't support.
- The connection to the brokerage can't be set up.
- They give up before buying anything, either before connecting or while browsing at the brokerage.
- Their phone or computer crashes or is switched off in the middle of the purchase.
- The brokerage doesn't confirm the purchase and puts it off instead.
- The brokerage doesn't send back everything we need to record the purchase, such as the price.

## How each is handled

- Unsupported brokerage: the app says so and asks for another; they pick another or cancel.
- Connection fails: the app reports it with advice on what to do; they try again, with the same brokerage or another, or give up.
- Giving up before buying: the app closes the brokerage session if there is one, and the portfolio stays as it was.
- Crash or switched off mid-purchase: we haven't decided. Most likely the app checks with the brokerage the next time it starts, like for a put-off or incomplete purchase, but that's still open.
- Brokerage puts the purchase off: the app logs it as pending, doesn't touch the portfolio, and tells them the brokerage hasn't confirmed it yet and that the app will ask them later how it turned out. That's where this ends; the follow-up is the separate job.
- Missing information: the app logs what's missing and asks them for the missing details there and then; once they give them, the purchase is recorded and the updated portfolio is shown.

## Durations

- Opening the session with the brokerage takes a few seconds.
- Picking up the confirmation, logging it and updating the portfolio is immediate.

## Out of scope

- A wrong or invalid order: the brokerage checks the order in its own session, and the app only sees the result.
- Signing in at the brokerage and whether they're allowed to trade: that's the brokerage's to check, in its own session.
- Exporting or erasing their holdings: that's a separate account privacy job, not part of buying.
