---
id: UC-014
title: Invite a friend to a Blend
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-014: Invite a friend to a Blend

| Field | Value |
|---|---|
| **Primary actor** | Listener (free or paid subscriber) |
| **Supporting actors** | None |
| **Scope** | Music streaming service (mobile and desktop apps, and the recommendation engine) |
| **Level** | User goal |
| **Trigger** | The Listener wants a shared, self-updating mix with a specific friend. |
| **Preconditions** | The Listener is signed in. |
| **Minimal guarantees** | No Blend is created and nothing of either listener's listening history is shared until a friend accepts the invitation; an invitation link nobody accepts stops working when it expires (BR-1). |
| **Success guarantees** | A single-use invitation link to a Blend with the Listener exists (BR-1), and the Listener has sent it to the friend. Pending: the friend's acceptance (use case Join a Blend). When the friend accepts, the Blend playlist is built and added to both listeners' libraries, and the Listener is notified; if the link expires unused, no Blend is created. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Listener | Gets a shared mix with a friend for no more effort than sending a message. |
| Invited friend | Both tastes are represented fairly in the Blend, without the friend's private listening habits being exposed. |
| Artists and rights holders | Streams of Blend tracks are counted to each listener who plays them. |

## Main success scenario

1. (actor) The Listener asks to create a Blend.
2. (system) The system creates a single-use invitation link with an expiry (BR-1) and offers it for sharing.
3. (actor) The Listener sends the invitation link to a friend through a messaging or social channel of their choice.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | n/a | n/a | n/a | n/a |
| 3 | n/a | out-of-scope: the system cannot see where the link is sent; a second person opening a link already accepted is handled in Join a Blend (BR-1) | n/a | yes: UC-014.3a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | out-of-scope: a lost connection is handled the same way across the whole app, not by this use case | n/a | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing a listener's listening data and Blends belongs to a separate account privacy use case.

## Extensions

- **UC-014.3a** The Listener does not send the invitation link:
  1. The system keeps the link unused until it expires (BR-1); no Blend is created and nothing is shared.
  2. The use case ends.

  *Example:* Maya creates an invitation link for her brother Theo, is called into a meeting before sending it and never comes back to it; once it expires, nobody can use it and no Blend exists.

## Technology and data variations

- 3: the Listener sends the link through a messaging app, posts it on a social network, or copies it to paste anywhere.

## Related information

- **Frequency:** Occasional: a listener starts a Blend a few times a year.
- **Business rules:** BR-1 an invitation link can be accepted once, by one listener, and expires 48 hours after it is created (step 2, UC-014.3a).
- **Related use cases:** Join a Blend, Refresh a Blend.
- **Open issues:** None
