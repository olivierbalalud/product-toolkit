* **Use Case ID:** UC-B2C-03
* **Level:** Sea-Level (User Goal)
* **Primary Actor:** Language Learner (Free or Super Duolingo subscriber)
* **Scope:** Duolingo Gamification & Habit Loop Platform
* **Stakeholders & Interests:**
  * *Learner:* Values streak continuity as a psychological motivator and personal investment.
  * *Product Retention Team:* Wants to balance forgiving occasional lapses with preserving streak credibility to drive daily app return rates.
* **Preconditions:**
  1. Actor’s daily learning streak has broken due to failing to complete a lesson before midnight in their registered local timezone.
  2. The lapse occurred within the permissible recovery grace period (less than 48 hours elapsed since lapse).
* **Success Guarantees (Postconditions):**
  1. The numeric streak counter is restored to its pre-lapse cumulative integer value.
  2. The redemption currency (Gems/Lingots) is deducted, a pre-equipped "Streak Freeze" is consumed, or a repair challenge is marked completed.
  3. The learner’s public profile and leaderboard display reflect the active streak status.
* **Trigger:** The learner opens the application after missing a calendar day and encounters the broken streak notification.

**Main Success Scenario (MSS):**
1. System presents the broken streak state to the Actor along with eligible recovery options based on account tier and inventory.
2. Actor elects to recover the streak using an eligible recovery method (e.g., redeeming in-app currency or using a Super Duolingo monthly perk).
3. System validates that the Actor possesses sufficient virtual currency or an available subscription privilege.
4. System executes the transaction, decrementing the required balance.
5. System updates the streak data model, restoring the consecutive day count and clearing the lapsed flag for the target calendar date.
6. System displays the restored streak milestone animation and transitions the Actor to their current course path.

**Extensions (Alternate & Failure Paths):**
* **1a. The streak broke outside the permissible recovery grace period (> 48 hours):**
  * 1a1. System informs the Actor that the streak cannot be restored.
  * 1a2. System encourages the Actor to start a new Day 1 streak today with a motivational benchmark.
  * 1a3. Use Case ends in failure of the recovery goal.
* **2a. Actor chooses to recover the streak via a "Streak Repair Practice Session":**
  * 2a1. System launches an accelerated review session covering recent weak vocabulary/grammar items.
  * 2a2. Actor completes the practice lesson with an accuracy score above the passing threshold (e.g., $\ge 80\%$).
  * 2a3. System records the successful practice and resumes at Step 5.
  * *Sub-extension 2a2a (Actor abandons or fails the review lesson):*
    * 2a2a1. System preserves the broken state and allows the Actor to retry the lesson or choose a currency redemption path.
* **3a. Actor possesses insufficient virtual currency (Gems) to fund the redemption:**
  * 3a1. System notifies the Actor of the currency deficit.
  * 3a2. System offers the Actor the choice to purchase a top-up gem pack, take a repair practice lesson, or accept the streak reset.
