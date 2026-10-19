# Foundations Sources: Product, Requirements, UX

Status: fact check, 2026-10-19 (curl + stdlib text extraction, YouTube oEmbed, YouTube search-result metadata, WebFetch, Wayback Machine). Input to the onboarding "Foundations" document. "(inferred)" marks a point that was not verified directly.

**How to read the tables**
- Every URL was fetched successfully on 2026-10-19. Word counts come from the page text with nav, scripts and footers stripped. They still include sidebars and "related article" lists, so they run **5–20% high**. Reading time assumes 200 words/min.
- Every video passed a YouTube oEmbed check (title and channel match). Durations come from YouTube's own search-result metadata, not from the watch page.
- **Free** means it opens with no login and no paywall. A source that needs a form is flagged as such.
- Book rows carry no link unless a free, official copy exists.

## 1. Use cases (Jacobson; Cockburn "fully dressed")

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | "Object-oriented development in an industrial environment", OOPSLA '87 | Ivar Jacobson, 1987 | — (ACM DL returned 403) | paper | — |
| Literature | *Object-Oriented Software Engineering: A Use Case Driven Approach* | Jacobson et al., 1992 | — | book | — |
| Literature | *Writing Effective Use Cases* | Alistair Cockburn, 2000 | — | book | — |
| Text | Use-Case Foundation v1.1 (joint definition, Feb 2024) | Jacobson & Cockburn | <https://alistaircockburn.com/Use%20Case%20Foundation.pdf> | 5 pp, ~750 words, ~4 min | 2026-10-19 |
| Text | Basic use case template (source of the "fully dressed" fields; the 2001 note maps it to the book) | Cockburn, 1996/1998, archived | <https://web.archive.org/web/20140330001816/http://alistair.cockburn.us/Basic+use+case+template> | ~3,300 words, ~17 min | 2026-10-19 |
| Text | Use Case (bliki) | Martin Fowler, 2004 | <https://martinfowler.com/bliki/UseCase.html> | ~150 words, 1 min | 2026-10-19 |
| Video | Alistair Cockburn on Use Cases & User Stories | Humanizing Work | <https://www.youtube.com/watch?v=CRvwbRqi_ss> | 41:43 | 2026-10-19 |

- The Foundation PDF is the shortest authoritative definition: actor, goal, basic scenario, extensions. Both originators co-signed it.
- Cockburn's old site is gone (alistair.cockburn.us now serves only a stub). His older articles survive only on the Wayback Machine.

## 2. Use-Case 2.0 and use-case slices

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | *Use-Case 2.0: The Guide to Succeeding with Use Cases* (ebook) | Jacobson, Spence, Bittner, 2011 | IJI page, archived 2025-02-10: <https://web.archive.org/web/20250210154328/https://www.ivarjacobson.com/publications/white-papers/use-case-20-e-book> | ~55 pp (inferred) | 2026-10-19 |
| Text | "Use-Case 2.0: The Hub of Software Development", ACM Queue 14(1), 2016-04-05 | Jacobson, Spence, Kerr | Archived copy: <https://web.archive.org/web/20250908161806/https://queue.acm.org/detail.cfm?id=2912151> | ~6,700 words, ~33 min | 2026-10-19 |
| Video | "Use-Case 2.0: The Hub of Modern Software Development" | Ivar Jacobson, ACM channel | <https://www.youtube.com/watch?v=p5gDbf0je8k> | 58:50 | 2026-10-19 |

- Both ivarjacobson.com and queue.acm.org return **403 (Cloudflare)** to curl and WebFetch, so the links above are Wayback copies. The archived IJI page says "Download the Use-Case 2.0 e-Book for free below". The download itself (direct file or form) could not be checked.
- The ACM Queue article runs slightly over the 30-minute budget. Its slice definition comes in the first third.

