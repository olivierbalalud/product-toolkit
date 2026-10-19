# GDPR One-Pager

> **Not legal advice.** Last verified: 2026-10-19. Review every 6 months or when the regulation changes. Owned by the founders until a lawyer or DPO reviews it. [R12-Q7]

Part of [Foundations](README.md). The General Data Protection Regulation, Regulation (EU) 2016/679, has applied since 25 May 2018 (Art. 99). Article numbers below refer to its official text ([Sources](#10-sources)).

## 1. Key terms (Art. 4)

| Term | Meaning, in short |
|---|---|
| Personal data | Any information about an identified or identifiable person |
| Processing | Anything done with personal data: collecting, storing, using, sharing, deleting |
| Controller | Decides why and how data is processed, and is accountable for it (Art. 5(2), Art. 24) |
| Processor | Processes data on the controller's behalf, e.g. a cloud host or an LLM API vendor (inferred for our case) |

## 2. Principles (Art. 5)

| Principle (Art. 5(1)) | What it asks |
|---|---|
| (a) Lawfulness, fairness, transparency | A lawful basis, no hidden processing, people told what happens |
| (b) Purpose limitation | Collected for stated purposes, not reused for incompatible ones |
| (c) Data minimisation | Only what the purpose needs |
| (d) Accuracy | Kept correct and up to date |
| (e) Storage limitation | Kept no longer than needed |
| (f) Integrity and confidentiality | Appropriate security |
| **Accountability** (Art. 5(2)) | The controller must be able to *show* compliance |

## 3. Lawful bases (Art. 6(1))

Every processing needs one: (a) consent (conditions in Art. 7), (b) contract, (c) legal obligation, (d) vital interests, (e) public task, (f) legitimate interests. Special categories of data (health, beliefs and others) have stricter rules (Art. 9).

## 4. Rights of the people concerned

| Right | Article |
|---|---|
| Information when data is collected | Art. 12–14 |
| Access | Art. 15 |
| Rectification | Art. 16 |
| Erasure | Art. 17 |
| Restriction | Art. 18 |
| Portability | Art. 20 |
| Objection | Art. 21 |
| Not to be subject to a decision based solely on automated processing, including profiling, with legal or similarly significant effects | Art. 22 (relevant to LLM features that decide about people) |

A request must be answered **without undue delay and within one month**, extendable by two further months for complex or numerous requests (Art. 12(3)).

## 5. Obligations on the company

| Obligation | Article | In short |
|---|---|---|
| Data protection by design and by default | Art. 25 | Build privacy in; protective defaults |
| Security of processing | Art. 32 | Appropriate technical and organisational measures |
| Processors | Art. 28 | Only processors with sufficient guarantees; a contract with the mandatory content (28(3)); sub-processors need prior written authorisation (28(2)) |
| Records of processing | Art. 30 | Kept by controllers and processors. The exemption below 250 employees (30(5)) does **not** apply when processing is likely to be risky, is not occasional, or involves special categories |
| Breach notification | Art. 33–34 | Notify the supervisory authority without undue delay and, where feasible, within **72 hours**, unless the breach is unlikely to be a risk; inform the people concerned when the risk is high |
| Data protection impact assessment (DPIA; French *AIPD*) | Art. 35 | Required when processing using new technologies is likely to be high-risk, in particular systematic automated evaluation including profiling (35(3)(a)); authorities publish lists (35(4)) |
| Data protection officer | Art. 37 | Required in some cases |
| Transfers outside the EEA | Art. 44–49 | Adequacy decisions (Art. 45; the US is covered for organisations in the EU-US Data Privacy Framework), appropriate safeguards such as standard contractual clauses or binding corporate rules (Art. 46–47), or narrow derogations (Art. 49) |

**Fines (Art. 83):** up to €10M or 2% of worldwide annual turnover (83(4)); up to €20M or 4% for breaches of the principles, lawful bases and rights (83(5)).

## 6. Cookies and analytics trackers (French law, alongside the GDPR)

Reading or storing trackers on a user's device (cookies, local storage, SDK identifiers) is governed by **Article 82 of the French *loi Informatique et Libertés***, which transposes the ePrivacy Directive. It needs **consent**, except for trackers that are strictly necessary. The CNIL exempts **audience measurement** from consent only if it ([CNIL, 4 July 2025](https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies-solutions-pour-les-outils-de-mesure-daudience)):

- serves only to measure the audience of the site or app, for the publisher alone;
- produces anonymous statistics only;
- is not cross-referenced with other processing, and passes no non-anonymous data to third parties;
- does not track a person across sites or apps.

The CNIL also recommends informing users, a tracker lifetime of about 13 months without automatic renewal, and keeping the collected data for at most 25 months.

## 7. Pending change

A "Digital Omnibus" proposal (procedure 2025/0360(COD), November 2025) would amend the GDPR. On 2026-10-19 the European Parliament's Legislative Observatory showed it as **"Awaiting committee decision"**. **The GDPR text is unchanged.** The AI Act applies alongside the GDPR and does not affect it, except for its new Art. 4a on processing special-category data for bias detection (see the [AI Act one-pager](ai-act-one-pager.md)).

## 8. What this means for our framework

| GDPR requirement | Where the framework handles it |
|---|---|
| Purpose, minimisation, storage limitation (Art. 5) | PRD §11 privacy data inventory: data, where, purpose, legal basis, retention, shown to ([`prd.md`](../templates/prd.md)) [R2-Q3 (k)] |
| Lawful basis (Art. 6) | The *Legal basis* column of PRD §11 |
| By design and by default (Art. 25) | The inventory is a Design-complete item, written before any code [R2-Q3 (k)]; see [privacy by design](security-privacy-ai.md#17-privacy-by-design) |
| Access control, security (Art. 32) | PRD §10 *Who may perform each action* → the authorisation test matrix [R4-Q9] |
| Erasure, retention, minimal responses | Privacy tests derived from §11: retention, erasure and pseudonymisation, no personal data in logs, responses limited to their purpose ([chapter 8](../guide/08-testing.md#85-security-and-privacy-tests)) [R4-Q9] |
| Analytics trackers (Art. 82 LIL) | Each event in the tracking plan declares `consent: exempt \| required`; `exempt` only when it meets every CNIL condition above, checked by the privacy reviewer; `required` events are sent only after consent ([`tracking-plan.md`](../templates/tracking-plan.md)) [R21-Q1] |
| Analytics | Every event property carries a privacy class; `personal` needs a reason in the PRD's inventory and is flagged by the privacy reviewer ([`tracking-plan.md`](../templates/tracking-plan.md)) [R4-Q4c, R9-Q2] |
| Processors and transfers (Art. 28, 44–49) | PRD §11b *AI use* names the model provider and the data sent to it [R12-Q6a]; the contract and transfer basis are checked outside the framework |
| DPIA (Art. 35) | Not a framework gate; whether one is needed is decided outside the framework. The PRD's §11 inventory is the main input to it. |
| Ongoing review | The GDPR/CNIL privacy review skill in the security lane ([chapter 9](../guide/09-review-lanes.md), [chapter 12](../guide/12-skills-to-build.md)) [R4-Q7a] |

## 9. Learn more

- [Data protection explained](https://commission.europa.eu/law/law-topic/data-protection/data-protection-explained_en) (European Commission, ~6 min).
- [GDPR Developer's Guide](https://lincnil.github.io/GDPR-Developer-Guide/) (CNIL, English; may lag the French version) and the authoritative [Guide RGPD de l'équipe de développement](https://lincnil.github.io/Guide-RGPD-du-developpeur/) (CNIL, French; read by fiche).
- [Comprendre le RGPD](https://www.cnil.fr/fr/comprendre-le-rgpd) (CNIL, ~2 min) and [L'analyse d'impact relative à la protection des données (AIPD)](https://www.cnil.fr/fr/RGPD-analyse-impact-protection-des-donnees-aipd) (CNIL, ~2 min).
- Video: [Overview of GDPR, cybersecurity and ePrivacy](https://www.youtube.com/watch?v=AeffByaxbDE) (Wojciech Wiewiórowski, EDPS, 16:29; about nine years old). French: [RGPD pour les développeurs](https://www.youtube.com/watch?v=wkbQ6Ec4qXY) (François Delbrayelle, DevFest Lille 2022, 54:19; not CNIL).

## 10. Sources

- Regulation (EU) 2016/679, official text: [English](http://publications.europa.eu/resource/cellar/3e485e15-11bd-11e6-ba9a-01aa75ed71a1.0006.03/DOC_1), [French](http://publications.europa.eu/resource/cellar/3e485e15-11bd-11e6-ba9a-01aa75ed71a1.0009.03/DOC_1) (EU Publications Office; ELI `eli/reg/2016/679/oj` on EUR-Lex).
- [Adequacy decisions](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en) and [Standard Contractual Clauses](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en) (European Commission).
- [Procedure 2025/0360(COD)](https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2025/0360(COD)) (European Parliament, Legislative Observatory).
- [Guide RGPD du développeur](https://www.cnil.fr/fr/guide-rgpd-du-developpeur) (CNIL).
- [Cookies : solutions pour les outils de mesure d'audience](https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies-solutions-pour-les-outils-de-mesure-daudience) (CNIL, 4 July 2025).
