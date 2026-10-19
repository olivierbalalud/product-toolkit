# Foundations Sources: Engineering, Security, Legal

Status: fact check, 2026-10-19 (curl, GitHub API, YouTube oEmbed plus the `lengthSeconds` field of the watch page, WebFetch, WebSearch). Input to the onboarding "Foundations" document. "(inferred)" marks a point that was not verified directly.

**Conventions**
- **Kind:** Lit = key literature. Text = crash course (free, under 30 min unless flagged). Video. FR = French resource.
- **Length:** word counts are approximate and come from the fetched HTML, including some page chrome. Reading time assumes 200 words/min. Video durations come from the watch page.
- **Checked:** every link below was fetched successfully on 2026-10-19. A book without a link is paid or was not fetched.
- **EUR-Lex:** `eur-lex.europa.eu` answers automated clients with an AWS WAF challenge (HTTP 202, empty body), so no EUR-Lex link could be verified. The official texts were fetched instead from the EU Publications Office (`publications.europa.eu/resource/cellar/...`), which serves the same Official Journal documents. The ELI identifiers are given in the text so a reader can open EUR-Lex in a browser.

---

## 1. BDD, specification by example, Gherkin, example mapping

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit + Text | Introducing BDD | Dan North, 2006 (blog dated 20 Sep 2006) | <https://dannorth.net/blog/introducing-bdd/> | ~2,700 words, ~13 min | 2026-10-19 |
| Lit | *Specification by Example* (book) | Gojko Adzic, Manning, 2011 | <https://gojko.net/books/specification-by-example/> | book page, ~4 min | 2026-10-19 |
| Lit | *Specification by Example*, chapter 1 (free PDF from Manning, linked from the book page) | Gojko Adzic | <https://manning-content.s3.amazonaws.com/download/0/e31349c-e7f9-457d-834d-3a29e71e9136/adzic_ch01.pdf> | PDF, 2.5 MB | 2026-10-19 |
| Text | Specification By Example (bliki) | Martin Fowler | <https://martinfowler.com/bliki/SpecificationByExample.html> | ~900 words, ~5 min | 2026-10-19 |
| Text | Given When Then (bliki) | Martin Fowler | <https://martinfowler.com/bliki/GivenWhenThen.html> | ~700 words, ~3 min | 2026-10-19 |
| Text | Gherkin Reference | Cucumber docs | <https://cucumber.io/docs/gherkin/reference/> | ~3,100 words, ~15 min | 2026-10-19 |
| Text | Introducing Example Mapping | Matt Wynne, cucumber.io, 8 Dec 2015 | <https://cucumber.io/blog/bdd/example-mapping-introduction/> | ~1,800 words, ~9 min | 2026-10-19 |
| Video | 20 Years of BDD | Daniel Terhorst-North (Dan North), PHP UK Conference, 2025 | <https://www.youtube.com/watch?v=og8Gr05dz6Y> | 29:45 | 2026-10-19 |
| Video | Specification By Example (Small Talk) | Gojko Adzic, Avanscoperta, 2022 | <https://www.youtube.com/watch?v=0R9g24KQE0w> | 33:01 | 2026-10-19 |
| Video | Introducing Example Mapping | Cucumber channel. The description names Aslak Hellesøy and Steve Tooke, not Matt Wynne. | <https://www.youtube.com/watch?v=VwvrGfWmG_U> | 39:29 | 2026-10-19 |

## 2. TDD

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit | *Test-Driven Development: By Example* | Kent Beck, Addison-Wesley, 2002 | — (paid book) | — | — |
| Text | Canon TDD | Kent Beck, *Tidy First?* newsletter, 11 Dec 2023. Free to read; the paid tier only adds extras. The URL redirects to `newsletter.kentbeck.com`. | <https://tidyfirst.substack.com/p/canon-tdd> | ~1,500 words, ~7 min | 2026-10-19 |
| Text | Test Driven Development (bliki) | Martin Fowler | <https://martinfowler.com/bliki/TestDrivenDevelopment.html> | ~400 words, ~2 min | 2026-10-19 |
| Video | Canon Test-Driven Development | Kent Beck, Craft 2025 (CraftHub Events) | <https://www.youtube.com/watch?v=90VBvjYedWI> | 48:46 | 2026-10-19 |
| Video (alt) | TDD: Theme & Variations | Kent Beck, Tech Excellence | <https://www.youtube.com/watch?v=C5IH0ABmyc0> | 57:30 | 2026-10-19 |

## 3. Changing legacy code safely

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit | *Working Effectively with Legacy Code* | Michael Feathers, Prentice Hall, 2004 | — (paid book) | — | — |
| Text | Characterization Testing | Michael Feathers, blog, 8 Aug 2016 | <https://michaelfeathers.silvrback.com/characterization-testing> | ~1,200 words, ~6 min | 2026-10-19 |
| Text | Strangler Fig (bliki; 2004 original, rewritten 22 Aug 2024) | Martin Fowler | <https://martinfowler.com/bliki/StranglerFigApplication.html> | ~1,100 words, ~5 min | 2026-10-19 |
| Text | Parallel Change (expand / migrate / contract) | Danilo Sato, martinfowler.com bliki, 13 May 2014 | <https://martinfowler.com/bliki/ParallelChange.html> | ~1,300 words, ~6 min | 2026-10-19 |
| Lit | Feature Toggles (aka Feature Flags) | Pete Hodgson, martinfowler.com, page dated 9 Oct 2017 | <https://martinfowler.com/articles/feature-toggles.html> | ~7,750 words, ~39 min (**over 30**; read the first sections) | 2026-10-19 |
| Text | Feature Flag (bliki; the short version) | Martin Fowler | <https://martinfowler.com/bliki/FeatureFlag.html> | ~1,200 words, ~6 min | 2026-10-19 |
| Video | Looking Back at Working Effectively with Legacy Code | Michael Feathers, InfoQ | <https://www.youtube.com/watch?v=5OA5v-ALkbM> | 29:58 | 2026-10-19 |
| Video | Feature Flags Suck! | Pete Hodgson, CNCF | <https://www.youtube.com/watch?v=MDERgrcaT6w> | 29:56 | 2026-10-19 |
| Video | Monolith Decomposition Patterns | Sam Newman, GOTO 2019. That it covers the strangler fig is inferred. | <https://www.youtube.com/watch?v=9I9GdSQ1bbM> | 43:57 | 2026-10-19 |