## 3. User stories (Beck/XP, Connextra, three Cs, Cohn)

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | *Extreme Programming Explained* | Kent Beck, 1999 | — | book | — |
| Literature | *User Stories Applied* | Mike Cohn, 2004 | <https://www.mountaingoatsoftware.com/books/user-stories-applied> (book page, not free text) | book | 2026-10-19 |
| Text | Essential XP: Card, Conversation, Confirmation (2001-08-30) | Ron Jeffries | <https://ronjeffries.com/xprog/articles/expcardconversationconfirmation/> | ~640 words, ~3 min | 2026-10-19 |
| Text | User Story (bliki): Beck origin, INVEST, "As a… I want… so that…" | Martin Fowler, 2013 | <https://martinfowler.com/bliki/UserStory.html> | ~370 words, 2 min | 2026-10-19 |
| Text | User Stories: what they are, how to write them | Mike Cohn | <https://www.mountaingoatsoftware.com/agile/user-stories> | ~3,400 words, ~17 min | 2026-10-19 |
| Video | User Stories Explained | Mike Cohn, Mountain Goat Software | <https://www.youtube.com/watch?v=6q5-cVeNjCE> | 52:04 | 2026-10-19 |

- **Connextra template:** the Agile Alliance glossary (fetched via WebFetch; curl returned 403) says that in "2001: the 'role-feature-reason' format … is invented at Connextra in the UK". It names no person. The credit to **Rachel Davies** comes only from Wikipedia and secondary sources (inferred). Wikipedia notes that Davies credits the whole Connextra team.

