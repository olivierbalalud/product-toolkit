# Answers: create and assign a work item

## Actor, goal and scope

- The system is our work tracking service.
- The goal is a work item that can be tracked, with someone responsible for getting it done.
- They start because they've spotted a task, a bug or some other piece of work that needs tracking.
- Before they start they're signed in, and the project already exists.
- Having permission to create work items in the project is not a given: the service checks it.
- Nobody else takes part in creating the item. The only other person involved is the project administrator, who receives an access request if the member asks for one.
- The work type can be a task, a bug, or whatever other type the project offers.
- It happens several times a day per team member.

## Stakeholders and guarantees

- The team member wants to record the work quickly, with enough detail, and make clear who's responsible.
- The assignee should only get work they're eligible for, and the description should tell them what's expected.
- The project lead wants every work item to carry what the project needs to plan and track it, including where it sits under larger work.
- The project administrator wants only people with permission creating work items in the project.
- However it ends, no work item is ever half-created or created without what its work type requires.
- When creation fails, they're told what to correct, and what they typed is kept.
- When it works, the item is in the project with its type, title, description and required information, plus the priority, assignee and parent if they gave them, and they see its record for tracking.

## Main scenario

- Once they've picked the project and the work type, the service shows what that type requires in that project; each project configures this per work type.
- The description covers the task, its context and the expected result.
- Priority and assignee are set where relevant; leaving the item unassigned is fine.
- Submitting is part of the same moment as filling in the required information.
- On submit, the service checks the item, creates it and shows its record.

## What can go wrong

- They don't have permission to create work items in the project they picked.
- The title, or something the work type requires, is missing.
- The person they chose as assignee isn't eligible for work in that project.
- The work belongs under a larger work item; that's not a failure, just something they may want to record.
- Creation fails partway through.
- They cancel or walk away before submitting.

## How each is handled

- No permission: the service says so and names the project's administrator. They pick another project, or request access; the request goes to the administrator, they're told they'll be notified of the decision, and nothing is created for now. Granting access is the administrator's own job.
- Something missing: nothing is created, and the service points to what needs attention so they can fill it in and submit again.
- Ineligible assignee: the service says that person can't be given work in the project; they pick someone else or leave it unassigned.
- Larger work item: they name the parent, but only if the project is set up to allow parent links.
- Partial failure: nothing of the item is kept, what they typed is kept, and they're told it wasn't created so they can submit again.
- Cancelling or walking away: what they entered is thrown away and no item is created.

## Durations

- Showing what the work type requires is instant.
- Creating the item and showing its record is instant too.

## Out of scope

- Spotting that a work item for the same task already exists: the service doesn't look for that when creating; duplicates are linked or closed later, when the work is triaged.
- The project being archived or deleted while someone is creating an item in it: that's for the administrator's own use case to decide.
- Exporting or erasing a person's data across work items: a separate privacy job, not part of creating an item.
- Doing the work itself, running a whole sprint, or configuring the project's workflows.
