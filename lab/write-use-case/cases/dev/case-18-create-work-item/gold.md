---
id: UC-018
title: Create and assign a work item
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-018: Create and assign a work item

| Field | Value |
|---|---|
| **Primary actor** | Project team member |
| **Supporting actors** | Project administrator (receives access requests, UC-018.1a) |
| **Scope** | Work tracking service |
| **Level** | User goal |
| **Trigger** | The team member identifies a task, bug or other piece of work that needs tracking. |
| **Preconditions** | The team member is signed in, and the project exists. |
| **Minimal guarantees** | No work item is created in part or without the information its work type requires; when creation fails, the team member is told what to correct and the details entered are kept. |
| **Success guarantees** | The work item exists in the project with its work type, title, description and required information, and with the priority, assignee and parent if given; its record is presented to the team member for tracking. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Project team member | Records the work quickly, with enough detail, and makes clear who is responsible for it. |
| Assignee | Is given only work they are eligible for, with a description that says what is expected. |
| Project lead | Every work item carries the information the project needs to plan and track it, including its place under larger work. |
| Project administrator | Only people with permission create work items in the project. |

## Main success scenario

1. (actor) The team member chooses the project and the work type.
2. (system) The system presents the information that work type requires in that project (BR-1).
3. (actor) The team member gives a concise title and a description of the task, its context and the expected result.
4. (actor) The team member supplies the required information, sets the priority and the assignee where relevant, and submits the work item.
5. (system) The system validates the work item, creates it in the project and presents its record for tracking.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | n/a | n/a | yes: UC-018.1a | yes: UC-018.1-4a |
| 3 | yes: UC-018.3-4a | out-of-scope: the system does not look for existing work items on the same task; duplicates are linked or closed when the work is triaged | n/a | yes: UC-018.1-4a |
| 4 | yes: UC-018.3-4a, UC-018.4a | n/a | n/a | yes: UC-018.1-4a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 5 | out-of-scope: archiving or deleting a project is an administrator's use case, which decides what happens to work items being created | n/a | n/a | yes: UC-018.5a | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, a work item names the people who created it and are assigned to it; exporting or erasing a person's data across work items belongs to a separate account privacy use case.

## Extensions

- **UC-018.1-4a** The team member cancels or walks away before submitting the work item:
  1. The system discards the details entered; no work item is created.
  2. The use case ends.

  *Example:* Ana starts a bug in the "Mobile App" project, is pulled into a call before submitting, and never comes back; no work item is created.
- **UC-018.1a** The team member has no permission to create work items in the chosen project:
  1. The system says the team member cannot create work items in that project and names its administrator.
  2. The team member chooses another project: returns to step 1. Or the team member requests access: the system sends the request to the project administrator and tells the team member they will be notified of the decision; the use case ends with no work item created.

  *Example:* Priya chooses the "Billing" project, where she cannot create work items; she requests access from Omar, its administrator, and is told she will be notified of his decision.
- **UC-018.3-4a** A title or information the work type requires is missing (BR-1):
  1. The system creates nothing and names the information that needs attention.
  2. Returns to step 3 for a missing title or description, or to step 4 for other required information.

  *Example:* Ben submits a bug in the "Web Store" project without the affected version, which bugs require there; the system names the affected version, Ben adds "2.4", and submits again.
- **UC-018.4a** The chosen assignee is not eligible for work in the project (BR-3):
  1. The system says that person cannot be assigned work in this project.
  2. The team member chooses another assignee or leaves the work item unassigned: returns to step 4.

  *Example:* Ana assigns the task "Renew TLS certificate" to Lucas, who is not a member of the "Platform" project; she assigns it to Mei instead.
- **UC-018.4b** The work belongs under a larger work item, and the project supports parent links (BR-2):
  1. The team member names the parent work item.
  2. Returns to step 4.

  *Example:* Ben creates the task "Add CSV export button" and places it under the epic "Reporting improvements".
- **UC-018.5a** The work item cannot be created in full:
  1. The system keeps nothing of the work item, keeps the details entered, and tells the team member it was not created.
  2. Returns to step 4.

  *Example:* Priya submits the bug "Login fails on Safari"; the creation fails part way, no work item appears in the project, and her title and description are kept for her to submit again.

## Technology and data variations

- 1: the work type is a task, a bug or another type the project offers.

## Related information

- **Frequency:** several times a day per team member.
- **Business rules:** BR-1 each work type in a project requires its own information, set by the project configuration (step 2, UC-018.3-4a) · BR-2 a work item can be placed under a parent only when the project configuration supports it (UC-018.4b) · BR-3 only people eligible for work in the project can be assigned (UC-018.4a).
- **Related use cases:** Grant Project Access.
- **Open issues:** None
