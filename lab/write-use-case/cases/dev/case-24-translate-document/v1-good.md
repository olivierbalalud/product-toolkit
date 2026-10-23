- **ID / Name:** UC-24 — Translate a Document
- **Scope:** Document translation service (black box) · **Level:** User goal (!)
- **Primary actor:** Subscriber (e.g. an account manager translating a contract)
- **Stakeholders & interests:**
  - Subscriber — gets the document in the target language with its layout intact and the company's terms translated consistently, within a few minutes.
  - Owner of the document's content — confidential text is not kept after the job.
  - Account owner — the character quota is charged only for delivered translations.
- **Trigger:** Subscriber needs a document in another language.
- **Preconditions:** Subscriber is signed in on a plan that includes document translation.
- **Minimal guarantees:** The document and its translation are deleted once downloaded, or after 24 hours (BR-2); characters are charged only for a delivered translation.
- **Success guarantees:** The translated document is available in the original format with its layout kept and the chosen glossary applied; the characters are deducted from the quota.

**Main success scenario**
1. Subscriber provides the document and chooses the target language.
2. System detects the source language and counts the characters to translate.
3. Subscriber chooses a glossary and the level of formality, and confirms the character cost.
4. System translates the document while keeping its layout, showing progress (from about 10 seconds to several minutes for long documents).
5. System presents the translated document, listing any glossary terms it could not apply.
6. Subscriber downloads the translated document.

**Extensions**
- 1a. Format not supported, file over the size limit, or password-protected: System says which; Subscriber provides another file (continue at step 1) or abandons (use case ends).
- 2a. Source language cannot be detected, or the document mixes languages: System asks the Subscriber to choose the source language; continue at step 3.
- 2b. The document is a scan with no text: System says it cannot be translated without text recognition; use case ends.
- 3a. Not enough characters left in the quota: System states the shortfall; Subscriber chooses a page range that fits (continue at step 4) or abandons (use case ends).
- 4a. Subscriber cancels during the translation: System stops, discards the partial translation and charges nothing; use case ends.
- 4b. Translation fails part-way: System discards the partial result, charges nothing and offers to retry (continue at step 4); Subscriber may abandon (use case ends).
- 6a. Subscriber does not download within 24 hours: System deletes both files; the Subscriber must translate the document again.

**Business rules:** BR-1 files up to 30 MB · BR-2 files are deleted after download or after 24 hours · BR-3 characters are counted on the source text.
**Technology & data variations:** word-processor, PDF or slide files.
**Related:** Manage Glossary, Upgrade Plan.
