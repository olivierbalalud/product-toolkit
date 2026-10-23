---
id: UC-017
title: Add colleagues to an existing project channel
status: Draft
driver: lab
priority: TBD
source_locale: en
inputs: []
stories: []
---

# UC-017: Add colleagues to an existing project channel

| Field | Value |
|---|---|
| **Primary actor** | Workspace member |
| **Supporting actors** | None |
| **Scope** | The chat service |
| **Level** | User goal |
| **Trigger** | The member decides that more colleagues need to take part in a project's discussions in a channel that already exists, and asks to add them to it. |
| **Preconditions** | The member is signed in to the right workspace, and the channel exists. |
| **Minimal guarantees** | Nobody is added unless the member confirmed them, and nobody from outside the workspace is added. For any colleague who can't be added, the channel membership stays as it was. |
| **Success guarantees** | The selected colleagues are members of the channel and can see it according to its permissions. The member is told who was added. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Workspace member | Gets the right colleagues in quickly, and can fix a wrong pick before anyone is actually added. |
| Colleagues being added | Have access to the project's discussions as soon as they are in. |
| Existing channel members | Their discussions are not opened to the wrong people. |
| Workspace administrators | Channel membership follows the workspace's permissions, and nobody from outside the workspace gets in this way. |

## Main success scenario

1. (actor) The member asks to add colleagues to the project channel.
2. (system) The system checks that the member may add people to this channel [BR-1] and asks whom to add.
3. (actor) The member names one or more colleagues to add.
4. (system) The system finds each colleague among the workspace's members [BR-2] and adds them to the selection.
5. (actor) The member reviews the selection and confirms it [BR-3].
6. (system) The system adds the selected colleagues to the channel, gives them access according to the channel's permissions, and tells the member who was added.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | n/a | n/a | yes: UC-017.1a | yes: UC-017.1-5a |
| 3 | yes: UC-017.3a | yes: UC-017.3b | n/a | yes: UC-017.1-5a |
| 5 | yes: UC-017.5a | n/a | n/a | yes: UC-017.1-5a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | yes: UC-017.3a | n/a | n/a | n/a | n/a | n/a | n/a |
| 6 | yes: UC-017.6a | out-of-scope: if someone else adds the same colleague at the same moment, the person ends up a member either way | n/a | yes: UC-017.6a | out-of-scope: channels have no member limit to enforce here | yes: UC-017.6a | n/a |

**Privacy request:** yes: `deferred`, exporting or erasing a member's personal data, such as which channels they belong to, is a separate account privacy use case, not part of adding people to a channel.

## Extensions

- **UC-017.1a** The member is not allowed to add people to this channel [BR-1]:
  1. The system tells the member, as soon as they ask, that they can't add people to this channel and who can: the channel's managers or a workspace administrator.
  2. Nothing changes; the member takes it up with that person themselves. The use case ends.

  *Example:* Ana asks to add Ben to #room-booking-redesign, but only the channel's managers may add people there; she is told to ask Carla, the channel manager.
- **UC-017.1-5a** The member gives up before confirming:
  1. The system discards the selection; nobody is added.
  2. The use case ends.

  *Example:* Ana picks Ben and Dev, then decides to wait until the project kickoff and leaves without confirming; neither is added.
- **UC-017.3a** No workspace member matches the colleague the member names (a different spelling, or the person is not in the workspace) [BR-2]:
  1. The system says that nobody in the workspace matches.
  2. The member checks the name and whether the person is in the workspace, and returns to step 3. If the person is not in the workspace, the member carries on with the others or gives up (UC-017.1-5a).

  *Example:* Ana searches for "Jon Smyth"; nobody matches, she retries with "John Smith" and finds him.
- **UC-017.3b** The colleague is already a member of the channel:
  1. The system shows that the person is already a member and does not add them to the selection.
  2. Returns to step 3.

  *Example:* Ana looks for Ben, who joined #room-booking-redesign last week; he is shown as already a member and is not added to the selection.
- **UC-017.5a** The member notices a wrong pick before confirming:
  1. The member takes that person out of the selection.
  2. Returns to step 3 to pick again.

  *Example:* Ana picked Dev Patel from Finance instead of Dev Patil from Facilities; she removes him and picks the right Dev.
- **UC-017.6a** One or more selected colleagues can no longer be added, because their account was deactivated or removed from the workspace in the meantime:
  1. The system adds the others.
  2. The system tells the member who could not be added and why, and leaves the membership as it was for them.
  3. The use case ends.

  *Example:* Ana confirms Ben and Dev, but Dev's account was deactivated a minute earlier; Ben is added and Ana is told Dev couldn't be added because his account is deactivated.

## Technology and data variations

- Step 3: one colleague or several colleagues at once.

## Related information

- **Frequency:** a few times a week in an active workspace, whenever a project takes on people.
- **Business rules:**
  - **BR-1** Who may add people to a channel is set by the channel's and the workspace's permissions. A member who may not do it is pointed to the channel's managers or a workspace administrator.
  - **BR-2** Only people who are already members of the workspace can be added. Bringing someone new into the workspace, or giving people from another organisation access to the channel, is a separate use case.
  - **BR-3** Nobody is added to the channel unless the member confirmed them.
- **Open issues:**
  - Priority is not yet set.
  - What happens if the member's permission to add people is withdrawn between step 2 and step 6.
