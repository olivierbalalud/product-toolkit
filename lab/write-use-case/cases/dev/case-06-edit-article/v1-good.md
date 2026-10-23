- **Name:** Edit an Article
- **Scope:** Wiki system (black box) · **Level:** User goal (!)
- **Primary actor:** Member (registered user)
- **Stakeholders & interests:**
  - Member — edits quickly, can preview and compare, never loses work.
  - Readers — articles stay accurate and readable.
  - Watchers — are informed of changes to articles they follow.
  - Community moderators — every change is attributable and reversible.
- **Trigger:** Member asks to edit the whole article or one section.
- **Preconditions:** An article with editing enabled is presented to the Member.
- **Minimal guarantees** *(added)*: The published article is never partially modified; unsaved changes are never published.
- **Success guarantees:** Article saved and updated view shown; an edit record is created so watchers can be informed.

**Main success scenario**
1. System presents the article's content (or only the section's content) for editing, with a pre-filled edit summary.
2. Member modifies the content until satisfied.
3. Member writes the edit summary, states whether to watch the article, and submits the edit.
4. System saves the article, records the edit, and completes any post-processing.
5. System presents the updated article.

**Extensions**
- 2–3a. Member asks for a preview: System shows the rendered content and warns it is not saved yet; continue at step 2.
- 2–3b. Member asks to see changes: System shows the differences from the latest saved version; continue at step 2.
- 2–3c. Member cancels: System discards the changes; continue at step 5 (unchanged article).
- 4a. Member's session has expired *(rewritten)*: System keeps the submitted content and asks the Member to sign in again; continue at step 4.
- 4b. Another member saved the article meanwhile *(added)*: System shows both versions so the Member can reconcile them; continue at step 2.
