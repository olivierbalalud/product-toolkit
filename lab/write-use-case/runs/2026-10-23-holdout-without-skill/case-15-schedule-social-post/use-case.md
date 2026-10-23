---
id: UC-015
title: Schedule a finished design to post on social networks
status: Draft
driver: lab
priority: TBD
source_locale: en
inputs: []
stories: []
---

# UC-015: Schedule a finished design to post on social networks

| Field | Value |
|---|---|
| **Primary actor** | Content creator, typically a small business owner on a paid plan |
| **Supporting actors** | The social networks the creator posts to, through their publishing services |
| **Scope** | The online design service: its content planner and publishing part |
| **Level** | User goal |
| **Trigger** | The creator asks to schedule a finished design for posting |
| **Preconditions** | The creator is on a paid plan that includes scheduling; the creator has connected their own social network accounts to the service; the design is finished |
| **Minimal guarantees** | The original design is never changed (any resized version is a separate copy). A channel is scheduled only if its post is saved in the content calendar and, for a network that accepts scheduled posts, that network has confirmed it; no channel is left half-scheduled. Each scheduling attempt and its outcome per channel is logged [BR-9]. |
| **Success guarantees** | The post sits in the content calendar at the chosen date and time on each selected channel, with that channel's own rendered image(s), caption and tags. Each network that accepts scheduled posts has confirmed it. The creator can follow each post's status in the content calendar, and will be notified when it goes out or fails at publication time (publication itself is a separate, time-triggered use case). |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Content creator | Get a finished promotional design posted at peak engagement hours without being online at the time; each channel's caption fits that channel; a failure on one channel doesn't cost the others. |
| Social networks | Their rate limits, posting limits, supported aspect ratios and media size limits are respected. |
| Service operator | Scheduling is reliable on the plans that include it; failures are explained and traceable for support. |

## Main success scenario

1. (actor) The creator chooses a finished design, either the whole design or some of its pages, and starts scheduling it.
2. (actor) The creator selects the destination channels and the publication date and time.
3. (system) The system checks each chosen page against each selected network's supported aspect ratios, dimensions and file size limits, checks each connection's authorization status from what it already knows (without contacting the network), and checks that the time is valid [BR-2, BR-3]. It flags any other post already scheduled on a selected channel at that time [BR-5].
4. (actor) The creator writes a caption and tags for each channel and confirms the schedule [BR-4].
5. (system) The system checks each channel's caption and tags against that network's character and hashtag limits, and checks again that the time is still valid [BR-2, BR-4].
6. (system, wait) The system renders the final image formats for each channel from the design as it is at confirmation [BR-6], hands the post to each network that accepts scheduled posts and receives its confirmation, saves each channel's post in the content calendar queue, and confirms to the creator which channels are scheduled.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-015.1a | n/a | n/a | yes: UC-015.1-5a |
| 2 | yes: UC-015.2a | yes: UC-015.2b | n/a | yes: UC-015.1-5a |
| 4 | yes: UC-015.4a | n/a | n/a | yes: UC-015.1-5a |

No permission is n/a throughout: the plan already includes scheduling (precondition) and the connected accounts are the creator's own, so there is no permission check in this flow.

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 3 | yes: UC-015.3-6a | yes: UC-015.2b | n/a | n/a | n/a | yes: UC-015.3a | n/a |
| 5 | yes: UC-015.3-6a | n/a | n/a | n/a | n/a | yes: UC-015.5a | n/a |
| 6 | yes: UC-015.3-6a | yes: UC-015.6b | yes: UC-015.6a | yes: UC-015.6a | yes: UC-015.6a | yes: UC-015.6a | n/a |

Step 3 does not contact the networks, so a slow or unreachable network cannot affect it. The time-window limits (lead time, horizon) are invalid input on step 2, not a quota.

**Privacy request:** no: the personal data involved is the creator's account and connected social accounts; export and erasure are handled by the service's general account privacy process, not by scheduling.

## Extensions

- **UC-015.1a** A chosen page does not meet a selected network's supported aspect ratios, dimensions or file size limit:
  1. The system names the affected network and what is wrong.
  2. The system offers to resize and reformat the design automatically for that network; if the creator accepts, it makes a copy for that network and leaves the original untouched [BR-3]. Alternatively, the creator picks other pages that do comply.
  3. Returns to step 3, where everything is checked again.

  *Example:* Mia picks her square bakery promo for a network that only accepts vertical images; the system says the aspect ratio isn't supported there, and she accepts a reformatted copy for that network.
- **UC-015.2a** The chosen time is in the past, sooner than the minimum lead time, or beyond the maximum horizon [BR-2]:
  1. Nothing is scheduled; the system says why the time is not accepted and asks for a valid time.
  2. Returns to step 2.

  *Example:* Mia sets Friday 08:00 but it is already Friday 09:15; the system asks for a future time.
- **UC-015.2b** Another post, including the same design, is already scheduled on a selected channel at the same time (not a failure):
  1. The system tells the creator which channel and which post clash.
  2. The creator keeps the time or changes it; both are allowed [BR-5].
  3. Continues at step 4 (or returns to step 2 if they change the time).

  *Example:* Mia schedules her weekend promo again on her page for Saturday 10:00, where it is already scheduled; the system notes it, and she keeps both.