## 4. Hexagonal architecture / ports and adapters

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit + Text | Hexagonal Architecture (Ports & Adapters). The page carries 2005 dates and a 2025-04-18 update (inferred from the dates on the page). | Alistair Cockburn | <https://alistair.cockburn.us/hexagonal-architecture/> | ~4,700 words, ~23 min | 2026-10-19 |
| Lit | *Hexagonal Architecture Explained* (book, 2024) | A. Cockburn, J. M. Garrido de Paz | — (paid; not fetched) | — | — |
| Video | Hexagonal Architecture | Alistair Cockburn, Tech Excellence | <https://www.youtube.com/watch?v=k0ykTxw7s0Y> | 56:16 | 2026-10-19 |
| Video (alt) | The Hexagonal – Ports & Adapters Architecture | iSAQB, SAG 2025 | <https://www.youtube.com/watch?v=ChUlRa0xsWo> | 44:41 | 2026-10-19 |

## 5. Domain-driven design

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit | *Domain-Driven Design: Tackling Complexity in the Heart of Software* | Eric Evans, Addison-Wesley, 2003 | — (paid book) | — | — |
| Lit | DDD Reference (free PDF, 2015-03 edition) | Eric Evans, Domain Language | <https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf> | PDF, ~60 pp (inferred) | 2026-10-19 |
| Text | Domain Driven Design (bliki) | Martin Fowler | <https://martinfowler.com/bliki/DomainDrivenDesign.html> | ~500 words, ~3 min | 2026-10-19 |
| Text | Bounded Context (bliki) | Martin Fowler | <https://martinfowler.com/bliki/BoundedContext.html> | ~700 words, ~4 min | 2026-10-19 |
| Text | Ubiquitous Language (bliki) | Martin Fowler | <https://martinfowler.com/bliki/UbiquitousLanguage.html> | ~200 words, ~1 min | 2026-10-19 |
| Video | What is DDD | Eric Evans, DDD Europe 2019 | <https://www.youtube.com/watch?v=pMuiVlnGqjk> | 57:05 | 2026-10-19 |
| Video (alt) | Bounded Contexts | Eric Evans, DDD Europe | <https://www.youtube.com/watch?v=am-HXycfalo> | 34:01 | 2026-10-19 |

## 6. Architecture decision records

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit + Text | Documenting Architecture Decisions | Michael Nygard, Cognitect blog, 15 Nov 2011 | <https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions> | ~1,300 words, ~7 min | 2026-10-19 |
| Text | MADR (Markdown Architectural Decision Records), v4.0.0, 17 Sep 2024 | adr GitHub organisation | <https://adr.github.io/madr/> | ~1,900 words, ~9 min | 2026-10-19 |
| Text | ADR overview and tooling hub | adr.github.io | <https://adr.github.io/> | ~550 words, ~3 min | 2026-10-19 |
| Video | Creating effective and objective ADRs | Piet van Dongen, Devoxx (a practitioner, not Nygard) | <https://www.youtube.com/watch?v=DSRQ-90eDBw> | 39:18 | 2026-10-19 |

## 7. Contract-first / API design-first with OpenAPI

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit | OpenAPI Specification **v3.2.1** (released 2026-09-10; 3.2.0 came out 2025-09-19) | OpenAPI Initiative | <https://spec.openapis.org/oas/latest.html> | reference, ~40,000 words | 2026-10-19 |
| Text | Best Practices: "Use a Design-First Approach" | OpenAPI Initiative, learn.openapis.org | <https://learn.openapis.org/best-practices.html> | ~1,400 words, ~7 min | 2026-10-19 |
| Text | Getting Started | learn.openapis.org | <https://learn.openapis.org/> | ~500 words, ~3 min | 2026-10-19 |
| Text | Understanding the API-First Approach to Building Products. Vendor article; the URL redirects to swagger.io/blog. | Swagger (SmartBear) | <https://swagger.io/resources/articles/adopting-an-api-first-approach/> | ~1,300 words, ~6 min | 2026-10-19 |
| Video | The Language of API Design: Creating your OpenAPI Description | Erik Wilde. That he is a recognised API practitioner is inferred. | <https://www.youtube.com/watch?v=V5fMaz0sybw> | 12:10 | 2026-10-19 |

## 8. Spec-driven development (SDD) in AI-assisted coding

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit + Text | Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl | Birgitta Böckeler, martinfowler.com, 15 Oct 2025 | <https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html> | ~3,400 words, ~17 min | 2026-10-19 |
| Text | Tech Radar: Spec-driven development. Ring: **Assess**, Nov 2025. The page notes it is not on the current edition. | Thoughtworks | <https://www.thoughtworks.com/radar/techniques/spec-driven-development> | ~400 words, ~2 min | 2026-10-19 |
| Text | Tech Radar Vol. 34 (Apr 2026): GitHub Spec Kit, **Assess** | Thoughtworks | <https://www.thoughtworks.com/radar/languages-and-frameworks/github-spec-kit> | ~370 words, ~2 min | 2026-10-19 |
| Text | Tech Radar Vol. 34 (Apr 2026): OpenSpec, **Assess** | Thoughtworks | <https://www.thoughtworks.com/radar/tools/openspec> | ~300 words, ~2 min | 2026-10-19 |
| Lit | github/spec-kit (MIT; created 2025-08-21; latest release v1.2.2, 2026-10-19). CLI is `specify`; it uses a "constitution". | GitHub | <https://github.com/github/spec-kit> | README ~1,500 words, ~8 min | 2026-10-19 |
| Text | Spec-driven development with AI: Get started with a new open source toolkit | GitHub Blog | <https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/> | ~2,300 words, ~11 min | 2026-10-19 |
| Text | Kiro docs: Specs (`requirements.md` or `bugfix.md`, `design.md`, `tasks.md`) | Kiro (AWS) | <https://kiro.dev/docs/specs/> | ~950 words, ~5 min | 2026-10-19 |
| Video | The ONLY guide you'll need for GitHub Spec Kit | channel "Den". That this is Den Delimarsky, the spec-kit maintainer, is inferred. | <https://www.youtube.com/watch?v=a9eR1xsfvHg> | 40:00 | 2026-10-19 |
| Video | Spec-driven development with Kiro (DEV314) | AWS Events, re:Invent 2025 | <https://www.youtube.com/watch?v=4qcWgPb-8Fk> | 49:15 | 2026-10-19 |

