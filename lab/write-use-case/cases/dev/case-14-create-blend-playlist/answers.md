# Answers: create a Blend playlist

## Actor, goal and scope

- The person starting it is a listener on our music streaming service, on a free or a paid plan.
- The system is our music streaming service: the mobile and desktop apps and the recommendation engine behind them.
- They start because they want a shared mix that keeps itself up to date, with one specific friend.
- Before they start they're signed in. They don't need a minimum listening history to send an invitation; a new account with little history is dealt with when the mix is built.
- The friend usually opens the link some time later, often hours afterwards, and the listener doesn't sit and wait for it. Once the link is sent, the listener's part is done.
- The friend opening the link, accepting, and the mix being built and put in both libraries is the friend's own job, not part of sending the invitation. The daily refresh of the mix also runs on its own, separately.
- No outside system takes part in sending the invitation: the listener sends the link themselves, through whatever app they like. We don't integrate with those apps.
- They can send the link through a messaging app, post it on a social network, or copy it and paste it anywhere.
- It's occasional: a listener starts a mix like this a few times a year.

## Stakeholders and guarantees

- The listener wants a shared mix with a friend for no more effort than sending a message.
- The invited friend wants both tastes represented fairly, without their private listening habits being exposed.
- Artists and rights holders want the streams of the mix's tracks counted to each listener who plays them.
- However it ends, nothing is created and nothing of either person's listening history is shared until someone accepts the invitation.
- A link nobody accepts simply stops working when it expires.
- When it works: there's an invitation link that only one person can use, and the listener has sent it to their friend. What's still pending is the friend accepting.
- When the friend accepts, the mix is built and added to both libraries, and the listener gets a notification. If the link expires unused, there's no mix.
- Exporting or erasing someone's listening data and their mixes belongs to the account privacy work, not to this.

## Main scenario

- The system makes the link straight away and offers to share it.
- The link can be accepted once, by one person: whoever accepts first joins.
- The link expires 48 hours after it's made. That's our fixed window, not just an example.

## What can go wrong

- They make the link but never send it, or change their mind.

## How each is handled

- Link never sent: nothing to clean up. The link stays unused until it expires, no mix is created and nothing is shared.

## Durations

- Making the link is immediate.

## Out of scope

- Sending the same link to several people: we can't see where the link goes. Only the first person to accept joins, and anyone else who opens it afterwards is told it's no longer valid; that's handled on the friend's side.
- An expired or already-used link, an account with too little listening history, and tracks that aren't licensed in one of the two countries are all dealt with when the friend opens the link and the mix is built, not here.
- Losing the connection while the link is made: handled the same way everywhere in the app, nothing special here.
- Asking for an invitation again isn't a problem: a listener can have several invitations open at once, one per friend, and each request makes a new link.
- We don't cap how many mixes or open invitations a listener has.
- Free and paid listeners can both send invitations; nobody signed in is refused.
