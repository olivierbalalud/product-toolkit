# UX lens: from use case to clickable flow

What a UX designer needs to think and do to turn a complete use case into a prototype that passes Design-complete. The reading path and the other lenses are in [`README.md`](README.md); the PM side is in [`pm-lens.md`](pm-lens.md), the engineering side in [`swe-lens.md`](swe-lens.md). Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md).

All links were checked on 2026-10-19 ([sources](../research/foundations-sources-product-ux.md)). **Time** counts the text plus any video under 30 minutes; longer videos are marked optional.

## Contents

- [1. Key behaviours](#1-key-behaviours)
- [2. Concepts](#2-concepts)
  - [2.1 Task flows and wireframes](#21-task-flows-and-wireframes)
  - [2.2 Interaction states](#22-interaction-states)
  - [2.3 Design systems and atomic design](#23-design-systems-and-atomic-design)
  - [2.4 Component inventory](#24-component-inventory)
  - [2.5 Design tokens](#25-design-tokens)
  - [2.6 Modalities and touch points](#26-modalities-and-touch-points)
  - [2.7 Accessibility](#27-accessibility)
  - [2.8 UX writing, voice and tone](#28-ux-writing-voice-and-tone)
  - [2.9 Usability testing and heuristics](#29-usability-testing-and-heuristics)

## 1. Key behaviours

- **Design states, not screens.** A screen is one state among several: empty, loading, error, partial, success, no permission, stale data. Every screen gets a row in the state matrix before it is "done" [R2-Q3].
- **Keep flow, look and voice apart.** A PRD designs the **flow** (screens, transitions, key information and actions). The **look** (tokens, components, motion) is global and only used, never redesigned per PRD. The **voice** has a global guide and a per-PRD copy deck [R1-Q4].
- **Write real copy from the first sketch.** A button reads "Next step" or "Étape suivante", never `screen1.panel2.next.label` [R1-Q4].
- **Design with the design system only.** If a component is missing, raise an enabler slice instead of drawing a one-off [R2-Q3 (g), R7-Q2].
- **Prototype in the real stack.** Screens are built with Next.js and the shadcn-based design system, against mocked data. Sketches elsewhere are throwaway [R1-Q5, R2-Q1].

## 2. Concepts

### 2.1 Task flows and wireframes

- **Roles:** UX [core] · PM [optional] · SWE [optional]
- **Time:** ~11 min (text + video)

**Definition**

A task flow (or user flow) is the sequence of steps and decisions a user goes through to complete one task in the product. A wireframe is a low-fidelity layout of one screen; a wireflow combines both, showing screens joined by the transitions between them.

**Why it matters**

- **UX:** it is where the use case turns into screens.
- **PM:** it shows whether the story's path is complete before anything is built.
- **SWE:** it lists every screen and transition the slice must implement.

**In this framework**

The flow map and screen list live in [`flows.md`](../templates/flows.md) as a Mermaid diagram plus one block per screen, with key information and key actions traced to the story [R2-Q3 (c, e)]. We skip separate wireframes: the "wireframe" is the coded prototype under `(prototypes)/`, built from real components [R1-Q5]. A task flow usually matches one **user-goal** use case ([goal levels](pm-lens.md#22-goal-levels)): it starts where the user takes up the goal and ends where they can walk away with it done, the coffee-break test [R28-Q1]. A flow that spans several sittings is a summary goal, split into several use cases; one that covers a single field or choice is a subfunction, a step inside a flow. See [design playbook, step 4](../guide/03-design-playbook.md#35-step-4-explore).

**Learn it**

- Text: [User Journeys vs. User Flows](https://www.nngroup.com/articles/user-journeys-vs-user-flows/) (NN/g, ~7 min)
- Text: [Wireflows](https://www.nngroup.com/articles/wireflows/) (NN/g, ~9 min)
- Video: [User Journeys vs. User Flows](https://www.youtube.com/watch?v=dsviXwJwslI) (NNgroup, 3:47)

**Key literature**

- Jesse James Garrett, *The Elements of User Experience* (2002), as a general reference

### 2.2 Interaction states

- **Roles:** UX [core] · PM [optional] · SWE [optional]
- **Time:** ~28 min (text + video)

**Definition**

Every screen exists in several states, not only the ideal one: before there is data, while it loads, when something fails, when only part of it is available, and when it works. Scott Hurff calls this set the "UI stack" (blank, loading, partial, error, ideal).

**Why it matters**

- **UX:** the missing states are where users get lost.
- **SWE:** each state is a code path that needs a test.
- **PM:** failure states are where use-case extensions become visible.

**In this framework**

Our state matrix has seven columns, two more than Hurff's stack: empty, loading, error, partial, success, **no permission** and **stale data** [R2-Q3 (d)]. It is in [`flows.md`](../templates/flows.md), and a state-matrix checker runs in the UX review lane [R4-Q7a, R4-Q7d].

**Learn it**

- Text: [Why your user interface is awkward: you're ignoring the UI stack](https://www.scotthurff.com/posts/why-your-user-interface-is-awkward-youre-ignoring-the-ui-stack/) (Scott Hurff, ~25 min)
- Video: [Empty States in Application Design: 3 Guidelines](https://www.youtube.com/watch?v=MUh3xyvEWDE) (NNgroup, 3:22)
- *Note:* No video covers all the states.

**Key literature**

- Scott Hurff, *Designing Products People Love* (2015)

### 2.3 Design systems and atomic design

- **Roles:** UX [core] · PM [optional] · SWE [optional]
- **Time:** ~21 min (text; video +37 min optional)

**Definition**

A design system is the shared set of components, rules and tokens a product's interfaces are built from. Atomic design (Brad Frost) organises it in five levels: atoms, molecules, organisms, templates and pages.

**Why it matters**

- **UX:** designs stay consistent and fast to produce.
- **SWE:** one component, built once and tested once, is reused everywhere.
- **PM:** new screens cost less as the system grows.

**In this framework**

The design system is code: `src/packages/ui`, a pnpm workspace package based on shadcn/ui, with a Storybook story per component [R3-Q5′, R3-Q3]. Figma mirrors it through the Obra shadcn kit and Code Connect, but **code is the source of truth** [R1-Q3, R3-Q3]. A PRD may use only design-system components; new ones and third-party blocks enter through an enabler slice [R2-Q3 (g), R3-Q5′]. See chapter [6](../guide/06-design-system-and-figma.md).

**Learn it**

- Text: [Atomic Design, ch. 2 "Atomic Design Methodology"](https://atomicdesign.bradfrost.com/chapter-2/) (Brad Frost, ~21 min)
- Video (optional): [Is Atomic Design Dead?](https://www.youtube.com/watch?v=PK_PICNTgAg) (Brad Frost, Hatch Conference 2023, 36:59)

**Key literature**

- Brad Frost, *Atomic Design* (2016), free online

### 2.4 Component inventory

- **Roles:** UX [core] · SWE [optional]
- **Time:** ~5 min (text)

**Definition**

An interface inventory is a catalogue of every distinct UI element a product already uses (buttons, form fields, cards and so on), gathered in one place to expose duplicates and inconsistencies.

**Why it matters**

- **UX:** it shows what exists before you design something new.
- **SWE:** it reveals near-duplicate components to merge.

**In this framework**

Storybook is the living inventory of `src/packages/ui` [R3-Q3]. Before proposing a new component in *Exploring*, check Storybook; if nothing fits, raise an enabler slice with `adds_ds_component: true` [R7-Q2], using [`enb.md`](../templates/enb.md).

**Learn it**

- Text: [Interface Inventory](https://bradfrost.com/blog/post/interface-inventory/) (Brad Frost, ~5 min)
- *Note:* No suitable video found.

**Key literature**

- Brad Frost, *Atomic Design* (2016), ch. 4

### 2.5 Design tokens

- **Roles:** UX [core] · SWE [optional]
- **Time:** ~16 min (text + video)

**Definition**

Design tokens are named design decisions (a colour, a spacing step, a duration) stored as data, so every platform and tool reads the same value. The W3C Design Tokens Community Group (DTCG) defines a common JSON format; its Format Module 2025.10 is a stable Community Group report, not a W3C Standard.

**Why it matters**

- **UX:** one change to a token changes every screen consistently.
- **SWE:** no hard-coded colours or durations in feature code.

**In this framework**

DTCG JSON in `src/packages/tokens` is canonical; Style Dictionary builds the shadcn `globals.css` [R3-Q2]. The technical founder updates Figma Variables from it; a token changed in Figma comes back as a Claude-generated PR, never the other way round. No Tokens Studio. Lint forbids raw colours and arbitrary Tailwind values [R3-Q2]. **Motion tokens** (durations, easings) are in `src/packages/tokens/src/motion.json`; presets in `src/packages/ui/src/motion/`; flows name only an interaction *intent* from `docs/design/motion.md` [R3-Q6′]. The idea is often traced to Salesforce's design system (unverified).

**Learn it**

- Text: [Design Tokens specification reaches first stable version](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/) (W3C DTCG, ~4 min)
- Video: [WTF are Design Tokens?](https://www.youtube.com/watch?v=q5qIowMyVt8) (Jina Anne, 11:46)

**Key literature**

- W3C DTCG, [Design Tokens Format Module 2025.10](https://www.designtokens.org/TR/2025.10/format/) (2025)

### 2.6 Modalities and touch points

- **Roles:** UX [core] · PM [optional]
- **Time:** ~17 min (text + video)

**Definition**

*Modalities* are the ways people operate an interface: touch, mouse, keyboard, voice, screen reader. *Touch points* are the places a user meets the product: the web app, emails, notifications, later a mobile app.

**Why it matters**

- **UX:** a flow that works only with a mouse, or only on the web, leaves users out.
- **PM:** touch points outside the app (an email, a reminder) are part of the user's journey.

**In this framework**

The UX meaning is decided in [R12-Q4]; the engineering meaning (inbound adapters) is in [`swe-lens.md`](swe-lens.md#27-modalities). Keyboard use and labels are part of checklist item (h); responsive behaviour is item (i) [R2-Q3]. Framework v1 covers responsive web only; native mobile is later [R3-Q8].

**Learn it**

- Text: [How People with Disabilities Use the Web: Input](https://www.w3.org/WAI/people-use-web/tools-techniques/input/) (W3C WAI, ~6 min) and [How Channels, Devices, and Touchpoints Impact the Customer Journey](https://www.nngroup.com/articles/channels-devices-touchpoints/) (NN/g, ~5 min)
- Video: [Don't Map Touch Points. Do THIS Instead](https://www.youtube.com/watch?v=zTIeNEV9cOU) (Service Design Show, 4:36) and [Keyboard Compatibility](https://www.youtube.com/watch?v=93UgG72os8M) (W3C WAI, 0:48)
- French: [Outils et techniques](https://www.w3.org/WAI/people-use-web/tools-techniques/fr) (W3C WAI)

**Key literature**

- W3C WAI, [WCAG 2.2 Guideline 2.5 "Input Modalities"](https://www.w3.org/WAI/WCAG22/Understanding/input-modalities)

### 2.7 Accessibility

- **Roles:** UX [core] · PM [optional] · SWE [optional]
- **Time:** ~21 min (text + video)

**Definition**

Accessibility means people with disabilities can perceive, operate and understand the product. WCAG 2.2 (W3C) is the international reference; in France, the RGAA turns it into criteria and tests.

**Why it matters**

- **UX:** it is part of usable design, not an add-on.
- **SWE:** semantic markup and focus handling are much cheaper built in than retrofitted.
- **PM:** it widens the market, and public-sector buyers may require it.

**In this framework**

Design-complete item (h) covers focus order, keyboard use, labels and contrast through tokens [R2-Q3]; PRD §13 holds the notes ([`prd.md`](../templates/prd.md)). The UX lane runs a WCAG 2.2 accessibility reviewer on prototypes and slice PRs [R4-Q7a, R4-Q7d]. The current RGAA is 4.1.2 (2023); **RGAA 5 is planned for late 2026**, so recheck this entry then.

**Learn it**

- Text: [WCAG 2 Overview](https://www.w3.org/WAI/standards-guidelines/wcag/) (W3C WAI, ~6 min) and [What's New in WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/) (W3C WAI, ~11 min)
- Video: [Introduction to Web Accessibility and W3C Standards](https://www.youtube.com/watch?v=20SHvU2PKsM) (W3C WAI, 4:07)
- French: [WCAG 2 : vue d'ensemble](https://www.w3.org/WAI/standards-guidelines/wcag/fr) (W3C WAI) and the [RGAA](https://accessibilite.numerique.gouv.fr/) (DINUM)

**Key literature**

- W3C, [WCAG 2.2](https://www.w3.org/TR/WCAG22/) (2023)

### 2.8 UX writing, voice and tone

- **Roles:** UX [core] · PM [core]
- **Time:** ~18 min (text + video; second video +33 min optional)

**Definition**

UX writing is the text inside the interface: labels, buttons, messages, errors, empty states. *Voice* is the product's constant personality; *tone* adapts it to the situation (an error is not a welcome screen).

**Why it matters**

- **UX:** words carry most of the interface's meaning.
- **PM:** the copy deck is where the story's intent becomes concrete.
- **Both:** error and empty-state copy decide whether users recover.

**In this framework**

The voice guide, `docs/design/voice-and-tone.md`, has a shared core plus per-locale rules; for French: *vous*, epicene wording rather than *points médians*, non-breaking spaces before `: ; ! ?`, and room for about 30% text expansion [R2-Q7]. Each PRD has a copy deck, [`copy.md`](../templates/copy.md), with semantic keys and context for translators [R2-Q6]. When rules conflict, our voice guide wins over the Vercel writing guidelines, which win over the web guidelines [R3-D6]. See chapter [7](../guide/07-i18n-and-voice.md).

**Learn it**

- Text: [Voice and Tone](https://styleguide.mailchimp.com/voice-and-tone/) (Mailchimp, ~3 min) and [The Four Dimensions of Tone of Voice](https://www.nngroup.com/articles/tone-of-voice-dimensions/) (NN/g, ~12 min)
- Video: [The Four Dimensions of Tone of Voice in UX Writing](https://www.youtube.com/watch?v=0ar4DezKKGI) (NNgroup, 3:01)
- Video (optional): [Strategic writing for UX](https://www.youtube.com/watch?v=1Z8gbVnrTfE) (Torrey Podmajersky, 32:37)
- *Note:* No good free French resource found.

**Key literature**

- Torrey Podmajersky, *Strategic Writing for UX* (2019)

### 2.9 Usability testing and heuristics

- **Roles:** UX [core] · PM [core]
- **Time:** ~26 min (text + video)

**Definition**

A usability test watches real users try to complete tasks with a prototype, to find where they struggle. Jakob Nielsen showed that about five users find most of the problems in one round. His ten heuristics are rules of thumb for reviewing an interface without users.

**Why it matters**

- **UX:** it is the only check on a design that involves actual users.
- **PM:** it catches a wrong flow before a slice is built.

**In this framework**

Design-complete item **(q)** is **strongly recommended, not mandatory**: test a new flow's prototype with 3–5 real users and record the findings in [`reviews.md`](../templates/reviews.md); the gate check only warns if it is missing [R11-Q10]. The persona *agents* that review designs are not user research; they apply heuristics and checklists, not observation.

**Learn it**

- Text: [Why You Only Need to Test with 5 Users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/) (NN/g, ~8 min) and [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/) (NN/g, ~11 min)
- Video: [Usability Testing w. 5 Users](https://www.youtube.com/watch?v=RhgUirqki50) (NNgroup, 3:37) and [Heuristic Evaluation of User Interfaces](https://www.youtube.com/watch?v=6Bw0n6Jvwxk) (NNgroup, 3:14)

**Key literature**

- Nielsen & Landauer, "A mathematical model of the finding of usability problems" (1993)

---

**Core time for this lens:** about 2 h 45 min (the nine entries above, optional videos excluded).
