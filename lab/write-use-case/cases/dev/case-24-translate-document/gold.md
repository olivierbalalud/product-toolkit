---
id: UC-024
title: Translate a document
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-024: Translate a document

| Field | Value |
|---|---|
| **Primary actor** | Subscriber (e.g. an account manager translating a contract) |
| **Supporting actors** | None |
| **Scope** | Document translation service |
| **Level** | User goal |
| **Trigger** | The Subscriber needs a document in another language. |
| **Preconditions** | The Subscriber is signed in on a plan that includes document translation. |
| **Minimal guarantees** | The document and its translation are deleted once the translation is downloaded, or after 24 hours (BR-2); characters are charged only for a delivered translation, never for a cancelled or failed one. |
| **Success guarantees** | The Subscriber has the translated document in the original format, with its layout kept and the chosen glossary and formality applied, and knows which glossary terms could not be applied; the characters (BR-3) are deducted from the quota; the document and its translation are deleted from the service (BR-2). |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Subscriber | Gets the document in the target language with its layout intact and the company's terms translated consistently, within a few minutes. |
| Owner of the document's content | Confidential text is not kept after the job. |
| Account owner | The character quota is charged only for delivered translations. |

## Main success scenario

1. (actor) The Subscriber provides the document and chooses the target language.
2. (system, wait) The system detects the source language, counts the characters to translate (BR-3) and presents the cost against the characters left in the quota.
3. (actor) The Subscriber chooses a glossary and the level of formality, and confirms the cost.
4. (system, long) The system translates the document, keeping its layout and applying the glossary and the formality, and shows its progress.
5. (system) The system deducts the characters from the quota and presents the translated document, listing any glossary terms it could not apply and saying until when it can be downloaded (BR-2).
6. (actor) The Subscriber downloads the translated document.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-024.1a, UC-024.1b | n/a | n/a | yes: UC-024.1-3a |
| 3 | n/a | n/a | n/a | yes: UC-024.1-3a |
| 6 | n/a | n/a | n/a | yes: UC-024.6a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | n/a | n/a | yes: UC-024.2b | n/a | n/a |
| 4 | n/a | n/a | yes: UC-024.4b | yes: UC-024.4b | out-of-scope: the quota is checked at step 2 and the cost confirmed at step 3; it is not checked again during the translation | n/a | yes: UC-024.4a |
| 5 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

**Privacy request:** no: the document and its translation are kept only until the translation is downloaded, and never longer than 24 hours (BR-2), so there is nothing left to export or erase.

## Extensions

- **UC-024.1-3a** The Subscriber abandons before confirming the cost:
  1. The system translates nothing and charges nothing; the document is deleted within 24 hours (BR-2).
  2. The use case ends.

  *Example:* Marta provides `supply-contract.docx`, sees it will cost 48,200 characters, and leaves without confirming; nothing is translated or charged.
- **UC-024.1a** The file cannot be used: its format is not supported, it is over the size limit (BR-1), or it is password-protected:
  1. The system says which of these applies.
  2. The Subscriber provides another file and the use case returns to step 2, or abandons (UC-024.1-3a).

  *Example:* Marta provides `tender-pack.pdf`, 42 MB; the system says it is over 30 MB, and she provides the 6 MB contract on its own instead.
- **UC-024.1b** The document is a scan with no text:
  1. The system says the document cannot be translated without text recognition.
  2. The use case ends.

  *Example:* Jonas provides `signed-lease.pdf`, photographed pages with no text in them; the system says it cannot translate it without text recognition.
- **UC-024.2a** The source language cannot be detected, or the document mixes languages:
  1. The system asks the Subscriber to choose the source language.
  2. The Subscriber chooses it; returns to step 3.

  *Example:* Marta's contract has its body in French and its annexes in Dutch; the system asks for the source language and she chooses French.
- **UC-024.2b** The quota does not have enough characters left for the document:
  1. The system states the shortfall.
  2. The Subscriber chooses a page range that fits: the system counts the characters of that range and returns to step 3. Or the Subscriber abandons (UC-024.1-3a).

  *Example:* Marta's contract has 52,000 characters and her quota has 30,000 left; she chooses pages 1 to 12, which come to 27,400 characters.
- **UC-024.4a** The Subscriber cancels during the translation:
  1. The system stops the translation, discards the partial translation and charges nothing.
  2. The use case ends.

  *Example:* At 40 % Marta sees she chose Spanish instead of Portuguese and cancels; nothing is charged.
- **UC-024.4b** The translation fails part-way:
  1. The system discards the partial result, charges nothing and offers to retry.
  2. The Subscriber retries: returns to step 4. Or the Subscriber abandons: the use case ends.

  *Example:* The translation of Jonas's 80-slide deck fails at 65 %; nothing is charged, he retries, and the translation completes.
- **UC-024.6a** The Subscriber does not download the translated document within 24 hours, by the time given at step 5:
  1. The system deletes the document and its translation (BR-2); the characters stay charged, because the translation was delivered.
  2. The Subscriber must translate the document again; the use case ends.

  *Example:* Marta's Spanish contract is ready at 16:50 on Wednesday; she is called away before downloading it and comes back on Friday; both files were deleted at 16:50 on Thursday, and she has to translate the contract again.

## Technology and data variations

- 1: the document is a word-processor, PDF or slide file.

## Related information

- **Frequency:** a few times a week per Subscriber.
- **Business rules:** BR-1 files are up to 30 MB (UC-024.1a) · BR-2 the document and its translation are deleted once the translation is downloaded, or after 24 hours (step 5, UC-024.1-3a, UC-024.6a) · BR-3 characters are counted on the source text (step 2).
- **Duration:** the translation takes from about 10 seconds to several minutes for long documents (step 4).
- **Related use cases:** Manage Glossary, Upgrade Plan.
- **Open issues:** None
