# 7. i18n and Voice

The **voice** layer, and how a PRD written in one language ships in several. Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md). Concepts are in the [UX lens](../foundations/ux-lens.md#28-ux-writing-voice-and-tone).

## 7.1 Principles

1. **Voice is a layer of its own**, separate from flows and from the look: a global voice guide plus a per-PRD copy deck [R1-Q4].
2. **Each document has a source language** (`source_locale: en | fr`), chosen per PRD. The other languages are generated from it [R1-Q11].
3. **Readable copy from the first screen.** Prototypes show real text in the source language, never raw keys [R1-Q4].
4. **Code, commits, ADRs, TRDs and Gherkin are English**, whatever the PRD's language [R1-Q11, R3-Q1a].
5. **English and French now; other Latin languages later.** Nothing assumes there are only two [brief].

## 7.2 The voice guide

`docs/design/voice-and-tone.md` has a **shared core** and **per-locale rules** [R2-Q7]. The product is **B2B**.

| Rule | French |
|---|---|
| Address | **vous** by default |
| Inclusive writing | Epicene wording (*les personnes inscrites*), not *points médians* |
| Typography | A non-breaking space before `:` `;` `!` `?` |
| Layout budget | Allow about **30% text expansion** over English |

Where guides disagree, the order is: **our voice guide > Vercel writing guidelines > Vercel web guidelines**. The Vercel writing guidelines apply to English copy only; French rules live only in our guide. Each conflict is settled once in the guidelines skill's `overrides.md` [R3-D1, R3-D6].

## 7.3 From copy deck to message catalogs

```
docs/product/…/US-012.1-<slug>/copy.md          copy deck: key | source text | context | screen
src/packages/i18n/messages/<locale>/<feature>.json   one ICU catalog per feature per locale
src/packages/i18n/status/<locale>/<feature>.json     review status of each translated key [R19-Q1]
src/packages/i18n/locales.ts                         which locale is enabled in which environment [R19-Q2]
```

1. **Write the copy deck** during *Exploring*, in the source language, following the voice guide [R2-Q6, R2-Q7].
2. **An agent derives semantic keys**, `<feature>.<screen>.<element>` (e.g. `bookings.new.submit`), and writes them into the feature's catalog for the source locale [R2-Q6].
3. **The prototype reads strings through next-intl** from the start [R3-Q4].
4. **The translation skill** generates the other locales, using the bilingual glossary (`docs/product/glossary.md`) and the voice guide. Every generated string is marked **`needs-review`** [R2-Q6, R3-A5]. The mark lives in a **sidecar** beside each catalog, `status/<locale>/<feature>.json`: per key, its status (`needs-review` or `reviewed`), the reviewer and date, and a fingerprint of the source text it was translated from. When the source text changes, CI resets the translation to `needs-review`, so a stale translation can't stay marked reviewed [R19-Q1].
5. **CI validates** every catalog: ICU syntax, and that each translation has the same placeholders as its source [R2-Q6].

**Why one catalog per feature per locale:** parallel PRDs then edit different files, so their strings don't collide at merge time [R2-Q6].

## 7.4 Library: next-intl

[R3-Q4]

- **next-intl**, with semantic keys and ICU messages in JSON.
- **Don't use `useExtracted`**: its single global source locale conflicts with a source language per PRD.
- **Native mobile later** reads the same catalogs through i18next with ICU, so `src/packages/i18n/` is a shared package.

## 7.5 Copy in specs and tests

- **Gherkin refers to UI text by copy-deck key**, and only where the exact wording matters: `Then the "bookings.new.success" message is shown` [R3-C2].
- **Playwright steps resolve keys through the catalogs**, so `@ui` scenarios run in every enabled locale and double as i18n tests [R3-C2, R14-Q2].
- **Domain words in steps** use the glossary's English term [R3-C3].
- A French-source PRD links to its English `.feature` files; an agent can render a French reading view on demand, never authoritative [R3-C1].

## 7.6 When translations must be reviewed

[R4-Q10]

| Where | Rule |
|---|---|
| A slice reaching *Done* | Catalogs exist for every locale; non-source strings may still be `needs-review` |
| Staging | `needs-review` strings are allowed |
| Production | Every string in a locale **enabled for production** has been reviewed by a native speaker. A locale can be switched off in production until its review is complete. |

**Switching locales on and off** [R19-Q2]: `src/packages/i18n/locales.ts` lists each locale with the environments it is enabled in, e.g. `fr: ["staging", "production"]`, `en: ["staging"]`. The **production build fails** if a locale enabled for production has a `needs-review` string. It lives in code, not in `settings.yaml`, because it changes what ships.

## 7.7 Adding a language

Adding a locale, such as a third Latin language, is an **enabler slice** [R19-Q3] that adds:

1. the locale's column in the glossary;
2. its rules in the voice guide;
3. its catalogs, generated by the translation skill, all `needs-review`;
4. a layout check for its text expansion;
5. the locale in `locales.ts`, enabled for staging only.

It is switched on in production once its native review is complete [R4-Q10].
