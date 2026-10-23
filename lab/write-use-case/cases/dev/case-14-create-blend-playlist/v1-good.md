* **Use Case ID:** UC-B2C-01
* **Level:** Sea-Level (User Goal)
* **Primary Actor:** Spotify Consumer (Free or Premium subscriber)
* **Scope:** Spotify Mobile/Desktop SaaS Client & Recommendation Engine
* **Stakeholders & Interests:**
  * *Invited Friend:* Expects mutual musical preferences represented fairly without exposing private listening habits.
  * *Content Licensing / Artists:* Requires stream counts to route appropriately across individual user playback sessions.
* **Preconditions:**
  1. Actor has an active Spotify account with at least 30 days of active listening data.
  2. Actor has an authorized internet connection capable of transmitting deep links.
* **Success Guarantees (Postconditions):**
  1. A persistent, auto-updating "Blend" playlist is generated containing a balanced synthesis of both users' catalog tastes.
  2. A unique Taste Match percentage and shared discovery cards are generated.
  3. The playlist is saved to the music libraries of both participants.
* **Trigger:** Actor wants a unified, self-updating music mix shared with a specific friend.

**Main Success Scenario (MSS):**
1. Actor initiates the creation of a new collaborative Blend.
2. System generates a secure, one-time invitation link with an embedded time-to-live (TTL) expiration window (e.g., 48 hours).
3. Actor shares the invitation link with a recipient via external messaging or social channels.
4. Recipient opens the link, authenticating their own Spotify account, and accepts the collaboration invite.
5. System evaluates the distinct listening histories, favorite genres, and recurring artists of both users.
6. System compiles a balanced 50-track playlist and calculates an algorithmic "Taste Match" score with overlapping artist highlights.
7. System adds the Blend playlist to both users' libraries and schedules an automated daily track refresh.

**Extensions (Alternate & Failure Paths):**
* **4a. The invitation link expires or has already been accepted by another user:**
  * 4a1. System notifies the recipient that the invitation is no longer valid.
  * 4a2. System prompts the original Actor with an option to generate a fresh invite link.
* **5a. Either user has insufficient listening history (e.g., brand-new account < 7 days old):**
  * 5a1. System falls back to a curated taste-onboarding questionnaire for the new account or substitutes broad genre preferences.
  * 5a2. System informs both users that the Blend will refine its selections as listening history develops.
* **6a. Regional catalog licensing restrictions prevent certain tracks from being accessible to one user:**
  * 6a1. System omits country-restricted tracks from the mutual playlist, substituting an alternative high-affinity track available in both territories.
