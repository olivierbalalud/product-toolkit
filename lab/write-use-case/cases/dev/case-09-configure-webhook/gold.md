---
id: UC-009
title: Configure a webhook endpoint
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-009: Configure a webhook endpoint

| Field | Value |
|---|---|
| **Primary actor** | Integration engineer (a backend developer) |
| **Supporting actors** | The integration engineer's receiving endpoint (answers the test event) |
| **Scope** | Payment platform (billing and events) |
| **Level** | User goal |
| **Trigger** | The integration engineer needs their own systems to receive payment and billing events as they happen. |
| **Preconditions** | The integration engineer is signed in with a Developer or Administrator role. |
| **Minimal guarantees** | Nothing is saved for a URL that fails validation or an endpoint the engineer abandons; no event is sent to an endpoint that has not confirmed receipt of the test event; a signing secret is never shown again once the engineer has left it. |
| **Success guarantees** | The endpoint is registered and live in production mode, and the chosen event types are subscribed and queued for delivery to it; it has confirmed receipt of a test event; its signing secret, unique to it, has been shown to the engineer once. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Integration engineer | The chosen events reach their own server; learns at once whether the endpoint works and why not; gets the secret to verify each event. |
| Finance and operations | Payment settlement notifications arrive reliably, without duplicate ledger updates. |
| Platform security | The origin and integrity of every event can be verified cryptographically. |

## Main success scenario

1. (actor) The integration engineer gives the endpoint URL, an optional description, and the event types to send to it.
2. (system) The system validates the URL (BR-1) and generates a signing secret unique to this endpoint.
3. (system, wait) The system sends a zero-value test event to the endpoint, which confirms receipt (BR-2).
4. (system) The system sets the endpoint live in production mode for the chosen event types and shows the signing secret once, with instructions to store it securely (BR-3).
5. (actor) The integration engineer confirms they have stored the signing secret.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-009.1a | out-of-scope: several endpoints may share a URL | n/a | yes: UC-009.1b |
| 5 | n/a | n/a | n/a | yes: UC-009.5a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | n/a | n/a | out-of-scope: no limit on the number of endpoints per account is defined | n/a | n/a |
| 3 | yes: UC-009.3a | n/a | yes: UC-009.3a | n/a | n/a | n/a | n/a |
| 4 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

**Privacy request:** no: the use case stores the endpoint's URL, description, event types and signing secret, none of which is personal data; the personal data in the events delivered later is covered by the platform's own privacy use cases.

## Extensions

- **UC-009.1a** The URL fails validation: it does not use HTTPS, points to a local or private address, or its certificate is not trusted (BR-1):
  1. The system says which rule the URL breaks; nothing is saved.
  2. The integration engineer gives a compliant URL: returns to step 2. Or the engineer abandons (UC-009.1b).

  *Example:* Kofi gives `http://hooks.kofi-shop.example/payments`; the system says an endpoint must use HTTPS, and he gives the `https://` address instead.
- **UC-009.1b** The integration engineer abandons before submitting the endpoint:
  1. The system saves nothing.
  2. The use case ends.

  *Example:* Kofi starts describing a new endpoint, notices he copied his staging server's URL, and leaves; no endpoint is created.
- **UC-009.3a** The endpoint does not confirm receipt: it cannot be reached, answers with a non-success status, drops the connection, or does not answer within 5 seconds (BR-2):
  1. The system marks the endpoint unreachable, pending verification, and shows the engineer the status returned or the failure diagnostic.
  2. The system offers to save the endpoint disabled, so it can be debugged without receiving live events.
  3. The integration engineer saves it disabled: the use case ends with the endpoint stored disabled, receiving no events (use case Re-enable a Webhook Endpoint). Or the engineer declines: nothing is saved and the use case ends.

  *Example:* Kofi's server answers the test event with a 500 status; the system shows the 500 with its diagnostic, and Kofi saves the endpoint disabled while he fixes his handler.
- **UC-009.5a** The integration engineer leaves without confirming they have stored the signing secret:
  1. The system warns that the secret cannot be shown again and must be rolled if lost (BR-3).
  2. The engineer stores it and confirms: the use case ends as in step 5. Or the engineer leaves anyway: the use case ends, the endpoint stays live, and the secret can only be rolled (use case Roll a Signing Secret).

  *Example:* Kofi starts to leave before confirming; the system warns him the secret won't be shown again, so he copies it into his server's settings and confirms.

## Technology and data variations

- None

## Related information

- **Frequency:** Occasional: a few times per account, when an integration is set up or a new receiving service is added.
- **Business rules:** BR-1 an endpoint URL uses HTTPS with TLS 1.3, a certificate from a trusted authority and a public address, never a local or private one such as 127.0.0.1 (step 2, UC-009.1a) · BR-2 an endpoint is verified when it answers the test event with a success (2xx) status within 5 seconds (step 3, UC-009.3a) · BR-3 a signing secret is shown only once; if lost, it must be rolled (step 4, UC-009.5a).
- **Related use cases:** Edit a Webhook Endpoint, Re-enable a Webhook Endpoint, Roll a Signing Secret.
- **Open issues:** None
