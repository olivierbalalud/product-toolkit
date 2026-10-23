**Use case ID:** B2B-05

**Name:** Schedule and invite participants to a Zoom meeting

- **Primary actor:** Meeting host.
- **Goal:** Schedule a future meeting with the correct timing and distribute the information needed for participants to join.
- **Trigger:** The host needs to arrange a discussion, such as a customer meeting or team review.
- **Preconditions:**
  - The host can access Zoom and schedule meetings.
  - The host has determined the intended participants and an appropriate meeting time.
  - Any required account or administrator settings permit the selected meeting options.

**Main success scenario**

1. The host initiates meeting scheduling in Zoom.
2. The host enters the meeting topic, date, time, duration, and applicable meeting options.
3. The host specifies the participants or prepares the meeting invitation for distribution.
4. The host reviews the meeting details and saves the scheduled meeting.
5. Zoom creates the meeting and makes its joining information available.
6. The host sends or distributes the invitation so the intended participants can join.

**Alternative and exception flows**

- If the host cannot schedule the meeting because of account restrictions, the host resolves the restriction or uses an authorized alternative.
- If calendar integration is unavailable, the host uses another supported invitation method, such as copying and sharing the meeting invitation.
- If the time or participant list is incorrect, the host updates the details before distributing the invitation.
- If the meeting cannot be saved, the host corrects the reported problem and retries.

**Postconditions**

- **Success:** The meeting is scheduled, joining information is available, and the invitation has been prepared or distributed as intended.
- **Failure:** The meeting is not successfully scheduled, or the invitation remains undistributed until the problem is resolved.

**Scope boundary:** This use case covers scheduling and inviting participants, not conducting the meeting, recording it, or managing follow-up actions.
