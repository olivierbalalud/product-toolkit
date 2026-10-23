# Questions for the product owner: Order a meal

1. Who places the order, and what do you call them?
2. What exactly is the system under design, and where does its boundary stop?
3. Is the goal one meal order for one date, finished in a single sitting?
4. What must already be true before the Patron starts (logged in, registered for payroll deduction)?
5. Which outside systems or people does the ordering call on or inform?
6. How many people order, how often, and at what times of day?
7. Which related tasks (changing or cancelling an order, registering for payroll) are separate use cases?
8. Who else has a stake in an order, and what does each of them need protected?
9. What must be true however an attempt ends, and what is true once an order is accepted?
10. Which date is used if the Patron doesn't pick one?
11. What does a date's menu contain?
12. How long are delivery windows, and are full windows still offered?
13. Is pickup offered as an alternative to delivery, and when?
14. Does the Patron choose delivery or pickup before or after seeing the total?
15. What does delivery require (window, location, payment method), and what does pickup require?
16. What does the summary list?
17. Which is the usual case: delivery or pickup?
18. Can the Patron order several of the same item?
19. After seeing the summary, can the Patron go back and change or add to the order?
20. When can a date not be ordered for?
21. What if the Patron asks for more of an item than the cafeteria can supply?
22. What if every delivery window is full?
23. Are there items that can't be delivered, and what happens if one is in a delivery order?
24. Who is allowed to order delivery, and who may order at all?
25. What if a window fills up or an item runs out between being shown and the order going through?
26. What if the inventory system doesn't answer, or reserves only some items?
27. What if the cutoff passes while the Patron is still ordering?
28. What happens when the Patron cancels or walks away?
29. Does any system step make the Patron wait more than a second?
30. What if notifying the cafeteria staff fails after the order is accepted?
31. Can a Patron ask to export or erase their order history, and is that handled here?