Radar Vol. 34 also flags "semantic diffusion" around the term SDD: it is used inconsistently and overlaps with "harness engineering".

## 9. Repo conventions: Conventional Commits, monorepos

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit + Text | Conventional Commits 1.0.0 | conventionalcommits.org (last repo commit 2026-03-11) | <https://www.conventionalcommits.org/en/v1.0.0/> | ~1,600 words, ~8 min | 2026-10-19 |
| Text | Monorepo Explained. Vendor-maintained: "Made with love by Nx". | monorepo.tools | <https://monorepo.tools/> | ~1,500 words, ~8 min | 2026-10-19 |
| Lit | "Why Google Stores Billions of Lines of Code in a Single Repository" | R. Potvin, J. Levenberg, *CACM*, 2016 | — (not fetched) | — | — |
| Video | Improve your Git workflow with Conventional Commits | Andrii Pugach (community talk; no official video found) | <https://www.youtube.com/watch?v=oXB3oPKdrmM> | 44:19 | 2026-10-19 |
| Video | Monorepos – Benefits, Challenges and Importance of Tooling Support | Juri Strumpflohner, Devoxx. That he is from the Nx team is inferred. | <https://www.youtube.com/watch?v=15VeTQLnWrs> | 45:04 | 2026-10-19 |
| Video (alt, Python) | The Gentle Monorepo | PyData Amsterdam 2025 | <https://www.youtube.com/watch?v=k49496sH9aw> | 35:00 | 2026-10-19 |

## 10. Interaction modalities: one business core, several inbound adapters

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit + Text | Hexagonal Architecture. The stated intent: "Allow an application to equally be driven by users, programs, automated test or batch scripts". | Alistair Cockburn | <https://alistair.cockburn.us/hexagonal-architecture/> | ~23 min | 2026-10-19 |
| Text | Hexagonal Architecture – Ports and Adapters Pattern. Covers driver (primary) and driven sides, with test/real driver adapter combinations. | Juan Manuel Garrido de Paz, Cockburn's co-author | <https://jmgarridopaz.github.io/content/hexagonalarchitecture.html> | ~4,500 words, ~22 min | 2026-10-19 |
| Text | Hexagonal architecture pattern. Says the adapter overhead "is justified only if" there are several input sources and outputs. | AWS Prescriptive Guidance | <https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/hexagonal-architecture.html> | ~1,700 words, ~9 min | 2026-10-19 |
| Text | DDD, Hexagonal, Onion, Clean, CQRS… How I put it all together | Herberto Graça, 2017 | <https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/> | ~8,000 words, ~40 min (**over 30**) | 2026-10-19 |
| Video | Stop Mixing FastAPI with Business Logic: Fix It with Ports & Adapters | ArjanCodes. Matches our stack. Whether it shows several inbound adapters is unverified. | <https://www.youtube.com/watch?v=FXwBWS4qDAA> | 25:23 | 2026-10-19 |

The Netflix Tech Blog post "Ready for changes with Hexagonal Architecture" returned 403 (Cloudflare), so it is not included.

## 11. The "-ilities": ISO/IEC 25010, arc42

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit | ISO/IEC 25010:2023, product quality model | ISO/IEC (paid). iso.org returned 403 to every automated fetch. | — | — | — |
| Text | ISO 25010 overview: **nine** characteristics, including the 2023 additions such as Interaction Capability | iso25000.com (a Spanish evaluation portal, not ISO) | <https://iso25000.com/index.php/en/iso-25000-standards/iso-25010> | ~800 words, ~4 min | 2026-10-19 |
| Text | arc42 Section 10: Quality requirements (quality tree, scenarios) | arc42 docs | <https://docs.arc42.org/section-10/> | ~1,000 words, ~5 min | 2026-10-19 |
| Text | arc42 Quality Model (Q42): definitions, aliases, mapped to standards | quality.arc42.org | <https://quality.arc42.org/> | reference site | 2026-10-19 |
| Video | Getting Quality Right | Gernot Starke, arc42 co-creator, NewCrafts 2024 | <https://www.youtube.com/watch?v=4Zb4q27u2EU> | 46:54 | 2026-10-19 |
| Video (alt) | ISO 25010 explainer | NUCIDA Group (vendor) | <https://www.youtube.com/watch?v=HrGEA0HT71Q> | 15:25 | 2026-10-19 |

The 2023 list of nine is: functional suitability, performance efficiency, compatibility, interaction capability, reliability, security, maintainability, flexibility, safety. The overview page confirms "nine" and the first four names; the other five are inferred.

## 12. OWASP ASVS

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit | OWASP ASVS **5.0.0**, the latest stable release, published on GitHub 2025-05-30 at Global AppSec EU Barcelona; CC BY-SA 4.0. The GitHub "latest" tag is a bleeding-edge build. | OWASP | <https://owasp.org/www-project-application-security-verification-standard/> | project page ~650 words, ~3 min | 2026-10-19 |
| Text | ASVS repo README: what is new in 5.0 and requirement IDs such as `v5.0.0-1.2.5` | OWASP | <https://github.com/OWASP/ASVS> | ~1,200 words, ~6 min | 2026-10-19 |
| Video | What's New in ASVS V5 | Eden Yardeni, NDC Security 2026 | <https://www.youtube.com/watch?v=SHSpUsVmDLA> | 45:29 | 2026-10-19 |
| Video (alt) | ASVS talk, OWASP Foundation channel (version not checked) | Shanni Prutchi, Ryan Armstrong | <https://www.youtube.com/watch?v=BnP2vls88fw> | 35:17 | 2026-10-19 |

