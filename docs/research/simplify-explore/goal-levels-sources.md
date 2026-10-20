# Goal Levels Sources: Cockburn and Larman

Status: fact check, 2026-10-20 (curl, Wayback Machine CDX, YouTube oEmbed plus the `lengthSeconds` field of the watch page, WebFetch, WebSearch, and text extracted from the PDFs). Input to the "simplify explore" work on use case goal levels and the coffee-break test. "(inferred)" marks a point that was not verified directly.

**Conventions**
- **Kind:** Lit = key literature. Text = crash course (free, under 30 min unless flagged). Video. FR = French resource.
- **Length:** word counts are approximate and come from the fetched HTML or from text extracted from the PDF, including some page chrome. Reading time assumes 200 words/min. Video durations come from the watch page.
- **Checked:** every link below was fetched successfully on 2026-10-20. A book without a link is paid or was not fetched.
- **Cockburn's site:** `alistair.cockburn.us` now serves only its home page and the hexagonal architecture page (its `sitemap.xml` lists just these two). The old use case articles 404 there, so they are cited from the Wayback Machine or from university mirrors.
- **Book drafts:** the free copies of *Writing Effective Use Cases* are pre-publication drafts (1999 and 21 Feb 2000) hosted on university course pages. The Larman chapter is also a course-hosted copy. Whether the hosting is authorised is not known (inferred: course readings). Quotes below come from the drafts; the published wording may differ slightly.

---

## 1. Learn it: crash courses (about 22 min in total)

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Text | Use Case Levels (section of "User Requirements", course TTM4115) | NTNU, course notes. Short table of cloud, kite, sea level, fish and clam, plus sea-level checks (2 to 20 minutes, coffee break, "go away happy"). Two small slips: it says "3 to 8 steps" (Cockburn: 3 to 9) and "about five" summary use cases (Cockburn: 2 to 5 outermost use cases). | <https://ttm4115.iik.ntnu.no/unit-4-req/preparation-1.html> | ~860 words, ~4 min | 2026-10-20 |
| Text | *Writing Effective Use Cases*, pre-publication draft #3 (2000-02-21), extract. Read chapter 5 "Three Named Goal Levels", pages 57 to 62. | Alistair Cockburn; PDF hosted by the University of Zurich (IfI) | <https://www.ifi.uzh.ch/dam/jcr:00000000-25a0-3d08-0000-00000ce96422/weuc_extract.pdf> | PDF, 780 KB, ~44,000 words in all; chapter 5 is ~2,100 words, ~10 min | 2026-10-20 |
| Text | *Applying UML and Patterns* (2nd ed.), chapter 6 "Use-Case Model: Writing Requirements in Context". Read section 6.8 "Goals and Scope of a Use Case", from "Use Cases for Elementary Business Processes" to "Use Cases and Goals". | Craig Larman; PDF hosted on a Duke course page | <https://courses.cs.duke.edu/cps108/spring04/readings/usecaseslarman.pdf> | PDF, 235 KB, ~12,000 words in all; the EBP part is ~1,550 words, ~8 min | 2026-10-20 |
| Text (alt) | Use Case (bliki) | Martin Fowler. One paragraph; calls Cockburn's book "by far the best book on use cases". | <https://martinfowler.com/bliki/UseCase.html> | ~160 words, ~1 min | 2026-10-20 |

