---
id: UC-015
title: Schedule a social media post
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-015: Schedule a social media post

| Field | Value |
|---|---|
| **Primary actor** | Content creator (a small business owner on a paid plan) |
| **Supporting actors** | Social networks (reconnect the creator's account; accept scheduled posts) |
| **Scope** | Online design service (content planner and publishing) |
| **Level** | User goal |
| **Trigger** | The creator has finished a promotional design and wants it published at peak engagement hours while they are offline. |
| **Preconditions** | The creator is on a plan that includes scheduling and has connected their social network accounts to the service. |
| **Minimal guarantees** | Nothing is scheduled on a channel unless the design was rendered for that channel and accepted for it; the original design is never altered; editing one channel's caption never changes another's; a cancelled or abandoned schedule leaves nothing scheduled. |
| **Success guarantees** | The design is rendered in a format each chosen network accepts; the post, with each channel's caption, tags and hashtags, is in the content calendar at its publishing date and time, and each network that accepts scheduled posts has confirmed it. Pending: publication at that time; the creator sees each post's status in the content calendar and is notified when it is published or if publishing fails (use case Publish a Scheduled Post). |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Content creator | Posts are published unattended at the chosen times on several networks, without the design's formatting being corrupted. |
| Social networks | Posts respect their rate limits, supported aspect ratios and media size restrictions. |

## Main success scenario

1. (actor) The creator chooses a finished design, the social channels to publish it on, and the publishing date and time.
2. (system) The system validates that each chosen channel's connection is active and that the design's dimensions and file size meet each network's publishing guidelines (BR-1).
3. (actor) The creator writes the caption, tags and hashtags for each channel.
4. (system) The system validates each channel's caption against that network's character limit and hashtag restrictions (BR-2).
5. (actor) The creator confirms the schedule.
6. (system, wait) The system renders the design in each network's format, registers the post for its publishing time with each network that accepts scheduled posts, places the post in the content calendar, and confirms the schedule to the creator.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-015.1a, UC-015.1b | out-of-scope: scheduling the same design again is allowed; reposting is the creator's choice | n/a | yes: UC-015.1-5a |
| 3 | yes: UC-015.3a | n/a | n/a | yes: UC-015.1-5a |
| 5 | n/a | n/a | n/a | yes: UC-015.1-5a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | n/a | n/a | n/a | yes: UC-015.2a | n/a |
| 4 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 6 | n/a | n/a | yes: UC-015.6a | yes: UC-015.6a | yes: UC-015.6a | n/a | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing the creator's account data, including connected social accounts and scheduled posts, is the service's own account privacy use case.

## Extensions

- **UC-015.1-5a** The creator cancels or abandons before confirming the schedule:
  1. The system schedules nothing; the original design is unchanged.
  2. The use case ends.

  *Example:* Omar chooses two channels and Friday 18:00 for his opening-hours graphic, is called away to the shop counter and never comes back to it; nothing is scheduled.
- **UC-015.1a** The design does not meet a chosen network's publishing guidelines: an unsupported aspect ratio, format or page count, or a file that is too large (BR-1):
  1. The system names the network and what is incompatible, and offers an automatic resize and reformat for that network.
  2. The creator accepts the conversion, which makes a copy for that network and leaves the original design unchanged, or chooses other pages of the design that comply.
  3. Returns to step 2.

  *Example:* Maya schedules her four-page spring sale flyer to the photo-sharing network, which does not take multi-page documents; she accepts the conversion into a set of square images.
- **UC-015.1b** The publishing time is not in the future, when chosen or by the time the creator confirms the schedule (BR-3):
  1. The system schedules nothing, says the time has passed, and asks for a future time; the captions already written are kept.
  2. The creator gives a new date and time: returns to step 2.

  *Example:* Omar sets 18:00 today for his happy-hour post but confirms at 18:03; the system asks for a new time and he chooses 19:00.
- **UC-015.2a** A chosen channel's connection has expired or been revoked:
  1. The system says which channel's connection is inactive.
  2. The system takes the creator through reconnecting that account with the social network, keeping the post's channels, date and time.
  3. Once the account is reconnected, returns to step 2. If the creator does not reconnect it, they remove that channel and the use case returns to step 2.

  *Example:* Maya's connection to the professional network was revoked when she changed her password there; she reconnects it, and her chosen channels and Tuesday 08:30 slot are kept.
- **UC-015.3a** A channel's caption exceeds that network's character limit or hashtag restrictions (BR-2):
  1. The system flags that channel's caption and shows by how much it exceeds the limit.
  2. The creator edits that caption; the other channels' captions are unchanged.
  3. Returns to step 4.

  *Example:* Omar's 310-character caption is 30 characters over the microblogging network's 280-character limit; he shortens it, and his longer caption for the professional network stays as written.
- **UC-015.6a** The post cannot be scheduled on one or more channels: the design cannot be rendered for it, or the network does not answer, or refuses the post because the account has reached its posting limit:
  1. The system schedules the post on the other channels and says which channels failed and why.
  2. The creator retries the failed channels: returns to step 6. Or the creator drops them: the use case ends with the post scheduled on the other channels.

  *Example:* Maya schedules her flyer to two networks; the professional network does not answer, so the post is scheduled on the photo-sharing network only, and her retry a minute later schedules it on the professional network too.

## Technology and data variations

- 1: the creator schedules the whole design or only some of its pages.
- 6: the network holds the scheduled post and publishes it itself, or the service holds it and sends it to the network at the publishing time.

## Related information

- **Frequency:** a few times a week per creator.
- **Business rules:** BR-1 each network's publishing guidelines: supported aspect ratios, formats, page counts and file sizes (step 2, UC-015.1a) · BR-2 each network's caption character limit and hashtag restrictions (step 4, UC-015.3a) · BR-3 the publishing time must be in the future (UC-015.1b).
- **Related use cases:** Publish a Scheduled Post.
- **Open issues:** None