## 4. INVEST (Bill Wake, 2003)

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Text | INVEST in Good Stories, and SMART Tasks (2003-08-17) | Bill Wake, xp123.com | <https://xp123.com/invest-in-good-stories-and-smart-tasks/> | ~1,500 words, ~8 min | 2026-10-19 |
| Video | Agile Book Club: User Stories (with Bill Wake) | James Shore | <https://www.youtube.com/watch?v=6i6c-ZiHWs8> | 39:49 | 2026-10-19 |
| FR text | INVESTissez dans de bonnes stories et dans des tâches SMART | Les traducteurs agiles (linked from Wake's page) | <http://www.les-traducteurs-agiles.org/2015/02/23/investissez-dans-de-bonnes-stories-et-dans-des-taches-smart.html> | ~1,500 words, ~8 min | 2026-10-19 |
| FR video | INVEST : Qu'est-ce qu'une bonne User Story ? | Scrum Life | <https://www.youtube.com/watch?v=PO4vDYkezgY> | 10:06 | 2026-10-19 |

## 5. Use cases vs user stories

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | *Unifying User Stories, Use Cases, Story Maps* (2nd ed.) | Cockburn, 2025 (inferred year) | Free chapter 0 (PDF, © 2025): <https://alistaircockburn.com/UnifyingV2_chapter0.pdf> | 22 pp; word count unverified (font-encoded PDF) | 2026-10-19 |
| Text | Use Cases And Stories (bliki, 2003-08-18) | Martin Fowler | <https://martinfowler.com/bliki/UseCasesAndStories.html> | ~320 words, 2 min | 2026-10-19 |
| Text | Advantages of User Stories over Requirements and Use Cases | Mike Cohn | <https://www.mountaingoatsoftware.com/agile/advantages-of-user-stories-for-requirements> | ~1,900 words, ~9 min | 2026-10-19 |
| Slides | Unifying user stories, use cases, story maps: the talk | Cockburn | <https://alistaircockburn.com/Unifying%20us%20uc%20sm.pdf> | 26 slides, ~1,250 words, ~6 min | 2026-10-19 |
| Video | Use Cases and User Stories: Perfect Partners with Mike Cohn | Ivar Jacobson International | <https://www.youtube.com/watch?v=yT3FLPR8OFU> | 1:04:14 | 2026-10-19 |
| Video (alt.) | Use-Cases or User Stories... or Both? | Ivar Jacobson International | <https://www.youtube.com/watch?v=lwVo8G_5li4> | 1:07:28 | 2026-10-19 |

What the sources say, by dimension:

| Dimension | Use case | User story | Source |
|---|---|---|---|
| Origin | Jacobson, late 1980s | Beck/XP; three Cs 2001; Connextra template 2001 | Fowler bliki; Agile Alliance |
| Purpose | Narrative of how users reach goals | Chunks of work for planning | Fowler 2003 |
| Format | Main scenario plus numbered extensions, full sentences | Short phrase or card, plus conversation | Cockburn slides |
| Granularity | One user goal; "don't decompose below fish level" | Fits one iteration; can be split "down to clam level" | Cockburn slides; Fowler |
| Failure paths | Explicit (extensions and failure handling) | Not intrinsic; often captured as acceptance tests | Foundation PDF; Jeffries |
| Lifespan | Lives as a spec of behaviour | Lives in a conversation; often discarded after delivery (inferred from Cohn / IJI framing) | Cockburn slides; IJI page |
| Complement | A use case is sliced into story-sized pieces; "thinnest full transaction as slice 1" | Story map lays them out | Cockburn slides; Use-Case 2.0 |

## 6. Story mapping (Jeff Patton)

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | *User Story Mapping* | Jeff Patton, O'Reilly, 2014 | — | book | — |
| Text | The New User Story Backlog is a Map (2008-10-08) | Jeff Patton | <https://jpattonassociates.com/the-new-backlog/> | ~3,300 words, ~16 min | 2026-10-19 |
| Video | User Stories & Story Mapping Demystified | Jeff Patton, ConfEngine | <https://www.youtube.com/watch?v=5R1z8POfvgQ> | 55:53 | 2026-10-19 |
| FR video | Le User Story Mapping | Scrum Life | <https://www.youtube.com/watch?v=dvnU_R0mu98> | 12:44 | 2026-10-19 |

## 7. Story splitting, vertical slices, tracer bullets

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | *The Pragmatic Programmer* (tracer bullets; 20th-anniversary ed. 2019) | Hunt & Thomas, 1999 | — | book | — |
| Text | The Humanizing Work Guide to Splitting User Stories (2020, updated 2026) | Richard Lawrence & Peter Green | <https://www.humanizingwork.com/the-humanizing-work-guide-to-splitting-user-stories/> | ~6,000 words, ~30 min | 2026-10-19 |
| Text | Elephant Carpaccio exercise (thin vertical slices) | Cockburn, archived | <https://web.archive.org/web/20150220065851/http://alistair.cockburn.us/Elephant+Carpaccio+exercise> | ~970 words, ~5 min | 2026-10-19 |
| Text | Pragmatic Programmer tips (Tip #20 "Use Tracer Bullets to Find the Target", one line) | pragprog.com | <https://pragprog.com/tips/> | one line | 2026-10-19 |
| Video | How to Split a User Story | Humanizing Work | <https://www.youtube.com/watch?v=irorOjThcD8> | 10:20 | 2026-10-19 |
| Video | Anniversary Edition of The Pragmatic Programmer | Dave Thomas & Andy Hunt, GOTO 2020 | <https://www.youtube.com/watch?v=taCNjiiusRk> | 29:37 | 2026-10-19 |

- The tracer-bullets chapter is **not** among pragprog's free extracts (DRY, shared state, inheritance tax, headlights, preface). No free official text on tracer bullets was found. The GOTO interview is about the book in general; whether it covers tracer bullets is not verified (inferred).

## 8. Jobs to be done; personas

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | "Know Your Customers' Jobs to Be Done", HBR Sept 2016 (paywalled); *Competing Against Luck*, 2016 | Christensen, Hall, Dillon, Duncan | — | article / book | — |
| Literature | *What Customers Want*, 2005; *Jobs to Be Done: Theory to Practice*, 2016 | Tony Ulwick | Free PDF **behind a contact form**: <https://jobs-to-be-done-book.com/> | book | 2026-10-19 |
| Literature | *The Inmates Are Running the Asylum* | Alan Cooper, 1998 (inferred: 1998/1999) | — | book | — |
| Text | Jobs to Be Done theory | Christensen Institute | <https://www.christenseninstitute.org/theory/jobs-to-be-done/> | ~2,000 words, ~10 min | 2026-10-19 |
| Text | Jobs to Be Done (JTBD): the original framework (Ulwick's firm, not his byline) | Strategyn | <https://strategyn.com/jobs-to-be-done/> | ~4,700 words, ~23 min | 2026-10-19 |
| Text | The Origin of Personas (Aug 2003) | Alan Cooper, archived | <https://web.archive.org/web/20101229080750/http://www.cooper.com/journal/2003/08/the_origin_of_personas.html> | ~2,500 words, ~12 min | 2026-10-19 |
| Text | Personas Make Users Memorable (2025) | Taylor Dykes, NN/g | <https://www.nngroup.com/articles/persona/> | ~1,100 words, ~6 min | 2026-10-19 |
| Video | Clay Christensen: The Jobs to be Done Theory (milkshake) | HubSpot Marketing | <https://www.youtube.com/watch?v=Stc0beAxavY> | 7:10 | 2026-10-19 |
| Video | The Outcome-Driven Innovation Process: Overview | Strategyn (Ulwick) | <https://www.youtube.com/watch?v=rth9XgqfHeM> | 29:42 | 2026-10-19 |
| Video | Personas 101 | NNgroup | <https://www.youtube.com/watch?v=rv9yfrV-EAs> | 3:42 | 2026-10-19 |
| Video (long) | Understanding Personas: An Interview with Alan Cooper | InfoQ | <https://www.youtube.com/watch?v=G7ljzXB40hw> | 1:06:48 | 2026-10-19 |

- The live cooper.com article returns 404; only the Wayback copy works.

## 9. Outcomes over output; product metrics

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | *Outcomes Over Output* | Josh Seiden, 2019 | — | short book | — |
| Literature | "Measuring the User Experience on a Large Scale" (HEART), CHI 2010 | Rodden, Hutchinson, Fu (Google) | <https://research.google.com/pubs/archive/36299.pdf> | 4 pp, ~3,700 words, ~18 min | 2026-10-19 |
| Literature | "The One Number You Need to Grow", HBR 2003 (NPS) | Fred Reichheld | — (paywalled) | article | — |
| Text | North Star Playbook (free online) | Amplitude; John Cutler co-author | <https://amplitude.com/books/north-star> | multi-chapter; intro ~750 words | 2026-10-19 |
| Text | Every Product Needs a North Star Metric | Julia Sholtz, Amplitude | <https://amplitude.com/blog/product-north-star-metric> | ~2,100 words, ~10 min | 2026-10-19 |
| Text | Measuring Your Net Promoter Score | Bain & Company | <https://www.netpromotersystem.com/about/measuring-your-net-promoter-score/> | ~550 words, ~3 min | 2026-10-19 |
| Text | Customer retention rate (formula: (end − new) / start × 100) | HubSpot blog | <https://blog.hubspot.com/service/customer-retention-rate> | ~1,500 words, ~7 min | 2026-10-19 |
| Text (alt.) | Retention analytics guide | Amplitude | <https://amplitude.com/guides/retention-analytics> | ~1,150 words, ~6 min | 2026-10-19 |
| Video | Webinar: Outcomes over output with Josh Seiden | Sense & Respond Learning | <https://www.youtube.com/watch?v=o5z4Dj1EhbQ> | 58:09 | 2026-10-19 |
| Video | Product @ Amplitude: Making strategy actionable with the North Star | TPC (speaker not verified) | <https://www.youtube.com/watch?v=dftUliKgJAQ> | 50:29 | 2026-10-19 |
| Video | Build Brand Loyalty with the Net Promoter Score (with Fred Reichheld) | CXOTalk #733 | <https://www.youtube.com/watch?v=36oXmAwGhWw> | 43:14 | 2026-10-19 |

- **No free text by Seiden was reachable.** jseiden.com and senseandrespondpress.com do not resolve in DNS; the Intercom interview URLs return 404 or redirect to the blog index. Kerry Rodden's GV article "How to choose the right UX metrics for your product" is on library.gv.com, which also fails DNS, and the archive redirects into a Medium login wall. The 2010 paper (above) is the reliable source.
- No HEART video by its authors was found. The ones on YouTube come from third parties.
- The 2010 HEART paper lists the five HEART dimensions and the Goals-Signals-Metrics process; reading it settles any conflicting summaries (inferred from the extracted text).

## 10. Shape Up (Basecamp, Ryan Singer)

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | *Shape Up: Stop Running in Circles and Ship Work that Matters* (free online book) | Ryan Singer, Basecamp, 2019 | <https://basecamp.com/shapeup> | book | 2026-10-19 |
| Text | Introduction (six-week cycles, shaping, betting, overview) | Singer | <https://basecamp.com/shapeup/0.3-chapter-01> | ~1,800 words, ~9 min | 2026-10-19 |
| Text | Ch. 4 "Find the Elements" (breadboarding, fat-marker sketches) | Singer | <https://basecamp.com/shapeup/1.3-chapter-04> | ~2,400 words, ~12 min | 2026-10-19 |
| Video | Shaping in a Nutshell | Ryan Singer (own channel) | <https://www.youtube.com/watch?v=h_8M23wVjXk> | 17:54 | 2026-10-19 |

- Further chapters, all fetched: ch. 3 "Set Boundaries" (appetite, fixed time with variable scope) at <https://basecamp.com/shapeup/1.2-chapter-03>, ~2,000 words, ~10 min. Ch. 7 "Bets, Not Backlogs" (betting) at <https://basecamp.com/shapeup/2.1-chapter-07>, ~730 words, ~4 min.

## 11. Context only: design thinking, Double Diamond, IBM EDT, continuous discovery

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | *Continuous Discovery Habits* | Teresa Torres, 2021 | — | book | — |
| Text | Design Thinking Bootleg (method cards, PDF linked from page) | Stanford d.school | <https://dschool.stanford.edu/tools/design-thinking-bootleg> | page ~360 words; deck length unverified | 2026-10-19 |
| Text | Design Thinking by IDEO | IDEO | <https://designthinking.ideo.com/> | ~400 words, 2 min | 2026-10-19 |
| Text | The Double Diamond (history since 2003/2004) | UK Design Council | <https://www.designcouncil.org.uk/resources/the-double-diamond/> | ~700 words, ~4 min | 2026-10-19 |
| Text | Enterprise Design Thinking: Hills (framework pages, archived 2022) | IBM | <https://web.archive.org/web/20221221182334/http://www.ibm.com/design/thinking/page/framework/keys/hills/> | ~800 words, ~4 min | 2026-10-19 |
| Text | Product Discovery Basics (2021) | Teresa Torres | <https://www.producttalk.org/product-discovery/> | ~2,000 words, ~10 min | 2026-10-19 |
| Text (alt.) | Opportunity Solution Trees | Teresa Torres | <https://www.producttalk.org/opportunity-solution-trees/> | ~5,900 words, ~29 min | 2026-10-19 |
| Video | Stanford Webinar: Design Thinking: what is it and why should I care? | Stanford Online | <https://www.youtube.com/watch?v=GeUXQ_L-35M> | 57:57 | 2026-10-19 |
| Video | What is Design Thinking? | IDEO U | <https://www.youtube.com/watch?v=ldYzbV0NDp8> | 1:55 | 2026-10-19 |
| Video | Celebrating 20 years of the Double Diamond | Design Council | <https://www.youtube.com/watch?v=5FpKuJSCbx0> | 1:13 | 2026-10-19 |
| Video | Enterprise Design Thinking at IBM | Eleanor Bartosh (IBM), GIFLondon 2018 | <https://www.youtube.com/watch?v=8mcClemz_pM> | 22:50 | 2026-10-19 |
| Video | Introduction to Modern Product Discovery | Teresa Torres, Productized | <https://www.youtube.com/watch?v=l7-5x0ra2tc> | 36:45 | 2026-10-19 |

- **IBM:** `ibm.com/design/thinking` now redirects to a training page (~300 words) that covers neither the Loop, Hills, Playbacks nor Sponsor users. The framework pages exist only on the Wayback Machine. Pages other than Hills (Loop, Playbacks, Sponsor users) were not fetched (inferred: same archive path).

## 12. UX: task/user flows and wireframes

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | *The Elements of User Experience* (general reference; covers wireframes) | Jesse James Garrett, 2002 (inferred fit) | — | book | — |
| Text | User Journeys vs. User Flows (2023) | NN/g | <https://www.nngroup.com/articles/user-journeys-vs-user-flows/> | ~1,400 words, ~7 min | 2026-10-19 |
| Text | Wireflows: a UX deliverable for workflows and apps (2016, rev. 2025) | NN/g | <https://www.nngroup.com/articles/wireflows/> | ~1,800 words, ~9 min | 2026-10-19 |
| Video | User Journeys vs. User Flows | NNgroup | <https://www.youtube.com/watch?v=dsviXwJwslI> | 3:47 | 2026-10-19 |
| Video | Prototypes vs Wireframes in UX Projects | NNgroup | <https://www.youtube.com/watch?v=miVcrftnhzM> | 2:35 | 2026-10-19 |

## 13. Design systems, atomic design, interface inventory (Brad Frost)

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | *Atomic Design* (free online book) | Brad Frost, 2016 | <https://atomicdesign.bradfrost.com/> | book | 2026-10-19 |
| Text | Ch. 2 "Atomic Design Methodology" | Frost | <https://atomicdesign.bradfrost.com/chapter-2/> | ~4,300 words, ~21 min | 2026-10-19 |
| Text | Interface Inventory (2013-07-10) | Frost | <https://bradfrost.com/blog/post/interface-inventory/> | ~1,000 words, ~5 min | 2026-10-19 |
| Video | Is Atomic Design Dead? | Brad Frost, Hatch Conference Berlin 2023 | <https://www.youtube.com/watch?v=PK_PICNTgAg> | 36:59 | 2026-10-19 |

- The canonical "Atomic Design" talk (An Event Apart 2015, `W-h1FtNYim4`, 1:02:33) **failed oEmbed** (embedding probably disabled), so it is left out.

## 14. Design tokens (W3C DTCG; Salesforce origin)

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | Design Tokens Format Module 2025.10 (Final Community Group Report; **not** a W3C Standard) | W3C DTCG | <https://www.designtokens.org/TR/2025.10/format/> | ~9,500 words, ~48 min | 2026-10-19 |
| Text | Design Tokens specification reaches first stable version (2025-10-28) | DTCG (Kaelig Deloumeau-Prigent) | <https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/> | ~780 words, ~4 min | 2026-10-19 |
| Text | DTCG home | DTCG | <https://www.designtokens.org/> | ~280 words, 1 min | 2026-10-19 |
| Video | WTF are Design Tokens? | Jina Anne (own channel) | <https://www.youtube.com/watch?v=q5qIowMyVt8> | 11:46 | 2026-10-19 |
| Video | DTCG W3C release and adapting design systems for multiple brands | Figma, Schema 2025 | <https://www.youtube.com/watch?v=XI8cjfw8rt8> | 20:45 | 2026-10-19 |

- The **Salesforce origin (Jina Anne and Jon Levine)** comes from secondary sources only (inferred). The 2025.10 format module never mentions Salesforce, and no primary Salesforce page was fetched.
- `tr.designtokens.org/format/` now redirects to the *drafts* (`/tr/drafts/format/`). Link the dated 2025.10 version.

## 15. Interaction states: empty, loading, error, partial, ideal

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | *Designing Products People Love* | Scott Hurff, O'Reilly, 2015 (inferred) | — | book | — |
| Text | Why your user interface is awkward: you're ignoring the UI stack (2015-08-18) | Scott Hurff | <https://www.scotthurff.com/posts/why-your-user-interface-is-awkward-youre-ignoring-the-ui-stack/> | ~4,900 words, ~25 min | 2026-10-19 |
| Text | Designing Empty States in Complex Applications (2021) | NN/g | <https://www.nngroup.com/articles/empty-state-interface-design/> | ~2,000 words, ~10 min | 2026-10-19 |
| Video | Empty States in Application Design: 3 Guidelines | NNgroup | <https://www.youtube.com/watch?v=MUh3xyvEWDE> | 3:22 | 2026-10-19 |

- Hurff's article names five states: blank, loading, partial, error, ideal (confirmed in the text). No video covers all five; the NN/g video covers empty states only.

## 16. Modalities and touchpoints

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | WCAG 2.2 Guideline 2.5 "Input Modalities" (Understanding doc) | W3C WAI | <https://www.w3.org/WAI/WCAG22/Understanding/input-modalities> | ~300 words, 1 min (index to SCs) | 2026-10-19 |
| Text | How People with Disabilities Use the Web: Input (typing, writing, clicking) | W3C WAI | <https://www.w3.org/WAI/people-use-web/tools-techniques/input/> | ~1,300 words, ~6 min | 2026-10-19 |
| Text | How Channels, Devices, and Touchpoints Impact the Customer Journey (2016, rev. 2024) | NN/g | <https://www.nngroup.com/articles/channels-devices-touchpoints/> | ~1,050 words, ~5 min | 2026-10-19 |
| Text (alt.) | Service Blueprints: Definition (2017) | NN/g | <https://www.nngroup.com/articles/service-blueprints-definition/> | ~1,800 words, ~9 min | 2026-10-19 |
| Video | Web Accessibility Perspectives: Keyboard Compatibility | W3C WAI | <https://www.youtube.com/watch?v=93UgG72os8M> | 0:48 | 2026-10-19 |
| Video | Web Accessibility Perspectives: Voice Recognition | W3C WAI | <https://www.youtube.com/watch?v=7RHG_XiQ0ck> | 1:11 | 2026-10-19 |
| Video | Don't Map Touch Points. Do THIS Instead | Service Design Show | <https://www.youtube.com/watch?v=zTIeNEV9cOU> | 4:36 | 2026-10-19 |
| FR text | Outils et techniques | W3C WAI (French translation) | <https://www.w3.org/WAI/people-use-web/tools-techniques/fr> | ~4,000 words, ~20 min | 2026-10-19 |

- No single source covers both meanings (I/O modalities and service touchpoints). Pair the WAI page with the NN/g article.

## 17. Accessibility: WCAG 2.2 and RGAA

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | WCAG 2.2 (W3C Recommendation) | W3C | <https://www.w3.org/TR/WCAG22/> | ~23,000 words (reference) | 2026-10-19 |
| Text | WCAG 2 Overview | W3C WAI | <https://www.w3.org/WAI/standards-guidelines/wcag/> | ~1,100 words, ~6 min | 2026-10-19 |
| Text | What's New in WCAG 2.2 | W3C WAI | <https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/> | ~2,100 words, ~11 min | 2026-10-19 |
| Video | Introduction to Web Accessibility and W3C Standards | W3C WAI | <https://www.youtube.com/watch?v=20SHvU2PKsM> | 4:07 | 2026-10-19 |
| FR text | Règles pour l'accessibilité des contenus Web (WCAG) 2 : vue d'ensemble | W3C WAI | <https://www.w3.org/WAI/standards-guidelines/wcag/fr> | ~1,300 words, ~7 min | 2026-10-19 |
| FR text | RGAA (Référentiel général d'amélioration de l'accessibilité) home | DINUM / accessibilite.numerique.gouv.fr | <https://accessibilite.numerique.gouv.fr/> | ~230 words, 1 min | 2026-10-19 |
| FR reference | RGAA critères et tests | same | <https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/> | ~50,000 words (reference) | 2026-10-19 |

- **RGAA version:** RGAA 4 was published on 2019-09-16 and last updated on 2023-04-18 (4.1.2). The site says **RGAA 5 is being drafted, with publication planned for late 2026**. Recheck before the Foundations doc ships.
- WCAG 2.2 date details (Recommendation 2023-10, later edits) were not re-read from the spec (inferred).

## 18. UX writing, microcopy, voice and tone

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | *Strategic Writing for UX* | Torrey Podmajersky, O'Reilly, 2019 | — | book | — |
| Text | Voice and Tone (Content Style Guide; CC BY-NC) | Mailchimp | <https://styleguide.mailchimp.com/voice-and-tone/> | ~680 words, ~3 min | 2026-10-19 |
| Text | The Four Dimensions of Tone of Voice (2016) | NN/g | <https://www.nngroup.com/articles/tone-of-voice-dimensions/> | ~2,400 words, ~12 min | 2026-10-19 |
| Text (alt.) | UX Writing: Study Guide (links hub) | NN/g | <https://www.nngroup.com/articles/ux-writing-study-guide/> | ~2,100 words, ~11 min | 2026-10-19 |
| Video | Strategic writing for UX | Torrey Podmajersky, Optimal | <https://www.youtube.com/watch?v=1Z8gbVnrTfE> | 32:37 | 2026-10-19 |
| Video | The Four Dimensions of Tone of Voice in UX Writing | NNgroup | <https://www.youtube.com/watch?v=0ar4DezKKGI> | 3:01 | 2026-10-19 |

## 19. Usability testing (~5 users) and Nielsen's 10 heuristics

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Literature | "A mathematical model of the finding of usability problems", INTERCHI '93 | Nielsen & Landauer, 1993 (inferred citation) | — | paper | — |
| Text | Why You Only Need to Test with 5 Users (2000-03-18) | Jakob Nielsen, NN/g | <https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/> | ~1,600 words, ~8 min | 2026-10-19 |
| Text | 10 Usability Heuristics for User Interface Design (1994, reviewed 2024) | Jakob Nielsen, NN/g | <https://www.nngroup.com/articles/ten-usability-heuristics/> | ~2,250 words, ~11 min | 2026-10-19 |
| Video | Usability Testing w. 5 Users: Design Process (1 of 3) | NNgroup | <https://www.youtube.com/watch?v=RhgUirqki50> | 3:37 | 2026-10-19 |
| Video | Heuristic Evaluation of User Interfaces | NNgroup | <https://www.youtube.com/watch?v=6Bw0n6Jvwxk> | 3:14 | 2026-10-19 |

## Gaps

| Concept | Gap |
|---|---|
| 1 Use cases | Jacobson's 1987 OOPSLA paper is behind ACM DL (403). No talk by Jacobson on the *origin* of use cases under 60 min was found. |
| 2 Use-Case 2.0 | Primary sites block automated fetches (403). The free ebook download could not be verified, and the crash-course article runs 33 min. |
| 3 User stories | No primary source credits Rachel Davies; the Connextra link is via Agile Alliance only, with no name. |
| 7 Tracer bullets | No free official text; the book chapter is not among the free extracts. |
| 9 Outcomes over output | **No free text by Seiden is reachable** (his domains do not resolve). Only his video. |
| 9 HEART | No video by the authors; Rodden's GV article is unreachable. Use the 2010 paper. |
| 9 Retention rate | No recognised PM-authority source; HubSpot/Amplitude vendor content only. |
| 9 NPS | Reichheld's HBR article is paywalled; Bain's page is short. |
| 11 IBM EDT | Live site retired; Wayback only. |
| 12 Flows/wireframes | No canonical book or free primary text; NN/g only. |
| 14 Tokens origin | No primary Salesforce source for the origin story. |
| 15 States | No video covering the full set of states. |
| French | Good free French resources found only for INVEST, story mapping, WCAG/WAI and RGAA. |

## Unverified

- Rachel Davies as author of the Connextra template; the Use-Case 2.0 ebook's page count (~55 pp, from Goodreads via search) and how it is downloaded.
- Cockburn *Unifying…* 2nd-edition year (2025, from the PDF's © line only).
- Cooper *Inmates* year (1998 vs 1999); Hurff book title and year; Garrett as the wireframe reference; Nielsen & Landauer citation details.
- Salesforce / Jina Anne / Jon Levine origin of design tokens.
- IBM EDT Loop, Playbacks and Sponsor-user pages (only the archived Hills page was fetched).
- Whether the GOTO Pragmatic Programmer video covers tracer bullets; the speaker of the TPC North Star video.
- WCAG 2.2 Recommendation dates.
