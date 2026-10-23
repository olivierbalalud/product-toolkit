# Answers: add colleagues to an existing project channel

## Actor, goal and scope

- It's any member of the workspace; whether they're allowed to add people to that particular channel is checked, not assumed.
- They start because they've decided more colleagues need to take part in a project's discussions in a channel that already exists.
- Before they start they're signed in to the right workspace, and the channel exists.
- No outside system or other person takes part; the chat service does everything itself.
- Only people who are already members of the workspace can be added. Bringing someone new into the workspace, or giving people from another organisation access to the channel, is a separate job.
- They can add one colleague or several at once.
- It happens a few times a week in an active workspace, whenever a project takes on people.

## Stakeholders and guarantees

- The member wants the right colleagues in quickly, and wants to fix a wrong pick before anyone is actually added.
- The colleagues being added want access to the project's discussions as soon as they're in.
- The people already in the channel don't want their discussions opened to the wrong people.
- Workspace administrators want channel membership to follow the workspace's permissions, and nobody from outside the workspace getting in this way.
- However it ends, nobody is added unless the member confirmed them, and nobody outside the workspace is added.
- If a colleague can't be added, the membership simply stays as it was for that person.
- When it works, the colleagues are members of the channel, can see it according to its permissions, and the member is told who was added.

## Main scenario

- Opening the channel and getting to its members is just the member asking to add people to that channel; the screens don't matter.
- Who may add people to a channel is set by the channel's and the workspace's permissions.

## What can go wrong

- The member isn't allowed to add people to that channel.
- The colleague they look for can't be found among the workspace's members: a different spelling of the name, or the person isn't in the workspace at all.
- The colleague they look for is already in the channel.
- They notice they picked the wrong person before confirming.
- They give up before confirming.
- One of the colleagues they picked can't be added any more, because the account was deactivated or removed from the workspace in the meantime.

## How each is handled

- Not allowed: we tell them up front, when they ask, rather than after they've picked everyone. We say they can't add people there and who can: the channel's managers or a workspace administrator. Nothing changes, and they take it up with that person themselves.
- Can't find the colleague: we say nobody in the workspace matches. They check the name and whether the person is in the workspace, and look again. If the person isn't in the workspace, they carry on with the others or give up.
- Already in the channel: we show that the person is already a member and don't add them to the selection.
- Wrong person picked: they take that person out of the selection and pick again.
- Giving up before confirming: the selection is thrown away and nobody is added.
- A colleague can't be added any more: we add the others, say who couldn't be added and why, and leave the membership as it was for them.

## Durations

- Adding the colleagues and updating the membership is immediate.

## Out of scope

- Someone else adding the same colleague at the same moment: not something we need to handle; the person ends up a member either way.
- Limits on how many people a channel can hold: there are none to enforce here.
- Exporting or erasing a member's personal data, such as which channels they belong to: that's a separate account privacy job, not part of adding people to a channel.
