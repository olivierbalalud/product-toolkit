**Use case ID:** B2B-03

**Name:** Create and assign a project work item

- **Primary actor:** Project team member.
- **Goal:** Create a trackable work item and assign responsibility for completing it.
- **Trigger:** The actor identifies a task, bug, or other piece of work that needs tracking.
- **Preconditions:**
  - The actor is signed in to Jira.
  - The target project or space exists.
  - The actor has permission to create work items.
  - The required fields for the selected work type are known.

**Main success scenario**

1. The actor selects the target project or space and initiates work-item creation.
2. The actor selects the appropriate work type and enters a concise title.
3. The actor provides a description that explains the task, its context, and the expected result.
4. The actor supplies the required fields and, where relevant, sets the priority and assignee.
5. The actor submits the new work item.
6. Jira creates the work item and displays its record for further tracking.

**Alternative and exception flows**

- If required information is missing, Jira identifies the fields that need attention before creation can succeed.
- If the selected assignee is not eligible or the actor lacks permission, the actor corrects the assignment or requests access.
- If the work belongs under a larger item, the actor specifies the parent relationship when the project configuration supports it.

**Postconditions**

- **Success:** A work item exists in the selected project with the supplied details and assignment, if one was provided.
- **Failure:** No completed work item is produced, and the actor receives enough information to correct the submission.

**Scope boundary:** This use case covers creating a work item, not implementing the task, managing an entire sprint, or configuring Jira workflows.
