# Questions for the product owner: import contacts

1. What exactly is the system under design, and who is the primary actor?
2. What prompts the Marketing Manager to import contacts, and where does the list usually come from?
3. What must already be true before they start (signed in, permissions on the audience)?
4. Does any outside system or other person take part in the import?
5. In which formats can the contacts arrive: CSV, spreadsheet file, pasted rows, others?
6. How often does this happen per account?
7. What is out of scope: plan upgrades, sending a campaign, anything else?
8. What do the Manager, the contacts, the account owner and the deliverability team each need protected?
9. What must be true however the import ends, especially after a cancel or a failure?
10. What must be true when it succeeds, and what does the report contain?
11. What happens to the uploaded file afterwards, given it holds personal data?
12. What does the system show after reading the file: a sample, a proposed mapping?
13. How is a new contact told from an existing one?
14. Can the Manager choose whether existing contacts get updated, and can a blank cell overwrite a stored value?
15. How does the Manager state the contacts' consent, and what happens if consent is unknown or the list was purchased?
16. When are the contact limit and the new / existing / invalid counts checked: before the import, during it, or both?
17. When are new contacts tagged with the import's name: during the import or afterwards?
18. What makes a file unusable (format, encoding, empty, size), and is there a row limit per file?
19. How are malformed addresses, role addresses and repeated addresses handled?
20. What if no column can be recognised as the email address?
21. What happens if the import would exceed the plan's contact limit; is an upgrade offered?
22. What happens if the Manager gives up before starting, cancels during the import, or walks away without cancelling?
23. What happens if the service fails partway through the import?
24. How long does each step take: reading the file, the limit check, the import itself, the report?
25. Can the Manager ask to export or erase a contact's personal data as part of this?
