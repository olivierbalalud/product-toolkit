---
id: UC-010
title: Convert a qualified lead
status: Draft
driver: lab
priority:
source_locale: en
inputs: []
stories: []
---

# UC-010: Convert a qualified lead

| Field | Value |
|---|---|
| **Primary actor** | Sales Development Representative (SDR) |
| **Supporting actors** | Account Executive (receives the deal and is notified of it) |
| **Scope** | CRM service |
| **Level** | User goal |
| **Trigger** | A discovery call qualifies the prospect, and the SDR decides to hand the lead over to an Account Executive. |
| **Preconditions** | The lead is in an active pipeline with sales-qualified status; the SDR may edit leads and create contacts, companies and deals. |
| **Minimal guarantees** | The lead is never half-converted: either it is converted with its contact, company and deal all created and associated, or it stays unconverted and nothing is created from it. |
| **Success guarantees** | The lead is marked converted and locked out of SDR outreach cadences; a contact exists, associated with a new or matched company; a new deal is in the chosen pipeline stage with its value, close date and owner (the receiving Account Executive or the team lead queue), and carries the lead's original campaign attribution; the lead's activity history (emails, calls, meeting notes) is on the deal and company timelines; the owner is notified with the deal context and the discovery summary. |

## Stakeholders and interests

| Stakeholder | Interest |
|---|---|
| SDR | Hands the lead over in one go, without retyping what the lead already holds. |
| Sales leadership | Deals are attributed accurately and the pipeline shows every deal with its value and owner. |
| Account Executives | Receive a clean account history and no duplicate companies; know at once that a deal is theirs. |
| Marketing operations | Closed-loop reporting credits the campaign that first brought the lead in. |

## Main success scenario

1. (actor) The SDR asks to convert the qualified lead.
2. (system) The system matches the lead's corporate domain and company details against existing companies (BR-1), finds no duplicate, and presents the new company and contact it drafted from the lead.
3. (actor) The SDR gives the deal's pipeline stage, expected close date and estimated value, and chooses the receiving Account Executive.
4. (system, wait) The system verifies the stage's mandatory deal properties (BR-2) and the owner (BR-3); marks the lead converted and locks it out of SDR outreach cadences (BR-4); creates the contact, the company and the deal with the lead's campaign attribution, and associates them; moves the lead's activity history to the deal and company timelines; assigns the deal to the Account Executive; and notifies the Account Executive with the deal context and the discovery summary.

## Failure-category check

**Actor steps**

| Step | Invalid input | Duplicate | No permission | Cancel / abandon |
|---|---|---|---|---|
| 1 | n/a | yes: UC-010.2a | n/a | yes: UC-010.1-3a |
| 3 | yes: UC-010.3a, UC-010.3b | n/a | n/a | yes: UC-010.1-3a |

**System steps**

| Step | Not found | Conflict / concurrent edit | Timeout / external down | Partial failure | Quota / limit | Stale data | Cancel / abandon |
|---|---|---|---|---|---|---|---|
| 2 | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| 4 | n/a | out-of-scope: until it is converted, a lead is worked only by its owning SDR, so no one else converts or edits it at the same time | n/a | yes: UC-010.4a | n/a | n/a | n/a |

**Privacy request:** yes: `deferred`, the use case handles the prospect's contact details and call notes; exporting or erasing a contact's personal data is its own use case, not part of a conversion.

## Extensions

- **UC-010.1-3a** The SDR cancels or abandons the conversion before submitting it:
  1. The system discards the drafted company, contact and deal details; the lead stays unconverted and nothing is created.
  2. The use case ends.

  *Example:* Maya starts converting the Brightwell Logistics lead, is pulled into another call and never comes back; the lead is still unconverted and no deal exists.
- **UC-010.2a** One or more existing companies match the lead's corporate domain (BR-1):
  1. The system presents the matching companies, each with its match confidence.
  2. The SDR selects the existing company to use instead of creating a new one.
  3. The system will associate the new contact and the deal with that company: returns to step 3.

  *Example:* The lead's domain brightwell.example matches "Brightwell Logistics" at 95 % and "Brightwell Group" at 60 %; Maya selects Brightwell Logistics, and no second company is created.
- **UC-010.3a** The chosen pipeline stage requires deal properties that are empty (BR-2):
  1. The system names the missing properties and creates nothing.
  2. The SDR fills them in.
  3. Returns to step 4.

  *Example:* Maya puts the deal at the "Contract sent" stage, which requires an expected seat count and a contract term; the lead has neither, so she gives 40 seats and 12 months.
- **UC-010.3b** The chosen Account Executive's seat is suspended or reassigned (BR-3):
  1. The system creates nothing and asks for an active owner.
  2. The SDR chooses an active Account Executive, or the team lead queue.
  3. Returns to step 4.

  *Example:* Maya chooses Tom Okafor, whose seat is suspended during his leave; she assigns the deal to the Enterprise team lead queue instead.
- **UC-010.4a** The conversion cannot be completed in full:
  1. The system undoes what it created, leaves the lead unconverted, keeps the SDR's deal details, and says the conversion did not go through.
  2. The SDR tries again: returns to step 4. Or the SDR stops: the use case ends.

  *Example:* Maya submits the Brightwell Logistics conversion; the contact is created but the deal is not, so the system removes the contact, and her retry a minute later succeeds.

## Technology and data variations

- None

## Related information

- **Frequency:** several times a week per SDR, after each discovery call that qualifies a prospect.
- **Business rules:** BR-1 companies are matched on the corporate domain and company details, so the same company is not created twice (step 2, UC-010.2a) · BR-2 each pipeline stage has mandatory deal properties; a deal cannot be created at that stage while any of them is empty (step 4, UC-010.3a) · BR-3 a deal's owner is an active Account Executive seat or the team lead queue (step 4, UC-010.3b) · BR-4 a converted lead is locked out of SDR outreach cadences (step 4).
- **Open issues:** None
