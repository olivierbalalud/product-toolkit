# Answers: schedule a meeting

## Actor, goal and scope

- The system is our video meeting service.
- The host wants a future meeting set up at the right time, with everything participants need to join sent out to them.
- They start because they need to arrange a discussion, typically a customer meeting or a team review.
- Before they start, they're already signed in to the service.
- Whether the account lets them schedule, and which meeting options they may pick, isn't something we assume up front: the service checks it against the account's settings.
- The host's calendar service is what actually sends the invitation to the participants; it's outside our service.
- The host can name the participants and have the invitation sent through the calendar, or name nobody, copy the invitation and share it themself by email or chat.
- It happens a few times a week per host.
- Running the meeting, recording it and any follow-up are separate things, not part of scheduling. So is an administrator changing the account's settings.

## Stakeholders and guarantees

- The host wants the meeting at the right time and wants the joining information to reach the participants without retyping it.
- The participants need the correct date, time and joining information so they can join.
- The account administrator wants every meeting to respect the account's settings, such as its security options.
- A meeting is either saved completely, with its joining information, or not saved at all.
- Participants never get an invitation for a meeting that wasn't saved, or one whose details differ from what's saved.
- When it works: the meeting is saved with its topic, date, start time, duration and options, it has its joining information, and the participants have been sent an invitation with the details and the joining information.

## Main scenario

- Opening the scheduler isn't a step that matters; the host just starts giving the meeting details.
- The host looks over the details as part of saving; there's no separate review screen that matters.
- When the host saves, the service checks the details, saves the meeting with its joining information and shows the host the invitation.
- Sending is a separate choice the host makes after seeing the invitation.
- After sending through the calendar, the service confirms to the host that the invitation went out.

## What can go wrong

- The host abandons before saving.
- A detail is invalid, such as a start date that has already passed or a duration of zero.
- The account's settings don't allow the host to schedule meetings, or don't permit an option they chose.
- A participant's email address is malformed.
- The service can't save the meeting.
- The host notices a wrong time or participant list after saving but before sending.
- The host leaves after saving without sending the invitation.
- The calendar service doesn't answer or refuses the request.

## How each is handled

- Abandoning before saving: nothing is saved.
- Invalid detail: nothing is saved; the service names the invalid detail, keeps the rest, and the host corrects it.
- Account settings: the service says which setting is in the way and saves nothing. The host either picks an option that's allowed, or stops and asks an administrator to change the setting, then schedules again once the administrator tells them it's done.
- Malformed address: nothing is saved; the service names the address and the host corrects it.
- Can't save: nothing is saved, the host is told the meeting wasn't scheduled, their details are kept, and they can retry or stop.
- Wrong detail spotted before sending: the host corrects it, the service saves the change and shows the updated invitation, and they carry on to sending.
- Leaving without sending: the meeting stays scheduled with its joining information, and the invitation stays with the meeting so they can send it later.
- Calendar service unavailable: the host is told the invitation wasn't sent and is shown it to copy; they share it some other way, such as email or chat, and the meeting stays scheduled.

## Durations

- Saving the meeting and generating the joining information is immediate.
- Sending the invitation through the calendar service takes a few seconds.

## Out of scope

- Overlapping meetings: allowed; we don't check the host's or the participants' availability when scheduling.
- Some participants not getting the invitation after the calendar service accepted it: delivery to each person is the calendar service's job, not ours.
- Duplicate meetings, duplicate participants or sending twice: nothing to handle.
- Exporting or erasing personal data kept with scheduled meetings, such as participants' email addresses: a separate account privacy job, not part of scheduling.
