* **Use Case ID:** UC-B2B-02
* **Level:** Sea-Level (User Goal)
* **Primary Actor:** Sales Development Representative (SDR)
* **Scope:** HubSpot CRM SaaS
* **Stakeholders & Interests:**
  * *Sales Leadership:* Requires accurate deal attribution and pipeline visibility.
  * *Account Executives (AEs):* Need clean account history and deduplicated corporate entities.
  * *Marketing Ops:* Needs closed-loop reporting to credit original acquisition campaigns.
* **Preconditions:**
  1. The target Lead record exists in an active pipeline and meets the qualification threshold (e.g., SQL status).
  2. Actor has edit permissions on Leads and create permissions on Contacts, Companies, and Deals.
* **Success Guarantees (Postconditions):**
  1. The Lead record is flagged as `Converted` and locked from conflicting outbound SDR cadences.
  2. A verified Contact is established and associated with a new or matched Company record.
  3. A new Deal record is created in the designated sales pipeline with an assigned quota owner and monetary value.
  4. Full historical activity (emails, calls, meeting notes) is migrated to the associated Deal and Account timelines.
* **Trigger:** An SDR qualifies a prospect during an intake discovery call and transitions ownership to an AE.

**Main Success Scenario (MSS):**
1. Actor initiates the conversion of a qualified Lead record.
2. System analyzes the Lead’s domain and corporate parameters against existing CRM Company records to detect duplicates.
3. System confirms that no duplicate company exists and drafts a unified Company and Contact profile.
4. Actor specifies the target Deal pipeline stage, anticipated close date, estimated deal value, and the assigned Account Executive.
5. System verifies that all pipeline-specific mandatory deal fields are satisfied.
6. System converts the Lead, creates the new Deal, associates Contact/Company/Deal entities, and reassigns ownership to the designated AE.
7. System broadcasts an internal notification to the receiving AE containing the deal context and discovery summary.

**Extensions (Alternate & Failure Paths):**
* **2a. System detects one or more existing Company records matching the corporate domain:**
  * 2a1. System presents the existing candidate Company profiles alongside matching confidence scores.
  * 2a2. Actor selects an existing Company record to merge with instead of generating a duplicate.
  * 2a3. System associates the new Contact and Deal with the identified existing Company and resumes at Step 4.
* **5a. Pipeline stage requires mandatory deal properties that are empty on the Lead record:**
  * 5a1. System highlights the missing attributes (e.g., "Expected Seat Count", "Contract Term").
  * 5a2. Actor populates the required fields.
  * 5a3. System returns to Step 5.
* **6a. The assigned Account Executive’s seat is currently suspended or reassigned:**
  * 6a1. System halts assignment and prompts for a valid active pipeline owner.
  * 6a2. Actor selects an active owner or defaults to the Team Lead queue.
