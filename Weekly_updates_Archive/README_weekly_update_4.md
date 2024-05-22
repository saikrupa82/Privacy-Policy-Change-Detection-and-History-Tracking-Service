# Notification Service for Privacy Policy Change Detection and Historical Tracking

## Project Overview
This project, developed under the Ethical Software Lab at UMBC, aims to create a robust notification service that detects changes in privacy policies, highlights these changes, and maintains a historical log for tracking. The service enhances transparency and helps users easily understand modifications in privacy policies.

### Capstone Project Details:
- **Date and Time:** 05-09-2023, 7:42 PM
- **Student Name:** Sai Krupa Reddy Surarapu
- **Project Name:** Notification Service for Privacy Policy Change Detection and Historical Tracking
- **Sponsor:** Ethical Software Lab at UMBC
- **Advisor:** Dr. Samarah

## Features

1. **Change Detection and Highlighting**
   - **Visual Display:** Detected changes are visually highlighted directly within the text or JSON file format, improving user comprehension.
   - **Text/JSON Highlighting:** Changes in privacy policy text or JSON data are made easily noticeable.

2. **Historical Change Log**
   - **Development in Progress:** A feature to record and display all changes made to a privacy policy over time.

## Installation

To get started with this project, ensure you have Python installed. Follow these steps to set up the project:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/edit/main/Scripts_Store_History
   ```


## Usage
Function: extract_section_by_keyword
- This function searches a JSON file for specified keywords within the privacy policy content and extracts relevant sections.

### Parameters:
- **file_path (str):** Path to the JSON file.
- **keyword (str):** The keyword to search for.
### How to Run:
- **Prepare JSON File:** Ensure your JSON file is formatted correctly with a changes array containing content objects.
- Execute the Function:
Enter the Keyword when the file is running
![image](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/f165e725-3eda-49bc-b465-5f0aa350b324)


Run the file 
``` bash
python Fetchdata.py
```
![image](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/f5c14ae2-6c48-4df5-a5f8-5d1cbe62dec8)

**Function:** scrape_privacy_policy
- This function scrapes a privacy policy from an HTML file, extracts sections, compares them with historical records, and cleans old history files.

**Parameters:**
- **file_path (str):** Path to the HTML file.
- **history_folder (str):** Path to the directory containing historical records.
![image](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/717d6bc1-bd32-4035-86da-c9778ec89d61)


**Function:** extract_section_by_keyword
- This function searches a JSON file for specified keywords within the privacy policy content and extracts relevant sections.

**Parameters:**
- file_path (str): Path to the JSON file.
- keyword (str): The keyword to search for.

![image](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/f0bca8a1-3adc-4c2c-9344-dcc9b17663c8)


## Weekly Status Report
### Status Details:
**1. Work Accomplished This Week:**
- **Implemented Keyword-Based Section Extraction:** Enhanced the system to allow dynamic input of keywords for targeted analysis of privacy policy sections.
- **Optimized Data Retrieval and Testing:** Improved the data retrieval process for faster and more accurate extraction and validated functionality through comprehensive testing.
- **Developed User Interface and Updated Documentation:** Created a user-friendly command-line interface and updated documentation to ensure ease of use and accessibility for all users.
- **Testing and Validation:** Conducted thorough testing to validate the functionality of the keyword extraction feature. This included multiple scenarios to ensure that the feature accurately captures all relevant sections containing the specified keywords.

**2. Work Planned for Next Week:**
- Finalize the Historical Change Log feature.
- Conduct comprehensive testing.
- Prepare for the final presentation.
- Conduct a final checkpoint review.
  
**3. Problems, Obstacles, Needs, or Questions:**
- Ensure the Historical Change Log feature is robust.
- Manage time effectively to complete all tasks before the final presentation.
  
### Overall Status:
- Project Status Color: Green
- Previous Week's Status Color: Green
  
This week saw significant progress in developing the notification service. As we enter the final phase, our focus will be on ensuring completeness and accuracy, along with preparation for the final presentation. We are committed to delivering a high-quality solution that meets our stakeholders' needs.
