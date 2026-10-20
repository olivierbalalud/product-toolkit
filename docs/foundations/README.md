# Foundations

The concepts behind this framework, for onboarding new team members. Each entry gives a short definition, why it matters to each role, how [the guide](../guide/) uses it and where it departs from the literature, the key literature, and free resources to learn it: a text under 30 minutes and a video. Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md) [R11-Q3–Q9, R12].

## What this is, and what it isn't

- **It is** a curated reading list with context, tied to the guide. Read the entries for your role, then the guide chapters they link to.
- **It isn't** a process. The rules are in the guide; Foundations explains the ideas behind them.
- **It isn't** legal advice. The [GDPR](gdpr-one-pager.md) and [AI Act](ai-act-one-pager.md) one-pagers summarise official texts for orientation, carry a "last verified" date, and are reviewed every 6 months or when the law changes. They are owned by the founders until a lawyer or DPO reviews them [R12-Q7].
- **Sources.** Legal facts cite official sources only (EUR-Lex, CNIL, European Commission). Primers and training material may come from recognised unofficial sources [R12-Q7]. Every resource is free, with no login, and was checked on **2026-10-19**; text lengths assume 200 words per minute and run slightly high. Books are cited, but nobody has to buy them [R11-Q7].
- **Language.** English first; French resources are listed where a good free one exists [R11-Q8].

## How each entry reads

| Field | Content |
|---|---|
| **Roles / Time** | Whether the entry is core or optional for PM, UX and SWE; reading time of the core material, with optional long videos in brackets |
| **Definition** | Three sentences at most |
| **Why it matters** | Per role, where it differs |
| **In this framework** | How we use it, where we depart from the literature, links to guide chapters and templates |
| **Key literature** | Author, title, year |
| **Learn it** | Text crash course, video, and a French resource if one exists |

## Files

| File | Contents |
|---|---|
| [`use-cases-vs-user-stories.md`](use-cases-vs-user-stories.md) | The two compared on seven dimensions; one feature, "Upload a document", in both forms; how they complement each other |
| [`pm-lens.md`](pm-lens.md) | From use case to user story to PRD: decomposition, use cases, goal levels, the extension matrix, user stories, INVEST, story mapping, splitting, Shape Up, outcomes and metrics |
| [`ux-lens.md`](ux-lens.md) | From use case to clickable flow: task flows and wireframes, design systems, design tokens, component inventory, interaction states, modalities and touch points, accessibility, UX writing, usability testing |
| [`swe-lens.md`](swe-lens.md) | From prototype to maintained codebase: contract-first APIs, BDD, spec-driven development, TDD, hexagonal architecture and modalities, domain modelling, ADRs, legacy code, repo conventions, the "-ilities" |
| [`security-privacy-ai.md`](security-privacy-ai.md) | OWASP ASVS, threat modelling, OWASP for LLM and agentic applications, AI risk and governance, responsible AI, privacy by design |
| [`gdpr-one-pager.md`](gdpr-one-pager.md) | The GDPR on one page |
| [`ai-act-one-pager.md`](ai-act-one-pager.md) | The EU AI Act on one page, including the 2026 "Digital Omnibus" changes |

## Reading paths

Each core path fits within **6 hours**, inside the ~16 h training budget [R1-Q14, R11-Q3, R12-Q8]. Times count the text plus any video under 30 minutes; longer videos are optional and shown in each entry. The paths are generated from the **Roles** line of each entry, so an entry is core for a role exactly when its Roles line says so.

### Product manager: ~5 h 36 min

