
# Privacy Policy Change Detection and Historical Tracking Service

## Overview

The Privacy Policy Change Detection and Historical Tracking Service is a Python-based automation tool designed to help users monitor updates and changes in website privacy policies over time. It works by fetching the latest version of a privacy policy from a specified URL, parsing the text, and comparing it with a stored version to detect any changes. This tool is particularly useful for privacy-conscious individuals, researchers, and organizations that need to stay informed about how their or their users' information may be treated by service providers.

## Features

- **Automated Fetching:** Utilizes the Requests library to automatically retrieve the content of privacy policy webpages.
- **Intelligent Parsing:** Employs BeautifulSoup4 to parse HTML content and segment privacy policies into manageable sections based on headings.
- **Change Detection:** Leverages the difflib library to perform a detailed comparison between the current and previously stored versions of a policy, identifying additions, deletions, and modifications.
- **Historical Tracking:** Maintains a JSON file for each tracked privacy policy, logging all changes detected during each script run, along with timestamps for easy historical analysis.
- **Console Notifications:** Outputs a summary of detected changes and relevant metadata to the console, enabling quick reviews or integrations with further notification systems.

## Requirements

To run this tool, you will need:
- Python 3.6 or newer
- The Requests library for Python
- BeautifulSoup4 for HTML parsing

## Installation

Follow these steps to set up the Privacy Policy Change Detection tool:

1. **Clone the GitHub Repository:**

   ```shell
   git clone https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service.git
   ```

2. **Navigate to the Tool's Directory:**

   ```shell
   cd Privacy-Policy-Change-Detection-and-History-Tracking-Service/Scripts_Store_History
   ```

3. **Install Dependencies:**

   Ensure you have Python and pip installed on your system, then run:

   ```shell
   pip install requests beautifulsoup4
   ```

## Usage Guide

1. **Start the Script:**

   Run the script from your terminal or command prompt:

   ```python
   python Fetchdata.py
   ```

2. **Input the URL:**

   When prompted, enter the full URL of the privacy policy page you wish to track. Make sure to include the `http://` or `https://` prefix.

   ```plaintext
   Enter the URL of the privacy policy to scrape: [https://policies.google.com/privacy?hl=en-US](https://policies.google.com/privacy?hl=en-US)
   ```

3. **Review the Detected Changes:**

   After the script runs, it will output any detected changes directly to the console, along with the timestamp of the last check.

## How It Works

### Fetching and Parsing

- The script first sends a GET request to the specified URL to fetch the webpage content.
- It then parses the HTML using BeautifulSoup4, extracting text from headings and paragraphs to segment the privacy policy into distinct sections.

### Change Detection

- It compares the fetched policy text against a previously stored version (if available) in a JSON file named after the website's domain.
- The comparison is done section by section, using the difflib library to identify detailed changes.

## File Structure

- `Fetchdata.py`: The main Python script.
- `domainname_history.json`: Automatically generated files that store the change history for each tracked website's privacy policy.


## Screenshots
### Script Execution and JSON History File
![image](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/c761c3bd-36b5-44d5-859e-dd080c8bf88f)

- File Viewer: This part of VS Code shows several Python scripts (Fetchdata.py and others) and JSON files containing history logs (e.g., policies.google.com_history.json).
- Script Output: The integrated terminal displays a message indicating that the script did not detect any changes after running the Fetchdata.py script.
- History Log: The JSON file (policies.google.com_history.json) is open in the editor, displaying the structure of the stored history with timestamps and content from a privacy policy.

### Python Script Code and Command Execution
![image](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/6d86e64c-0bd0-4e0e-b162-acb8480297fd)

- Code Editor: Shows the Fetchdata.py script, which includes functions for fetching web content, parsing it, and comparing it to historical data to detect changes.
- 
### Detailed Script and Functionality

![image](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/3d31a622-c1ce-4568-91b4-2d842dc27178)

- Script Details: A continuation of the Fetchdata.py script is visible, showing more detailed code that handles the comparison of website content and updates the history file accordingly.
## License

This project is licensed under the MIT License - see the LICENSE.md file in the GitHub repository for details.
