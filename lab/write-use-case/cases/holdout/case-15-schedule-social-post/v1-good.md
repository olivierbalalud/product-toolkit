* **Use Case ID:** UC-B2C-02
* **Level:** Sea-Level (User Goal)
* **Primary Actor:** Content Creator / Small Business Owner (Canva Pro/Teams subscriber)
* **Scope:** Canva Web/Mobile SaaS (Content Planner & Publishing Engine)
* **Stakeholders & Interests:**
  * *Creator:* Needs posts published unattended at specific target times across multiple networks without formatting corruption.
  * *Social Media Networks (Instagram, LinkedIn, X):* Require compliance with API rate limits, supported image aspect ratios, and media size restrictions.
* **Preconditions:**
  1. The user has an active Canva Pro or Enterprise subscription.
  2. Actor has pre-authenticated target social media accounts via OAuth with valid publishing tokens.
* **Success Guarantees (Postconditions):**
  1. The graphical design is rendered into platform-compliant formats (e.g., JPEG 1:1, PNG 16:9).
  2. The post is queued in the Canva Content Planner for the designated release timestamps.
  3. Third-party platform scheduler APIs confirm scheduled payload registration (or receive the direct publish payload upon trigger).
* **Trigger:** The creator finishes a promotional graphic and needs it published during peak engagement hours while offline.

**Main Success Scenario (MSS):**
1. Actor initiates the schedule flow for a completed multi-page design.
2. Actor selects target social channels (e.g., Instagram Business, LinkedIn Company Page) and sets the publishing date and time.
3. System compares the design's dimensions against the publishing guidelines of each chosen network.
4. Actor inputs platform-specific captions, tags, and relevant hashtags.
5. System validates that captions adhere to platform character limits and hashtag restrictions.
6. Actor confirms the schedule.
7. System renders the design assets, locks the post in the visual Content Calendar, and arms the automated publishing worker.

**Extensions (Alternate & Failure Paths):**
* **2a. An authorized social channel’s OAuth refresh token has expired or been revoked:**
  * 2a1. System alerts the Actor that the connection to the specific platform is inactive.
  * 2a2. System routes the Actor through a non-destructive OAuth re-authentication flow.
  * 2a3. System returns to Step 2 upon successful re-authorization.
* **3a. The design dimensions or file sizes exceed a platform’s publishing limits (e.g., Instagram rejecting multi-page PDFs or non-standard aspect ratios):**
  * 3a1. System notifies the Actor of the incompatible media format.
  * 3a2. System offers an automated "Magic Resize & Format" option tailored to the platform.
  * 3a3. Actor accepts the automated conversion or selects alternative compliant pages.
* **5a. Caption exceeds character limits for one of the channels (e.g., X's character limit):**
  * 5a1. System flags the specific channel's caption field and displays the excess character count.
  * 5a2. Actor edits the channel's caption to comply while leaving other channel captions intact.
