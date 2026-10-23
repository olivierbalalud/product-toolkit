---
id: UC-015
title: Schedule a design as a social media post
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-015: Schedule a design as a social media post

| Field | Value |
|---|---|
| **Primary actor** | Content creator (typically a small business owner on a paid plan) |
| **Supporting actors** | Social networks (reconnect an account; register the scheduled post, for the networks that accept scheduled posts) |
| **Scope** | The online design service's content planner and publishing |
| **Level** | User goal |
| **Trigger** | The creator wants a finished design published on one or more social networks at a set time. |
| **Preconditions** | The creator is on a paid plan that includes scheduling, and has connected their social accounts to the service. |
| **Minimal guarantees** | The design is never altered by scheduling. Nothing counts as scheduled on a channel unless it was rendered for that channel and the channel accepted it (BR-1), so the content calendar shows the post only on channels where it is scheduled. Giving up leaves nothing scheduled. |
| **Success guarantees** | The post is in the content calendar at the chosen time on each chosen channel, rendered in that channel's format with that channel's caption. Each network that accepts scheduled posts has confirmed it; the service holds the post for the other networks and publishes it there at that time. The creator knows which channels it is scheduled on. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Content creator | Gets the post out on every chosen channel at the chosen time, in each channel's format and with its own caption, without the original design being changed. |
| Social networks | Their rate limits, supported aspect ratios and media size limits are respected. |

## Main success scenario

1. (actor) The creator chooses a finished design, the channels and the publication date and time.
2. (system) The system confirms the design meets each channel's media rules and each account connection is valid, and presents each channel's caption rules.
3. (actor) The creator writes a caption and tags for each channel (BR-2).
4. (actor) The creator confirms the schedule.
5. (system, wait) The system renders the design as it stood at confirmation (BR-3) in each channel's format, registers the post with each network that accepts scheduled posts, holds it for the others, records it in the content calendar and confirms the channels it is scheduled on (BR-1).

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-015.1a, UC-015.1b | n/a | yes: UC-015.1c | yes: UC-015.1-4a |
| 3 | yes: UC-015.3a | n/a | n/a | yes: UC-015.1-4a |
| 4 | yes: UC-015.4a | n/a | n/a | yes: UC-015.1-4a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | n/a | n/a | yes: UC-015.5a | yes: UC-015.5a | yes: UC-015.5a | n/a | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing the creator's account and connected social accounts is handled by the service's general account privacy process.

## Extensions

- **UC-015.1a** The chosen publication time is in the past:
  1. The system schedules nothing, keeps the design and the channels, and asks for a future time.
  2. The creator gives a future time.
  3. Returns to step 2.

  *Example:* On Tuesday at 14:00, Lea chooses Tuesday 09:00 for her bakery's spring offer; the system asks her for a later time and she picks Wednesday 09:00.
- **UC-015.1b** The design does not meet a channel's media rules (aspect ratio, file size, format or page count):
  1. The system names the network and the problem, and offers to resize and reformat a copy of the design for that network, leaving the original untouched, or to let the creator pick other pages that comply.
  2. The creator takes the copy or picks other pages: returns to step 2. Or takes that channel off: returns to step 3 with the remaining channels. Or walks away: continues as in UC-015.1-4a.

  *Example:* Lea's 12-page brochure is too many pages for a photo network that accepts at most 10; she picks pages 1 to 10, and the re-check passes.
- **UC-015.1c** The connection to a chosen channel's account has expired or been revoked:
  1. The system names the channel and walks the creator through reconnecting the account with that network, keeping the channels and the time.
  2. The creator reconnects: returns to step 2. Or takes that channel off: returns to step 3 with the remaining channels. Or walks away: continues as in UC-015.1-4a.

  *Example:* Lea revoked the service's access on her video network last month; she reconnects it, and her three channels and Friday 18:00 are still chosen.
- **UC-015.3a** A channel's caption or its tags go over that channel's limits:
  1. The system names the channel and the limit exceeded, and leaves the other channels' captions as they are.
  2. Returns to step 3 for that channel only.

  *Example:* Lea's caption for a short-text network runs to 320 characters against its 280-character limit; she shortens it, and her two other captions are unchanged.
- **UC-015.4a** The publication time has passed when the creator confirms:
  1. The system schedules nothing, keeps the captions and asks for a future time.
  2. The creator gives a future time.
  3. Returns to step 4.

  *Example:* Lea chooses 09:00 at 08:50, spends until 09:05 on her captions and confirms; she sets 12:00 and confirms again with her captions intact.
- **UC-015.5a** A channel can't be rendered, its network does not answer, or its network refuses the post because the account has reached its posting limit:
  1. The system keeps the post scheduled on the channels that worked (BR-1) and tells the creator which channels failed and why.
  2. The creator retries the failed channels: returns to step 5 for those channels only. Or drops them: the use case ends with the post scheduled on the channels that worked, or on none if every channel failed.

  *Example:* Lea schedules her spring offer on three networks; one refuses because her account reached its daily posting limit, so the post is scheduled on the other two and she drops the third.
- **UC-015.1-4a** The creator gives up before confirming the schedule:
  1. The system schedules nothing and leaves the design untouched.
  2. The use case ends.

  *Example:* Lea chooses two channels and writes one caption, then leaves to serve a customer without confirming; nothing appears in her content calendar.

## Technology and data variations

None.

## Related information

- **Frequency:** A few times a week per creator.
- **Business rules:**
  - BR-1 nothing counts as scheduled on a channel unless it was rendered for that channel and the channel accepted it (step 5, UC-015.5a).
  - BR-2 each channel has its own caption; editing one never changes another (step 3, UC-015.3a).
  - BR-3 the design is rendered as it stood when the creator confirmed; later edits don't change what is scheduled (step 5).
- **Related use cases:** Publish a scheduled post at its time (time-triggered continuation).
- **Open issues:** None.
