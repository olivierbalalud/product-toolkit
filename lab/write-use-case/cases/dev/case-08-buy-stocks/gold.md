---
id: UC-008
title: Buy stocks over the web
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-008: Buy stocks over the web

| Field | Value |
|---|---|
| **Primary actor** | Purchaser (app user) |
| **Supporting actors** | Brokerage (the Purchaser buys at it; it acknowledges or defers the purchase) |
| **Scope** | Personal finance app |
| **Level** | User goal |
| **Trigger** | The Purchaser decides to buy stocks. |
| **Preconditions** | The Purchaser is signed in to the app. |
| **Minimal guarantees** | Enough is logged for the app to detect that a purchase went wrong and to ask the Purchaser for its details. |
| **Success guarantees** | The brokerage has acknowledged the purchase; the purchase is in the log and in the Purchaser's portfolio, and the Purchaser has seen the updated portfolio. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Purchaser | Buys stocks and sees them added to the portfolio without entering them by hand. |
| Brokerage | Receives complete purchase information. |

## Main success scenario

1. (actor) The Purchaser asks to buy stocks and names the brokerage to use (BR-1).
2. (system, wait) The system opens a session with the brokerage for the Purchaser, keeping control of it so that it can capture the brokerage's responses.
3. (actor) The Purchaser browses and buys stock at the brokerage.
4. (system) The system captures the brokerage's acknowledgement of the purchase, records the purchase in the log, updates the Purchaser's portfolio and shows the updated portfolio.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-008.1a | n/a | n/a | yes: UC-008.1-3a |
| 3 | out-of-scope: the brokerage validates the order in its own session; the app sees only the outcome | n/a | out-of-scope: the brokerage checks the Purchaser's sign-in and trading rights in its own session | yes: UC-008.1-3a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | yes: UC-008.2a | n/a | n/a | n/a | n/a |
| 4 | n/a | n/a | yes: UC-008.4a | yes: UC-008.4b | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, the log and the portfolio hold the Purchaser's holdings; exporting or erasing them is an account privacy use case, not part of buying.

## Extensions

- **UC-008.1a** The Purchaser names a brokerage the app does not support (BR-1):
  1. The system says the brokerage is not supported and asks for another one.
  2. The Purchaser names another brokerage: returns to step 2. Or the Purchaser cancels: the use case ends.

  *Example:* Nadia names Harbor Trade, which the app does not support; she names Northgate Brokers instead.
- **UC-008.1-3a** The Purchaser abandons before buying anything:
  1. The system closes the session with the brokerage, if one is open; the portfolio is unchanged.
  2. The use case ends.

  *Example:* Nadia browses the funds on offer at Northgate Brokers, finds nothing she wants and leaves; the app closes the session and her portfolio is unchanged.
- **UC-008.2a** The session with the brokerage cannot be opened:
  1. The system reports the failure with advice on what to do.
  2. The Purchaser tries again, with the same or another brokerage: returns to step 1. Or the Purchaser abandons: the use case ends.

  *Example:* Northgate Brokers does not answer when Nadia connects; the app advises her to try again in a few minutes or to use another brokerage, and her second attempt connects.
- **UC-008.3a** The Purchaser's device crashes or is switched off during the purchase: `deferred`, how the app recovers a purchase interrupted this way is not decided (see Open issues).
- **UC-008.4a** The brokerage does not acknowledge the purchase but defers it:
  1. The system records the purchase as pending in the log, leaves the portfolio unchanged, and tells the Purchaser that the brokerage has not confirmed the purchase yet and that the app will ask them about its outcome.
  2. The use case ends; Resolve a Pending Purchase continues it.

  *Example:* Nadia buys 20 shares of Alder Energy after the market has closed; Northgate Brokers queues the order instead of confirming it, and the app shows it to her as pending.
- **UC-008.4b** The brokerage does not return all the information the app needs to record the purchase:
  1. The system logs what is missing and asks the Purchaser for the missing purchase details.
  2. The Purchaser gives them.
  3. The system records the purchase in the log, updates the portfolio and shows it; the use case ends.

  *Example:* Northgate Brokers confirms Nadia's purchase of 20 Alder Energy shares but sends no price; she enters 34.10 per share, and her portfolio shows the 20 shares.

## Technology and data variations

- 2: the system connects through an embedded session on the brokerage's site, or through the brokerage's API.

## Related information

- **Frequency:** a few times a month per Purchaser.
- **Business rules:** BR-1 purchases go only through the brokerages the app supports (step 1, UC-008.1a).
- **Related use cases:** Resolve a Pending Purchase.
- **Open issues:** How the app recovers a purchase interrupted when the Purchaser's device crashes or is switched off (UC-008.3a); reconciling with the brokerage at the next launch, as for a deferred or incomplete purchase, is the preferred direction.
