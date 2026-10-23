**Use Case:** CSV upload
**Actor:** Admin
1. Admin clicks "Audience", then "Import contacts".
2. Admin uploads the CSV file.
3. The system parses the CSV with pandas and maps the columns.
4. If the columns are wrong, the admin fixes the file in Excel and uploads it again.
5. The system inserts the rows into the contacts table.
6. A spinner is shown until the import is done.
7. Admin sends a campaign to the new contacts.