## 13. Threat modelling

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit | *Threat Modeling: Designing for Security* | Adam Shostack, Wiley, 2014 | — (paid book) | — | — |
| Text | The Ultimate Beginner's Guide to Threat Modeling. Built on the four questions: What are we working on? What can go wrong? What are we going to do about it? Did we do a good job? | Shostack + Associates | <https://shostack.org/resources/threat-modeling> | ~4,000 words, ~20 min | 2026-10-19 |
| Text | Threat Modeling Manifesto (2020, inferred) | Shostack et al. | <https://www.threatmodelingmanifesto.org/> | ~1,100 words, ~6 min | 2026-10-19 |
| Text | Threat Modeling Cheat Sheet | OWASP Cheat Sheet Series | <https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html> | ~2,500 words, ~12 min | 2026-10-19 |
| Text | Threat Modeling (community page; owasp.org/www-community redirects here) | OWASP | <https://community.owasp.org/Threat_Modeling> | ~900 words, ~5 min | 2026-10-19 |
| Text | Microsoft Threat Modeling Tool: Threats (STRIDE categories) | Microsoft Learn | <https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats> | ~600 words, ~3 min | 2026-10-19 |
| Video | Threat Modeling and the Four Question Framework | Adam Shostack, CyberRisk TV | <https://www.youtube.com/watch?v=-OBgxD_Zhdw> | 17:18 | 2026-10-19 |
| Video | Threat Modeling for Developers (panel) | OWASP Foundation | <https://www.youtube.com/watch?v=ekwOAPlkf9c> | 53:25 | 2026-10-19 |
| Video (STRIDE) | STRIDE explainer (small channel; no official Microsoft video found) | Netsec Explained | <https://www.youtube.com/watch?v=rEnJYNkUde0> | 21:49 | 2026-10-19 |

## 14. AI-specific security (OWASP)

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit | **OWASP Top 10 for LLM Applications 2026**, published 3 Aug 2026, which supersedes 2025 | OWASP GenAI Security Project | <https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/> | PDF, 2.4 MB | 2026-10-19 |
| Text | LLM Top 10 **2025** list (12 Mar 2025 per the page) and per-risk pages | OWASP GenAI Security Project | <https://genai.owasp.org/llm-top-10/> | list ~2 min, ~5 min per risk | 2026-10-19 |
| Lit | **OWASP Top 10 for Agentic Applications for 2026**, published 9 Dec 2025 | OWASP GenAI Security Project | <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/> | PDF, 1.3 MB | 2026-10-19 |
| Lit | Agentic AI – Threats and Mitigations v1.0, 17 Feb 2025 | OWASP GenAI Security Project | <https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/> | PDF | 2026-10-19 |
| Lit + Text | OWASP AI Exchange: "300+ pages of free … guidance", which feeds the AI Act and ISO standards | OWASP, founded by Rob van der Veer | <https://owaspai.org/> | home ~650 words, ~3 min | 2026-10-19 |
| Video | OWASP's Top 10 Ways to Attack LLMs (likely the 2025 edition, inferred) | IBM Technology | <https://www.youtube.com/watch?v=gUNXZMcd2jU> | 25:11 | 2026-10-19 |
| Video | Deep Dive into the OWASP Top 10 for Agentic AI Applications | John Sotiropoulos, OWASP London | <https://www.youtube.com/watch?v=-vXoC0UvpjY> | 52:23 | 2026-10-19 |
| Video | The OWASP AI Exchange in 3 minutes | Rob van der Veer, official channel | <https://www.youtube.com/watch?v=kQC7ouDB_z8> | 3:01 | 2026-10-19 |

- **LLM 2026** (taken from the PDF): LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Excessive Agency, LLM04 Supply Chain, LLM05 Data and Model Poisoning, LLM06 Unbounded Consumption, LLM07 Misinformation, LLM08 Hidden Context Exposure, LLM09 Vector and Embedding Weaknesses, LLM10 Improper Output Handling.
  - Compared with 2025, "System Prompt Leakage" no longer appears, and "Hidden Context Exposure" is new. That one replaces the other is inferred.
- **Agentic 2026** (taken from the PDF): ASI01 Agent Goal Hijack, ASI02 Tool Misuse and Exploitation, ASI03 Identity and Privilege Abuse, ASI04 Agentic Supply Chain Vulnerabilities, ASI05 Unexpected Code Execution, ASI06 Memory & Context Poisoning, ASI07 Insecure Inter-Agent Communication, ASI08 Cascading Failures, ASI09 Human-Agent Trust Exploitation, ASI10 Rogue Agents.
- **Newer resources:** the project also lists an "Agent Control Standard (ACS)" and a "GenAI Security Industry Framework Crosswalk", both dated 1 Sep 2026. Neither was reviewed.

