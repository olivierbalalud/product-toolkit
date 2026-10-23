**Q1.** First, the boundary. Who is the primary actor (I'd say a marketer or social media manager working in the design tool), and is the scope the design and scheduling product, with each social network (reached through the account connection the user set up) as a supporting actor? I'd also end the use case once the posts are stored in the publishing calendar, with the actual publication at the chosen time as its own time-triggered use case. Agreed?

**A1.** Not quite. The primary actor is a **content creator**, typically a small business owner on one of our paid plans, not a marketer or social media manager. The system is our online design service's content planner and publishing part, and the social networks do take part: the creator may have to reconnect an account with them, and the networks that accept scheduled posts register the post on their side. The connection is set up before the creator starts, so it's a precondition rather than a step in the use case.

Ending the use case once the post is in the content calendar, with publication at the chosen time as a separate, time-triggered use case, matches what we intend. Scheduling only succeeds once each network that accepts scheduled posts has confirmed it, so that confirmation comes before the end point.

**Q2.** Stakeholders. Besides the content creator (wants the post out on every chosen network at the chosen time, looking right on each), I see: the creator's audience/followers on each network (get a post that fits the network), and our company (only paid plans can schedule; we stay within each network's rules so connections aren't revoked). Who would you add or drop, and is there anyone off-stage, e.g. whoever answers for personal data in the captions or connected accounts?

**A2.** - **Keep the content creator and the social networks.** Both are stakeholders with stated guarantees.
- **Creator's audience/followers:** Not decided: whether followers are a stakeholder. Use your recommendation.
- **Our company:** Not decided: whether the company is a stakeholder in its own right. Use your recommendation. Paid plans are a precondition, since the creator already has scheduling before they start, but this use case does no permission check. The networks' rate limits, aspect ratios and size limits are their own requirements.
- **Personal data:** The personal data here is the creator's account and connected social accounts. Exporting or erasing it is handled by the service's general account privacy process, not by this use case.
- **Owner of that privacy process:** Not decided: who owns it. Use your recommendation.
- **Personal data in captions:** Not decided: who answers for it. Use your recommendation.

**Q3.** Guarantees. I'd write: minimal guarantee = no network is left with a scheduled post that the content calendar doesn't show, and the design itself is never changed; success guarantee = the post is in the content calendar for each chosen network at the chosen time, each network that accepts scheduled posts has confirmed it, and the others will be published by our service at that time. What are the networks' stated interests, and does that match your guarantees?

**A3.** **Networks' stated interests:** their rate limits, supported aspect ratios, and media size limits are respected.

**Does your draft match?** Mostly.

- **Minimal guarantee:** The design is never altered by scheduling, so that part matches. "No network left with a scheduled post the calendar doesn't show" is consistent with our rule that nothing counts as scheduled on a channel unless it was rendered for that channel and the channel accepted it. Cancelling leaves nothing scheduled. The facts don't state it in those words, so you may want to say it that way.
- **Success guarantee:** Yes, with one correction. Success means the post is in the content calendar at the chosen time on each chosen channel. Each network that accepts scheduled posts has confirmed it, and we publish the rest at that time. The rate limits, aspect ratios, and size limits are covered because each channel is rendered for its own format and must accept the post. Rate limits are only covered in the failure case, where a network refuses because the account has hit its posting limit. Partial failure is allowed: the post stays on the channels that worked, and the creator is told which ones failed.

**Q4.** Main scenario. I'd rewrite it as: 1. (actor) The creator chooses a finished design to schedule. 2. (actor) The creator chooses the channels and the publication time. 3. (system, wait) The system checks the design against each channel's media rules and each account connection, and presents each channel's caption rules. 4. (actor) The creator writes a caption and tags for each channel (the caption checks become failures of this step, not a step of their own). 5. (system, wait) The system renders the design in each channel's format, sends the post to each network that accepts scheduled posts, records it in the content calendar and confirms which channels it is scheduled on. Are those durations right (a few seconds each, the creator waiting), and is anything missing, such as a default for the time or one caption reused across channels?

**A4.** - **Durations:** Not quite. Checking the connections and the design against the guidelines is instant, and so is the caption check, so step 3 is not a wait. Rendering and registering after confirmation takes a few seconds, and the creator waits for that. Step 5 is right.
- **Missing confirmation:** Your rewrite has no step where the creator confirms the schedule. They explicitly confirm before anything is rendered or registered, so that step is needed between 4 and 5.
- **Merging steps 1 and 2:** The design, the channels and the date and time are chosen together, up front, so they belong in one step.
- **Default time:** Not decided: default for the time. Use your recommendation.
- **Caption reuse:** Each channel has its own caption, and editing one never changes another. Not decided: whether one caption can be copied to the other channels. Use your recommendation.
- **Networks:** Only networks that accept scheduled posts register the post on their side. For the others, we hold the post and send it when the time comes. Step 5 should say that.

**Q5.** Thanks. Steps now: 1. (actor) The creator chooses a finished design, the channels and the publication date and time. 2. (system) The system checks the design against each channel's media rules and each account connection, and presents each channel's caption rules. 3. (actor) The creator writes a caption and tags for each channel. 4. (actor) The creator confirms the schedule. 5. (system, wait) The system renders, registers with the networks that accept scheduled posts, holds the post for the others, records it in the content calendar and confirms. Now what can go wrong at the creator's steps. I see: at step 1, a time in the past; the design not meeting a channel's aspect ratio or size limit; a channel whose account connection has expired and must be reconnected; the same design already scheduled on that channel at that time; at step 3, a caption or tags over a channel's limits; and at steps 1 to 4, the creator giving up before confirming. What would you add or drop?

**A5.** **Drop:** the same design already scheduled on that channel at that time. We don't treat it as a duplicate. Scheduling it again is allowed, and reposting is the creator's call.

**Add:**
- **Time passes before confirmation.** The time can be in the past when they confirm, not only when they pick it. Nothing is scheduled, the system asks for a future time, and their captions are kept.
- **Channel fails at scheduling time (after step 4).** The design can't be rendered for a channel, the network doesn't answer, or the network refuses because the account hit its posting limit. The post is still scheduled on the other channels. The system says which channels failed and why, and the creator either retries those or drops them.

**Broaden:** the design-fit item also covers format and page count, not only aspect ratio and file size. The system names the network and the problem, then offers to resize and reformat a copy for that network (the original is untouched) or lets the creator pick other pages that comply.

**Keep:** expired or revoked connection (the system walks them through reconnecting, and keeps their channels and time), caption or hashtags over a limit (only that channel's caption is fixed), and giving up before confirming (nothing is scheduled, the design is untouched).

Not decided: whether the system shows each channel's caption rules at step 2. Use your recommendation.

**Q6.** At the system steps: step 2 is instant and only checks stored facts, so I see nothing that can fail there beyond what we key to step 1. At step 5 I have one condition: a channel can't be rendered, its network doesn't answer, or the network refuses because the account hit its posting limit, handled as you said. Is there anything else at step 5, for example the design being changed or deleted between confirmation and rendering, or a connection that expires between step 2 and step 5? My recommendation is no: nothing else.

**A6.** Yes, there are two more things to settle at step 5, though the first is already covered:

- **Design edited between confirmation and rendering:** Covered. We render the design as it is when they confirm, so later edits don't change what gets scheduled.
- **Design deleted between confirmation and rendering:** Not decided. Use your recommendation.
- **Connection expiring between step 2 and step 5:** Not decided. We only contact the networks at scheduling, so the expiry would surface there, but what happens then isn't specified. Use your recommendation.

Your three channel-failure conditions match what we agreed.

**Q7.** Handling for the creator-side conditions, where they return. I'd do: (a) a time in the past at step 1: the system asks for a future time, keeping the design and channels; back to step 1. (b) design doesn't fit a channel: the resized/reformatted copy or other compliant pages, then back to step 2; or the creator drops that channel and goes on. (c) expired or revoked connection: after reconnecting, back to step 2 with channels and time kept; if the creator can't or won't reconnect, they drop that channel or stop. (d) caption or tags over a limit: back to step 3 for that channel only. (e) time passed before confirming: the creator gives a future time, captions kept, back to step 4. (f) giving up at steps 1 to 4: nothing scheduled, design untouched, the use case ends. Correct?

**A7.** Mostly yes, with these gaps:

- **(a)** Yes, nothing is scheduled, the system asks for a future time, and the captions are kept. Not decided: whether the design and channels are kept. Use your recommendation.
- **(b)** Yes for the resized or reformatted copy (the original is untouched) or other compliant pages, followed by a full re-check. Not decided: whether the creator can drop that channel and carry on. Use your recommendation.
- **(c)** Yes. Reconnecting keeps the channels and time, and if they don't reconnect, they take that channel off and carry on. Walking away instead ends with nothing scheduled and the design untouched.
- **(d)** Yes. Only the flagged channel's caption is fixed, and the others stay as they were.
- **(e)** Yes. The system asks for a future time and keeps the captions. Not decided: whether the flow returns to step 4 specifically. Use your recommendation.
- **(f)** Yes for nothing scheduled and the design untouched. Not decided: whether the use case ends at that point. Use your recommendation.

**Q8.** Step 5 failures: I'd write that the post stays scheduled on the channels that worked, the system says which channels failed and why, and the creator either retries those channels (reconnecting first when the reason is an expired connection), which returns to step 5 for them only, or drops them, which ends the use case with the post scheduled on the rest. If every channel failed, dropping them all ends with nothing scheduled. Correct?

**A8.** Mostly yes, with two corrections:

- **Reconnecting:** Scheduling-time failures are a render failure, a network that doesn't answer, or a posting limit. An expired connection isn't one of them, so drop the reconnect clause from step 5.
- **Retry:** Not decided: whether a retry returns to step 5 for those channels only. Use your recommendation.

The rest holds. The post stays scheduled on the channels that worked, the system says which failed and why, and dropping the failed channels keeps the post on the rest. If every channel fails, nothing is scheduled, since a channel only counts as scheduled once it has been rendered and accepted.

**Q9.** Last one: how often does this happen? I'd guess a creator schedules a few posts a week, across two or three channels each. Is there a figure you know?

**A9.** Yes, it happens a few times a week per creator. The number of channels per post is not decided. Use your recommendation.