## 2. Key literature

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit | *Writing Effective Use Cases* | Alistair Cockburn, Addison-Wesley, published 5 Oct 2000, copyright 2001, 304 pages, ISBN 978-0-201-70225-5. **Chapter 5 "Three Named Goal Levels"**: User Goals (Blue, Sea-Level); Summary Level (White, Cloud/Kite); Subfunctions (Indigo/Black, Underwater/Clam); Summarizing Goal Levels; Using Graphical Icons to Highlight Goal Levels; Finding the Right Goal Level (Figure 14 "Ask 'Why' to Shift Levels"). Chapter 11 "Use Case Formats" covers casual and fully dressed formats. | <https://www.informit.com/store/writing-effective-use-cases-9780201702255> (publisher page with the table of contents; the book is paid) | book | 2026-10-20 |
| Lit | *Writing Effective Use Cases*, draft #3 inside covers ("Reminders", "Icons", "The Writing Process") | Alistair Cockburn, 2000-02-21; Duke course PDF. Shows the five goal level icons and the "+", "!", "-" name suffixes. | <https://courses.cs.duke.edu/compsci308/spring23/readings/cockburn_use_cases.pdf> | PDF, 3 pages, ~1 min | 2026-10-20 |
| Lit | *Writing Effective Use Cases*, 1999 draft (204 pages) | Alistair Cockburn; PDF hosted at ELTE (Budapest). Earlier wording of the user-goal tests: "one person, in one place, at one time (2-20 minutes)", "Can I go to lunch...", "Can I ask for a raise...". | <https://people.inf.elte.hu/molnarba/Informaciorendszerek_ELTE/Writing_effective_Use_cases_Cockburn.pdf> | PDF, 835 KB, ~85,000 words | 2026-10-20 |
| Lit | Structuring Use Cases with Goals | Alistair Cockburn. Humans and Technology report 1995; published in *Journal of Object-Oriented Programming*, Sep-Oct and Nov-Dec 1997 (dates from the page). The origin of goal levels and the "sea level" ship picture. Author's own site, archived 2014-03-29. | <https://web.archive.org/web/20140329202915/http://alistair.cockburn.us/Structuring+use+cases+with+goals> | ~10,000 words with page chrome and comments, ~50 min (**over 30**; read the "goal detail" part) | 2026-10-20 |
| Lit (mirror) | Structuring Use Cases with Goals | Same article, University of Otago course mirror | <https://www.cs.otago.ac.nz/coursework/cosc461/usecases.htm> | ~7,950 words, ~40 min (**over 30**) | 2026-10-20 |
| Lit | *Applying UML and Patterns*, 2nd ed. | Craig Larman, Prentice Hall, ISBN 0-13-092569-1, 2002 (year inferred). Chapter 6, section 6.8 "Goals and Scope of a Use Case": the EBP guideline. | see the Duke PDF in section 1 | book | 2026-10-20 |
| Lit | *Applying UML and Patterns*, 3rd ed. | Craig Larman, Prentice Hall, 2004 (year inferred). Chapter 6 "Use Cases", section "What Tests Can Help Find Useful Use Cases?": the boss test, the EBP test and the size test. Section title taken from W&M lecture slides based on the book; the section number was not verified. | <https://www.cs.wm.edu/~kemper/cs435/slides/l5.pdf> (slides, not the book) | PDF slides | 2026-10-20 |

## 3. Video

No good English video focused on goal levels was found. Two candidates, neither recommended as the main resource:

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Video (alt) | Alistair Cockburn on Use Cases & User Stories, Humanizing Work Show | Richard Lawrence and Peter Green with Alistair Cockburn, 22 Jan 2024. Cockburn talks about goal levels in passing (around 2:00) and about writing a "kite level" use case and spreading it across a story map (around 18:20 and 21:40). These timestamps are estimated from the word position in the transcript on the episode page (inferred, not watched). | <https://www.youtube.com/watch?v=CRvwbRqi_ss> (transcript: <https://www.humanizingwork.com/alistair-cockburn-on-use-cases-user-stories>) | 41:43 | 2026-10-20 |
| Video (alt, German) | Coffee Break Test & User Happiness Test | ArchiLab channel, in German. On topic (is a use case too small or too large?), but not English or French. | <https://www.youtube.com/watch?v=X3Ih6P7syKs> | 9:03 | 2026-10-20 |

## 4. French resource

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| FR (Lit) | *Rédiger des cas d'utilisation efficaces* | Alistair Cockburn, French translation, Eyrolles, collection Technologies objet, 27 Jul 2001, 320 pages, EAN 9782212092882. Paid book. | <https://www.eyrolles.com/Livre/9782212092882> | book | 2026-10-20 |

No free French text on goal levels or the coffee-break test was found.

---

## 5. Facts

Each fact gives its source. "Draft #3" is the UZH extract of *Writing Effective Use Cases* (2000-02-21); "inside covers" is the Duke PDF of the same draft.

