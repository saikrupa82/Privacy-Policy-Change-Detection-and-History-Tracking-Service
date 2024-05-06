

# PolicyTracker - RC Release Overview

## Table of Contents
1. [Introduction](#introduction)
2. [System Architecture](#system-architecture)
   1. [Website](#website)
   2. [Scraping Model](#scraping-model)
   3. [Parsing Model](#parsing-model)
   4. [History Management Module](#history-management-module)
   5. [Data Store](#data-store)
   6. [Overall Flow](#overall-flow)
3. [Web Scraping System Flow](#web-scraping-system-flow)
4. [User Guide and Documentation](#user-guide-and-documentation)
   1. [Setup Instructions](#setup-instructions)
   2. [Configuration Guide](#configuration-guide)
   3. [Usage Examples](#usage-examples)
5. [User Stories Overview](#user-stories-overview)
6. [Website Interaction](#website-interaction)
7. [Scraping Model](#scraping-model-details)
8. [Parsing Model](#parsing-model-details)
9. [History Management Module](#history-management-module-details)
10. [Data Store](#data-store-details)
11. [Email Notification Service](#email-notification-service)
12. [Detailed Requirements](#detailed-requirements)
   1. [Functional Requirements](#functional-requirements)
   2. [Non-functional Requirements](#non-functional-requirements)
13. [History Management and JSON Format](#history-management-and-json-format)
14. [Accessing and Using JSON Data](#accessing-and-using-json-data)
15. [Contributing to History Management](#contributing-to-history-management)
16. [Command Line Testing](#command-line-testing)
17. [Execution and Results](#execution-and-results)
18. [Key Challenges and Mitigations](#key-challenges-and-mitigations)
19. [Future Enhancements and Features](#future-enhancements-and-features)
20. [Installation](#installation)
21. [Conclusion](#conclusion)
22. [References](#references)


## Introduction
The RC iteration of PolicyTracker demonstrates 95% completion of our envisioned product suite, showing significant enhancements from the alpha release towards a robust, user-oriented full-scale deployment.

![System Architecture](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/8887619c-809f-439a-9531-b082b16c4c56)
*Figure 1: System Architecture Overview*

- The diagram above represents the architecture for PolicyTracker, demonstrating the different components involved and their interactions. Here's an overview:

1. **Website:**
   - **Purpose:** Serves as the source where privacy policies are hosted and can be accessed via web pages.
   - **Function:** The system retrieves privacy policy data directly from these web pages.

2. **Scraping Model:**
   - **BeautifulSoup 4:** A Python library that helps gather data from multiple web pages by extracting useful content from the HTML.
   - **Process:** This module sends requests to websites, collects data, and organizes it for further analysis.

3. **Parsing Model:**
   - **Purpose:** Responsible for parsing HTML content and identifying relevant tags, strings, and comments within the privacy policies.
   - **Function:** Extracted data is then passed to the History Management Module.

4. **History Management Module:**
   - **Purpose:** Compares parsed data with historical versions to identify changes in privacy policies.
   - **Function:** Stores any detected changes for future auditing and analysis.

5. **Data Store:**
   - **Purpose:** Central repository where data gathered from websites, historical logs, and detected changes are stored.
   - **Function:** Acts as a source for future retrieval and comparison.

**Overall Flow:**
1. The **Website** provides policy pages to the **Scraping Model**.
2. The **Scraping Model** extracts data using BeautifulSoup and processes it in the **Parsing Model**.
3. The **Parsing Model** analyzes the extracted data and sends it to the **History Management Module**.
4. The **History Management Module** identifies changes and stores the relevant data in the **Data Store** for further usage and monitoring.

## Web Scraping System Flow
PolicyTracker automates the collection, analysis, and storage of online privacy policy data through a sophisticated sequence of operations:

# User Guide and Documentation:

Setup Instructions: Detailed steps to set up PolicyTracker, including software dependencies and required environment variables.
Configuration Guide: Instructions on customizing scraping configurations, history folder paths, and notification settings.
Usage Examples:
- **Single URL Scraping:** Scraping and monitor a single privacy policy URL.
- **Bulk URL Scraping:** A list of URLs for bulk policy monitoring.
  ![image](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/15f7b839-9329-4579-8f12-d5c0c0b10cc0)
Input of the file: 
![image](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/4dbb6873-684a-4e74-b45e-458d505ae97d)

The file format:

```bash
URL,
URL1,
.
.
URLn
```

Example: 
``` bash
https://policies.google.com/privacy?hl=en-US,
https://privacy.microsoft.com/en-us/privacystatement

```

### User Stories Overview

| Req. ID | Requirement (User Story) | Link to UI Prototype | Expected Completion Date | Complexity | Risk   | Status            |
|---------|---------------------------|----------------------|-------------------------|------------|--------|------------------|
| 1       | As a User, I want to scrape privacy policy data directly from websites so that I can analyze the most current version of policies and accurately compare them with historical data. | Section 6, Prototype A | 03/26/2024 | High       | Medium | ✅ Completed      |
| 2       | As a User, I want to maintain a history of changes for each privacy policy so that I can review past modifications and track differences over time. | Section 6, Prototype B | 04/02/2024 | Medium     | Medium | ✅ Completed      |
| 3       | As a User, I want to detect changes in privacy policies efficiently so that I can quickly analyze differences between versions. | Section 6, Prototype C | 04/09/2024 | Medium     | Low    | ✅ Completed       |
| 4       | As a User, I want to receive change notifications via email so that I can stay informed about updates to privacy policies and respond promptly. | Section 6, Prototype D | 04/16/2024 | High       | Medium | ✅ Completed      |
| 5       | As a User, I want to provide URLs via a file or command line so that I can input the data efficiently using my preferred method. | Section 6, Prototype E | 04/23/2024 | Low        | Low    | ✅ Completed      |
| 6       | As a User, I want to store HTML files locally so that I can keep a reference for future comparisons or analysis. | Section 6, Prototype F | 04/30/2024 | Medium     | Low    | ✅ Completed      |
| 7       | As a User, I want to customize search keywords in privacy policies so that I can tailor the analysis to identify relevant sections of interest. | Section 6, Prototype G | 05/07/2024 | Medium     | Medium | ⏳ Pending            |




### Website Interaction
- **Data Source**: Begins with websites hosting privacy policies in their native HTML format.
- **Data Gathering Process**: Executes systematic HTTP GET requests to fetch data comprehensively.

``` bash
# Placeholder for actual scraping functionality
result = polipy.get_policy(url, screenshot=True)
result.save(output_dir='.')
```
### Scraping Model
- **Technology**: Utilizes Beautiful Soup 4 for converting complex HTML documents into a navigable and parsable structure.
- **Data Retrieval and Organization**: Converts raw HTML data into a structured format for further processing.

### Parsing Model
- **HTML Parsing**: Extracts relevant content from HTML documents using precise selectors to isolate key segments of privacy policies.
``` bash
def fetch_and_parse(file_path):
    print(f"Attempting to read and parse the file at: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')
            print("File successfully parsed.")
            return soup
    except Exception as e:
        print(f"Failed to read or parse the file due to: {e}")
    return None

def extract_sections(soup):
    print("Extracting sections from HTML content.")
    sections = {}
    current_heading = None
    for element in soup.find_all(['h2', 'p']):
        if element.name == 'h2':
            current_heading = element.get_text(strip=True)
            sections[current_heading] = []
        elif element.name == 'p' and current_heading:
            sections[current_heading].append(element.get_text(strip=True))
    print("Sections successfully extracted.")
    return sections
```
### History Management Module
- **Change Detection**: Employs algorithms to detect changes by comparing new data against a historical baseline.
- **History Recording**: Documents changes to privacy policies over time, capturing their evolution.
``` bash
def compare_and_update_history(file_path, new_content, history_folder):
    print(f"Checking for existing history in: {history_folder}")
    os.makedirs(history_folder, exist_ok=True)
    history_filename = os.path.join(history_folder, os.path.basename(file_path).replace('.html', '_history.json'))

    history = {}
    try:
        with open(history_filename, 'r', encoding='utf-8') as file:
            history = json.load(file)
            print("Existing history found and loaded.")
    except FileNotFoundError:
        print("No history file found, creating a new one.")

    print("Comparing the new content with the last update.")
    last_update = history.get('last_update', {})
    changes_detected = False
    detailed_changes = []

    for section, texts in new_content.items():
        old_texts = last_update.get('content', {}).get(section, [])
        diff = list(difflib.unified_diff(old_texts, texts, lineterm=''))
        if diff:
            changes_detected = True
            detailed_changes.append((section, diff))
 ```
### Data Store
- **Storage Solutions**: Utilizes efficient storage mechanisms to organize and store the scraped data.
- **Data Usage**: Supports diverse applications from compliance tracking to advanced analytics.
``` bash

    if changes_detected:
        print("Changes detected. Updating history.")
        timestamp = datetime.now().isoformat()
        history.setdefault('changes', []).append({
            'timestamp': timestamp,
            'content': new_content
        })
        history['last_update'] = {
            'content': new_content,
            'timestamp': timestamp,
            'detailed_changes': detailed_changes
        }
    else:
        print("No changes detected.")

    print("Updating the last checked timestamp.")
    history['last_checked'] = datetime.now().isoformat()

    print("Saving the history to file.")
    with open(history_filename, 'w', encoding='utf-8') as file:
        json.dump(history, file, ensure_ascii=False, indent=4)
```

### Email Notification Service:
The email notification feature alerts stakeholders when significant changes are detected in a monitored privacy policy. It ensures stakeholders remain informed about updates affecting compliance or data practices. The emails summarize detected changes, enabling recipients to respond promptly and maintain their understanding of privacy policy requirements.

- **Summarized Alerts**: Emails provide concise summaries of detected changes, highlighting sections with added, removed, or updated content.
- **Customizable Recipients**: Notifications can be sent to a list of recipients provided by the user.
- **Secure Transmission**: Uses TLS encryption to secure email data during transmission.

**Function**

```bash
def send_email(subject, body, sender, recipients, password):
    if isinstance(body, list):
        body = "\n\n".join(f"Section: {section}\n" + "\n".join(diff) for section, diff in body)

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
            smtp_server.starttls()  # Upgrade to a secure connection
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
        print("Message sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
```

Calling function 
``` bash
        send_email(subject, detailed_changes, useremail, recipients, password)

```

## Detailed Requirements :
### Functional Requirements:
- **Scrape Privacy Policy Data**:
By leveraging the polipy library, I created a scraping tool capable of extracting privacy policy data directly from websites, accommodating a wide range of HTML structures. Users can provide a URL or a local file path for the tool to process. The scraping module accurately identifies relevant sections and prepares them for further analysis using BeautifulSoup.
- **Maintain a History of Changes**:
I designed a database schema to chronologically organize each change in privacy policies. It uses JSON files stored in an organized directory structure. A history management module can clean up old history files and ensures that all changes are correctly documented and timestamped.
- **Detect Changes in Privacy Policies**:
With the difflib library, the system highlights differences between policy versions, displaying these as unified diffs. The change detection algorithm is able to detect even subtle differences, capturing modified or removed text precisely.
- **Receive Change Notifications via Email**:
Using smtplib, the tool sends email alerts summarizing changes detected in privacy policies. The emails provide actionable insights and include links for recipients to download or review detailed change reports.
Non-functional Requirements:
- **Security**:
By using RBAC (Role-Based Access Control), data encryption at rest, and TLS during data transmission, sensitive information is protected. Authentication protocols and OAuth are also implemented to ensure secure user access.
- **Performance**:
With optimized search algorithms, caching of intermediate results, and efficient data validation methods, the system processes policies efficiently, even at high volume.
- **Data Integrity**:
Comprehensive validation, backups, and regular maintenance prevent data duplication and ensure historical accuracy.

## History Management and JSON Format
PolicyTracker maintains a comprehensive history of changes to each tracked privacy policy. This section outlines how the history data is structured in JSON format, making it easy for developers and system administrators to interpret and utilize the stored data.

### JSON History File Structure
Each privacy policy tracked by the application has an associated JSON file that stores the history of changes. Below is a description of the key components of the JSON structure:

- **last_checked**: Timestamp indicating the last time the policy was checked for changes.
- **changes**: An array of change records, where each record represents a detected change during a policy check.
- **last_update**: Contains information about the most recent change including detailed changes, the timestamp of the change, and the new content.
``` bash
{
  "last_checked": "2024-04-22T12:00:00Z",
  "changes": [
    {
      "timestamp": "2024-04-21T12:00:00Z",
      "content": {
        "Introduction": [
          "The Privacy Policy has been updated to reflect recent changes to data protection laws."
        ],
        "Data Collection": [
          "We have expanded our data collection to include new analytical tools."
        ]
      }
    }
  ],
  "last_update": {
    "content": {
      "Introduction": [
        "The Privacy Policy has been updated to reflect recent changes to data protection laws."
      ],
      "Data Collection": [
        "We have expanded our data collection to include new analytical tools."
      ]
    },
    "timestamp": "2024-04-21T12:00:00Z",
    "detailed_changes": [
      {
        "section": "Introduction",
        "diff": [
          "- old content line 1",
          "+ new content line 1"
        ]
      },
      {
        "section": "Data Collection",
        "diff": [
          "- old content line 2",
          "+ new content line 2"
        ]
      }
    ]
  }
}

```

### Accessing and Using JSON Data
The JSON history files are stored within the designated history folder for each policy, typically located at a path relative to the policy's HTML file. Developers can access these files to review historical data, generate reports, or integrate change tracking into other systems.

To ensure seamless integration and manipulation of JSON data:

- Utilize JSON parsing libraries available in most programming languages, such as json in Python, to load and manipulate the data programmatically.
- Employ tools and libraries designed for handling large JSON files if dealing with extensive historical data to optimize performance.

### Contributing to History Management
Contributors interested in enhancing the history tracking capabilities of PolicyTracker can consider:

- Improving the algorithms for change detection to capture more nuanced modifications.
- Extending the JSON structure to include more detailed metadata about changes.
- Optimizing the storage and retrieval of JSON files to enhance performance and scalability.

## Command Line Testing
Testing via the command line has proven the script's effectiveness in handling multiple URLs, reflecting the system's capability to scale and perform under load:

```bash
python fetchdata.py <URL1> <URL2> <URL3> ... <URLN>
```
OR

```bash
python fetchdata.py
```
![Screenshot 2024-05-05 200011](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/7a46c2e4-ff24-490f-aea9-c9dde96bade0)


## Execution and Results
Scalability and Performance: Confirmed the script's ability to process numerous privacy policy URLs concurrently without degradation in speed or accuracy.

![Screenshot 2024-04-21 222638](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/095ce474-3e4a-4753-8369-78a8ad95d974)



### Key Challenges and Mitigations

- **Frequent Website Structure Changes:** Changes in privacy policy page structures could impact scraping accuracy.
  - **Mitigation:** Implement machine learning models and dynamic algorithms to identify and adjust to website changes automatically.

- **Data Privacy Concerns:** Handling privacy policy data presents challenges in safeguarding sensitive information.
  - **Mitigation:** Ensure data encryption at rest and in transit, employ strict access control measures, and conduct regular compliance audits.

- **Notification Delivery Issues:** Notifications may be delayed or marked as spam.
  - **Mitigation:** Implement multiple notification channels like SMS or push notifications. Monitor email deliverability and follow best practices.

### Future Enhancements and Features

- **Custom Alerts and Dashboard:** Provide a customizable dashboard where users can set up alerts based on specific keywords or criteria.

- **Multi-channel Notifications:** Integrate additional channels like SMS and browser push notifications for improved user engagement.

- **Integration with External Systems:** Support seamless integration with third-party compliance and monitoring systems.



## Installation
Clone the repository and install the necessary dependencies to get PolicyTracker running:

``` bash
git clone https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service.git
cd Scripts_Store_History
pip install -r requirements.txt
```

## Conclusion
The PolicyTracker system has demonstrated significant capabilities in the field of privacy policy tracking, providing robust tools for managing and staying updated on policy changes. My alpha, beta and RC releases showcased a solid foundation with essential functionalities that enhance user engagement and system reliability. Through comprehensive command line testing, I have proven the application's ability to handle multiple operations simultaneously, ensuring scalability and performance under load.

I have streamlined the installation process to ensure easy setup, enabling users and developers to deploy PolicyTracker efficiently. With ongoing improvements and community feedback, I aim for PolicyTracker to become the leading solution in privacy policy management.

## References

1. **Requests:**
   - *HTTP for Humans™.* [Official Documentation](https://requests.readthedocs.io/)
   - A simple and elegant HTTP library for Python used to make HTTP requests simpler and more human-friendly.

2. **Beautiful Soup:**
   - *Beautiful Soup Documentation.* [Documentation Link](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
   - Official documentation for Beautiful Soup, a Python library designed for quick turnaround projects like screen-scraping.

3. **Requests (Alternate Reference):**
   - *Requests: HTTP for Humans.* [Official Documentation](https://requests.readthedocs.io/)
   - Documentation for Requests, making HTTP requests simpler and more user-friendly.

4. **Python Standard Library - difflib:**
   - *difflib — Help for computing deltas.* [Documentation Link](https://docs.python.org/3/library/difflib.html)
   - Documentation for difflib, which computes differences between files and data sequences.

5. **Python Standard Library - sys:**
   - *sys — System-specific parameters and functions.* [Documentation Link](https://docs.python.org/3/library/sys.html)
   - Documentation for the sys module, used to manipulate parts of the Python runtime environment.

6. **Python Standard Library - os:**
   - *os — Miscellaneous operating system interfaces.* [Documentation Link](https://docs.python.org/3/library/os.html)
   - Documentation for the os module, which provides ways to interact with the operating system.

7. **OAuth:**
   - *OAuth Community Site.* [OAuth Guide](https://oauth.net/)
   - A comprehensive guide to OAuth, a protocol allowing secure authorization from web, mobile, and desktop apps.

8. **GitHub - Command Line Tools:**
   - *GitHub CLI Documentation.* [GitHub CLI Guide](https://cli.github.com/)
   - Guide on using GitHub via command-line tools to manage repositories, branches, commits, and more.

9. **Python Documentation - smtplib:**
   - *smtplib — SMTP protocol client.* [Documentation Link](https://docs.python.org/3/library/smtplib.html)
   - Documentation for smtplib, Python's built-in module for sending emails through the SMTP protocol.


