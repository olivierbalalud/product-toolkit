* **Use Case ID:** UC-B2B-01
* **Level:** Sea-Level (User Goal)
* **Primary Actor:** Integration Engineer / Backend Developer
* **Scope:** Stripe SaaS Platform (Billing & Events Infrastructure)
* **Stakeholders & Interests:**
  * *Finance & Operations:* Needs reliable delivery of payment settlement notifications without duplicated ledger updates.
  * *Platform Security:* Needs cryptographic verification of origin and payload integrity.
* **Preconditions:**
  1. The user has an authenticated Stripe account with `Developer` or `Admin` privileges.
  2. The target server exposes an active, publicly accessible HTTPS endpoint capable of TLS 1.3 negotiation.
* **Success Guarantees (Postconditions):**
  1. The endpoint URL is registered in production mode.
  2. A unique endpoint signing secret (`whsec_...`) is generated and securely displayed once.
  3. The system dispatches a verification handshake event to confirm endpoint reachability.
  4. Selected event types are subscribed and queued for delivery.
* **Trigger:** The developer needs downstream systems to ingest automated transaction lifecycle events.

**Main Success Scenario (MSS):**
1. Actor specifies the target HTTPS destination URL and an optional administrative description.
2. Actor selects specific business event types to route to this endpoint (e.g., `payment_intent.succeeded`, `charge.refunded`).
3. System verifies that the target URL adheres to valid public HTTPS URI standards.
4. System generates a dedicated HMAC signing secret unique to this endpoint.
5. System transmits an asynchronous zero-value ping event to the target endpoint to verify TLS handshake and receipt.
6. Target endpoint responds with an HTTP `2xx` status code.
7. System activates the endpoint status to `Live` and displays the signing secret to the Actor with storage instructions.

**Extensions (Alternate & Failure Paths):**
* **3a. Destination URL fails format or security validation (e.g., plain HTTP, local IP address `127.0.0.1`, untrusted SSL certificate):**
  * 3a1. System notifies Actor of the invalid URL scheme or certificate failure.
  * 3a2. Actor provides a compliant HTTPS URL.
  * 3a3. System resumes at Step 3 (or Actor aborts with no state saved).
* **5a. Endpoint returns a non-2xx status, times out (> 5 seconds), or drops connection:**
  * 5a1. System marks the endpoint status as `Unreachable / Pending Verification`.
  * 5a2. System logs the returned HTTP error code and failure diagnostic for the Actor.
  * 5a3. System provides an option to save the endpoint in `Disabled` mode for future debugging without routing live traffic.
* **7a. Actor closes the view without acknowledging the signing secret copy prompt:**
  * 7a1. System warns the Actor that the unmasked secret cannot be viewed again and must be rolled if lost.
