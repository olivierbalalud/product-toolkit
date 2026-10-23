**Use case ID:** B2B-01

**Name:** Add colleagues to an existing project channel

- **Primary actor:** Workspace member with permission to add people to the channel.
- **Goal:** Give selected colleagues access to an existing channel so they can participate in project discussions.
- **Trigger:** The actor determines that additional colleagues need to participate in the project.
- **Preconditions:**
  - The actor is signed in to the correct Slack workspace.
  - The target channel exists.
  - The actor has permission to add the intended members.
  - The intended colleagues are eligible to join the channel.

**Main success scenario**

1. The actor opens the target project channel.
2. The actor opens the channel's member management interface.
3. The actor searches for and selects the colleagues to add.
4. The actor confirms the selection.
5. Slack adds the selected colleagues to the channel and updates its membership.

**Alternative and exception flows**

- If a colleague cannot be found, the actor checks the person's workspace membership and identity before retrying.
- If the actor lacks permission, Slack prevents the addition and the actor requests assistance from an authorized administrator.
- If the actor selects the wrong person, the actor corrects the selection before confirming.

**Postconditions**

- **Success:** The selected colleagues are channel members and can access the channel according to its permissions.
- **Failure:** The channel membership remains unchanged for the unsuccessful addition.

**Scope boundary:** This use case covers adding existing workspace members, not onboarding new workspace members or managing external Slack Connect access.
