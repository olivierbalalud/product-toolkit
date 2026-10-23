---
id: UC-008
title: Buy stocks
status: Draft            # Draft | Complete [R28-Q11]
driver: lab
priority: TBD            # informs the pick, never makes it [R6-Q1]
source_locale: en        # en | fr [R1-Q11]
inputs: []
stories: []
---

# UC-008: Buy stocks

| Field | Value |
|---|---|
| **Primary actor** | Purchaser: a user of the personal finance app who has decided to buy stocks |
| **Supporting actors** | Brokerage: a supported brokerage, reached through an embedded session on its site that the app hosts, or through its API |
| **Scope** | The personal finance app |
| **Level** | User goal |
| **Trigger** | The Purchaser chooses to buy stocks. |
| **Preconditions** | The Purchaser is signed in to the app. |
| **Minimal guarantees** | The portfolio changes only for a purchase the brokerage confirmed, or one the Purchaser completed with the missing details (BR-3). No purchase is recorded twice (BR-4), and no purchase is half-recorded: its transaction-log entry and its portfolio change are saved together or not at all. Every attempt is logged with its brokerage, outcome and any missing details, enough to notice that a purchase went wrong and to ask the Purchaser for its details. The brokerage session, if there is one, is closed when the use case ends. |
| **Success guarantees** | Each purchase the Purchaser made at the brokerage is in the transaction log once, with at least its stock, quantity and price (BR-2); the portfolio holdings include it; the Purchaser has seen the updated portfolio. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Purchaser | A portfolio that matches what they actually bought, with nothing missed or counted twice; a clear statement of the outcome when the purchase did not go through or was not confirmed. |
| Brokerage | Complete information about the purchase. |
| Company running the app (support) | A log of every attempt detailed enough to spot a purchase that went wrong and to follow it up with the Purchaser. |

## Main success scenario

1. (actor) The Purchaser chooses to buy stocks and picks a supported brokerage (BR-1).
2. (system, wait) The system connects to the brokerage, through an embedded session it hosts or through the brokerage's API, and opens a purchase attempt that records the Purchaser, the brokerage, the connection type and the start time, so it can match what the brokerage sends back.
3. (actor) The Purchaser buys stock at the brokerage.
4. (system) The system captures the brokerage's confirmation of the purchase (stock, quantity, price, currency, fees, execution time, order reference) and closes the brokerage session, if there is one.
5. (system) The system records the purchase in the transaction log and updates the portfolio holdings as one change, marks the purchase attempt confirmed, and shows the Purchaser the updated portfolio.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-008.1a | n/a | n/a | yes: UC-008.1b |
| 3 | yes: UC-008.3a | n/a | yes: UC-008.2a, UC-008.3a | yes: UC-008.3b |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | yes: UC-008.2a | n/a | yes: UC-008.2a | n/a | n/a | n/a | n/a |
| 4 | yes: UC-008.4b | yes: UC-008.4c | yes: UC-008.4a | yes: UC-008.4d | n/a | n/a | n/a |
| 5 | n/a | n/a | yes: UC-008.5a | yes: UC-008.5a | n/a | n/a | n/a |

**Privacy request:** no: exporting or erasing holdings and transactions is a separate account privacy use case, not part of buying.

## Extensions

- **UC-008.1a** The Purchaser names a brokerage the app does not support:
  1. The system says the brokerage is not supported and asks for another.
  2. Returns to step 1; the Purchaser may pick another or cancel (UC-008.1b).

  *Example:* Ana names "Northbank Trading", which is not on the supported list; the app says so and she picks a supported brokerage instead.
- **UC-008.1b** The Purchaser cancels before the brokerage is connected:
  1. The system opens no connection and leaves the portfolio unchanged.
  2. The use case ends.

  *Example:* Ana opens the purchase, sees the brokerage list, and backs out without picking one.
