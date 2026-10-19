# AI Act One-Pager

> **Not legal advice.** Last verified: 2026-10-19. Review every 6 months or when the regulation changes. Owned by the founders until a lawyer or DPO reviews it. [R12-Q7]

Part of [Foundations](README.md). The EU Artificial Intelligence Act is Regulation (EU) 2024/1689, **as amended by Regulation (EU) 2026/1744**, the "Digital Omnibus on AI" (adopted 8 July 2026, in force since 27 July 2026). Article numbers below refer to these texts ([Sources](#sources)). No consolidated text was checked.

## Roles

| Role | Definition | Article |
|---|---|---|
| **Provider** | Develops an AI system or a general-purpose AI (GPAI) model, or has one developed, and places it on the market or puts it into service under its own name or trademark | Art. 3(3) |
| **Deployer** | Uses an AI system under its authority, other than for personal non-professional use | Art. 3(4) |
| **Becoming a provider** | A deployer or other third party becomes the provider of a *high-risk* system if it puts its name on it, substantially modifies it, or changes its intended purpose so that it becomes high-risk | Art. 25(1) |
| **GPAI model provider** | Obligations on the *model* (documentation, information for downstream providers, copyright policy, training-content summary) | Art. 53 |

Under the Commission's GPAI guidelines, a company that modifies a model becomes a GPAI model provider only if the modification uses more than a third of the original model's training compute.

## Risk tiers

| Tier | What it covers | Obligations | Articles |
|---|---|---|---|
| **Prohibited** | Eight practices (e.g. manipulative techniques, social scoring), plus a ninth group added by the omnibus (non-consensual sexual deepfakes and child sexual abuse material) | Banned | Art. 5 |
| **High-risk** | Safety components of products under Annex I law, and the use-case areas in **Annex III**: biometrics, critical infrastructure, education, employment and workers' management, access to essential private and public services (e.g. credit), law enforcement, migration and border control, justice and democratic processes | Requirements in Art. 8–15; provider duties from Art. 16; deployer duties in Art. 26 (use as instructed, human oversight, input data, monitoring, logs kept at least 6 months, informing workers and affected people). Art. 6(3) excludes some narrow or preparatory Annex III uses. | Art. 6, Annex I, Annex III |
| **Limited risk (transparency)** | Systems that interact with people or generate content | Providers: tell people they are dealing with AI unless obvious (50(1)); mark generated audio, image, video or text in a machine-readable way (50(2)). Deployers: disclose deepfakes and AI-generated public-interest text (50(4)); inform people exposed to emotion recognition or biometric categorisation (50(3)). Information is due at the latest at the first interaction (50(5)). | Art. 50 |
| **Minimal risk** | Most systems | No new rules | — |

**Every provider and deployer** must take measures to support the AI literacy of staff and others operating AI on their behalf. In the omnibus wording this does not require guaranteeing any specific level of literacy (Art. 4).

## Timeline (as amended by Regulation (EU) 2026/1744)

| Date | What applies | Source |
|---|---|---|
| 1 Aug 2024 | Entry into force | Art. 113 |
| 2 Feb 2025 | Definitions, **AI literacy (Art. 4)**, **prohibitions (Art. 5)** | Art. 113(a) |
| 2 Aug 2025 | GPAI model obligations, governance, penalties | Art. 113(b) |
| 27 Jul 2026 | The omnibus enters into force | Reg. 2026/1744, Art. 4; Commission news |
| 2 Aug 2026 | General application: **transparency (Art. 50)**; enforcement starts for GPAI, prohibitions, transparency and AI literacy | Art. 113; AI Act Service Desk |
| 2 Dec 2026 | New prohibitions (Art. 5(1)(ba), (bb)); Art. 50(2) marking deadline for generative systems placed on the market before 2 Aug 2026 | Reg. 2026/1744; new Art. 111(4) |
| 2 Aug 2027 | GPAI models placed on the market before 2 Aug 2025 must comply | Art. 111(3) |
| **2 Dec 2027** | High-risk rules for **Annex III** systems (originally 2 Aug 2026) | New Art. 113(c)(i); Commission news |
| **2 Aug 2028** | High-risk rules for **Annex I** product-embedded systems (originally 2 Aug 2027) | New Art. 113(c)(ii); Commission news |

**Penalties (Art. 99):** up to €35M or 7% for prohibited practices; up to €15M or 3% for other operator obligations, including Art. 26 and Art. 50; up to €7.5M or 1% for misleading information. For SMEs and start-ups the lower amount applies (Art. 99(6)).

## What applies today to a small company deploying third-party LLMs in a B2B product

Our reading of the sources, not an official interpretation:

1. **Role.** Building an LLM API into our own product, sold under our name, most likely makes us the **provider of an AI system** that integrates a GPAI model, and a **deployer** of any AI we use internally. We are not a GPAI model provider unless a fine-tune crosses the one-third compute threshold.
2. **Already in force:**
   - **AI literacy** (Art. 4): support the AI literacy of the team.
   - **Prohibitions** (Art. 5): check that no feature falls in, including the new group from 2 Dec 2026.
   - **Transparency** (Art. 50), since 2 Aug 2026: tell users they are interacting with AI where it is not obvious (50(1)); mark generated content in machine-readable form (50(2)), with a 2 Dec 2026 deadline for systems already on the market before 2 Aug 2026; as a deployer, disclose deepfakes and public-interest text (50(4)).
3. **What would change the picture:** a feature whose intended purpose falls in an **Annex III** area, such as screening candidates, managing workers or assessing creditworthiness. It would then be high-risk, with obligations from **2 Dec 2027**. Changing the purpose of a third-party system can make us its high-risk provider (Art. 25).
4. **The GDPR applies in parallel:** a processor contract with the model vendor, a transfer basis, a DPIA where Art. 35 requires one, and information to users (see the [GDPR one-pager](gdpr-one-pager.md)).

## What this means for our framework

| AI Act topic | Where the framework handles it |
|---|---|
| Risk tier of each feature | PRD §11b *AI use* records the AI Act risk category: prohibited, high-risk, limited (transparency) or minimal ([`prd.md`](../templates/prd.md)) [R12-Q6a]. A PRD marked `prohibited` is stopped; one marked `high-risk` (e.g. an Annex III area) needs an ADR, informed by legal advice, before it can reach Design-complete, and the gate check enforces both ([chapter 1](../guide/01-lifecycle-and-gates.md)) [R14-Q1]. |
| Transparency (Art. 50) | §11b records the copy key of the user-facing notice, so it is designed, translated and tested like any other string [R12-Q6a] |
| Human oversight | §11b records who checks or can override the output [R12-Q6a]; see [responsible AI](security-privacy-ai.md#responsible-ai-oversight-and-transparency) |
| Security of AI features | The OWASP Top 10 for LLM Applications reviewer in the security lane, for slices touching the LLM gateway or AI features [R12-Q6b]; prompt injection in the Eng threat check [R12-Q6c] ([`review-lanes.yaml`](../templates/review-lanes.yaml)) |
| AI literacy (Art. 4) | Partly met by this Foundations folder: [responsible AI](security-privacy-ai.md#responsible-ai-oversight-and-transparency) and this one-pager are on every role's core reading path ([README](README.md#reading-paths)) |

## Learn more

- [AI Act policy page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) (European Commission, ~13 min; [French](https://digital-strategy.ec.europa.eu/fr/policies/regulatory-framework-ai)).
- [AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en) (European Commission), with the AI Act Explorer and a Compliance Checker.
- [Guidelines on transparency obligations](https://digital-strategy.ec.europa.eu/en/policies/guidelines-transparency-ai-generated-content) (European Commission, ~3 min) and [AI Literacy – Questions & Answers](https://digital-strategy.ec.europa.eu/en/faqs/ai-literacy-questions-answers) (European Commission, ~28 min; not checked for omnibus updates).
- [Entrée en vigueur du règlement européen sur l'IA : les premières questions-réponses de la CNIL](https://www.cnil.fr/fr/entree-en-vigueur-du-reglement-europeen-sur-lia-les-premieres-questions-reponses-de-la-cnil) (CNIL, French, updated 17 Aug 2026 for the omnibus, ~19 min).
- Videos: [DIGITAL EXPLORERS – Europe's AI Act](https://www.youtube.com/watch?v=pxYrbU0BLYg) (DigitalEU, 2:15), [How You'll Know When It's AI](https://www.youtube.com/watch?v=0Xtd8vhytuo) (European Commission, 1:05), and, unofficial, [How the Digital Omnibus is reshaping the EU AI Act](https://www.youtube.com/watch?v=q-7IoeJw4aw) (HelloDPO, 27:00).

## Sources

- Regulation (EU) 2024/1689, original text: [English](http://publications.europa.eu/resource/cellar/dc8116a1-3fe6-11ef-865a-01aa75ed71a1.0006.03/DOC_1), [French](http://publications.europa.eu/resource/cellar/dc8116a1-3fe6-11ef-865a-01aa75ed71a1.0009.03/DOC_1) (EU Publications Office; ELI `eli/reg/2024/1689/oj` on EUR-Lex).
- Regulation (EU) 2026/1744, Digital Omnibus on AI: [English](http://publications.europa.eu/resource/cellar/b459c07f-86fb-11f1-bf5e-01aa75ed71a1.0006.03/DOC_1), [French](http://publications.europa.eu/resource/cellar/b459c07f-86fb-11f1-bf5e-01aa75ed71a1.0009.03/DOC_1) (EU Publications Office).
- [AI Omnibus enters into force](https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force) (European Commission, 27 Jul 2026).
- [Timeline for the implementation of the EU AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) (AI Act Service Desk).
- [Guidelines on obligations for GPAI providers](https://digital-strategy.ec.europa.eu/en/faqs/guidelines-obligations-general-purpose-ai-providers) (European Commission).
