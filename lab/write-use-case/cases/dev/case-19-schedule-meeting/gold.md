---
id: UC-019
title: Schedule a meeting
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-019: Schedule a meeting

| Field | Value |
|---|---|
| **Primary actor** | Meeting host |
| **Supporting actors** | Calendar service (sends the invitation to the participants) |
| **Scope** | Video meeting service |
| **Level** | User goal |
| **Trigger** | The host needs to arrange a discussion, such as a customer meeting or a team review. |
| **Preconditions** | The host is signed in to the video meeting service. |
| **Minimal guarantees** | A meeting is either saved in full with its joining information or not saved at all; participants are never sent an invitation for a meeting that is not saved, or with details that differ from the saved meeting. |
| **Success guarantees** | The meeting is saved with its topic, date, start time, duration and options, and has its joining information; the participants have been sent an invitation that holds the meeting details and the joining information. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Meeting host | Schedules the meeting at the right time and gets the joining information to the participants without retyping it. |
| Participants | Receive the correct date, time and joining information, so they can join. |
| Account administrator | Every meeting respects the account's settings, such as its security options. |

## Main success scenario

1. (actor) The host gives the meeting topic, date, start time, duration and meeting options (BR-1).
2. (actor) The host names the participants and saves the meeting.
3. (system) The system validates the details, saves the meeting with its joining information, and presents the invitation to the host.
4. (actor) The host asks to send the invitation to the participants.
5. (system, wait) The system sends the invitation through the host's calendar service and confirms to the host that it was sent.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-019.1a | n/a | yes: UC-019.1b | yes: UC-019.1-2a |
| 2 | yes: UC-019.2a | n/a | n/a | yes: UC-019.1-2a |
| 4 | n/a | n/a | n/a | yes: UC-019.4b |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 3 | n/a | out-of-scope: overlapping meetings are allowed; checking the host's or the participants' availability is not part of scheduling | yes: UC-019.3a | n/a | n/a | n/a | n/a |
| 5 | n/a | n/a | yes: UC-019.5a | out-of-scope: once the calendar service accepts the invitation, delivering it to each participant is its job | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, the meeting holds the participants' email addresses; exporting or erasing personal data kept with scheduled meetings belongs to a separate account privacy use case.

## Extensions

- **UC-019.1-2a** The host abandons scheduling before saving the meeting:
  1. The system saves nothing.
  2. The use case ends.

  *Example:* Ana starts scheduling the quarterly review, is called away before saving, and no meeting appears in her list.
- **UC-019.1a** A detail the host gave is invalid, such as a start date that has passed or a duration of zero:
  1. When it validates the details (step 3), the system saves nothing, names the invalid detail and keeps the others.
  2. Returns to step 1.

  *Example:* On 4 March Ana sets the supplier call for 3 March at 09:00; the system says the date has passed, and she moves it to 6 March.
- **UC-019.1b** The account's settings do not allow the host to schedule meetings, or do not permit a meeting option the host chose (BR-1):
  1. The system says which setting prevents it and saves nothing.
  2. The host chooses a permitted option: returns to step 1. Or the host stops to ask an account administrator to change the setting: nothing is saved, the use case ends, and the host schedules the meeting again once the administrator says the setting has changed (use case Change Account Meeting Settings).

  *Example:* Tom turns off the passcode for his customer demo, but his company's account requires one; the system says so, and he keeps the passcode.
- **UC-019.2a** A participant's email address is malformed:
  1. When it validates the details (step 3), the system saves nothing and names the address.
  2. Returns to step 2.

  *Example:* Tom adds `lena.berg@@northwind.example` to the demo; the system names that address, and he corrects it to `lena.berg@northwind.example`.
- **UC-019.3a** The service cannot save the meeting:
  1. The system saves nothing, tells the host the meeting was not scheduled, and keeps the host's details.
  2. The host tries again: returns to step 3. Or the host stops: the use case ends.

  *Example:* Ana saves the team review during a service outage; she is told it was not scheduled, and her retry a minute later succeeds with the same details.
- **UC-019.4a** The host notices a wrong detail, such as the time or the participant list, before sending the invitation:
  1. The host corrects the details.
  2. Returns to step 3, where the system saves the changes and presents the updated invitation.

  *Example:* Before sending, Ana sees she set the review for 30 minutes instead of 60; she corrects it, and the invitation now shows 60 minutes.
- **UC-019.4b** The host leaves without sending the invitation:
  1. The meeting stays scheduled with its joining information, and the invitation stays available with the meeting for the host to send later.
  2. The use case ends.

  *Example:* Tom saves the customer demo, is pulled into a call before sending the invitation, and finds the meeting and its invitation in his list when he gets back.
- **UC-019.5a** The calendar service does not answer or refuses the request:
  1. The system tells the host that the invitation was not sent and presents it for the host to copy.
  2. The host shares the invitation by another means, such as email or chat.
  3. The use case ends; the meeting is scheduled.

  *Example:* Ana asks to send the review invitation while her calendar service is down; she is told it was not sent, copies the invitation and posts it in her team's chat.

## Technology and data variations

- 2, 4-5: the host names the participants and the system sends the invitation through the calendar service; or the host names none, copies the invitation and shares it by email or chat.

## Related information

- **Frequency:** a few times a week per host.
- **Business rules:** BR-1 the account's settings decide whether a host may schedule meetings and which meeting options the host may choose (step 1, UC-019.1b).
- **Related use cases:** Change Account Meeting Settings, Host a Meeting.
- **Open issues:** None
