# Answers: translate a document

## Actor, goal and scope

- The system is our document translation service; we treat it as a black box.
- A typical subscriber is an account manager who needs a contract in another language.
- They start because they need a document in another language.
- Before they start they're already signed in, on a plan that includes document translation.
- No outside system or other person takes part; the service does the translation itself.
- The document can be a word-processor file, a PDF or a slide file.
- It happens a few times a week per subscriber.
- Managing glossaries and upgrading the plan are separate things, not part of this.

## Stakeholders and guarantees

- The subscriber wants the document in the target language with its layout intact and the company's terms translated consistently, within a few minutes.
- Whoever owns the document's content wants the confidential text not kept once the job is done.
- The account owner wants the character quota charged only for translations that were actually delivered.
- However it ends, the document and its translation are deleted once the translation is downloaded, or after 24 hours at most.
- A cancelled or failed translation is never charged.
- When it works: they have the translated document in its original format, layout kept, with the glossary and formality they chose applied, and they know which glossary terms couldn't be applied; the characters are taken off the quota; and both files are deleted.
- Nobody needs to ask us to export or erase their data: we only hold the files until download, 24 hours at the most, then they're gone.

## Main scenario

- Characters are counted on the source text, not the translation.
- Along with the count, the system shows the cost against the characters left in the quota, so they know what they're confirming.
- The translation keeps the layout and applies the chosen glossary and formality, and they see its progress.
- The characters are taken off the quota when the finished translation is presented, not when it's downloaded.
- When it presents the translation, the system also says until when it can be downloaded.
- Files are limited to 30 MB.

## What can go wrong

- The file can't be used: a format we don't support, over the 30 MB limit, or password-protected.
- The document is a scan with no text in it.
- The source language can't be detected, or the document mixes languages.
- There aren't enough characters left in the quota for the document.
- They give up before confirming the cost.
- They cancel while the translation runs.
- The translation fails partway through.
- They don't download the translation within 24 hours.

## How each is handled

- Unusable file: the system says which of the three problems it is; they provide another file or give up.
- Scan with no text: the system says it can't be translated without text recognition, and that's the end of it.
- Language not detected or mixed: the system asks them to choose the source language, and they carry on choosing the glossary and formality.
- Not enough characters: the system says how many are missing; they choose a page range that fits, which is counted again, or they give up.
- Giving up before confirming: nothing is translated or charged; the uploaded document is deleted within 24 hours like any other file.
- Cancelling during the translation: the system stops, throws away the partial translation, and charges nothing.
- Translation failure: the partial result is thrown away, nothing is charged, and the system offers to retry; they retry or give up.
- Not downloading within 24 hours, by the time the system gave them: both files are deleted, the characters stay charged because the translation was delivered, and they'd have to translate the document again.

## Durations

- Detecting the language and counting the characters takes a few seconds.
- The translation takes from about ten seconds to several minutes for long documents. They stay and watch the progress, and can cancel.
- Presenting the result is immediate once the translation is done.

## Out of scope

- The quota running short during the translation itself, for example because someone else on the account used characters meanwhile: not handled; the quota is checked and the cost confirmed before the translation starts, and not checked again while it runs.
