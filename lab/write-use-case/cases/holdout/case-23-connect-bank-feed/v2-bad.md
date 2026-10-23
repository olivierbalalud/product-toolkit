**Use Case:** Bank feed
**Actor:** System
1. User clicks "Bank" in the sidebar, then "Add bank".
2. User enters their online banking username and password in our form.
3. The system calls the Plaid /transactions/get endpoint.
4. The system loops over the transactions and inserts them into the ledger.
5. If the balance is wrong, the user contacts support.
6. Every night a cron job imports the new transactions.
