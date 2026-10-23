**Title:** Setting up webhooks  
**Actor:** User  
**Description:**  
The user clicks on the "Developers" tab on the left navbar. Then they click the blue "+ Add Destination" button in the top right. A modal pops up. The user types their URL into the input field `txt_url`. The user selects "All events" using the checkbox. Next, the React frontend makes a POST request to `/api/v1/endpoints` with a JSON payload containing the user's session token. If the user clicks Save, the Postgres database inserts a row into `tbl_webhooks`. An alert banner appears saying "Saved!". Then the user copies the key and pastes it into their environment variables file.
