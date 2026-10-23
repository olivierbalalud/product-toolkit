# Answers: schedule a social media post

## Actor, goal and scope

- The person doing this is a content creator, typically a small business owner on one of our paid plans.
- The system is our online design service, specifically its content planner and publishing part.
- They start because they've finished a promotional design and want it to go out at peak engagement hours, when they won't be online.
- Before they start, they're on a plan that includes scheduling and have already connected their social network accounts to the service.
- The social networks take part: the creator may have to reconnect an account with them, and the ones that accept scheduled posts register the post on their side.
- They can schedule the whole design or only some of its pages.
- Some networks hold the scheduled post and publish it themselves; for the others, we hold it and send it to the network when the time comes.
- It happens a few times a week per creator.
- Actually publishing the post at the chosen time is a separate thing that runs later on its own, not part of scheduling it.

## Stakeholders and guarantees

- The creator wants the posts to go out unattended at the chosen times on several networks, without the design's formatting getting mangled.
- The social networks want their rate limits, supported aspect ratios and media size limits respected.
- Nothing counts as scheduled on a channel unless the design was rendered for that channel and the channel accepted it.
- The original design is never altered by scheduling.
- Editing the caption for one channel never touches the caption for another.
- If they cancel or give up, nothing is scheduled.
- When it works: the design is rendered in a format each network accepts, the post with each channel's caption, tags and hashtags sits in the content calendar at its date and time, and each network that takes scheduled posts has confirmed it.
- After that, they can follow each post's status in the content calendar, and they get a notification when it's published or if publishing fails.
- Their personal data here is their account and connected social accounts; exporting or erasing that is handled by the service's general account privacy process, not here.

## Main scenario

- The design, the channels and the date and time are all chosen together, up front.
- Checking the connections and checking the design against each network's guidelines happen together, right after that choice.
- The guidelines that matter are each network's supported aspect ratios, formats, page counts and file sizes.
- The caption check covers each network's character limit and its hashtag restrictions.
- The creator explicitly confirms the schedule before anything is rendered or registered.
- After confirming, the system renders, registers the post with the networks that accept scheduled posts, puts it in the content calendar and tells the creator it's scheduled.

## What can go wrong

- The design doesn't fit a network's guidelines: wrong aspect ratio, a format or page count it doesn't take, or a file that's too big.
- The publishing time isn't in the future, either when they pick it or because it has passed by the time they confirm.
- The connection to one of the chosen accounts has expired or been revoked.
- A caption is over a network's character limit or breaks its hashtag rules.
- They cancel or walk away before confirming.
- When we go to schedule, a channel fails: the design can't be rendered for it, the network doesn't answer, or the network refuses because the account has hit its posting limit.

## How each is handled

- Design doesn't fit: the system says which network and what's wrong, and offers to resize and reformat it automatically for that network. They accept, which makes a copy for that network and leaves the original alone, or they pick other pages that do comply. Then everything is checked again.
- Time not in the future: nothing is scheduled, the system asks for a future time, and the captions they've written are kept.
- Expired or revoked connection: the system says which channel is affected and walks them through reconnecting it with the network, without losing the channels and time they've set. If they don't reconnect, they take that channel off the post and carry on.
- Caption too long or bad hashtags: the system flags that channel's caption and shows how far over the limit it is; they fix that one caption and the others stay as they were.
- Cancelling or walking away before confirming: nothing is scheduled and the design is untouched.
- A channel fails at scheduling time: the post is still scheduled on the other channels, and the system says which ones failed and why. They can retry the failed ones, or drop them and keep the post on the channels that worked.

## Durations

- Checking the connections and the design against the guidelines is instant.
- The caption check is instant.
- Rendering and registering with the networks after they confirm takes a few seconds; they wait for the confirmation.

## Out of scope

- Scheduling the same design again: allowed, we don't treat it as a duplicate; reposting is the creator's call.
- Permissions: the plan already includes scheduling and the accounts are theirs, so there's no permission check here.
- The networks being down while we check connections: we use what we already know about each connection at that point and only talk to the networks when scheduling.
- Teammates editing the design while it's being scheduled: we render the design as it is when they confirm.