- **UC-008.2a** The connection to the brokerage cannot be set up (the brokerage is unreachable or times out, or the Purchaser's sign-in at the brokerage fails; the brokerage checks sign-in in its own session, so the system sees only the connection result):
  1. The system logs the failed attempt, reports that the connection failed and advises what to do (check the brokerage sign-in, try again later, or pick another brokerage).
  2. Returns to step 2 with the same brokerage, or to step 1 for another one; if the Purchaser gives up, the portfolio is unchanged and the use case ends.

  *Example:* Ana picks her brokerage, but its site does not answer within 10 seconds; the app tells her the connection failed, and she tries again a minute later.
- **UC-008.3a** The brokerage rejects the purchase (for example for insufficient funds, or because the account may not trade that stock):
  1. The system captures the rejection and its reason, logs the attempt as rejected and leaves the portfolio unchanged.
  2. The system tells the Purchaser the brokerage rejected the purchase and why.
  3. Returns to step 3 while the brokerage session is open; otherwise the use case ends.

  *Example:* Ana orders 20 shares at 150 EUR with 2,000 EUR in her brokerage account; the brokerage rejects it for insufficient funds and the app shows that reason.
- **UC-008.3b** The Purchaser leaves the brokerage without buying anything (they may leave at any time):
  1. The system closes the brokerage session, if there is one, logs the attempt as abandoned and leaves the portfolio unchanged.
  2. The system tells the Purchaser that no purchase was made and the portfolio has not changed.
  3. The use case ends.

  *Example:* Ana looks at the share price at her brokerage, decides not to buy, and closes the brokerage window; the app confirms nothing was bought.
- **UC-008.3c** The Purchaser makes several purchases in the same brokerage session (an alternative, not a failure):
  1. The system captures each confirmation as it arrives (step 4) and records each purchase as a separate transaction-log entry (step 5).
  2. The system closes the session when the Purchaser leaves the brokerage and shows the updated portfolio once, with all the purchases.

  *Example:* Ana buys 10 shares of one company and 5 of another before leaving; the transaction log gets two entries and the portfolio shows both holdings.
- **UC-008.4a** The connection drops after the Purchaser may have bought, before the system has captured the confirmation:
  1. The system logs the attempt as unconfirmed, with what it knows (brokerage, time, any partial data), so the purchase can be followed up with the Purchaser, and leaves the portfolio unchanged.
  2. The system tells the Purchaser that it lost the connection before the brokerage confirmed anything, that the portfolio has not been updated, and that it will ask them for the purchase details if they bought.
  3. The use case ends.

  Whether the system later recovers the confirmation from the brokerage on its own (for example the next time the app starts) is open; see Open issues.

  *Example:* Ana confirms an order at her brokerage, and her connection drops before the confirmation reaches the app; the app tells her it did not get the confirmation and her portfolio is unchanged.
- **UC-008.4b** The confirmation lacks a detail needed to record the purchase (for example the price):
  1. The system logs which details are missing and asks the Purchaser for them.
  2. The Purchaser provides them; the system checks them (for example a price greater than zero) and asks again if they are invalid.
  3. Returns to step 5.

  If the Purchaser declines to provide them, the system logs the attempt as incomplete, leaves the portfolio unchanged and the use case ends.

  *Example:* The brokerage confirms 10 shares bought but sends no price; the app asks Ana, she enters 42.10 EUR per share, and the purchase is recorded.
- **UC-008.4c** The confirmation names a purchase already in the transaction log (same brokerage and order reference):
  1. The system does not record it again and logs the duplicate on the attempt (BR-4).
  2. Returns to step 5 with only the purchases not yet recorded, or straight to showing the portfolio if there are none.

  *Example:* The brokerage sends the confirmation for order 88412 twice; the app records the 10 shares once.
- **UC-008.4d** The brokerage reports the order only partly filled:
  1. The system records the filled quantity as the purchase (step 5).
  2. If the brokerage says the rest of the order is still open, the system logs the remainder as pending, as in UC-008.4e.
  3. The system shows the updated portfolio and tells the Purchaser how much was filled.

  *Example:* Ana orders 100 shares; the brokerage fills 60 and keeps 40 open; the portfolio shows 60 more shares and the app notes 40 are pending.
- **UC-008.4e** The brokerage puts off the purchase (for example pending because the market is closed) (an alternative, not a failure):
  1. The system logs the purchase as pending and leaves the portfolio unchanged.
  2. The system tells the Purchaser the brokerage has not confirmed the purchase yet, and that the app will ask them later how it turned out (following up is a separate use case).
  3. The use case ends.

  *Example:* Ana places an order on Saturday; the brokerage says it will execute when the market opens; the app logs it as pending and says it will ask her about it later.
- **UC-008.5a** The purchase cannot be saved (storage fails, or the log entry or the portfolio change cannot be written):
  1. The system saves neither, keeps the captured confirmation on the purchase attempt marked "not recorded" so support can notice it, and tells the Purchaser the purchase was made at the brokerage but is not in the portfolio yet.
  2. The system offers to retry; on success, returns to step 5. If the Purchaser declines or the retry fails, the attempt stays flagged for follow-up and the use case ends.

  *Example:* The brokerage confirms Ana's 10 shares, but the save fails; the app tells her the purchase went through at the brokerage, and a retry records it.
- **`UC-008.*a`** The Purchaser's app session ends (it expires, or the Purchaser closes the app) before the use case finishes:
  1. The system closes the brokerage session, if there is one.
  2. Any confirmation already captured is recorded as in step 5; a purchase made but not captured is handled as in UC-008.4a.
  3. The use case ends.

  *Example:* Ana's app session expires while she is still at the brokerage; the app closes the brokerage session and logs the attempt as unconfirmed.

## Technology and data variations

- Step 2: the brokerage is reached through an embedded session on its site, hosted by the app, or through the brokerage's API.
- Step 3: one purchase, or several in the same brokerage session (UC-008.3c).
- Step 4: a complete confirmation, or one the Purchaser completes with missing details (UC-008.4b).

## Related information

- **Frequency:** a few times a month per user.
- **Business rules:**
  - BR-1: Only brokerages on the app's supported list can be used. A user may use any number of supported brokerages, one per purchase attempt.
  - BR-2: A purchase is recorded only with its stock, quantity and price. The price is required; a missing required detail is asked of the Purchaser before recording. Currency, fees, execution time and order reference are recorded when the brokerage sends them.
  - BR-3: The portfolio changes only for a confirmed purchase, or one the Purchaser completed with the missing details. Pending, rejected, abandoned, unconfirmed and incomplete attempts leave it unchanged.
  - BR-4: Each brokerage purchase is recorded once, identified by its brokerage and order reference.
  - BR-5: The app sets no amount limits on purchases; the brokerage enforces its own.
  - BR-6: Transaction-log entries are kept as long as the Purchaser's account exists; logs of failed, abandoned and unconfirmed attempts are kept for 12 months.
- **Open issues:**
  - Whether the system recovers a lost confirmation from the brokerage on its own (UC-008.4a), for example by checking the next time the app starts, as the follow-up of a pending purchase would.
  - Holding a brokerage account is not a precondition: the brokerage handles a Purchaser without an account (sign-up or sign-in fails, UC-008.2a). To confirm.
  - Recommendations to confirm with the product owner: partly filled (UC-008.4d) and rejected (UC-008.3a) handling, several purchases per session (UC-008.3c), the recorded fields (BR-2), duplicate handling (UC-008.4c), save failure and retry (UC-008.5a), no amount limits (BR-5), no limit on brokerages per user (BR-1), retention (BR-6), and the messages for an abandoned or unconfirmed purchase.
  - Whether a regulator or auditor has an interest in the transaction log; none is assumed, since the brokerage is the party that executes the trade.
