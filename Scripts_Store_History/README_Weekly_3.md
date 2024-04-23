# Overview of Weekly Checkpoint 3
This project provides a robust tool for monitoring changes in privacy policies across various websites, enabling users to be automatically alerted to modifications. It leverages Python and several powerful libraries to scrape, compare, and log updates in privacy policy documents, thus fostering greater transparency and allowing users to make more informed decisions regarding their personal data.


# System Requirements
- **Operating System:** Windows 10/11, macOS Catalina or later, Ubuntu 18.04 or later.
- **Python Version:** 3.8 or higher to ensure compatibility with the latest features and security fixes.
- **Internet Connection:** Required for fetching privacy policies and updates.
- **Additional Software:** A modern web browser for testing and documentation purposes.

# Features
- **Real-Time Monitoring:** Automatically monitors specified URLs and detects changes as soon as they are published.
- **Detailed Comparison:** Utilizes the difflib Python library to perform a detailed comparison of the text, ensuring all modifications, no matter how minor, are captured.
- **Visual Difference Highlighting:** Uses color-coded differences to enhance readability and understanding of changes for users.
- **Historical Records:** Maintains a detailed log of all changes, providing a historical overview of privacy policy evolution.

# Usage
Simply launch the script with the command below and follow the interactive prompts to enter the URL of the privacy policy you wish to monitor:

``` bash
python Scripts_Store_History/Fetchdata.py
```
The script will provide a step-by-step guide through the process and output the results in a user-friendly format.


# Workflow
## Fetching and Parsing
Initially, the script fetches the HTML content from the provided URL using the requests library, which is then parsed with BeautifulSoup to isolate relevant sections such as headings and paragraphs.

Example Command
``` bash
python Scripts_Store_History/Fetchdata.py "http://example.com/privacy-policy"
```
## Change Detection
After parsing, the script analyzes the content, comparing it with previously stored versions to identify any changes. This comparison is logged and can be reviewed to see the historical evolution of the document.

## Logging Changes
Every detected change is timestamped and saved in a JSON format, providing a reliable and searchable log that can be audited for compliance or review purposes.

## History Management and JSON Format
PolicyTracker effectively logs every update made to privacy policies it monitors. This section details the JSON structure that captures and stores these changes, simplifying data interpretation for developers and system administrators.

## JSON History File Structure
Each privacy policy has a dedicated JSON file, storing:

- last_checked: The timestamp of the last policy review.
- changes: An array documenting each detected change.
- last_update: Details about the most recent update, including the exact changes and their timestamps.

``` bash
{
  "last_checked": "2024-04-22T12:00:00Z",
  "changes": [
    {
      "timestamp": "2024-04-21T12:00:00Z",
      "content": {
        "Introduction": ["The Privacy Policy has been updated to reflect changes in data protection laws."],
        "Data Collection": ["Data collection now includes new analytical tools."]
      }
    }
  ],
  "last_update": {
    "timestamp": "2024-04-21T12:00:00Z",
    "content": {...},
    "detailed_changes": [...]
  }
}
```
![alt text](image.png)

## Using JSON Data
JSON files are accessible within a dedicated history folder, offering insights for:

- Historical data review.
- Reporting.
- System integration.
## Troubleshooting
### Common Issues
- **Installation Errors:** Verify Python and pip versions; reinstall dependencies if necessary.
- **Scraping Issues:** Ensure the website’s URL is correct and accessible. Use a VPN if the site blocks requests from your IP address.
