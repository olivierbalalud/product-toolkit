# Answers: convert a qualified lead

## Actor, goal and scope

- The person converting is a Sales Development Representative, an SDR.
- The system is our CRM service.
- It starts when a discovery call has qualified the prospect and the SDR decides to hand the lead over to an Account Executive.
- Before they start, the lead is already in an active pipeline with sales-qualified status; qualifying it happens earlier, not here.
- The SDR already has the rights to edit leads and to create contacts, companies and deals; nobody without them gets this far.
- The Account Executive is the other person involved: they receive the deal and get notified about it. Nothing outside the CRM takes part.
- It happens several times a week per SDR, after each discovery call that qualifies a prospect.

## Stakeholders and guarantees

- The SDR wants to hand the lead over in one go, without retyping what the lead already holds.
- Sales leadership wants deals attributed accurately and wants to see every deal in the pipeline with its value and owner.
- Account Executives want a clean account history and no duplicate companies, and want to know straight away that a deal is now theirs.
- Marketing operations wants closed-loop reporting that credits the campaign that first brought the lead in, so the deal has to keep the lead's original campaign attribution.
- A conversion is all or nothing: either the lead is converted with contact, company and deal all created and linked, or the lead stays as it was and nothing is created from it.
- When it works: the lead is marked converted and taken out of the SDR outreach cadences so nobody keeps prospecting it; there's a contact linked to a new or existing company; there's a new deal in the chosen stage with its value, close date and owner; the lead's emails, calls and meeting notes show on the deal's and the company's timelines; and the owner has been notified.

## Main scenario

- Companies are matched on the corporate domain and the company details, so we never create the same company twice.
- When there's no match, the system shows the SDR the new company and contact it has drafted from the lead.
- Besides value, close date and Account Executive, the SDR picks the pipeline stage the deal starts at.
- Each pipeline stage has its own mandatory deal properties, and a deal can't be created at that stage while any of them is empty.
- A deal is owned by an Account Executive with an active seat, or by the team lead queue.
- Converting the lead, creating and linking the records, moving the history, reassigning ownership and notifying the Account Executive all happen together when the SDR submits.
- The notification to the Account Executive carries the deal context and the discovery summary.

## What can go wrong

- One or more existing companies match the lead's domain.
- The chosen stage needs deal properties that are still empty.
- The chosen Account Executive's seat is suspended or has been reassigned.
- The SDR cancels or walks away before submitting the conversion.
- The conversion fails partway, for example the contact gets created but the deal doesn't.

## How each is handled

- Matching companies: the system shows each candidate with how confident the match is, the SDR picks the existing company, and the contact and deal get attached to it instead of a new company; then they go on to the deal details.
- Missing mandatory properties: the system names what's missing and creates nothing; the SDR fills them in and submits again.
- Suspended or reassigned Account Executive: the system creates nothing and asks for an active owner; the SDR picks another active Account Executive or the team lead queue, and submits again.
- Cancelling or walking away: the drafts are thrown away, the lead stays unconverted and nothing is created.
- Partial failure: the system undoes whatever it created, leaves the lead unconverted, keeps what the SDR entered, and says the conversion didn't go through; the SDR can try again or stop.

## Durations

- Matching the company and drafting the company and contact is immediate.
- The conversion itself, with the checks, the new records, moving the history and the notification, takes a few seconds; the SDR waits for it.

## Out of scope

- Someone else converting or editing the same lead at the same moment: not handled; until it's converted, a lead is worked only by the SDR who owns it.
- Exporting or erasing the prospect's personal data: that's a separate job, not part of converting a lead.