- **UC-015.3a** A selected channel's connection is no longer authorized (expired or revoked):
  1. The system names the affected channel and walks the creator through reconnecting it with the network, keeping the channels and time already set.
  2. If the creator reconnects, returns to step 3.
  3. If not, that channel is removed from the post and the creator continues with the others at step 4. If no channel is left, returns to step 2.

  *Example:* Mia's photo-network authorization expired last week; the system asks her to reconnect it, and she does without re-entering her other choices.
- **UC-015.4a** A channel's caption or tags exceed that network's character or hashtag limits (detected at step 5):
  1. The system flags that channel's caption and shows how far over the limit it is; it never truncates [BR-4].
  2. The creator fixes that caption; the others are unchanged.
  3. Returns to step 5.

  *Example:* Mia's caption for the short-text network is 312 characters against a 280 limit; the system shows "32 over" on that channel only.
- **UC-015.5a** The chosen time has passed (or fallen under the minimum lead time) between picking it and confirming:
  1. Nothing is scheduled; the system asks for a future time and keeps all captions and tags.
  2. Returns to step 2, then continues to step 5.

  *Example:* Mia picked 14:00 at 13:58 and confirms at 14:03; the system asks for a new time and her captions are still there.
- **UC-015.3-6a** The design has been deleted before the schedule is committed (recommendation; not decided by the product owner):
  1. Nothing is scheduled; the system tells the creator the design no longer exists.
  2. The use case ends.

  *Example:* While Mia writes captions, her teammate deletes the promo design; on confirming, she is told it no longer exists.
- **UC-015.6a** Scheduling fails on one or more channels: rendering or saving fails, the network refuses (for example the account has reached its posting limit), or the network does not answer:
  1. The post stays scheduled on the channels that succeeded.
  2. The system says which channels failed and why.
  3. The creator retries the failed channels (returns to step 6 for those channels) or drops them and keeps the post on the channels that worked; the use case ends. If every channel failed, nothing is scheduled, and the creator retries or abandons (recommendation).

  *Example:* Mia schedules to three networks; one refuses because her account hit its daily posting limit; the other two are scheduled and she drops the third.
- **UC-015.6b** A teammate edited the design during scheduling:
  1. The system renders the design as it is at confirmation, so that version is posted [BR-6].
  2. If the edited version no longer meets a network's limits, that channel is handled as in UC-015.1a (recommendation).
  3. Continues at step 6.

  *Example:* Ben changes the promo headline while Mia writes captions; the scheduled post shows Ben's new headline.
- **UC-015.1-5a** The creator abandons before the schedule is committed, or their session ends:
  1. Nothing is scheduled and the design is untouched; no draft is kept [BR-8].
  2. The use case ends.

  *Example:* Mia picks channels and a time, then closes the planner; nothing appears in her calendar.

## Technology and data variations

- Step 1: the whole design, or only some of its pages; a multi-page selection posted as one multi-image post where the network supports it.
- Step 2: one channel or several.
- Step 4: an optional shared caption copied to each channel as a starting point, then edited per channel [BR-4].
- Step 6: a network that accepts scheduled posts (the post is handed over now and confirmed) or one that doesn't (the service holds the post and publishes it at the time).
- UC-015.1a: an automatically resized and reformatted copy per network.

## Related information

- **Frequency:** a few times a week per creator.
- **Business rules:**
  - **BR-1** Supported networks: the major social networks whose publishing services allow third-party posting of images (recommendation; the exact list is not decided).
  - **BR-2** Time: the publication time must be in the future both when picked and when confirmed. Recommendation (not decided): at least 10 minutes after confirmation; at most 6 months ahead, or the network's own scheduling window if shorter; entered and shown in the creator's account time zone, with the zone stated next to the time.
  - **BR-3** Media fit: each posted page must meet each network's supported aspect ratios, dimensions and file size limits. An automatic resize or reformat creates a copy for that network; the original design is never changed.
  - **BR-4** Captions: each channel has its own caption, tags and hashtags; editing one never changes another. Captions are never truncated. Recommendation (not decided): an optional shared caption that is copied once into each channel, after which each channel's copy is independent.
  - **BR-5** Reposting is the creator's call: scheduling the same design again on the same channel and time is allowed and not treated as a duplicate. A clash with another post at the same time is shown but not blocked (recommendation).
  - **BR-6** The posted version is the design as rendered at confirmation. Recommendation (not decided): later edits to the design do not change an already scheduled post; to change it, the creator edits the scheduled post (separate use case).
  - **BR-7** Each network's rate and posting limits are respected; a refusal fails that channel only (UC-015.6a). Recommendation (not decided): no service-side cap per plan on the number of scheduled posts, and no daily cap beyond the networks' own.
  - **BR-8** Abandoning keeps no draft (recommendation; not decided).
  - **BR-9** Each scheduling attempt is logged with its outcome per channel and the failure reason, for support (recommendation; not decided).
- **Open issues:**
  - Confirm the recommendations above: supported networks (BR-1), lead time, horizon and time zone (BR-2), shared caption (BR-4), clash handling (BR-5), edits after scheduling (BR-6), plan and daily caps (BR-7), draft on abandon (BR-8), logging (BR-9), design deleted before confirmation (UC-015.3-6a), all channels failing (UC-015.6a).
  - What a creator whose plan lacks scheduling sees when they try to start; treated as a precondition here, so it belongs to the plan or upgrade flow.
  - Related use cases: publish a scheduled post at its time (time-triggered, with the notification), edit or cancel a scheduled post, connect a social account.
