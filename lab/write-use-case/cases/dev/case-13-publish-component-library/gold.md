---
id: UC-013
title: Publish a component library update
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-013: Publish a component library update

| Field | Value |
|---|---|
| **Primary actor** | Design System Lead (senior UI designer) |
| **Supporting actors** | None |
| **Scope** | Collaborative design tool (workspace and library management) |
| **Level** | User goal |
| **Trigger** | The Design System Lead has changes to the organization's UI components, such as a brand colour shift or new button sizes, that every product team should receive. |
| **Preconditions** | The Design System Lead has edit permission on the organization's master design system file. |
| **Minimal guarantees** | A library version is published in full or not at all; a publication never modifies a subscriber file; changes that are not published stay in the master file as they were. |
| **Success guarantees** | The selected changes are published to the organization library as a new version with its release notes, breaking variant changes tagged, and retired components deprecated or removed as chosen; every subscriber file has a non-destructive update notice with a preview of the differences; the version history records the release, who published it and when. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Design System Lead | Releases only production-ready changes, with a clear record of what changed, without breaking the files that use the library. |
| Product Designers | Get predictable updates that never break the layout of their active design files. |
| Frontend Engineers | Token and variant names stay faithful to the code components; breaking changes are announced. |
| Organization administrators | Every release can be traced to who published it, when, and what changed. |

## Main success scenario

1. (actor) The Design System Lead asks to publish the changes made in the master design system file.
2. (system, wait) The system compares the master file with the published library and presents the changes, grouped as modified, added and deleted components and styles.
3. (actor) The Design System Lead excludes exploratory draft components and accepts the production changes for release.
4. (actor) The Design System Lead gives the release a semantic version (BR-3), writes the release notes and tags the breaking variant changes.
5. (system, wait) The system verifies that every selected component has its references resolved (BR-1), publishes the selected changes as the new library version with its release notes, gives every subscriber file a non-destructive update notice with a preview of the differences (BR-4), records the release in the version history with who published it and when, and confirms the publication.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | n/a | n/a | n/a | yes: UC-013.1-4a |
| 3 | yes: UC-013.3a | n/a | n/a | yes: UC-013.1-4a |
| 4 | yes: UC-013.4a | n/a | n/a | yes: UC-013.1-4a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | yes: UC-013.2a | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | n/a | yes: UC-013.5a | n/a | yes: UC-013.5b | n/a | yes: UC-013.5a | n/a |

**Privacy request:** yes: `deferred`, the version history names the member who published each release; exporting or erasing a member's data belongs to a separate account privacy use case, and the audit purpose of the history limits erasure.

## Extensions

- **UC-013.1-4a** The Design System Lead abandons the review before publishing:
  1. The system publishes nothing; the changes stay unpublished in the master file.
  2. The use case ends.

  *Example:* Nadia reviews the changes, decides the new spacing tokens need another pass, and leaves; the library stays at version 2.4.0 and her edits remain in the master file.
- **UC-013.2a** The master file has no unpublished changes:
  1. The system says there is nothing to publish.
  2. The use case ends.

  *Example:* Nadia asks to publish on Monday morning, but Tom published every change on Friday afternoon; the system says there is nothing to publish.
- **UC-013.3a** A selected component has a dangling reference: an unlinked token or style, or a nested component that is missing or excluded from the release (BR-1):
  1. The system flags each such component and names its dangling reference.
  2. The Design System Lead relinks the reference in the master file, or excludes the component from the release.
  3. Returns to step 3.

  *Example:* Nadia selects the new Button/Large variant, whose label colour points to the deleted token `color/brand-600`; the system names the token, and she relinks the label to `color/brand-700`.
- **UC-013.3b** The Design System Lead accepts the deletion of a component that subscriber files still use (BR-2):
  1. The system warns of the impact, giving the number of subscriber files that use the component, and recommends deprecating it instead of deleting it.
  2. The Design System Lead marks the component deprecated, or confirms its permanent retirement.
  3. Returns to step 3.

  *Example:* Nadia deletes the old Card/Legacy component, used in 340 subscriber files; the system recommends deprecation, and she marks it deprecated instead.
- **UC-013.4a** The version given is not a valid semantic version, or is not higher than the library's current version (BR-3):
  1. The system says why and shows the current version.
  2. Returns to step 4.

  *Example:* Nadia enters "2.4" for a library at version 2.4.0; the system shows the current version, and she enters 3.0.0 because the release removes a button variant.
- **UC-013.5a** Another member published a version of the library since the changes were presented:
  1. The system publishes nothing, reports the version conflict and names the version published meanwhile.
  2. The Design System Lead merges the latest published library into the master file.
  3. Returns to step 2.

  *Example:* Nadia confirms version 3.0.0 at 14:10, but Omar published 2.5.0 from his icons branch at 14:05; nothing is published, and after merging Omar's icons she reviews the changes again.
- **UC-013.5b** The publication fails part way:
  1. The system publishes nothing, so the library stays at its previous version and no subscriber file gets an update notice; it keeps the selection and the release notes, and tells the Design System Lead the update was not published.
  2. The Design System Lead publishes again: returns to step 5. Or the Design System Lead stops: the use case ends.

  *Example:* The publication of version 3.0.0 fails after 40 of Nadia's 62 components are written; the library stays at 2.4.0, and her second attempt, with the same notes, succeeds.

## Technology and data variations

- 2: the changes are to components and their variants, to styles, or to design tokens.

## Related information

- **Frequency:** a few times a month per organization library; more often during a brand refresh.
- **Business rules:** BR-1 a component is published only when all its references are resolved: its tokens, styles and nested components are already in the library or in the same release (step 5, UC-013.3a) · BR-2 deleting a component that subscriber files still use triggers a warning with the number of those files, and deprecation is recommended over deletion (UC-013.3b) · BR-3 each release has a semantic version higher than the library's current version, and breaking variant changes are tagged (step 4, UC-013.4a) · BR-4 a publication never changes a subscriber file: each file's owner accepts the update when ready (step 5).
- **Related use cases:** Accept Library Updates, Merge a Library Branch.
- **Open issues:** None
