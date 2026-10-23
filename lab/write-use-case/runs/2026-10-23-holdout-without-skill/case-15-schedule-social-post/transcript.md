**Q1.** Who is the primary actor (role), what system is this (scope), and what is their goal in one phrase? Also who else cares about the outcome (stakeholders)?

**A1.** **Primary actor:** A content creator, typically a small business owner on a paid plan.

**System (scope):** Our online design service, specifically its content planner and publishing part.

**Goal:** Get a finished promotional design posted at peak engagement hours, without being online at the time.

**Other stakeholders:** The social networks. They want their rate limits, supported aspect ratios, and media size limits respected.

**Q2.** What must already be true before this starts (e.g. social accounts connected, paid plan, a finished design)? And which social networks are supported?

**A2.** Before starting, the creator must be on a paid plan that includes scheduling, must have connected their social network accounts to the service, and must have a finished design.

Not decided: which social networks are supported. Use your recommendation.

**Q3.** At step 3, what happens if a connected account's authorization has expired or been revoked? Can the creator reconnect and continue, or is that channel dropped?

**A3.** The creator can reconnect and continue. The system names the affected channel and walks them through reconnecting it with the network, keeping the channels and time they've already set. If they don't reconnect, that channel is removed from the post and they carry on with the others.

**Q4.** At step 3, if the design's dimensions or file size don't fit a network's limits (e.g. wrong aspect ratio, too large), what should happen: auto-crop/resize, ask the creator, or block that channel?

**A4.** Neither exactly. The system tells the creator which network is affected and what's wrong, then offers to resize and reformat the design automatically for that network. (It's resize and reformat, not specifically crop.) If they accept, it makes a copy for that network and leaves the original alone. Alternatively, they can pick other pages that do comply. Either way, everything is checked again afterward. The channel isn't blocked outright.

**Q5.** What are the rules on the publication date and time: minimum lead time, maximum horizon, whose time zone, and what if the chosen time is in the past or already taken by another post?

**A5.** - **Minimum lead time:** Not decided: minimum lead time. Use your recommendation.
- **Maximum horizon:** Not decided: maximum horizon. Use your recommendation.
- **Whose time zone:** Not decided: whose time zone. Use your recommendation.
- **Time in the past:** The time must be in the future both when they pick it and when they confirm. If it isn't, nothing is scheduled, the system asks for a future time, and their captions are kept.
- **Time already taken by another post:** Not decided: clash with another post at the same time. Use your recommendation.

**Q6.** At step 5, when a caption or tags exceed a network's character or hashtag limits, what happens? Does the system truncate, or ask the creator to edit? Is there one shared caption with per-channel overrides?

**A6.** The system doesn't truncate. It flags that channel's caption and shows how far over the limit it is, and the creator fixes that caption. Each channel has its own caption, tags and hashtags, and editing one never changes another. Not decided: whether there is one shared caption that channels can override. Use your recommendation.

**Q7.** Step 6 renders the final images and queues them. How long does rendering take, does the creator wait, and what if rendering or saving fails for one channel but succeeds for others?

**A7.** It takes a few seconds, and the creator waits for the confirmation. If rendering or saving fails for one channel, the post stays scheduled on the other channels. The system says which channels failed and why, and the creator can retry the failed ones or drop them and keep the post on the channels that worked.

**Q8.** What happens if the creator is not on a plan that includes scheduling, or works in a team where they lack permission to publish to a connected account?

**A8.** **Not on a scheduling plan:** Not decided: what happens when the creator's plan doesn't include scheduling. Use your recommendation. This flow only starts for creators who are already on a plan that includes scheduling.

**Team without permission to publish:** There is no permission check in this flow. The plan already includes scheduling and the connected accounts are the creator's own, so nothing is blocked for lack of team permission.

**Q9.** Are there limits on how many posts can be scheduled (per plan, per network per day, rate limits)? What happens when one is hit?

**A9.** - **Per plan:** Not decided: a cap on how many posts a plan can schedule. Use your recommendation.
- **Per network per day:** Not decided: a daily posting limit for each network. Use your recommendation.
- **Rate limits:** Not decided: the specific limits. We must respect each network's rate limits, but the values aren't set here. Use your recommendation.
- **When one is hit:** If a network refuses because the account has reached its posting limit, that channel fails at scheduling time. The post stays scheduled on the other channels, and the system says which channel failed and why. The creator can retry the failed channel or drop it and keep the post on the channels that worked.

**Q10.** If the design is edited after it's scheduled, or someone else edits it while the creator is scheduling it, which version gets posted? And if the creator abandons midway, is a draft kept?

**A10.** - **Teammate edits during scheduling:** the design is rendered as it is when the creator confirms, so that version is posted.
- **Edits after it's scheduled:** Not decided: which version gets posted when the design is edited after scheduling. Use your recommendation.
- **Abandoning midway:** nothing is scheduled and the design is untouched.
- **Draft kept:** Not decided: whether a draft is kept when the creator abandons midway. Use your recommendation.

**Q11.** If a social network is unreachable or slow when the system checks the connection (step 3) or commits the post (step 6), what should happen?

**A11.** **Step 3 (connection check):** The system doesn't contact the network at this point. It uses what it already knows about each connection, so an unreachable or slow network doesn't affect this check.

**Step 6 (commit):** The network failing to answer makes that channel fail. The post stays scheduled on the other channels, and the system says which channels failed and why. The creator can retry the failed channels, or drop them and keep the post on the channels that worked.

**Q12.** If the creator schedules the same design to the same channel at the same time twice (e.g. double confirmation), what should happen? And can a design have several pages, with the creator choosing which pages to post?

**A12.** Yes, the same design can be scheduled again, and we don't treat it as a duplicate. Reposting is the creator's call, so a second confirmation for the same channel and time is allowed.

Yes, a design can have several pages, and the creator can schedule the whole design or only some of its pages.

**Q13.** How often does this happen (frequency), and does the scheduled post hold personal data that the creator could ask to export or erase? Is anything logged?

**A13.** - **Frequency:** A few times a week per creator.
- **Personal data:** The personal data involved is the creator's account and connected social accounts. Exporting or erasing it is handled by the service's general account privacy process, not by scheduling.
- **Logging:** Not decided: whether anything is logged. Use your recommendation.

**Q14.** If the design is deleted (e.g. by a teammate) before the creator confirms, what happens? And after scheduling succeeds, what does the creator see, and how do they learn later that the post went out or failed at publication time?

**A14.** Not decided: what happens if the design is deleted before they confirm. Use your recommendation.

After scheduling succeeds, the post sits in the content calendar at its chosen date and time, and each network that accepts scheduled posts has confirmed it. They can follow each post's status in the content calendar.

They learn that a post went out or failed at publication time through a notification.