## 15. AI risk, governance, responsible AI

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit | AI RMF 1.0 (NIST AI 100-1), 26 Jan 2023 | NIST | <https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf> | PDF, 48 pp | 2026-10-19 |
| Lit | Generative AI Profile (NIST AI 600-1), 26 Jul 2024 | NIST | <https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf> | PDF, 64 pp | 2026-10-19 |
| Text | AI Risk Management Framework landing page. Covers 1.0, 600-1 and a 7 Apr 2026 concept note for a critical-infrastructure profile. | NIST | <https://www.nist.gov/itl/ai-risk-management-framework> | ~650 words, ~3 min | 2026-10-19 |
| Text | AI RMF (Govern / Map / Measure / Manage) | NIST AI Resource Center | <https://airc.nist.gov/airmf-resources/airmf/> | ~470 words, ~2 min | 2026-10-19 |
| Lit | ISO/IEC 42001:2023, AI management system. Overview only: published 2023-12-18, ed. 1.0, 51 pp, **CHF 225**. iso.org returned 403. | IEC Webstore | <https://webstore.iec.ch/publication/90574> | abstract | 2026-10-19 |
| Text | OECD AI Principles overview (adopted May 2019, updated May 2024) | OECD.AI | <https://oecd.ai/en/ai-principles> | ~800 words, ~4 min | 2026-10-19 |
| FR | Les fiches pratiques IA (index of CNIL's AI how-to sheets) | CNIL | <https://www.cnil.fr/fr/les-fiches-pratiques-ia> | ~850 words, ~4 min | 2026-10-19 |
| FR | IA et RGPD : la CNIL publie ses nouvelles recommandations (7 Feb 2025) | CNIL | <https://www.cnil.fr/fr/ia-et-rgpd-la-cnil-publie-ses-nouvelles-recommandations-pour-accompagner-une-innovation-responsable> | ~1,300 words, ~7 min | 2026-10-19 |
| FR | Développement des systèmes d'IA : les recommandations de la CNIL pour respecter le RGPD | CNIL | <https://www.cnil.fr/fr/developpement-des-systemes-dia-les-recommandations-de-la-cnil-pour-respecter-le-rgpd> | ~9,900 words, ~50 min (**over 30**) | 2026-10-19 |
| Text (EN) | AI system development: CNIL's recommendations to comply with the GDPR | CNIL | <https://www.cnil.fr/en/ai-system-development-cnils-recommendations-to-comply-gdpr> | ~8,700 words, ~43 min (**over 30**) | 2026-10-19 |
| Video | Demystifying the NIST AI Risk Management Framework (no official NIST video found) | SANS Institute | <https://www.youtube.com/watch?v=eqKwuYCBlVE> | 9:43 | 2026-10-19 |
| Video | What is ISO/IEC 42001? | ISO (official) | <https://www.youtube.com/watch?v=O4iKEr5AIi4> | 9:54 | 2026-10-19 |

The 12 GenAI risks in NIST AI 600-1, taken from the PDF's table of contents: CBRN information or capabilities, confabulation, dangerous/violent/hateful content, data privacy, environmental impacts, harmful bias and homogenization, human-AI configuration, information integrity, information security, intellectual property, obscene/degrading/abusive content, value chain and component integration.

## 16. Privacy by design

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit | Privacy by Design: The 7 Foundational Principles | Ann Cavoukian, IPC Ontario, 2009 (rev. 2011, inferred) | IPC original returned 404/403. A copy hosted by IETF fetched as a PDF, but its text could not be extracted: <https://www.ietf.org/slides/slides-privacyws-privacy-by-design-the-seven-foundational-principles-00.pdf> | PDF, 5 pp | 2026-10-19 |
| Text | Privacy by design (the 7 principles are listed and confirmed) | Wikipedia | <https://en.wikipedia.org/wiki/Privacy_by_design> | ~5,200 words, ~26 min | 2026-10-19 |
| Lit | GDPR Art. 25, "Data protection by design and by default" | Reg. (EU) 2016/679, see §17 | see §17 | — | 2026-10-19 |
| Lit | Guidelines 4/2019 on Article 25 Data Protection by Design and by Default | EDPB | <https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-42019-article-25-data-protection-design-and_en> | landing page plus PDF | 2026-10-19 |
| Video | Privacy by Design, Security by Design | Dr Ann Cavoukian, Information Security Forum | <https://www.youtube.com/watch?v=xqreZlGL8Dk> | 33:40 | 2026-10-19 |
| FR | Guide RGPD de l'équipe de développement, e.g. fiche 5 (architecture) and fiche 7 (minimisation) | CNIL | see §17 | — | 2026-10-19 |

The seven principles: proactive not reactive; privacy as the default; privacy embedded into design; full functionality (positive-sum); end-to-end security; visibility and transparency; respect for user privacy.

## 17. GDPR

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit | Regulation (EU) 2016/679 (GDPR), EN, official OJ text. ELI `eli/reg/2016/679/oj`; EUR-Lex was not fetchable. | EU Publications Office | <http://publications.europa.eu/resource/cellar/3e485e15-11bd-11e6-ba9a-01aa75ed71a1.0006.03/DOC_1> | 99 articles (reference) | 2026-10-19 |
| FR | Règlement (UE) 2016/679, FR, official text | EU Publications Office | <http://publications.europa.eu/resource/cellar/3e485e15-11bd-11e6-ba9a-01aa75ed71a1.0009.03/DOC_1> | reference | 2026-10-19 |
| Text | Data protection explained | European Commission | <https://commission.europa.eu/law/law-topic/data-protection/data-protection-explained_en> | ~1,200 words, ~6 min | 2026-10-19 |
| FR | Guide RGPD de l'équipe de développement: fiches 0–18, open source (GPLv3 / Licence Ouverte 2.0); repo last pushed 2024-04-16 | CNIL (LINCnil) | <https://lincnil.github.io/Guide-RGPD-du-developpeur/> | ~18,600 words, ~93 min (whole guide; read by fiche) | 2026-10-19 |
| FR | Guide RGPD du développeur, CNIL landing page | CNIL | <https://www.cnil.fr/fr/guide-rgpd-du-developpeur> | ~900 words, ~4 min | 2026-10-19 |
| FR | Guide repo, open to contributions | CNIL (LINCnil) | <https://github.com/LINCnil/Guide-RGPD-du-developpeur> | — | 2026-10-19 |
| Text (EN) | GDPR Developer's Guide. The French version is authoritative; the EN repo's last commit is 2021-10-06, so it may lag. | CNIL (LINCnil) | <https://lincnil.github.io/GDPR-Developer-Guide/> | ~9,800 words, ~49 min | 2026-10-19 |
| Text (EN) | GDPR developer's guide, CNIL landing page | CNIL | <https://www.cnil.fr/en/gdpr-developers-guide> | ~900 words, ~4 min | 2026-10-19 |
| FR | Comprendre le RGPD | CNIL | <https://www.cnil.fr/fr/comprendre-le-rgpd> | ~500 words, ~2 min | 2026-10-19 |
| FR | L'analyse d'impact relative à la protection des données (AIPD) | CNIL | <https://www.cnil.fr/fr/RGPD-analyse-impact-protection-des-donnees-aipd> | ~500 words, ~2 min | 2026-10-19 |
| Text | Adequacy decisions; the US is listed for organisations in the EU-US Data Privacy Framework | European Commission | <https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en> | ~1,100 words, ~6 min | 2026-10-19 |
| Text | Standard Contractual Clauses (SCC) | European Commission | <https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en> | ~600 words, ~3 min | 2026-10-19 |
| Video | Overview of GDPR, cybersecurity and ePrivacy (about 9 years old) | Wojciech Wiewiórowski, EDPS | <https://www.youtube.com/watch?v=AeffByaxbDE> | 16:29 | 2026-10-19 |
| Video (FR) | RGPD pour les développeurs. Speaker: François Delbrayelle, not CNIL; no official CNIL video found. | GDG France, DevFest Lille 2022 | <https://www.youtube.com/watch?v=wkbQ6Ec4qXY> | 54:19 | 2026-10-19 |

### Facts for the one-pager (checked against the official OJ text above)

**Principles and lawful bases**
- **Scope and roles:** definitions are in Art. 4: personal data, processing, controller, processor. The controller's accountability is in Art. 5(2) and Art. 24.
- **Principles (Art. 5(1)):** lawfulness, fairness and transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality. Accountability is Art. 5(2).
- **Lawful bases (Art. 6(1)):** (a) consent, (b) contract, (c) legal obligation, (d) vital interests, (e) public task, (f) legitimate interests. Consent conditions are in Art. 7. Special categories are in Art. 9.
- **Transparency:** Art. 12 (modalities), Art. 13 (data collected from the person) and Art. 14 (data obtained otherwise).

**Data subject rights**
- Access (Art. 15), rectification (16), erasure (17), restriction (18), portability (20), objection (21).
- Automated individual decisions, including profiling: Art. 22. This is relevant for LLM features that decide about people.

**Obligations on the company**
- **By design and by default:** Art. 25. **Security of processing:** Art. 32.
- **Processors (Art. 28):**
  - Only processors that give sufficient guarantees may be used (28(1)).
  - A sub-processor needs the controller's prior written authorisation (28(2)).
  - A binding contract with the mandatory content is required (28(3)).
  - In our case this covers LLM API vendors and cloud hosts (inferred).
- **Records of processing (Art. 30):** these apply to controllers and processors. The exemption for organisations with **fewer than 250 employees** (30(5)) does not apply when processing is likely to result in a risk, is not occasional, or involves special categories.
- **Breach notification:**
  - The controller notifies the supervisory authority "without undue delay and, where feasible, not later than **72 hours**" (Art. 33(1)), unless the breach is unlikely to result in a risk.
  - A processor notifies the controller without undue delay (33(2)).
  - Data subjects are informed when the risk is high (Art. 34).
- **DPIA (Art. 35):** required when processing "using new technologies" is likely to result in a high risk. It is required in particular for:
  - systematic evaluation by automated processing, including profiling (35(3)(a));
  - large-scale special-category data (35(3)(b));
  - large-scale systematic monitoring of public areas (35(3)(c)).
  - Supervisory authorities publish lists of processing that needs one (35(4)). The CNIL calls a DPIA an "AIPD".
- **DPO:** Art. 37.

**Transfers outside the EEA, fines, timeline**
- **International transfers (Chapter V, Art. 44–49):**
  - adequacy decisions (Art. 45; the US is covered via the EU-US Data Privacy Framework for participating organisations, per the Commission page checked 2026-10-19);
  - appropriate safeguards such as SCCs and BCRs (Art. 46; BCRs are in Art. 47);
  - derogations (Art. 49).
- **Fines (Art. 83):** up to €10M or 2% of worldwide annual turnover (83(4)), and up to €20M or 4% (83(5), which covers principles, lawful bases and rights).
- **Dates:** the GDPR has applied since 25 May 2018 (Art. 99).
- **Pending reform:** the "Digital Omnibus" proposal (2025/0360(COD), Nov 2025) would amend the GDPR. On the European Parliament's Legislative Observatory, its status is **"Awaiting committee decision"** (fetched 2026-10-19: <https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0360(COD)>). **The GDPR text is unchanged.**
- **With the AI Act:** the GDPR applies in parallel. AI Act Art. 2(7), as amended, says the AI Act does not affect the GDPR, except for the new Art. 4a, which allows special-category data to be processed for bias detection.

## 18. EU AI Act

| Kind | Title | Source/author | URL | Length | Checked |
|---|---|---|---|---|---|
| Lit | Regulation (EU) 2024/1689 (AI Act), EN, OJ L, 12.7.2024. ELI `eli/reg/2024/1689/oj`; EUR-Lex was not fetchable. This is the **original** text; no consolidated version was fetched. | EU Publications Office | <http://publications.europa.eu/resource/cellar/dc8116a1-3fe6-11ef-865a-01aa75ed71a1.0006.03/DOC_1> | 113 articles + 13 annexes | 2026-10-19 |
| FR | Règlement (UE) 2024/1689, FR | EU Publications Office | <http://publications.europa.eu/resource/cellar/dc8116a1-3fe6-11ef-865a-01aa75ed71a1.0009.03/DOC_1> | reference | 2026-10-19 |
| Lit | **Regulation (EU) 2026/1744, "Digital Omnibus on AI"**, of 8 Jul 2026, OJ L 24.7.2026, amending 2024/1689 | EU Publications Office | <http://publications.europa.eu/resource/cellar/b459c07f-86fb-11f1-bf5e-01aa75ed71a1.0006.03/DOC_1> | 4 articles, 43 amending points | 2026-10-19 |
| FR | Règlement (UE) 2026/1744 (omnibus IA), FR | EU Publications Office | <http://publications.europa.eu/resource/cellar/b459c07f-86fb-11f1-bf5e-01aa75ed71a1.0009.03/DOC_1> | reference | 2026-10-19 |
| Text | AI Act: the Commission's policy page, updated for the omnibus | European Commission | <https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai> | ~2,700 words, ~13 min | 2026-10-19 |
| FR | Législation sur l'IA (FR version of the same page) | European Commission | <https://digital-strategy.ec.europa.eu/fr/policies/regulatory-framework-ai> | ~3,700 words, ~18 min | 2026-10-19 |
| Text | Timeline for the Implementation of the EU AI Act ("takes into account the … Digital Omnibus on AI") | AI Act Service Desk | <https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act> | ~300 words, ~2 min | 2026-10-19 |
| Text | AI Act Service Desk / Single Information Platform (AI Act Explorer, Compliance Checker) | European Commission | <https://ai-act-service-desk.ec.europa.eu/en> | hub | 2026-10-19 |
| Text | AI Omnibus enters into force (news, 27 Jul 2026) | European Commission | <https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force> | ~450 words, ~2 min | 2026-10-19 |
| Text | Guidelines on transparency obligations (Art. 50) | European Commission | <https://digital-strategy.ec.europa.eu/en/policies/guidelines-transparency-ai-generated-content> (redirects to `/guidelines-ai-transparency-obligations`) | ~600 words, ~3 min plus PDF | 2026-10-19 |
| Text | Code of Practice on Transparency of AI-generated Content: voluntary, about 190 signatories by end of July 2026 | European Commission | <https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content> | ~1,200 words, ~6 min | 2026-10-19 |
| Text | AI Literacy – Questions & Answers. The omnibus status of the page was not checked. | European Commission | <https://digital-strategy.ec.europa.eu/en/faqs/ai-literacy-questions-answers> | ~5,700 words, ~28 min | 2026-10-19 |
| Text | Guidelines on obligations for GPAI providers (FAQ) | European Commission | <https://digital-strategy.ec.europa.eu/en/faqs/guidelines-obligations-general-purpose-ai-providers> | ~3,000 words, ~15 min | 2026-10-19 |
| Text | The General-Purpose AI Code of Practice | European Commission | <https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai> | ~750 words, ~4 min | 2026-10-19 |
| Text | European AI Office | European Commission | <https://digital-strategy.ec.europa.eu/en/policies/ai-office> | ~1,500 words, ~7 min | 2026-10-19 |
| FR | Entrée en vigueur du règlement européen sur l'IA : les premières questions-réponses de la CNIL. "Mis à jour le 17 août 2026" to include the omnibus. | CNIL | <https://www.cnil.fr/fr/entree-en-vigueur-du-reglement-europeen-sur-lia-les-premieres-questions-reponses-de-la-cnil> | ~3,800 words, ~19 min | 2026-10-19 |
| Video | How You'll Know When It's AI (Art. 50, from 2 Aug 2026) | European Commission | <https://www.youtube.com/watch?v=0Xtd8vhytuo> | 1:05 | 2026-10-19 |
| Video | DIGITAL EXPLORERS – Europe's AI Act (risk tiers) | DigitalEU (Commission) | <https://www.youtube.com/watch?v=pxYrbU0BLYg> | 2:15 | 2026-10-19 |
| Video | How the Digital Omnibus is reshaping the EU AI Act (unofficial) | HelloDPO | <https://www.youtube.com/watch?v=q-7IoeJw4aw> | 27:00 | 2026-10-19 |
| Video (FR) | AI Omnibus & AI Act : nouvelles obligations de transparence et échéances 2026 (consultancy) | DPO Consulting | <https://www.youtube.com/watch?v=xja-qOFDAyY> | 64:44 (**over 60**) | 2026-10-19 |

### Current status (2026-10-19), from official sources

- **The omnibus was adopted and is in force.**
  - The Commission proposed it on 19 Nov 2025. Political agreement came on **7 May 2026** (Commission AI Act page).
  - It was adopted as **Regulation (EU) 2026/1744 of 8 July 2026** and published in OJ L on 24.7.2026. It entered into force on **27 July 2026**: its Art. 4 says "third day following … publication", and the Commission news item confirms the date.
- **High-risk obligations are postponed, not removed.** The new Art. 113(c) applies Chapter III, Sections 1–3:
  - from **2 Dec 2027** for Annex III use cases;
  - from **2 Aug 2028** for Annex I products. This replaces the original 2 Aug 2026 and 2 Aug 2027 dates.

| Date | What applies | Source |
|---|---|---|
| 1 Aug 2024 | Entry into force (20th day after OJ publication on 12 Jul 2024) | Art. 113; Commission page |
| 2 Feb 2025 | Chapters I–II: definitions, **AI literacy (Art. 4)**, **prohibitions (Art. 5)**, practices 1–8 | Art. 113(a) |
| 2 Aug 2025 | GPAI model obligations (Chapter V), governance, penalties chapter (Art. 101 excepted) | Art. 113(b) |
| 2 Aug 2026 | General application. **Transparency (Art. 50)** applies; enforcement starts at national and EU level for GPAI, prohibitions, transparency and AI literacy. | Art. 113; Service Desk timeline |
| 2 Dec 2026 | New prohibitions on non-consensual sexual deepfakes and CSAM (Art. 5(1)(ba), (bb)). Art. 50(2) deadline for generative systems placed on the market before 2 Aug 2026 (new Art. 111(4)). | Reg. 2026/1744 pts (7), (39), (40) |
| 2 Aug 2027 | GPAI models placed on the market before 2 Aug 2025 must comply (Art. 111(3)). At least one regulatory sandbox per Member State. | Art. 111(3); Service Desk |
| 2 Dec 2027 | High-risk rules for **Annex III** systems | new Art. 113(c)(i) |
| 2 Aug 2028 | High-risk rules for **Annex I** (product-embedded) systems | new Art. 113(c)(ii) |

### Facts for the one-pager

**Risk tiers**
- **Prohibited (Art. 5):** eight practices have applied since 2 Feb 2025. The omnibus adds a ninth group, (ba) and (bb), from 2 Dec 2026. Commission guidelines on prohibited practices exist.
- **High-risk:**
  - Classification is in Art. 6: (1) safety components of products under Annex I law; (2) the use-case areas listed in Annex III.
  - The Annex III areas are biometrics, critical infrastructure, education, **employment and workers' management**, **access to essential private/public services** (e.g. credit), law enforcement, migration/asylum/border, and justice and democratic processes.
  - The requirements are Art. 8–15. Provider obligations start at Art. 16; deployer obligations are in Art. 26 (use per instructions, human oversight, input data, monitoring, logs for at least 6 months, informing workers and affected persons).
- **Limited risk, i.e. transparency (Art. 50):**
  - (1) Providers must design systems that interact with people so those people are told they are dealing with AI, unless that is obvious.
  - (2) Providers of systems that generate synthetic audio, image, video or text must mark outputs in a machine-readable, detectable way.
  - (3) Deployers of emotion recognition or biometric categorisation must inform the people exposed.
  - (4) Deployers must disclose deepfakes, and AI-generated text published to inform the public on matters of public interest. The text case does not apply where a human reviews it under editorial responsibility.
  - (5) The information must be given at the latest at the first interaction.
  - Only 50(7), on codes of practice, was amended by the omnibus.
- **Minimal risk:** the AI Act adds no rules. The Commission says the "vast majority" of systems fall here.

**Roles**
- **Provider (Art. 3(3)):** develops an AI system or GPAI model, or has one developed, and places it on the market or puts it into service under its own name or trademark.
- **Deployer (Art. 3(4)):** uses an AI system under its authority, outside personal non-professional use.
- **Becoming a provider (Art. 25(1)):** a deployer or other third party becomes the provider of a *high-risk* system if it puts its name or trademark on it, makes a substantial modification, or changes the intended purpose so that the system becomes high-risk.

**GPAI**
- **Obligations:** the duties in Art. 53 fall on providers of the *model* (technical documentation, information for downstream providers, copyright policy, training-content summary). Systemic risk is presumed above 10^25 FLOP (Art. 51(2)). GPAI Code of Practice: July 2025.
- **Commission guidelines:** a model is indicatively GPAI above 10^23 FLOP. A downstream modifier becomes a GPAI provider **only if the modification uses more than one-third of the original model's training compute**.

**AI literacy (Art. 4)**
- **Original wording:** "take measures to ensure, to their best extent, a sufficient level of AI literacy".
- **As replaced by 2026/1744:** providers and deployers "shall take measures to support the development of AI literacy" of staff and others operating AI on their behalf. "This obligation does not require … guarantee any specific level of AI literacy of any individual." The Commission and Member States must support this, especially for SMEs.

**Penalties (Art. 99)**
- **Ceilings:** up to €35M or 7% for Art. 5 breaches. Up to €15M or 3% for other operator obligations, including deployers under Art. 26 and transparency under Art. 50. Up to €7.5M or 1% for misleading information.
- **SMEs and start-ups:** the lower of the two amounts applies (Art. 99(6)). The omnibus extends this to small mid-caps (SMCs) for 99(4)–(5).

**Other omnibus changes**
- SME measures extended to SMCs.
- New Art. 4a on special-category data for bias detection.
- Registration of exempted systems in the EU database simplified (Commission news).
- AI Office enforcement powers detailed (new Art. 75a–75d).

### What applies today to a small French B2B company that deploys third-party LLMs

This section is inferred from the sources above. It is not legal advice.

1. **Role.** Calling an LLM API inside our own product, sold under our name, most likely makes us the **provider of an AI system** that integrates a GPAI model, and also a **deployer** when we use AI internally. We are **not a GPAI model provider** unless a fine-tune uses more than a third of the original training compute.
2. **In force now:**
   - Art. 4 AI literacy, in its lighter omnibus wording.
   - Art. 5 prohibitions: check that no use case falls in.
   - **Art. 50** since 2 Aug 2026:
     - tell users they are interacting with AI where that is not obvious (50(1));
     - mark generated content in machine-readable form (50(2)), with a deadline of 2 Dec 2026 if the system was on the market before 2 Aug 2026;
     - as a deployer, disclose deepfakes and public-interest text (50(4)).
3. **High-risk only if the intended purpose falls in Annex III**, for example HR screening, creditworthiness or education scoring. Those obligations start on 2 Dec 2027. Art. 6(3) excludes some narrow or preparatory Annex III uses. Art. 25 can turn us into a high-risk provider if we change a system's purpose.
4. **GDPR in parallel** (§17):
   - a DPA under Art. 28 with the LLM vendor;
   - transfer safeguards (Chapter V);
   - a DPIA where Art. 35 is triggered;
   - transparency (Art. 13–14).

---

## Gaps

- **EUR-Lex was not fetchable** (AWS WAF challenge). The official texts were verified through the Publications Office cellar instead. No consolidated AI Act text (2024/1689 as amended by 2026/1744) was fetched; consolidation was not checked.
- **iso.org returned 403** (Cloudflare) for ISO/IEC 25010 and 42001. Only third-party overviews and the IEC Webstore abstract are cited.
- **Cavoukian's 7 principles:** the IPC Ontario original is gone (404/403). The IETF-hosted PDF fetched, but its text could not be extracted (no PDF tooling installed), so its content is unverified. Wikipedia was used for the list.
- **No suitable video found** for:
  - an example-mapping talk by Matt Wynne himself;
  - parallel change / expand–contract by a recognised author;
  - ADRs by Nygard or the MADR authors;
  - SDD by Böckeler or Thoughtworks;
  - an official NIST talk;
  - an official CNIL talk on GDPR or AI;
  - an official, current, French AI Act video (one may exist on the Commission channel; not checked).
- **Over 30 min**, with no shorter equivalent picked: Feature Toggles (39 min), Graça (40 min), the CNIL AI recommendations (43–50 min), the CNIL developer guide (read by fiche).
- **OWASP LLM Top 10 2026** is newer than most training material. No video covering the 2026 edition was found.
- The **AI literacy Q&A** page was not checked for omnibus updates.

## Unverified

- The ISO/IEC 25010:2023 characteristic names beyond the first four.
- The page count of the DDD Reference (~60 pp).
- The date of the Threat Modeling Manifesto (2020).
- The 2011 revision of Cavoukian's paper.
- That *Hexagonal Architecture Explained* (2024) exists as described.
- The video topics flagged "inferred" in the tables: Sam Newman covering the strangler fig, IBM covering the LLM Top 10 2025 edition, the identity of the "Den" channel, Strumpflohner's Nx affiliation.
- That "Hidden Context Exposure" replaces "System Prompt Leakage" in the LLM Top 10 2026.
- The role classification and the "what applies today" reading for our company. These are interpretation, not an official source.
- The GDPR Digital Omnibus is still in committee. Its final content and timing are unknown, and nothing was checked beyond the procedure status on the Legislative Observatory.
