# Answers: publish a component library update

## Actor, goal and scope

- The person publishing is the Design System Lead, usually a senior UI designer.
- The system is our collaborative design tool, specifically its workspace and library management.
- They start because changes to the organization's UI components, like a brand colour shift or new button sizes, need to reach every product team.
- Before they start they already have edit permission on the organization's master design system file; we don't re-check that here.
- No outside system or other person takes part; the design tool does everything itself.
- The changes can be to components and their variants, to styles, or to design tokens.
- It happens a few times a month per organization library, more often during a brand refresh.
- Accepting the updates in a subscriber file is the product designers' own job, and merging a library branch is a separate job too.

## Stakeholders and guarantees

- The Design System Lead wants to release only production-ready changes, with a clear record of what changed, without breaking the files that use the library.
- Product designers want predictable updates that never break the layout of the design files they're working in.
- Frontend engineers need token and variant names to stay faithful to the code components, and need breaking changes announced.
- Organization administrators want every release traceable to who published it, when, and what changed.
- However it ends, a library version is published completely or not at all.
- Publishing never modifies a subscriber file; each file's owner accepts the update when they're ready.
- Anything not published stays in the master file exactly as it was.
- When it works: the chosen changes are live as a new library version with its release notes, breaking variant changes tagged, retired components deprecated or removed as they chose; every subscriber file has an update notice with a preview of the differences; and the version history records the release, who published it and when.

## Main scenario

- The changes are compared against the published library and grouped as modified, added and deleted components and styles.
- They leave out exploratory draft components and accept the production changes.
- They give the release a semantic version, and it has to be higher than the library's current version.
- They write the release notes and tag the breaking variant changes themselves.
- A component can only be published when everything it references is resolved: its tokens, styles and nested components must already be in the library or go out in the same release.
- Publishing, sending the update notices to subscriber files and recording the release in the version history all happen together, and the system confirms when it's done.
- The update notice in each subscriber file comes with a preview of the differences.

## What can go wrong

- There's nothing unpublished in the master file to publish.
- A selected component points at a token or style that's no longer linked, or nests a component that's missing or that they left out of the release.
- They delete a component that subscriber files still use.
- The version they type isn't a valid semantic version, or isn't higher than the current one.
- Someone else published a version of the library, from another branch, after the changes were shown.
- The publication fails partway through.
- They give up before publishing.

## How each is handled

- Nothing to publish: the system says so and that's the end of it.
- Dangling reference: the system flags each affected component and names the reference; they either relink it in the master file or leave the component out, then look at their selection again.
- Deleting a component still in use: the system warns them with the number of subscriber files that use it and recommends deprecating it instead. They choose deprecation or confirm the permanent retirement. We warn whenever the component is used in any subscriber file, not only when it's used in hundreds.
- Bad version: the system says what's wrong, shows the current version, and they enter another.
- Someone else published meanwhile: nothing is published; the system reports the version conflict and names the version that went out. They merge the latest library into the master file and review the changes again.
- Publication fails partway: nothing is published, so the library stays on its previous version and no subscriber file gets a notice. Their selection and release notes are kept and they can publish again or stop.
- Giving up before publishing: nothing is published and their changes stay unpublished in the master file.

## Durations

- Comparing the master file with the library and showing the changes takes a few seconds.
- Verifying, publishing, sending the notices and recording the release takes a few seconds too; they stay until it's confirmed. Subscriber files don't have to be updated for it to finish, they only get a notice.

## Out of scope

- Not having permission isn't handled here: edit permission on the master file is in place before they start.
- No outside service is involved, so nothing can time out or be down.
- There's no limit on library size or number of releases that this has to deal with.
- Changes going stale while they review means someone else published in the meantime, which is the version conflict above.
- They can't cancel the publication itself; it takes only a few seconds.
- Exporting or erasing a member's data, such as their name in the version history, is a separate account privacy job, and the history's audit purpose limits erasure.