1. **Three named levels.** Cockburn names three goal levels: summary, user goal and subfunction. Chapter 5 is titled "Three Named Goal Levels" in the published table of contents (InformIT) and in draft #3 (page 57).
2. **Colours.** "The color gradient runs white to blue, to indigo, to black. The user goal is blue." Summary is white, subfunction is indigo, and black marks "a goal ... so low level that it would be a mistake to write a use case for it" (draft #3, p. 57).
3. **Altitude names and icons.**
   - Summary: cloud or kite. The cloud is "very high summary" ("way up in the clouds"); the kite is "summary", "like a kite, just above sea level" (draft #3, pp. 58 to 59; inside covers icon legend).
   - User goal: sea level, marked with a **waves** icon (draft #3 glossary: "Marked graphically with waves").
   - Subfunction: underwater, marked with a **fish** (draft #3 glossary; published heading "Subfunctions (Indigo/Black, Underwater/Clam)").
   - Too low: **clam**, black. "Using the clam signifies that the use case is too low level and should not be written at all" (draft #3 glossary); "It doesn't even swim... it's a clam!" (p. 60).
   - The inside covers label the five icons "Very high summary", "Summary", "User-goal", "Subfunction", "too low".
   - The archived 1997 article says Cockburn describes levels "using the words cloud, kite, sea-level, underwater, and clam".
4. **Name suffixes.** As an alternative to icons: append "+" to summary use case names, "!" or nothing to user-goal names, "-" to subfunction names (inside covers). The published book lists "USE CASE 18 Operate an Insurance Policy+" (InformIT table of contents).
5. **Coffee-break test, wording.** Draft #3, section 5.1: "A user goal addresses the question, 'Can the primary actor go away happy after having done this?' For a clerk, it would be, 'Does your job performance depend on how many of these you do today?' or the coffee break test: 'After I get done with this, I can take a coffee break.' In most circumstances, it passes the test: One person, one sitting (2-20 minutes)." That the published book keeps this wording is inferred (the book was not checked).
6. **The 2 to 20 minutes figure is Cockburn's.** Draft #3, section 5.1 ("One person, one sitting (2-20 minutes)") and glossary: a user-goal use case is "Typically performed by one primary actor in one sitting of 2-20 minutes (less if the primary actor is a computer), after which they can leave and proceed with other things." The 1999 draft has "Is it done by one person, in one place, at one time (2-20 minutes)?". The 1997 article does not give a time figure or the coffee break (searched, no match).
7. **Counter-examples.** "Complete an on-line auction purchase" fails the single-sitting test (it takes days); "Log on" fails because logging on 42 times does not satisfy job responsibilities; "Register a new customer" and "Buy a book" are user goals (draft #3, p. 57).
8. **User goal = elementary business process.** Cockburn: the user goal "corresponds to 'elementary business process' in the business process engineering literature" (draft #3, p. 57). The 1997 article: "what might be called 'user task', or 'elementary business process'".
9. **Larman's EBP.** "A task performed by one person in one place at one time, in response to a business event, which adds measurable business value and leaves the data in a consistent state. e.g., Approve Credit or Price Order [original source lost]." Larman calls an EBP-level use case "a user goal-level use case". He adds that the main success scenario "is probably five or ten steps" and the task is "probably between a few minutes and an hour in length" (2nd ed., ch. 6, Duke PDF). So Larman's time range is wider than Cockburn's 2 to 20 minutes. A footnote says EBP is similar to "user task" in usability engineering.
10. **Larman's three tests (3rd ed.).** Boss test ("What have you been doing all day?"), EBP test, size test (W&M slides based on the book; wording of the book itself not checked).
11. **Summary level.** "Summary-level goals involve multiple user goals." They show context, show life-cycle sequencing of related goals, and give a table of contents for lower-level use cases. They "typically execute over hours, days, weeks, months, or years" (draft #3, p. 58 to 59). Cockburn earlier used both "strategic" and "summary" and chose "summary" for the book (p. 58 footnote).
12. **Outermost use cases.** "Typically, there are only 2-5 outermost use cases for the entire system ... I highly recommend writing the outermost use cases. It takes very little time" (draft #3, chapter 3).
13. **Subfunctions.** "Include them only as you have to"; examples "Find a product", "Find a Customer", "Save as a file" (draft #3, p. 59).
14. **Moving between levels.** "Ask 'why' to find a next-higher level goal" (inside covers); published Figure 14 "Ask 'Why' to Shift Levels".
15. **Main success scenario length.** "Use 3 to 9 steps" (inside covers, "The Writing Process", step 8).
16. **Summary level in a looser format: not stated as a rule.** No sentence saying summary use cases may be written in a looser format was found in the drafts. Cockburn's examples point that way: "Operate an Insurance Policy" (Level: summary) is just four steps with no extensions (draft #3, p. 59), and the 1999 draft shows a summary-level "Buy something" in the casual template. But draft #3 also shows a summary-level business use case that is "fully dressed in form". So "summary use cases may be written in a looser format" is **(inferred)** from his examples and from "it takes very little time", not a quote. Cockburn's general rule is that there are two templates, "a casual one for low-ceremony projects, and a fully dressed one for higher-ceremony projects" (draft #3, chapter 1), chosen per project rather than per level.
