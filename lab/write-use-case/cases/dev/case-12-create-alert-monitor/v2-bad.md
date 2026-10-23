**Title:** Make a Datadog Alert  
**Actor:** Developer  
**Description:**  
The developer goes to Monitors -> New Monitor. They pick "Metric" from the list of icons. In the search box, they type their query `avg(last_5m):avg:system.cpu.user{*} by {host} > 80`. Then they choose the radio button for "Alert threshold" and put 80. In the text area below, they write "CPU is high, fix it please @slack-channel". They click the purple Save button at the bottom of the page. The monitor is now running in Datadog.
