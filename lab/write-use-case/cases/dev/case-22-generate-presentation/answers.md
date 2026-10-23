# Answers: generate a presentation from a prompt

## Actor, goal and scope

- The system is our AI presentation service.
- The Presenter is typically a teacher or a consultant.
- They start because they need a deck on some topic.
- Before they start they're already signed in.
- We call on an outside AI model provider: it produces both the outline and the slides.
- They can start from a prompt, by pasting a document, or by uploading an outline of their own.
- A Presenter does this a few times a month.
- Buying credits and exporting a deck are separate things, not part of this.

## Stakeholders and guarantees

- The Presenter wants an editable first draft in their language and theme within a couple of minutes, and wants to be able to stop a generation that's going wrong.
- The account owner wants AI credits spent only on slides the Presenter actually keeps.
- Trust and safety needs the service never to generate prohibited content.
- Image rights holders need only licensed images to end up in decks.
- Whatever happens, credits are only charged for slides that were delivered and kept.
- No prohibited content is ever produced.
- A failed or cancelled generation never leaves behind a deck the Presenter didn't choose to keep.
- When it works: the new deck is saved in the Presenter's workspace, editable, with the slides and theme they asked for; the credits are taken; and the generation shows up in the account's usage history.

## Main scenario

- The outline the system proposes is a list of slide titles.
- One slide costs one credit; that's the cost we state before they confirm.
- We check that enough credits remain before stating the cost.
- Images in the slides come only from our licensed library.
- When the generation is done the deck is saved in their workspace and the generation is logged in the usage history.

## What can go wrong

- They ask for prohibited content.
- They ask for more than 30 slides, which is the most one generation makes.
- When editing the outline they add prohibited content, or take it over 30 slides.
- The AI model provider doesn't answer within 10 seconds when we ask for the outline.
- There aren't enough credits left for the slides in the outline.
- They give up before confirming the generation.
- They cancel while the slides are being generated.
- The generation fails partway, or the AI model provider stops answering during it.
- They walk away while the slides are being generated, without cancelling.

## How each is handled

- Prohibited content in the request: the system declines and names the policy; they rephrase, or give up.
- Too many slides requested: the system states the 30-slide limit; they lower the number, or give up.
- Prohibited content or too many slides in the edited outline: the system declines the outline and names the offending titles or states the limit, and they keep editing.
- Provider doesn't answer for the outline: the system says so and offers to try again; they retry, or give up.
- Not enough credits: the system states the shortfall; they cut slides from the outline and we check again, or they give up. We don't offer to buy credits from here.
- Giving up before confirming: the request and outline are thrown away; no deck is saved and no credits are spent.
- Cancelling during generation: the system stops; they either keep the slides done so far as a draft deck and pay only for those, or discard them and pay nothing.
- Generation fails partway or the provider stops: the system keeps the finished slides, marks the failed ones, and offers to regenerate those at no extra cost; generation then picks up again for just those slides.
- Walking away during generation: the generation still finishes, the deck is saved and charged as normal and logged in the usage history, and it shows up in their recent decks.

## Durations

- Proposing the outline takes a few seconds.
- Checking the credits and stating the cost is immediate.
- Generating the slides typically takes 20 to 90 seconds. They stay and watch the slides appear, and can cancel.
- Saving the deck and opening it for editing is immediate.

## Out of scope

- Credits being spent elsewhere on the account while the generation runs, so there aren't enough left when we deduct: not handled; we check credits once, before they confirm, and not again.
- Exporting or erasing a Presenter's decks and prompts, which may hold personal data: that's an account privacy matter, not part of generating a deck.
- Duplicates and permissions don't come up: confirming is a single action, and any signed-in Presenter can generate a deck.