| # | Entry | Time |
|---|---|---|
| 1 | [Use cases vs user stories](use-cases-vs-user-stories.md) | 17 min |
| 2 | [Use cases](pm-lens.md#21-use-cases) (PM lens) | 22 min |
| 3 | [Goal levels](pm-lens.md#22-goal-levels) (PM lens) | 14 min |
| 4 | [The extension matrix](pm-lens.md#24-the-extension-matrix) (PM lens) | 10 min |
| 5 | [User stories](pm-lens.md#25-user-stories) (PM lens) | 22 min |
| 6 | [INVEST](pm-lens.md#26-invest) (PM lens) | 8 min |
| 7 | [Story mapping](pm-lens.md#27-story-mapping) (PM lens) | 16 min |
| 8 | [Story splitting and vertical slices](pm-lens.md#28-story-splitting-and-vertical-slices) (PM lens) | 45 min |
| 9 | [Shape Up](pm-lens.md#29-shape-up) (PM lens) | 49 min |
| 10 | [Measurable outcomes and product metrics](pm-lens.md#210-measurable-outcomes-and-product-metrics) (PM lens) | 38 min |
| 11 | [UX writing, voice and tone](ux-lens.md#28-ux-writing-voice-and-tone) (UX lens) | 18 min |
| 12 | [Usability testing and heuristics](ux-lens.md#29-usability-testing-and-heuristics) (UX lens) | 26 min |
| 13 | [BDD, specification by example and Gherkin](swe-lens.md#22-bdd-specification-by-example-and-gherkin) (SWE lens) | 16 min |
| 14 | [Responsible AI: oversight and transparency](security-privacy-ai.md#16-responsible-ai-oversight-and-transparency) (Security, privacy and AI) | 15 min |
| 15 | [GDPR one-pager](gdpr-one-pager.md) | 10 min |
| 16 | [AI Act one-pager](ai-act-one-pager.md) | 10 min |
| | **Total** | **~5 h 36 min** |

Optional: [Use-Case 2.0 and slices](pm-lens.md#23-use-case-20-and-slices); [Jobs to be done and personas](pm-lens.md#31-jobs-to-be-done-and-personas); [Task flows and wireframes](ux-lens.md#21-task-flows-and-wireframes); [Interaction states](ux-lens.md#22-interaction-states); [Design systems and atomic design](ux-lens.md#23-design-systems-and-atomic-design); [Component inventory](ux-lens.md#24-component-inventory); [Design tokens](ux-lens.md#25-design-tokens); [Modalities and touch points](ux-lens.md#26-modalities-and-touch-points); [Accessibility](ux-lens.md#27-accessibility); [Contract-first APIs](swe-lens.md#21-contract-first-apis); [Spec-driven development](swe-lens.md#23-spec-driven-development); [TDD](swe-lens.md#24-tdd); [Domain modelling and DDD](swe-lens.md#25-domain-modelling-and-ddd); [Hexagonal architecture](swe-lens.md#26-hexagonal-architecture); [Modalities](swe-lens.md#27-modalities); [Repo conventions](swe-lens.md#28-repo-conventions); [Characterisation tests, strangler fig and parallel change](swe-lens.md#29-characterisation-tests-strangler-fig-and-parallel-change); [ADRs](swe-lens.md#210-adrs); [The "-ilities"](swe-lens.md#211-the--ilities); [Feature toggles and expand–contract migrations](swe-lens.md#212-feature-toggles-and-expandcontract-migrations); [OWASP ASVS](security-privacy-ai.md#11-owasp-asvs); [Threat modelling: STRIDE and the four questions](security-privacy-ai.md#12-threat-modelling-stride-and-the-four-questions); [OWASP Top 10 for LLM Applications](security-privacy-ai.md#13-owasp-top-10-for-llm-applications); [OWASP agentic AI and the AI Exchange](security-privacy-ai.md#14-owasp-agentic-ai-and-the-ai-exchange); [AI risk and governance](security-privacy-ai.md#15-ai-risk-and-governance); [Privacy by design](security-privacy-ai.md#17-privacy-by-design); the [PM context section](pm-lens.md#4-context); and the long videos in every entry.

### UX designer: ~4 h 43 min

| # | Entry | Time |
|---|---|---|
| 1 | [Use cases vs user stories](use-cases-vs-user-stories.md) | 17 min |
| 2 | [Use cases](pm-lens.md#21-use-cases) (PM lens) | 22 min |
| 3 | [Goal levels](pm-lens.md#22-goal-levels) (PM lens) | 14 min |
| 4 | [The extension matrix](pm-lens.md#24-the-extension-matrix) (PM lens) | 10 min |
| 5 | [User stories](pm-lens.md#25-user-stories) (PM lens) | 22 min |
| 6 | [Task flows and wireframes](ux-lens.md#21-task-flows-and-wireframes) (UX lens) | 11 min |
| 7 | [Interaction states](ux-lens.md#22-interaction-states) (UX lens) | 28 min |
| 8 | [Design systems and atomic design](ux-lens.md#23-design-systems-and-atomic-design) (UX lens) | 21 min |
| 9 | [Component inventory](ux-lens.md#24-component-inventory) (UX lens) | 5 min |
| 10 | [Design tokens](ux-lens.md#25-design-tokens) (UX lens) | 16 min |
| 11 | [Modalities and touch points](ux-lens.md#26-modalities-and-touch-points) (UX lens) | 17 min |
| 12 | [Accessibility](ux-lens.md#27-accessibility) (UX lens) | 21 min |
| 13 | [UX writing, voice and tone](ux-lens.md#28-ux-writing-voice-and-tone) (UX lens) | 18 min |
| 14 | [Usability testing and heuristics](ux-lens.md#29-usability-testing-and-heuristics) (UX lens) | 26 min |
| 15 | [Responsible AI: oversight and transparency](security-privacy-ai.md#16-responsible-ai-oversight-and-transparency) (Security, privacy and AI) | 15 min |
| 16 | [GDPR one-pager](gdpr-one-pager.md) | 10 min |
| 17 | [AI Act one-pager](ai-act-one-pager.md) | 10 min |
| | **Total** | **~4 h 43 min** |

Optional: [Use-Case 2.0 and slices](pm-lens.md#23-use-case-20-and-slices); [INVEST](pm-lens.md#26-invest); [Story mapping](pm-lens.md#27-story-mapping); [Story splitting and vertical slices](pm-lens.md#28-story-splitting-and-vertical-slices); [Shape Up](pm-lens.md#29-shape-up); [Measurable outcomes and product metrics](pm-lens.md#210-measurable-outcomes-and-product-metrics); [Jobs to be done and personas](pm-lens.md#31-jobs-to-be-done-and-personas); [Contract-first APIs](swe-lens.md#21-contract-first-apis); [BDD, specification by example and Gherkin](swe-lens.md#22-bdd-specification-by-example-and-gherkin); [Spec-driven development](swe-lens.md#23-spec-driven-development); [TDD](swe-lens.md#24-tdd); [Domain modelling and DDD](swe-lens.md#25-domain-modelling-and-ddd); [Hexagonal architecture](swe-lens.md#26-hexagonal-architecture); [Modalities](swe-lens.md#27-modalities); [Repo conventions](swe-lens.md#28-repo-conventions); [Characterisation tests, strangler fig and parallel change](swe-lens.md#29-characterisation-tests-strangler-fig-and-parallel-change); [ADRs](swe-lens.md#210-adrs); [The "-ilities"](swe-lens.md#211-the--ilities); [Feature toggles and expand–contract migrations](swe-lens.md#212-feature-toggles-and-expandcontract-migrations); [OWASP ASVS](security-privacy-ai.md#11-owasp-asvs); [Threat modelling: STRIDE and the four questions](security-privacy-ai.md#12-threat-modelling-stride-and-the-four-questions); [OWASP Top 10 for LLM Applications](security-privacy-ai.md#13-owasp-top-10-for-llm-applications); [OWASP agentic AI and the AI Exchange](security-privacy-ai.md#14-owasp-agentic-ai-and-the-ai-exchange); [AI risk and governance](security-privacy-ai.md#15-ai-risk-and-governance); [Privacy by design](security-privacy-ai.md#17-privacy-by-design); the [PM context section](pm-lens.md#4-context); and the long videos in every entry.

### Software engineer: ~5 h 45 min

| # | Entry | Time |
|---|---|---|
| 1 | [Use cases vs user stories](use-cases-vs-user-stories.md) | 17 min |
| 2 | [Contract-first APIs](swe-lens.md#21-contract-first-apis) (SWE lens) | 19 min |
| 3 | [BDD, specification by example and Gherkin](swe-lens.md#22-bdd-specification-by-example-and-gherkin) (SWE lens) | 16 min |
| 4 | [Spec-driven development](swe-lens.md#23-spec-driven-development) (SWE lens) | 17 min |
| 5 | [TDD](swe-lens.md#24-tdd) (SWE lens) | 7 min |
| 6 | [Domain modelling and DDD](swe-lens.md#25-domain-modelling-and-ddd) (SWE lens) | 8 min |
| 7 | [Hexagonal architecture](swe-lens.md#26-hexagonal-architecture) (SWE lens) | 23 min |
| 8 | [Characterisation tests, strangler fig and parallel change](swe-lens.md#29-characterisation-tests-strangler-fig-and-parallel-change) (SWE lens) | 47 min |
| 9 | [ADRs](swe-lens.md#210-adrs) (SWE lens) | 16 min |
| 10 | [OWASP ASVS](security-privacy-ai.md#11-owasp-asvs) (Security, privacy and AI) | 55 min |
| 11 | [Threat modelling: STRIDE and the four questions](security-privacy-ai.md#12-threat-modelling-stride-and-the-four-questions) (Security, privacy and AI) | 40 min |
| 12 | [OWASP Top 10 for LLM Applications](security-privacy-ai.md#13-owasp-top-10-for-llm-applications) (Security, privacy and AI) | 45 min |
| 13 | [Responsible AI: oversight and transparency](security-privacy-ai.md#16-responsible-ai-oversight-and-transparency) (Security, privacy and AI) | 15 min |
| 14 | [GDPR one-pager](gdpr-one-pager.md) | 10 min |
| 15 | [AI Act one-pager](ai-act-one-pager.md) | 10 min |
| | **Total** | **~5 h 45 min** |

Optional: [Use cases](pm-lens.md#21-use-cases); [Goal levels](pm-lens.md#22-goal-levels); [Use-Case 2.0 and slices](pm-lens.md#23-use-case-20-and-slices); [The extension matrix](pm-lens.md#24-the-extension-matrix); [User stories](pm-lens.md#25-user-stories); [INVEST](pm-lens.md#26-invest); [Story mapping](pm-lens.md#27-story-mapping); [Story splitting and vertical slices](pm-lens.md#28-story-splitting-and-vertical-slices); [Shape Up](pm-lens.md#29-shape-up); [Measurable outcomes and product metrics](pm-lens.md#210-measurable-outcomes-and-product-metrics); [Jobs to be done and personas](pm-lens.md#31-jobs-to-be-done-and-personas); [Task flows and wireframes](ux-lens.md#21-task-flows-and-wireframes); [Interaction states](ux-lens.md#22-interaction-states); [Design systems and atomic design](ux-lens.md#23-design-systems-and-atomic-design); [Component inventory](ux-lens.md#24-component-inventory); [Design tokens](ux-lens.md#25-design-tokens); [Modalities and touch points](ux-lens.md#26-modalities-and-touch-points); [Accessibility](ux-lens.md#27-accessibility); [UX writing, voice and tone](ux-lens.md#28-ux-writing-voice-and-tone); [Usability testing and heuristics](ux-lens.md#29-usability-testing-and-heuristics); [Modalities](swe-lens.md#27-modalities); [Repo conventions](swe-lens.md#28-repo-conventions); [The "-ilities"](swe-lens.md#211-the--ilities); [Feature toggles and expand–contract migrations](swe-lens.md#212-feature-toggles-and-expandcontract-migrations); [OWASP agentic AI and the AI Exchange](security-privacy-ai.md#14-owasp-agentic-ai-and-the-ai-exchange); [AI risk and governance](security-privacy-ai.md#15-ai-risk-and-governance); [Privacy by design](security-privacy-ai.md#17-privacy-by-design); the [PM context section](pm-lens.md#4-context); and the long videos in every entry.

## Keeping it current

- A link check runs monthly and on every PR that changes these files [R11-Q9].
- Things to recheck: the French RGAA, whose version 5 is due in late 2026; the OWASP Top 10 for LLM Applications, whose 2026 edition is newer than most training material; and the AI Act, whose dates the 2026 "Digital Omnibus" changed.
