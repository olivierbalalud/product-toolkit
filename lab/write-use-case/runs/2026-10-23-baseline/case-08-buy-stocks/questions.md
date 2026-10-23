# Questions for the product owner (UC-008)

1. What exactly is the system under design, and is the brokerage inside or outside it?
2. Who is the person buying, and what prompts them to start?
3. What must already be true before they start (for example, signed in to the app)?
4. Which outside parties take part, and what does each one do?
5. Can they use any brokerage, or only ones the app supports?
6. How does the app connect to a brokerage: an embedded session, an API, or both?
7. How often does a user buy stocks this way?
8. Is following up on a purchase that isn't confirmed yet part of this use case or a separate one?
9. What does each stakeholder (buyer, brokerage, your team) need protected or achieved?
10. What must be true however the purchase ends, and what is true when it succeeds?
11. Does the buyer name the brokerage when asking to buy, or in a later step?
12. Why must the app keep control of the brokerage session?
13. Do logging, updating the portfolio and showing it happen together once the confirmation arrives?
14. What happens if they name a brokerage the app doesn't support?
15. What happens if the connection to the brokerage can't be set up?
16. What happens if they give up before buying, before connecting or while at the brokerage?
17. What happens if their device crashes or is switched off in the middle of the purchase?
18. What happens if the brokerage doesn't confirm the purchase right away and puts it off?
19. What happens if the brokerage's confirmation lacks details you need, such as the price?
20. Who checks that the order itself is valid, and who checks the buyer may trade at the brokerage?
21. How long does opening the brokerage session take, and how long does recording the confirmation take?
22. Can the buyer ask to export or erase the holdings data this use case handles, and is that in scope here?
23. What is this use case's priority?
