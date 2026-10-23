# Answers: configure a webhook endpoint

## Actor, goal and scope

- The system is our payment platform, the billing and events part of it.
- The person doing this is an integration engineer, usually a backend developer on the customer's side.
- They start because they need their own systems to receive payment and billing events as they happen.
- Before they start they're already signed in with a Developer or Administrator role.
- The only outside party is their own server, the endpoint, which has to answer our test event.
- We don't assume their server is ready beforehand: whether the address is acceptable and whether it answers is exactly what we check during the setup.
- It happens occasionally: a few times per account, when an integration is set up or a new receiving service is added.
- Changing an existing endpoint's event types, re-enabling a disabled endpoint, and rolling a lost signing secret are separate jobs, not part of this.

## Stakeholders and guarantees

- The integration engineer wants the chosen events to reach their server, to know straight away whether the endpoint works and why not, and to get the secret they need to verify each event.
- Finance and operations need payment settlement notifications to arrive reliably, and never to cause the same ledger update twice.
- Platform security needs the origin and integrity of every event to be verifiable cryptographically.
- If the address is rejected or they give up, nothing is saved.
- We never send events to an endpoint that hasn't confirmed it received the test event.
- Once they've left the secret behind, it's never shown again.
- When it works: the endpoint is registered and live in production mode, the event types they chose are subscribed and queued for delivery, the endpoint has confirmed the test event, and they've seen its secret, which is unique to that endpoint, exactly once.

## Main scenario

- Along with the address and the event types, they can add a description of the endpoint for their own records.
- An acceptable address uses HTTPS with TLS 1.3, has a certificate from a trusted authority, and is on a public address, never a local or private one such as 127.0.0.1.
- The secret is generated before we send the test event.
- The test event carries a zero amount.
- The endpoint counts as verified when it answers the test event with a 2xx status within 5 seconds.
- Once verified, the endpoint goes live in production mode for the chosen event types.
- We show the secret once, with instructions to store it securely, and they confirm they've stored it.

## What can go wrong

- The address isn't acceptable: plain HTTP, a local or private address, or a certificate we don't trust.
- They give up before submitting the endpoint.
- The endpoint can't be reached, answers with a non-2xx status, drops the connection, or takes more than 5 seconds to answer.
- They try to leave without confirming they've stored the secret.

## How each is handled

- Unacceptable address: the system says which rule it breaks and saves nothing; they give a compliant address and carry on, or give up.
- Giving up before submitting: nothing is saved.
- Endpoint doesn't confirm the test event: the system marks it unreachable, pending verification, and shows them the status code it got back or the failure diagnostic. It offers to save the endpoint disabled so they can debug it without live events going to it. If they save it, the endpoint is stored disabled and receives nothing until they re-enable it; if they decline, nothing is saved.
- Leaving without confirming the secret: the system warns that the secret can't be shown again and would have to be rolled if lost. They can store it and confirm, or leave anyway; the endpoint stays live either way, and a lost secret can only be rolled.

## Durations

- Checking the address and generating the secret is instant.
- The test event takes a few seconds at most: we wait up to 5 seconds for the answer, and they wait for it.
- Setting the endpoint live and showing the secret is instant.

## Out of scope

- A limit on the number of endpoints per account: we haven't defined one, so there's nothing to handle.
- An address that's already registered: several endpoints may share the same address, so there's nothing to handle.
- Exporting or erasing personal data: the setup only stores the address, description, event types and secret, none of which is personal data; the personal data in the events delivered later is handled by the platform's own privacy processes.
