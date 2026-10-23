---
id: UC-008
title: Buy stocks over the web
status: Draft
driver: lab
priority: unset
source_locale: en
inputs: []
stories: []
---

# UC-008: Buy stocks over the web

| Field | Value |
|---|---|
| **Primary actor** | Purchaser (a user of the personal finance app) |
| **Supporting actors** | Brokerage (outside the app: takes the purchase and confirms it or puts it off) |
| **Scope** | The personal finance app |
| **Level** | User goal |
| **Trigger** | The Purchaser decides to buy stocks and asks the app to, naming a brokerage. |
| **Preconditions** | The Purchaser is signed in to the app. |
| **Minimal guarantees** | Enough is logged to notice that a purchase went wrong and to ask the Purchaser for its details. The portfolio changes only for a purchase the brokerage has confirmed and whose details are complete (BR-2). No brokerage session the app opened is left open by the app when the use case ends without a purchase. |
| **Success guarantees** | The brokerage has confirmed the purchase; the purchase is in the transaction log and in the Purchaser's portfolio; the Purchaser has seen the updated portfolio. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Purchaser | Their stocks show up in their portfolio without typing them in; they know whether the purchase went through. |
| Brokerage | Receives complete information about the purchase. |
| App operator (support) | Enough is logged to notice a purchase that went wrong and to ask the Purchaser for its details. |

## Main success scenario

1. (actor) The Purchaser asks to buy stocks and names a supported brokerage (BR-1).
2. (system, wait) The system opens a session with the brokerage and keeps control of it, so it can pick up what the brokerage sends back (BR-3).
3. (actor) The Purchaser buys stock at the brokerage, and the brokerage confirms the purchase.
4. (system) The system picks up the brokerage's confirmation, logs the transaction, adds the purchase to the Purchaser's portfolio (BR-2) and shows the Purchaser the updated portfolio.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-008.1a | n/a | n/a | yes: UC-008.1-3a |
| 3 | out-of-scope: the brokerage checks the order in its own session; the app only sees the result | n/a | out-of-scope: signing in at the brokerage and the right to trade are the brokerage's to check, in its own session | yes: UC-008.1-3a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | yes: UC-008.2a | n/a | n/a | n/a | n/a |
| 4 | n/a | n/a | yes: UC-008.4a | yes: UC-008.4b, UC-008.3-4a | n/a | n/a | n/a |

**Privacy request:** no: exporting or erasing the Purchaser's holdings is a separate account privacy job, not part of buying.

## Extensions

- **UC-008.1a** The Purchaser names a brokerage the app doesn't support (BR-1):
  1. The system says the brokerage isn't supported and asks for another.
  2. The Purchaser names another brokerage and the use case returns to step 2, or cancels and the use case ends.

  *Example:* Ana asks to buy through Harbor Street Brokers, which the app doesn't support; she picks Northline Invest instead.
- **UC-008.2a** The session with the brokerage can't be set up:
  1. The system reports that the connection failed, with advice on what to do.
  2. The Purchaser tries the same brokerage again and the use case returns to step 2, names another brokerage and the use case returns to step 2, or gives up and the use case ends with the portfolio unchanged.

  *Example:* Ben asks to buy through Northline Invest, but its site doesn't respond; the app suggests trying again in a few minutes, and Ben retries.
- **UC-008.1-3a** The Purchaser gives up before buying anything, either before the session is opened or while browsing at the brokerage:
  1. The system closes the brokerage session, if one is open.
  2. The use case ends with the portfolio unchanged.

  *Example:* Ana opens a session with Northline Invest, looks at a few share prices and decides not to buy today.
- **UC-008.3-4a** The Purchaser's device crashes or is switched off in the middle of the purchase: `deferred`, the handling isn't decided yet. Most likely the app checks with the brokerage the next time it starts, as for a put-off or incomplete purchase (see Open issues).
- **UC-008.4a** The brokerage doesn't confirm the purchase and puts it off instead:
  1. The system logs the purchase as pending and leaves the portfolio unchanged (BR-2).
  2. The system tells the Purchaser that the brokerage hasn't confirmed the purchase yet and that the app will ask them later how it turned out.
  3. The use case ends. Following up on the pending purchase is a separate use case.

  *Example:* Ben buys 20 shares at Northline Invest, which holds the order for review; the app shows "not confirmed yet, we'll check with you later".
- **UC-008.4b** The brokerage's confirmation lacks details the app needs to record the purchase, such as the price:
  1. The system logs which details are missing and asks the Purchaser for them.
  2. The Purchaser provides the missing details.
  3. The system records the purchase, adds it to the portfolio and shows the Purchaser the updated portfolio. The use case ends.

  *Example:* Northline Invest confirms Ana's purchase of 10 shares but sends no price; the app asks her for it, she enters 42.50, and her portfolio shows the 10 shares.

## Technology and data variations

- Step 2: the app connects through an embedded session on the brokerage's site, or through the brokerage's API.

## Related information

- **Frequency:** a few times a month per user.
- **Business rules:**
  - BR-1: The Purchaser can buy only through a brokerage the app supports.
  - BR-2: A purchase enters the portfolio only once the brokerage has confirmed it and its details (such as the price) are complete.
  - BR-3: The app keeps control of the brokerage session for the whole purchase, so it can pick up what the brokerage sends back.
- **Open issues:**
  - How to handle a device crash or switch-off mid-purchase (UC-008.3-4a); likely a check with the brokerage on the app's next start.
  - UC-008.4b: what happens if the Purchaser can't or won't provide the missing details, and whether the details they give are checked.
