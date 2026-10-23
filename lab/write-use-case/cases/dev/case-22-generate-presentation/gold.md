---
id: UC-022
title: Generate a presentation from a prompt
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-022: Generate a presentation from a prompt

| Field | Value |
|---|---|
| **Primary actor** | Presenter (e.g. a teacher or a consultant) |
| **Supporting actors** | AI model provider (produces the outline and the slides) |
| **Scope** | AI presentation service |
| **Level** | User goal |
| **Trigger** | The Presenter needs a deck on a topic. |
| **Preconditions** | The Presenter is signed in. |
| **Minimal guarantees** | Credits are charged only for slides that are delivered and kept; no prohibited content is produced; a failed or cancelled generation never leaves a deck the Presenter did not choose to keep. |
| **Success guarantees** | A new editable deck with the requested slides and theme is saved in the Presenter's workspace and open for editing; the credits for its slides are deducted; the generation is recorded in the account's usage history. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| Presenter | Gets an editable first draft in their language and theme within a couple of minutes; can stop a generation that is going wrong. |
| Account owner | AI credits are spent only on slides the Presenter keeps. |
| Trust and safety | The service never generates prohibited content. |
| Image rights holders | Only licensed images are placed in decks. |

## Main success scenario

1. (actor) The Presenter describes the topic, the audience, the number of slides and the language.
2. (system, wait) The system asks the AI model provider for an outline and proposes the slide titles.
3. (actor) The Presenter edits the outline and chooses a theme.
4. (system) The system confirms that enough credits remain and states the cost (BR-1).
5. (actor) The Presenter confirms the generation.
6. (system, long) The system has the AI model provider generate the slides in the chosen language and theme, with images only from the licensed library (BR-3), and shows each slide as it is completed.
7. (system) The system saves the deck in the Presenter's workspace, deducts the credits (BR-1), records the generation in the account's usage history, and opens the deck for editing.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | yes: UC-022.1a, UC-022.1b | n/a | n/a | yes: UC-022.1-5a |
| 3 | yes: UC-022.3a | n/a | n/a | yes: UC-022.1-5a |
| 5 | n/a | n/a | n/a | yes: UC-022.1-5a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | yes: UC-022.2a | n/a | n/a | n/a | n/a |
| 4 | n/a | n/a | n/a | n/a | yes: UC-022.4a | n/a | n/a |
| 6 | n/a | n/a | yes: UC-022.6b | yes: UC-022.6b | n/a | n/a | yes: UC-022.6a, UC-022.6c |
| 7 | n/a | n/a | n/a | n/a | out-of-scope: the credits are checked once, at step 4; credits spent elsewhere on the account during the generation are not handled here | n/a | n/a |

**Privacy request:** yes: `deferred`, the prompt and the deck may hold personal data, but exporting or erasing a Presenter's decks and prompts is an account privacy use case, not part of generating a deck.

## Extensions

- **UC-022.1-5a** The Presenter abandons before confirming the generation:
  1. The system discards the request and the outline; no deck is saved and no credits are spent.
  2. The use case ends.

  *Example:* Marta gets an outline for "Photosynthesis for Year 8", is called into a parents' meeting and never confirms; no deck is saved and her 120 credits are untouched.
- **UC-022.1a** The request asks for prohibited content:
  1. The system declines and names the policy the request breaks.
  2. The Presenter rephrases: returns to step 1. Or abandons (UC-022.1-5a).

  *Example:* Sam asks for a deck mocking a named classmate; the system declines and names the harassment policy, and Sam asks instead for a deck on kindness online.
- **UC-022.1b** The request asks for more slides than one generation allows (BR-2):
  1. The system states the limit of 30 slides.
  2. The Presenter lowers the number of slides: returns to step 1. Or abandons (UC-022.1-5a).

  *Example:* Priya asks for 45 slides on the French Revolution; the system says one generation makes at most 30, and she asks for 30.
- **UC-022.2a** The AI model provider does not answer within 10 seconds:
  1. The system says the outline could not be produced and offers to try again.
  2. The Presenter tries again: returns to step 2. Or abandons (UC-022.1-5a).

  *Example:* Karim asks for a 12-slide deck on supply chain risks; no outline comes back within 10 seconds, he tries again and gets the outline.
- **UC-022.3a** The edited outline asks for prohibited content or has more than 30 slides (BR-2):
  1. The system declines the outline and names the titles that break the policy, or states the limit.
  2. Returns to step 3.

  *Example:* Jonas adds six slide titles to a 28-slide outline on cloud migration; the system says the limit is 30, and he removes four.
- **UC-022.4a** Not enough credits remain for the slides in the outline (BR-1):
  1. The system states the shortfall.
  2. The Presenter removes slides from the outline: returns to step 4. Or abandons (UC-022.1-5a).

  *Example:* Karim's outline has 25 slides and 18 credits remain; the system says he is 7 credits short, and he cuts the outline to 18 slides.
- **UC-022.6a** The Presenter cancels while the slides are being generated:
  1. The system stops the generation.
  2. The Presenter keeps the completed slides as a draft deck, and the system deducts credits for those slides only (BR-1); or discards them, and nothing is charged.
  3. The use case ends.

  *Example:* Lena sees that the first slides of her 20-slide deck use the wrong theme and cancels after 8; she keeps the 8 as a draft and is charged 8 credits.
- **UC-022.6b** The generation fails part way, or the AI model provider stops answering:
  1. The system keeps the completed slides and marks the failed ones.
  2. The system offers to regenerate the failed slides at no extra cost (BR-1).
  3. Returns to step 6 for the failed slides.

  *Example:* Slides 14 to 16 of Tom's 20-slide deck fail; the system keeps the other 17, marks the three, and Tom regenerates them without spending more credits.
- **UC-022.6c** The Presenter leaves before the generation finishes, without cancelling it:
  1. The system completes the generation, saves the deck, deducts the credits (BR-1) and records the generation in the account's usage history.
  2. The deck appears in the Presenter's recent decks.
  3. The use case ends.

  *Example:* Ana confirms a 30-slide deck and closes her laptop to catch a bus; the deck is completed and saved, and later she finds it among her recent decks.

## Technology and data variations

- 1: the Presenter starts from a prompt, a pasted document or an uploaded outline.

## Related information

- **Frequency:** a few times a month per Presenter.
- **Business rules:** BR-1 one credit per slide (steps 4 and 7, UC-022.4a, UC-022.6a, UC-022.6b, UC-022.6c) · BR-2 at most 30 slides per generation (UC-022.1b, UC-022.3a) · BR-3 images come only from the licensed library (step 6).
- **Duration:** proposing the outline takes a few seconds (step 2); generating the slides typically takes 20 to 90 seconds (step 6).
- **Related use cases:** Buy Credits, Export Deck.
- **Open issues:** None
