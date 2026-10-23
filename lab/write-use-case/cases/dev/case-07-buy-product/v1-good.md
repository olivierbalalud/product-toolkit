- **Name:** Buy a Product
- **Scope:** Online store (black box) · **Level:** User goal (!)
- **Primary actor:** Customer
- **Supporting actors:** Payment provider, Notification service
- **Stakeholders & interests:**
  - Customer — gets the right items at the price shown, delivered as chosen, never charged twice.
  - Merchant — is paid and the order is captured for fulfillment.
  - Fulfillment — receives complete shipping information.
  - Payment provider — receives valid authorization requests.
- **Trigger:** Customer decides to buy.
- **Preconditions:** Catalog is published.
- **Minimal guarantees** *(added)*: Customer is never charged without a recorded order; an order is never confirmed without authorized payment.
- **Success guarantees:** Order recorded; payment authorized; confirmation shown and emailed; order queued for fulfillment.

**Main success scenario**
1. Customer browses the catalog and selects items to buy.
2. Customer proceeds to checkout.
3. Customer provides shipping details (address and delivery speed).
4. System presents the full price, including shipping and taxes.
5. Customer provides payment details.
6. System obtains payment authorization.
7. System confirms the order to the Customer.
8. System sends the Customer an order confirmation email.

**Extensions**
- 3a. Returning customer: System proposes the stored shipping details, pricing and the last four digits of the stored card; Customer accepts or overrides them; continue at step 6.
- 4a. An item went out of stock since selection *(added)*: System says so; Customer removes or replaces it; continue at step 4.
- 6a. Authorization fails: System says so; Customer provides other payment details (continue at step 5) or cancels (use case ends).
- 6b. Card issuer requires strong customer authentication *(added)*: Customer completes the challenge; continue at step 6.

**Technology & data variations:** card, digital wallet or bank transfer; guest or signed-in checkout.
