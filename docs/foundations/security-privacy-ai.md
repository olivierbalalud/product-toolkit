# Security, Privacy and AI

Part of [Foundations](README.md). The concepts behind the framework's security and privacy tests, its threat check, and its checks on AI features. The legal side is summarised in the [GDPR one-pager](gdpr-one-pager.md) and the [AI Act one-pager](ai-act-one-pager.md). Decision IDs in brackets point to [`../grilling-log.md`](../grilling-log.md).

Every link was checked on 2026-10-19 ([sources](../research/foundations-sources-eng-legal.md)). Reading times assume 200 words per minute.

| Concept | SWE | PM | UX | Time |
|---|---|---|---|---|
| [OWASP ASVS](#owasp-asvs) | core | optional | — | ~55 min |
| [Threat modelling: STRIDE and the four questions](#threat-modelling-stride-and-the-four-questions) | core | optional | optional | ~40 min |
| [OWASP Top 10 for LLM Applications](#owasp-top-10-for-llm-applications) | core | optional | optional | ~45 min |
| [OWASP agentic AI and the AI Exchange](#owasp-agentic-ai-and-the-ai-exchange) | optional | optional | — | ~60 min |
| [AI risk and governance](#ai-risk-and-governance) | optional | core | optional | ~30 min |
| [Responsible AI: oversight and transparency](#responsible-ai-oversight-and-transparency) | core | core | core | ~15 min |
| [Privacy by design](#privacy-by-design) | core | core | optional | ~40 min |

---

### OWASP ASVS

**Roles:** SWE core · PM optional   **Time:** ~55 min (text + video)

**Definition.** The OWASP Application Security Verification Standard is a catalogue of testable security requirements for web applications and services, grouped by area (authentication, access control, input handling and so on) and by level. Level 1 is the baseline every application should meet. The current stable release is 5.0.0 (May 2025).

**Why it matters.**
- SWE: it turns "make it secure" into a list of checks a slice can pass or fail.
- PM: it gives a shared, external definition of "secure enough" for a B2B buyer's security questionnaire.

**In this framework.** Every slice tests the ASVS level 1 items relevant to it, alongside the authorisation matrix and the privacy tests ([chapter 8, §8.5](../guide/08-testing.md#85-security-and-privacy-tests)) [R4-Q9]. The security and privacy review lane checks that these tests exist ([chapter 9](../guide/09-review-lanes.md)) [R4-Q7a].

**Key literature.** OWASP, *Application Security Verification Standard 5.0.0* (2025).

**Learn it.** Text: [ASVS project page](https://owasp.org/www-project-application-security-verification-standard/) (OWASP, ~3 min) and [ASVS repository README](https://github.com/OWASP/ASVS) (OWASP, ~6 min). Video: [What's New in ASVS V5](https://www.youtube.com/watch?v=SHSpUsVmDLA) (NDC Security 2026, 45:29).

---

### Threat modelling: STRIDE and the four questions

**Roles:** SWE core · PM optional · UX optional   **Time:** ~40 min (text + video)

**Definition.** Threat modelling is a structured look at a design to find what can go wrong before it is built. Adam Shostack frames it as four questions: *What are we working on? What can go wrong? What are we going to do about it? Did we do a good job?* STRIDE, from Microsoft, is a checklist for the second question: **S**poofing, **T**ampering, **R**epudiation, **I**nformation disclosure, **D**enial of service, **E**levation of privilege.

**Why it matters.**
- SWE: tests only check the threats someone thought of; threat modelling is how they get thought of.
- PM and UX: some answers to "what can go wrong" change the flow (confirmation steps, rate limits, what is shown to whom).

**In this framework.** For a PRD that adds an endpoint, a data store or a third party, the Eng persona review includes a short STRIDE-style threat check before Design-complete [R11-Q12]. When a PRD sends user or third-party content to an LLM, the check covers **prompt injection** [R12-Q6c] (see [the next entry](#owasp-top-10-for-llm-applications)). See [chapter 1, §1.5](../guide/01-lifecycle-and-gates.md#15-exploring--design-complete) and [chapter 3, §3.10](../guide/03-design-playbook.md#310-step-9-prepare-the-gate).

**Key literature.** Adam Shostack, *Threat Modeling: Designing for Security* (2014).

**Learn it.** Text: [The Ultimate Beginner's Guide to Threat Modeling](https://shostack.org/resources/threat-modeling) (Shostack + Associates, ~20 min); for STRIDE, [Microsoft Threat Modeling Tool: Threats](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats) (Microsoft Learn, ~3 min); optional, [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) (OWASP, ~12 min). Video: [Threat Modeling and the Four Question Framework](https://www.youtube.com/watch?v=-OBgxD_Zhdw) (Adam Shostack, CyberRisk TV, 17:18).

---

### OWASP Top 10 for LLM Applications

**Roles:** SWE core · PM optional · UX optional   **Time:** ~45 min (text + video)

**Definition.** A ranked list of the most critical security risks specific to applications built on large language models, maintained by the OWASP GenAI Security Project. The 2026 edition (3 August 2026) lists: LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Excessive Agency, LLM04 Supply Chain, LLM05 Data and Model Poisoning, LLM06 Unbounded Consumption, LLM07 Misinformation, LLM08 Hidden Context Exposure, LLM09 Vector and Embedding Weaknesses, LLM10 Improper Output Handling.

**Why it matters.**
- SWE: an LLM treats every piece of text it reads as possible instructions, so classic input validation does not cover it.
- PM: misinformation and unbounded consumption are product and cost risks as much as security ones.
- UX: how model output is shown (as a suggestion, with sources, editable) is part of the mitigation.

**In this framework.** Slices that touch the LLM gateway or AI features are reviewed against this list by a reviewer in the security lane ([`review-lanes.yaml`](../templates/review-lanes.yaml)) [R12-Q6b]. The Eng threat check covers prompt injection at design time [R12-Q6c]. The PRD's §11b *AI use* records whether user or third-party content reaches a model ([`prd.md`](../templates/prd.md)) [R12-Q6a].

**Key literature.** OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2026* (2026).

**Learn it.** Text: [the 2026 edition](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) (OWASP, PDF; read LLM01, LLM02 and LLM10 first, ~15 min); the per-risk pages of the [2025 list](https://genai.owasp.org/llm-top-10/) are shorter (OWASP, ~5 min per risk). Video: [OWASP's Top 10 Ways to Attack LLMs](https://www.youtube.com/watch?v=gUNXZMcd2jU) (IBM Technology, 25:11). No video covers the 2026 edition yet; this one likely follows 2025.

---

### OWASP agentic AI and the AI Exchange

**Roles:** SWE optional · PM optional   **Time:** ~60 min (text + video)

**Definition.** The *OWASP Top 10 for Agentic Applications 2026* (December 2025) covers risks that appear when an LLM can plan and act through tools: ASI01 Agent Goal Hijack, ASI02 Tool Misuse and Exploitation, ASI03 Identity and Privilege Abuse, ASI04 Agentic Supply Chain Vulnerabilities, ASI05 Unexpected Code Execution, ASI06 Memory & Context Poisoning, ASI07 Insecure Inter-Agent Communication, ASI08 Cascading Failures, ASI09 Human-Agent Trust Exploitation, ASI10 Rogue Agents. The **OWASP AI Exchange** is a large, free body of AI security guidance that also feeds the AI Act standards.

**Why it matters.**
- SWE: the team develops with coding agents, plugins and MCP servers; supply chain, tool misuse and code execution apply to our own tooling, not only to the product.
- PM: agentic features in the product would bring these risks to customers.

**In this framework.** The plugin install policy (project scope, pinned by SHA, reviewed hooks and shell commands, no skill that reads `.env` or calls third-party model APIs) is a supply-chain control for our own agents ([chapter 11](../guide/11-tooling-and-plugins.md)) [R3-B4]. External content read by our skills is treated as data, never instructions [R3-D2]. Product features that let a model act through tools fall under the LLM reviewer above [R12-Q6b].

**Key literature.** OWASP GenAI Security Project, *OWASP Top 10 for Agentic Applications for 2026* (2025); OWASP, *Agentic AI – Threats and Mitigations* v1.0 (2025).

**Learn it.** Text: [the agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) (OWASP, PDF) and the [OWASP AI Exchange](https://owaspai.org/) home page (OWASP, ~3 min). Video: [The OWASP AI Exchange in 3 minutes](https://www.youtube.com/watch?v=kQC7ouDB_z8) (Rob van der Veer, 3:01); deeper, [Deep Dive into the OWASP Top 10 for Agentic AI Applications](https://www.youtube.com/watch?v=-vXoC0UvpjY) (John Sotiropoulos, OWASP London, 52:23).

---

### AI risk and governance

**Roles:** PM optional · SWE optional · UX optional   **Time:** ~30 min (text + video)

**Definition.** AI governance is how an organisation decides which AI uses are acceptable, who is accountable, and how risks are found and managed over time. The NIST AI Risk Management Framework (2023) organises this into four functions, **Govern, Map, Measure, Manage**, and its Generative AI profile (2024) lists twelve risks specific to generative AI, such as confabulation, data privacy and information security. ISO/IEC 42001 (2023) is the certifiable management-system standard for AI, and the OECD AI Principles (2019, updated 2024) are the reference set of values.

**Why it matters.**
- PM: B2B customers increasingly ask how AI features are governed; a light, written answer is cheaper than an improvised one.
- SWE: the risks in the GenAI profile map onto concrete tests and review findings.

**In this framework.** The framework does not adopt a governance standard. Its governance is the per-PRD record in §11b *AI use* (model and provider, data sent, human oversight, transparency notice, AI Act risk category), checked at Design-complete [R12-Q6a], plus the review lanes. The legal obligations are in the [AI Act one-pager](ai-act-one-pager.md).

**Key literature.** NIST, *AI Risk Management Framework 1.0* (NIST AI 100-1, 2023); NIST, *Generative AI Profile* (NIST AI 600-1, 2024); ISO/IEC 42001:2023 (paid); OECD, *AI Principles* (2019, updated 2024).

**Learn it.** Text: [NIST AI RMF](https://airc.nist.gov/airmf-resources/airmf/) (NIST AI Resource Center, ~2 min), [NIST AI RMF landing page](https://www.nist.gov/itl/ai-risk-management-framework) (NIST, ~3 min) and [OECD AI Principles](https://oecd.ai/en/ai-principles) (OECD.AI, ~4 min). Video: [Demystifying the NIST AI Risk Management Framework](https://www.youtube.com/watch?v=eqKwuYCBlVE) (SANS Institute, 9:43) and [What is ISO/IEC 42001?](https://www.youtube.com/watch?v=O4iKEr5AIi4) (ISO, 9:54). French: [Les fiches pratiques IA](https://www.cnil.fr/fr/les-fiches-pratiques-ia) (CNIL, ~4 min).

---

### Responsible AI: oversight and transparency

**Roles:** SWE core · PM core · UX core   **Time:** ~15 min (text + video)

**Definition.** Responsible AI means designing AI features so people know when they are dealing with AI, can understand and contest what it produces, and a human stays accountable for decisions that matter. Two practices carry most of the weight in a product: **human oversight** (someone can check, correct or override the output) and **transparency** (users are told that AI is involved, at the latest at their first interaction).

**Why it matters.**
- PM: transparency is a legal obligation (AI Act Art. 50) and a trust argument with B2B buyers.
- UX: the notice, how output is labelled, and how a user corrects it are design work, with copy in the copy deck.
- SWE: oversight needs real mechanisms (review queues, edit and undo, logs), not only a disclaimer.

**In this framework.** PRD §11b *AI use* records the human oversight and the copy key of the transparency notice for every AI feature ([`prd.md`](../templates/prd.md)) [R12-Q6a]. Decisions about people taken by automated processing also touch GDPR Art. 22 (see the [GDPR one-pager](gdpr-one-pager.md)).

**Key literature.** OECD, *AI Principles* (2019, updated 2024); CNIL, *Recommendations on AI system development* (2025).

**Learn it.** Text: [OECD AI Principles](https://oecd.ai/en/ai-principles) (OECD.AI, ~4 min) and the European Commission's [Guidelines on transparency obligations](https://digital-strategy.ec.europa.eu/en/policies/guidelines-transparency-ai-generated-content) (European Commission, ~3 min). Video: [How You'll Know When It's AI](https://www.youtube.com/watch?v=0Xtd8vhytuo) (European Commission, 1:05). French: [IA et RGPD : la CNIL publie ses nouvelles recommandations](https://www.cnil.fr/fr/ia-et-rgpd-la-cnil-publie-ses-nouvelles-recommandations-pour-accompagner-une-innovation-responsable) (CNIL, ~7 min).

---

### Privacy by design

**Roles:** SWE optional · PM optional · UX optional   **Time:** ~40 min (text + video)

**Definition.** Privacy by design means building privacy into a system from the start rather than adding it later. Ann Cavoukian's seven principles are: proactive not reactive; privacy as the default; privacy embedded into design; full functionality (positive-sum, not zero-sum); end-to-end security; visibility and transparency; respect for user privacy. The GDPR makes "data protection by design and by default" a legal obligation (Art. 25).

**Why it matters.**
- PM: what data a feature collects, why and for how long is a product decision, made in the PRD.
- SWE: minimisation, retention and erasure are far cheaper to build in than to retrofit.
- UX: defaults (what is shared, what is visible to whom) are where privacy is won or lost.

**In this framework.** Every PRD has a privacy data inventory (§11: data, where, purpose, legal basis, retention, shown to), including analytics event properties with a privacy class (`none`, `pseudonymous`, `personal`) [R2-Q3 (k), R4-Q4c, R9-Q2]. The inventory becomes privacy tests: retention, erasure and pseudonymisation, no personal data in logs, responses limited to their purpose [R4-Q9]. A GDPR/CNIL privacy review runs in the security lane [R4-Q7a]. See [`prd.md`](../templates/prd.md), [`tracking-plan.md`](../templates/tracking-plan.md) and [chapter 8](../guide/08-testing.md).

**Key literature.** Ann Cavoukian, *Privacy by Design: The 7 Foundational Principles* (IPC Ontario, 2009); EDPB, *Guidelines 4/2019 on Article 25 Data Protection by Design and by Default* (2019).

**Learn it.** Text: [Privacy by design](https://en.wikipedia.org/wiki/Privacy_by_design) (Wikipedia; read the principles section, ~5 min; the original paper is no longer online) and the [EDPB Guidelines 4/2019](https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-42019-article-25-data-protection-design-and_en) (EDPB, landing page and PDF). Video: [Privacy by Design, Security by Design](https://www.youtube.com/watch?v=xqreZlGL8Dk) (Dr Ann Cavoukian, Information Security Forum, 33:40). French: [Guide RGPD de l'équipe de développement](https://lincnil.github.io/Guide-RGPD-du-developpeur/) (CNIL; read fiche 5 on architecture and fiche 7 on minimisation).
