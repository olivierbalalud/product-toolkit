**Q1.** Boundary first. I'd treat this as one sitting: the Purchaser places the order at the brokerage and the brokerage confirms the purchase at once, so the use case ends with the updated portfolio shown. If an order can be left pending at the brokerage (e.g. a limit order or market closed), I'd end the use case at the hand-over and make the later fill its own use case. Does the brokerage confirm at once, and is that the right boundary?

**A1.** No. The brokerage either confirms the purchase or puts it off, so it doesn't always confirm at once. If it confirms, the use case runs to the updated portfolio being shown. If it puts the purchase off, the app logs it as pending, leaves the portfolio alone, and tells the buyer the brokerage hasn't confirmed it and the app will ask later how it turned out. Your boundary is right for that case: the use case ends at the put-off, and the follow-up is a separate job.

**Q2.** Boundary facts, to confirm together: (a) the app is the system under design and the brokerage is a supporting actor we call, not something we build; (b) precondition: the Purchaser is signed in to the app and already has an account at the chosen brokerage (opening a brokerage account is outside this use case); (c) the follow-up for a put-off purchase is a separate, time-triggered use case ('Check on a pending purchase'). Correct?

**A2.** Yes to (a) and (c), with one part of (c) not decided. Not decided on the account part of (b).

(a) Yes. The app is the system, and the brokerage is an outside party it connects to.

(b) Partly. The Purchaser is signed in to the app before starting. Not decided: whether the Purchaser already has an account at the chosen brokerage. Use your recommendation.

(c) Yes, the follow-up for a put-off purchase is a separate job, not part of buying. Not decided: whether it is time-triggered and what it is named. Use your recommendation.

**Q3.** Stakeholders. I see: the Purchaser (buys the stock they meant to, and the portfolio shows exactly what was bought); the brokerage (receives orders only through a session it controls); the app's owner (a record of every transaction, and never showing a purchase the brokerage didn't confirm); and whoever answers for personal data (portfolio and transactions are personal financial data). What should I add or drop, and what does each one need?

**A3.** **Keep and correct:**

- **Purchaser:** Mostly right. They want their stocks to show up in the portfolio without typing them in. The app doesn't check that the order is what they meant. The brokerage checks the order in its own session, and we only see the result.
- **Brokerage:** Not quite. The app stays in control of the brokerage session, so the brokerage doesn't control it. The brokerage wants complete information about the purchase, and it either confirms the purchase or puts it off.
- **App's owner:** Right that a purchase the brokerage hasn't confirmed never shows in the portfolio. A put-off purchase is logged as pending. The log's purpose is to notice when a purchase went wrong and to ask the buyer for missing details, so "a record of every transaction" is broader than what we've decided.

**Drop:**

- **Personal data owner:** Erasing or exporting holdings is a separate account privacy job, so it's out of scope for this use case. The facts don't say who answers for personal data, so Not decided: who answers for personal data, and what they need. Use your recommendation.

**Add:** Nothing. The follow-up on put-off purchases is a separate job, so it isn't a stakeholder here.

**Q4.** Guarantees. Minimal (true however it ends): the portfolio never shows a purchase the brokerage hasn't confirmed, and the attempt is logged so a purchase that went wrong can be noticed. Success: the purchased stock is in the Purchaser's portfolio, and the transaction is logged as confirmed by the brokerage. Agreed, or what would you change?

**A4.** Agreed. The facts support both guarantees as written:

- **Minimal:** The portfolio is updated only once the brokerage's confirmation comes in, so an unconfirmed purchase never reaches it. Whatever happens, we log enough to notice a purchase that went wrong and to ask the buyer for its details.
- **Success:** The confirmed purchase is in the portfolio, and it is logged along with the brokerage's confirmation.

**Q5.** Main scenario, rewritten in 4 steps: 1 (actor) the Purchaser asks to buy stocks and chooses a supported brokerage; 2 (system, wait: a few seconds) the system opens a session with the brokerage, keeping control of it; 3 (actor) the Purchaser buys the stock at the brokerage; 4 (system) the system captures the brokerage's confirmation, adds the purchase to the portfolio, logs it with the confirmation and shows the updated portfolio (instant). Are the durations right, and does the app enforce any rule of its own here (e.g. which brokerages are supported, any limit)?

**A5.** **Durations:** Yes. Opening the brokerage session takes a few seconds, and capturing the confirmation, logging it and updating the portfolio is immediate.

