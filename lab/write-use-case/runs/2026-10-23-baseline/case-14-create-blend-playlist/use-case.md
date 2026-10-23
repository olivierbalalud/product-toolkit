---
id: UC-014
title: Invite a friend to a Blend
status: Draft
driver: lab
priority: <to set>
source_locale: en
inputs: []
stories: []
---

# UC-014: Invite a friend to a Blend

| Field | Value |
|---|---|
| **Primary actor** | Listener (free or paid plan) |
| **Supporting actors** | None |
| **Scope** | The music streaming service: mobile and desktop apps and the recommendation engine behind them |
| **Level** | User goal |
| **Trigger** | The listener asks to start a Blend, a shared mix that keeps itself up to date, with one specific friend |
| **Preconditions** | The listener is signed in. |
| **Minimal guarantees** | However it ends, no Blend is created and nothing of the listener's listening history is shared until someone accepts the invitation (BR-6). A link nobody accepts stops working when it expires (BR-2). |
| **Success guarantees** | An invitation link exists that only one person can use (BR-1), and the listener has sent it to their friend. Pending: the friend accepting it within 48 hours (BR-2). When the friend accepts, the Blend is built and added to both libraries and the listener gets a notification; if the link expires unused, there is no Blend. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Listener | Gets a shared mix with a friend for no more effort than sending a message. |
| Invited friend | Both tastes are represented fairly, and their private listening habits are not exposed; nothing of theirs is used before they accept. |
| Artists and rights holders | Streams of the Blend's tracks are counted to each listener who plays them. |

## Main success scenario

1. (actor) The listener asks to start a Blend with a friend.
2. (system) The system creates a new invitation link that can be accepted once, by one person (BR-1), and that expires 48 hours after it is made (BR-2), and offers the listener ways to share it.
3. (actor) The listener sends the link to the friend through a channel of their choice. The use case ends; the friend accepting the invitation, and the Blend being built and added to both libraries, belong to the friend's own use case.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | n/a | n/a: a repeated request is not a failure; it makes a new link (BR-3), see UC-014.1a | n/a: every signed-in listener, free or paid, may invite (BR-5) | n/a |
| 3 | n/a | out-of-scope: the system can't see where the link goes; if it reaches several people, only the first to accept joins (BR-1) and the others are told it's no longer valid in the friend's use case | n/a | yes: UC-014.3a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | out-of-scope: losing the connection while the link is made is handled the same way everywhere in the app | n/a | n/a: no cap on Blends or open invitations (BR-4) | n/a | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing a listener's listening data and their Blends belongs to the account privacy work. This use case shares no listening data (BR-6).

## Extensions

- **UC-014.1a** The listener already has open invitations to other friends:
  1. The system creates a new, independent link; the open invitations are unchanged (BR-3, BR-4).
  2. Returns to step 2.

  *Example:* Ana sent Ben an invitation this morning; in the afternoon she asks for a Blend with Chloé and gets a second link, while Ben's link stays valid until it expires.
- **UC-014.3a** The listener never sends the link, or changes their mind:
  1. The system does nothing: there is nothing to clean up. The link stays unused until it expires 48 hours after it was made (BR-2), no Blend is created and nothing is shared (BR-6).
  2. The use case ends.

  *Example:* Ana creates a link for Ben, closes the app without sending it, and two days later the link no longer works and no Blend exists.

## Technology and data variations

- Step 1: the listener starts from the mobile app or the desktop app.
- Step 3: the listener sends the link through a messaging app, posts it on a social network, or copies it and pastes it anywhere. The service does not integrate with those apps.

## Related information

- **Frequency:** occasional; a listener starts a Blend a few times a year.
- **Business rules:**
  - **BR-1** An invitation link can be accepted once, by one person: whoever accepts first joins.
  - **BR-2** An invitation link expires 48 hours after it is made. This window is fixed.
  - **BR-3** Each request makes a new link. A listener can have several invitations open at once, one per friend.
  - **BR-4** There is no cap on how many Blends or open invitations a listener has.
  - **BR-5** Free and paid listeners can both send invitations; no signed-in listener is refused. No minimum listening history is needed to invite; too little history is dealt with when the Blend is built.
  - **BR-6** Nothing is created and nothing of either person's listening history is shared until someone accepts the invitation.
- **Open issues:**
  - Is the listener told when a link expires unused, or does it lapse silently?
  - Can the listener see or revoke their open invitations before they expire?
  - Out of scope here and owned by the friend's use case: expired or already-used links, accounts with too little listening history, and tracks not licensed in one of the two countries.
