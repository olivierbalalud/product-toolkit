---
id: UC-008
title: Buy stocks through a brokerage
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-008: Buy stocks through a brokerage

| Field | Value |
|---|---|
| **Primary actor** | App user |
| **Supporting actors** | Brokerage (hosts the purchase in its own session and confirms it or puts it off) |
| **Scope** | The portfolio app |
| **Level** | User goal |
| **Trigger** | The user wants to buy stocks through a brokerage. |
| **Preconditions** | The user is signed in to the app. |
| **Minimal guarantees** | The portfolio is updated only once the brokerage's confirmation is captured, so a purchase the brokerage hasn't confirmed never reaches it. The app logs enough to notice a purchase that went wrong and to ask the user for its details. |
| **Success guarantees** | The confirmed purchase is in the user's portfolio, and the transaction is logged with the brokerage's confirmation. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| App user | Their purchased stocks show up in the portfolio without typing them in. |
| Brokerage | Gets complete information about the purchase in its own session, and either confirms the purchase or puts it off. |
| App owner | A purchase the brokerage hasn't confirmed never shows in the portfolio; the log shows when a purchase went wrong so the user can be asked for missing details. |

## Main success scenario

1. (actor) The user asks to buy stocks and names a brokerage (BR-1).
2. (system, wait) The system opens a session with the brokerage, keeping control of it.
3. (actor) The user buys the stock at the brokerage.
4. (system) The system captures the brokerage's confirmation of the purchase, adds the purchase to the user's portfolio, logs the transaction with the confirmation and shows the updated portfolio.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-008.1a | n/a | n/a | yes: UC-008.1-3a |
| 3 | out-of-scope: the brokerage checks the order in its own session; the app only sees the result | n/a | out-of-scope: signing in at the brokerage and the right to trade are the brokerage's checks | yes: UC-008.1-3a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | yes: UC-008.2a | n/a | n/a | n/a | n/a |
| 4 | yes: UC-008.4b | n/a | yes: UC-008.4c | yes: UC-008.4d | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing a user's holdings and transactions is a separate account privacy use case.

## Extensions

- **UC-008.1a** The brokerage the user names is not a supported brokerage (BR-1):
  1. The system tells the user it doesn't work with that brokerage and asks for another.
  2. The user names another brokerage: returns to step 1. Or cancels: the use case ends, with nothing opened and the portfolio as it was.

  *Example:* Lena asks to buy stocks through "Northgate Trading", which the app doesn't support; she names "Harbour Invest" instead.
- **UC-008.1-3a** The user gives up before buying, or closes the brokerage session without buying:
  1. The system closes the brokerage session, if one is open.
  2. The portfolio stays as it was. The use case ends.

  *Example:* Tom opens a session with Harbour Invest, looks at the share price and closes the session without placing an order; his portfolio is unchanged.
- **UC-008.2a** The brokerage doesn't answer or is down, so the session can't be opened:
  1. The system tells the user the connection to the brokerage can't be set up, with advice on what to do.
  2. The user tries again with the same brokerage: returns to step 2. Or names another brokerage: returns to step 1. Or gives up: the use case ends, with the portfolio as it was.

  *Example:* Lena chooses Harbour Invest at 08:55 during its maintenance window; the app reports that the connection can't be set up and suggests trying again after 09:00.
- **UC-008.3a** The user's device crashes or is switched off during the purchase at the brokerage: `deferred`, the driver left the handling open; the likely approach is that the app checks with the brokerage the next time it starts.
- **UC-008.4a** The brokerage puts the purchase off instead of confirming it:
  1. The system logs the purchase as pending and leaves the portfolio as it was.
  2. The system tells the user the brokerage hasn't confirmed the purchase yet and that the app will ask later how it turned out.
  3. The use case ends.

  *Example:* Tom orders 20 shares of Acme Corp at Harbour Invest on Saturday; the brokerage puts the purchase off until the market opens, and Tom's portfolio does not show the shares yet.
- **UC-008.4b** The brokerage's confirmation lacks details the portfolio needs, such as the price or the quantity:
  1. The system logs which details are missing and asks the user for them.
  2. The user gives the missing details.
  3. The system adds the purchase to the portfolio, logs the transaction with the confirmation and the details given, and shows the updated portfolio. The use case ends.

  *Example:* Harbour Invest confirms Lena's purchase of Acme Corp shares without the price; Lena enters 42.10 per share and the portfolio shows the 10 shares.
- **UC-008.4c** The brokerage session ends before any confirmation arrives:
  1. The system logs the purchase as pending and leaves the portfolio as it was.
  2. The system tells the user no confirmation came from the brokerage and that the app will check with the brokerage later how the purchase turned out.
  3. The use case ends.

  *Example:* Tom places an order for 5 shares at Harbour Invest and the brokerage session drops before its confirmation reaches the app; the purchase is logged as pending.
- **UC-008.4d** The confirmation is captured but the portfolio can't be updated:
  1. The system keeps the confirmation in the log, flagged as not yet in the portfolio.
  2. The system tells the user the purchase went through at the brokerage but the portfolio isn't updated yet.
  3. The use case ends.

  *Example:* Harbour Invest confirms Lena's purchase of 10 Acme Corp shares, but the portfolio store rejects the update; the log holds the confirmation flagged for follow-up and Lena is told her portfolio will catch up.

## Technology and data variations

- None.

## Related information

- **Frequency:** a few times a month per user.
- **Business rules:** BR-1 the app works only with supported brokerages (step 1, UC-008.1a).
- **Related use cases:** Find out how a pending purchase turned out (the follow-up for UC-008.4a and UC-008.4c); account privacy (export or erase holdings).
- **Open issues:** What happens when the user's device crashes or is switched off during the purchase at the brokerage (UC-008.3a).
