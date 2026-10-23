- **Name:** Buy Stocks over the Web
- **Scope:** Personal finance app (black box) · **Level:** User goal (!)
- **Primary actor:** Purchaser (app user)
- **Supporting actor:** Brokerage
- **Stakeholders & interests:**
  - Purchaser — buys stocks and sees them added to their portfolio automatically.
  - Brokerage — receives complete purchase information.
- **Trigger:** Purchaser decides to buy stocks.
- **Preconditions:** Purchaser is signed in to the app.
- **Minimal guarantees:** Enough is logged for the app to detect that something went wrong and ask the Purchaser for the details.
- **Success guarantees:** Brokerage acknowledged the purchase; log and portfolio are updated.

**Main success scenario**
1. Purchaser chooses to buy stocks online.
2. App obtains from the Purchaser which brokerage to use.
3. App opens a connection to the brokerage, keeping control of the session.
4. Purchaser browses and buys stock at the brokerage.
5. App captures the brokerage's responses and updates the Purchaser's portfolio.
6. App shows the Purchaser the updated portfolio.

**Extensions**
- 2a. Brokerage not supported: App asks for another one; Purchaser may cancel (use case ends).
- 3a. Connection failure during setup: App reports the failure with advice and returns to step 2; Purchaser retries or abandons.
- 4a. Device crashes or is switched off during the purchase: *open issue in the source* — recommended handling is reconciliation with the brokerage at next launch (same mechanism as 4b/5a).
- 4b. Brokerage does not acknowledge the purchase but defers it: App logs the pending purchase and later asks the Purchaser about the outcome.
- 5a. Brokerage does not return the needed information: App logs the gap and asks the Purchaser to complete the purchase details.

**Technology & data variations:** connection through an embedded broker session or a broker API.
