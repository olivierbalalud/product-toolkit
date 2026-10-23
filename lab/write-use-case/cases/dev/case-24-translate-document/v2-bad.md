**Use Case:** Translation
**Actor:** User
**Precondition:** The document is in English.
1. User drags the PDF onto the page.
2. The file is stored in an S3 bucket.
3. A Lambda function sends each paragraph to the translation engine.
4. The user waits.
5. The translated PDF is emailed to the user.
6. If there was an error, the user tries again.
