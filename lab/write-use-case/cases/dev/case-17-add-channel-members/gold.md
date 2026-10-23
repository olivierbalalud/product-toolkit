---
id: UC-017
title: Add colleagues to a project channel
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-017: Add colleagues to a project channel

| Field | Value |
|---|---|
| **Primary actor** | Workspace member |
| **Supporting actors** | None |
| **Scope** | Team chat service |
| **Level** | User goal |
| **Trigger** | The member decides that more colleagues need to take part in a project's discussions in an existing channel. |
| **Preconditions** | The member is signed in to the workspace that holds the project channel, and the channel exists. |
| **Minimal guarantees** | Only colleagues the member confirmed are ever added; the membership is unchanged for every colleague who could not be added; nobody outside the workspace is added. |
| **Success guarantees** | The selected colleagues are members of the channel and can access it according to its permissions; the member is told who was added. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Workspace member | Brings the right colleagues into the project quickly, and can correct a wrong selection before anyone is added. |
| Added colleagues | Get access to the project's discussions as soon as they are added. |
| Channel members | Their discussions are not opened to the wrong people. |
| Workspace administrators | Channel membership follows the workspace's permissions; people outside the workspace never join through this route. |

## Main success scenario

1. (actor) The member asks to add colleagues to the project channel.
2. (actor) The member finds and selects the colleagues to add among the workspace's members (BR-1).
3. (actor) The member confirms the selection.
4. (system) The system adds the selected colleagues to the channel, updates its membership, and tells the member who was added.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | n/a | n/a | yes: UC-017.1a | yes: UC-017.1-3a |
| 2 | yes: UC-017.2a | yes: UC-017.2b | n/a | yes: UC-017.1-3a |
| 3 | n/a | n/a | n/a | yes: UC-017.1-3a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 4 | yes: UC-017.4a | n/a | n/a | yes: UC-017.4a | n/a | yes: UC-017.4a | n/a |

**Privacy request:** yes: `deferred`, channel membership ties each colleague's name to the channel; exporting or erasing a member's workspace data is a separate account privacy use case, not part of adding people to a channel.

## Extensions

- **UC-017.1a** The member is not allowed to add people to this channel (BR-2):
  1. The system says the member cannot add people to this channel and names who can: the channel's managers or a workspace administrator.
  2. The use case ends; the membership is unchanged.

  *Example:* Ines asks to add two designers to the private "atlas-launch" channel, where only channel managers may add people; she is told that Marta, its manager, can add them.
- **UC-017.2a** No workspace member matches the colleague the member looks for (BR-1):
  1. The system says that no workspace member matches.
  2. The member checks the person's name and workspace membership and looks again: returns to step 2. If the person is not a workspace member, the member continues with the other colleagues or abandons (UC-017.1-3a).

  *Example:* Ines looks for "Jon Ferreira" and finds no one; his account is under "João Ferreira", so she looks for "João" and selects him.
- **UC-017.2b** A colleague the member looks for is already in the channel:
  1. The system shows that the colleague is already a member and leaves them out of the selection.
  2. Returns to step 2.

  *Example:* Ines looks for Paulo Reis to add him and sees that he is already a member of "atlas-launch".
- **UC-017.3a** The member notices a wrong person in the selection before confirming:
  1. The member removes that person from the selection.
  2. Returns to step 2.

  *Example:* Ines selected Ana Costa from finance instead of Ana Cruz from design; she removes Ana Costa and selects Ana Cruz.
- **UC-017.1-3a** The member abandons before confirming the selection:
  1. The system discards the selection; the membership is unchanged.
  2. The use case ends.

  *Example:* Ines has selected three colleagues, is called into a meeting and never confirms; nobody is added to "atlas-launch".
- **UC-017.4a** Some selected colleagues can no longer be added: their account was deactivated or removed from the workspace after they were selected (BR-1):
  1. The system adds the other colleagues, names those it could not add with the reason, and leaves the membership unchanged for them.
  2. The use case ends.

  *Example:* Ines confirms Ana Cruz and Rui Mota; Rui's account was deactivated a minute earlier, so Ana is added and Ines is told that Rui could not be added because his account is no longer active.

## Technology and data variations

- 2: the member selects one colleague, or several at once.

## Related information

- **Frequency:** a few times a week in an active workspace, whenever a project takes on people.
- **Business rules:** BR-1 only existing members of the workspace can be added to a channel; people outside it are invited to the workspace or connected from another organisation through other use cases (step 2, UC-017.2a, UC-017.4a). BR-2 who may add people to a channel is set by the channel's and the workspace's permissions (UC-017.1a).
- **Related use cases:** Invite a Person to the Workspace, Share a Channel with an External Organisation.
- **Open issues:** None
