- **ID / Name:** UC-22 — Generate a Presentation from a Prompt
- **Scope:** AI presentation service (black box) · **Level:** User goal (!)
- **Primary actor:** Presenter (e.g. a teacher or a consultant)
- **Supporting actor:** AI model provider
- **Stakeholders & interests:**
  - Presenter — gets an editable first draft in their language and theme within a couple of minutes; can stop a generation that is going wrong.
  - Account owner — AI credits are spent only on slides the Presenter keeps.
  - Trust & safety — the service never generates prohibited content.
  - Image rights holders — only licensed images are placed in decks.
- **Trigger:** Presenter needs a deck on a topic.
- **Preconditions:** Presenter is signed in.
- **Minimal guarantees:** Credits are charged only for slides that are delivered and kept; no prohibited content is produced; a failed or cancelled generation never leaves a deck the Presenter did not choose to keep.
- **Success guarantees:** A new editable deck with the requested slides and theme is saved in the Presenter's workspace; credits are deducted; the generation is recorded in the account's usage history.

**Main success scenario**
1. Presenter describes the topic, the audience, the number of slides and the language.
2. System proposes an outline of slide titles.
3. Presenter edits the outline and chooses a theme.
4. System checks that enough credits remain and states the cost.
5. Presenter confirms the generation.
6. System generates the slides, showing each one as it is completed (typically 20 to 90 seconds).
7. System saves the deck, deducts the credits and opens the deck for editing.

**Extensions**
- 1a. The request asks for prohibited content: System declines and names the policy; Presenter rephrases (continue at step 1) or abandons (use case ends).
- 2a. The AI model provider does not answer within 10 seconds: System says so and offers to retry (continue at step 2); Presenter may abandon (use case ends).
- 4a. Not enough credits: System states the shortfall; Presenter reduces the number of slides (continue at step 4) or abandons (use case ends).
- 6a. Presenter cancels while slides are being generated: System stops; Presenter keeps the completed slides as a draft or discards them; only kept slides are charged; use case ends.
- 6b. Generation fails part-way: System keeps the completed slides, marks the failed ones and offers to regenerate them at no extra cost; continue at step 6 for those slides.
- 6c. Presenter leaves before the generation finishes: System completes and saves the deck; it appears in the Presenter's recent decks; use case ends.

**Business rules:** BR-1 one credit per slide · BR-2 at most 30 slides per generation · BR-3 images come only from the licensed library.
**Technology & data variations:** start from a prompt, a pasted document or an uploaded outline.
**Related:** Buy Credits, Export Deck.
