---
prd: PRD-012.1
source_locale: en
feature: bookings          # the catalog file: src/packages/i18n/messages/<locale>/<feature>.json [R2-Q6]
---
<!-- Copied to …/stories/US-012.1-<slug>/copy.md. The VOICE layer for this PRD [R1-Q4].
     Source text is real, readable copy in the source locale: "Next step", never "screen1.panel2.next.label" [R1-Q4].
     It follows doc/design/voice-and-tone.md [R2-Q7]. Keys are semantic: <feature>.<screen>.<element> [R2-Q6]. -->

# Copy deck: PRD-012.1

| Key | Source text | Context for translators | Screen |
|---|---|---|---|
| `bookings.new.title` | Book a room | Page heading | S1 |
| `bookings.new.submit` | Next step | Button; moves to the confirmation screen | S1 |
| `bookings.new.error.tooLong` | A booking can last {maxHours, plural, one {# hour} other {# hours}} at most. | ICU plural; `maxHours` is a number | S1 |