**App rules:** We only work with supported brokerages. Step 1 should say the Purchaser names a brokerage at the same time as asking to buy, and that it may be one we don't support. If it isn't supported, the app says so and asks for another; they can pick another or cancel.

**Limits:** Not decided: any limit on purchases. Use your recommendation.

**Q6.** Conditions at the Purchaser's own steps. Step 1: the brokerage named isn't supported (you covered this); the Purchaser gives up before the session opens. Step 3 (at the brokerage): the Purchaser leaves or closes the brokerage session without buying; the brokerage refuses the order (e.g. not enough funds, not signed in to the brokerage). What else can go wrong or differ at these two steps, and what should I drop?

**A6.** **Step 1 (before the session opens):** Nothing else goes wrong here beyond the unsupported brokerage you covered. If they give up before connecting, there is no session to close, and the portfolio stays as it was.

**Step 3 (at the brokerage):**
- **Leaves or closes the session without buying:** The app closes the brokerage session if there is one, and the portfolio stays as it was.
- **Brokerage refuses the order:** Not decided: how the app records and shows a refusal. Use your recommendation. The brokerage does its own checks in its own session, and the app only sees the result.
- **Crash or switched off mid-purchase:** Not decided. The most likely approach is that the app checks with the brokerage on next start, but that's still open.

**Drop from the app's scope:**
- Wrong or invalid orders. I read insufficient funds as one of these, since the brokerage checks it.
- Signing in at the brokerage, and whether the user is allowed to trade.

**Q7.** Conditions at the system steps. Step 2 (opening the session): the brokerage doesn't answer or is down. Step 4 (capturing the confirmation): the brokerage puts the purchase off (you covered this); the confirmation comes back with details missing (e.g. no price or quantity); the session drops before any confirmation arrives; the confirmation is captured but the portfolio can't be updated. What else can go wrong at these steps, and what should I drop?

**A7.** **Step 2 (brokerage doesn't answer or is down):** Covered. The app reports that the connection can't be set up, with advice on what to do. The buyer can try again with the same brokerage or another, or give up.

**Step 4 (capturing the confirmation):**
- **Brokerage puts the purchase off:** Covered. The app logs it as pending, leaves the portfolio alone, and tells the buyer it will ask later how it turned out.
- **Confirmation comes back with details missing (e.g. no price or quantity):** The app logs what's missing and asks the buyer for those details right then. Once they give them, the purchase is recorded and the updated portfolio is shown.
- **Session drops before any confirmation arrives:** Not decided: what happens when the session drops without a device crash. The crash or switched-off case is still open; most likely the app checks with the brokerage the next time it starts. Use your recommendation.
- **Confirmation is captured but the portfolio can't be updated:** Not decided: how a failed portfolio update is handled. Use your recommendation.

**Other things that can go wrong at these steps:** Not decided: any failure conditions beyond the ones listed. Use your recommendation.

**What to drop:**
- A wrong or invalid order. The brokerage checks it in its own session; the app only sees the result.
- Signing in at the brokerage and whether the buyer is allowed to trade. That's the brokerage's check.
- Exporting or erasing holdings. That's a separate account privacy job.
- Following up on a purchase the brokerage hasn't confirmed. That's a separate job, not part of buying.

**Q8.** Handling at step 4, my recommendations, to confirm together: (a) the brokerage reports it refused the purchase: the app logs the refusal, leaves the portfolio alone, closes the session and tells the buyer the brokerage didn't make the purchase; the use case ends. (b) The session drops before any confirmation: handled like a put-off: logged as pending, portfolio untouched, the buyer is told the app will check with the brokerage later. (c) The confirmation is captured but the portfolio can't be updated: the confirmation stays in the log flagged as not yet in the portfolio, and the buyer is told the purchase went through at the brokerage but the portfolio isn't updated yet. Correct?

**A8.** **(a)** Not decided: the brokerage reporting a refusal and how the app handles it. Use your recommendation.

**(b)** Not decided: the session dropping before any confirmation. Use your recommendation.

**(c)** Not decided: the confirmation being captured but the portfolio failing to update. Use your recommendation.

**Q9.** Last one: how often does this happen, roughly (e.g. a few purchases per Purchaser per month)?

**A9.** Yes. It happens a few times a month per user. The actor is an app user, not a "Purchaser."

