# PolicyTracker - Privacy Policy Tracking System

PolicyTracker is an innovative solution designed to keep users informed about the updates and changes to the privacy policies of various online services. This document outlines the core functionalities of PolicyTracker, focusing on its features, security measures, and the future direction of the platform.

#### [Demo Video of the application](https://drive.google.com/file/d/1SUcW5Zj4U6RNXyxki4oXlN0SHsDo1A0U/view?usp=drive_link)
# PolicyTracker - Privacy Policy Tracking System

PolicyTracker is an innovative solution designed to keep users informed about the updates and changes to the privacy policies of various online services. This document outlines the core functionalities of PolicyTracker, focusing on its features, security measures, and the future direction of the platform.

<details>
<summary><h2>Table of Contents</h2></summary>

- [Introduction](#policytracker---privacy-policy-tracking-system)
- [Demo Video](#demo-video-of-the-application)
- [Alpha Checkpoint](#alpha-checkpoint)
  - [Core Features Implementation](#core-features-implementation)
  - [Known Issues and Bugs Documentation](#known-issues-and-bugs-documentation)
  - [Testing Guidelines](#testing-guidelines)
  - [Installation and Configuration Instructions](#installation-and-configuration-instructions-for-policytracker)
- [Beta Checkpoint](#beta-checkpoint)
  - [Web Scraping System Flow](#web-scraping-system-flow)
  - [Functional Specifications](#beta-functional-specifications)
  - [Quality Criteria](#quality-criteria-for-beta-functionality)
  - [Command Line Testing](#command-line-testing)
- [Architecture Overview](#architecture-overview)
- [Load Testing](#load-testing)
- [Risk Assessment and Mitigation Strategies](#risk-assessment-and-mitigation-strategies-for-policytracker)
- [Roadmap for Beta Release](#roadmap-for-beta-release-of-policytracker)
- [References](#references)
- [Installation Instructions](#installation-instructions)

</details>

## Demo Video of the application
[Demo Video of the application](https://drive.google.com/file/d/1SUcW5Zj4U6RNXyxki4oXlN0SHsDo1A0U/view?usp=drive_link)

## Alpha Checkpoint

<details>
<summary>PolicyTracker Alpha Release Overview</summary>

### Core Features Implementation
- [My Tracked Pages](#my-tracked-pages)
- [Track New Page](#track-new-page)
- [Detailed Policy View/Management](#detailed-policy-viewmanagement)
- [User Authentication System](#user-authentication-system)
- [Privacy Policy Tracking and Management](#privacy-policy-tracking-and-management)
- [Alerts and Notifications](#alerts-and-notifications)
- [Data Retrieval and Processing](#data-retrieval-and-processing)
- [Security Measures](#security-measures)
- [Database Models](#database-models)
- [Database Selection](#database-selection)
- [SQL in Django](#sql-in-django)
- [Security](#security)

### Known Issues and Bugs Documentation
- [Current Known Issues](#current-known-issues)
- [Reporting New Issues](#reporting-new-issues)

### Testing Guidelines
- [Overview](#overview)
- [Testing Environment](#testing-environment)
- [Reporting Issues](#reporting-issues)
- [Continuous Integration (CI) and Continuous Deployment (CD)](#continuous-integration-ci-and-continuous-deployment-cd)

### Installation and Configuration Instructions for PolicyTracker
- [Prerequisites](#prerequisites)
- [Step 1: Clone the Repository](#step-1-clone-the-repository)
- [Step 2: Set Up a Virtual Environment](#step-2-set-up-a-virtual-environment)
- [Step 3: Install Dependencies](#step-3-install-dependencies)
- [Step 4: Configure the Application](#step-4-configure-the-application)
- [Step 5: Initialize the Database](#step-5-initialize-the-database)
- [Step 6: Run the Development Server](#step-6-run-the-development-server)
- [Additional Configuration](#additional-configuration)

</details>

## Beta Checkpoint
<details>
<summary>PolicyTracker Beta Release Overview</summary>

### Introduction
- [Introduction](#introduction)

### Web Scraping System Flow
- [Web Scraping System Flow](#web-scraping-system-flow)

### Beta Functional Specifications
- [Beta Functional Specifications](#beta-functional-specifications)

### Quality Criteria for Beta Functionality
- [Quality Criteria for Beta Functionality](#quality-criteria-for-beta-functionality)

### History Management and JSON Format
- [ History Management and JSON Format](#history-management-and-json-format)

### Command Line Testing
- [Command Line Testing](#command-line-testing)

### Installation
- [Installation](#installation)

### References
- [References](#references)

</details>

# PolicyTracker - Alpha Release Overview

## Core Features Implementation

PolicyTracker offers a comprehensive suite of functionalities aimed at enhancing the user experience in tracking and managing privacy policy updates.

## My Tracked Pages
![image](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/e731e0fe-99a2-4a9e-adcb-f64f7a317b43)

### Functionality

This is the main dashboard where users can view and manage the list of privacy policies they are monitoring.

### Features

- **List of Policies**: Shows a concise view of all tracked policies along with their respective titles, URLs, and statuses.
- **Pagination Support**: Allows navigation across different pages if the list is too long to fit on one page.
- **Add New Policy**: Users can track new policies using the provided interface.

  
## Track New Page
![Screenshot 2024-03-30 204112](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/fc25e8e3-e7d4-47dd-8822-a11596b37677)

![Screenshot 2024-03-30 204011](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/5d3cf0af-8d24-402f-9b05-7e6afb724e5c)

![Screenshot 2024-03-30 204139](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/8cf82eb4-d5a4-45cb-9bb9-135b77c075c5)


### Functionality

A feature-rich page dedicated to adding new privacy policies to the user's tracking list.

### Features

- **Single URL Submission**: Users can add a single URL for tracking, accompanied by a custom title if needed.
- **Bulk URL Addition**: Provides the ability to add multiple policy URLs at once, which is particularly useful for tracking several policies simultaneously.

## Detailed Policy View/Management
![Screenshot 2024-03-30 204040](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/40b8bd87-45fd-448d-ad2b-1f93af06a7fc)
![Screenshot 2024-03-30 204054](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/d340b71e-b232-41c4-9548-eff86ddeb5c0)

### Functionality

Offers a granular view of each policy's tracking settings, giving users full control over the monitoring process.

### Features

- **Monitoring Controls**: Edit, pause, or delete the monitoring of privacy policies.
- **Instant Check**: Allows users to manually trigger a check for changes.
- **Notification Preferences**: Customize how and where to receive notifications about policy updates.
- **Advanced Settings**: Set specific criteria for monitoring, like alerting on certain keywords.


### User Authentication System

- **Secure Sign-Up and Login**: Leveraging Django's robust authentication system, PolicyTracker ensures secure management of user credentials. Passwords are encrypted with state-of-the-art hashing algorithms, securing them against unauthorized access.

### Privacy Policy Tracking and Management

- **Policy Addition and Management**: Users can add URLs of privacy policies they wish to track with ease. Each tracked policy can be managed through intuitive edit and delete options, giving users complete control over their tracking list.

- **Automated Change Detection**: Utilizing Python's `requests` and `BeautifulSoup`, PolicyTracker automates the process of checking for updates on specified privacy policy pages, ensuring users are always informed about the latest changes.

### Alerts and Notifications

- **Customizable Notification Settings**: Users have the flexibility to choose how they receive notifications about policy updates, with options including email.

- **Real-Time Alerts**: When changes are detected in a privacy policy, PolicyTracker sends out real-time alerts to users, ensuring prompt and transparent communication of modifications.

### Data Retrieval and Processing

- **Efficient Data Scraping**: At its core, PolicyTracker features an efficient data scraping mechanism that fetches content from policy URLs, leveraging `requests` for HTTP operations and `BeautifulSoup` for HTML parsing, highlighting key changes.

- **Content Extraction and Analysis**: Following data retrieval, advanced algorithms analyze the scraped content to identify significant changes, categorize them, and present a summarized view to the user.

### Security Measures

- **Comprehensive Security Framework**: Embedding security at every layer, PolicyTracker employs data encryption, CSRF tokens, and secure user authentication protocols to protect user data and system integrity.

- **Regular Security Audits**: To maintain a high security standard, PolicyTracker undergoes periodic security audits, ensuring adherence to best practices and mitigation of potential vulnerabilities.

## Database Models


<img src="https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/67384de9-1848-4142-bc1e-2e835a53d8eb" width="50%" height="50%">


### CustomUser
This model extends the Django `AbstractUser`, adding additional fields like `full_name` and `age` for a more complete user profile.

``` bash
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=False)
    age = models.PositiveIntegerField(null=True, blank=True)

```
**Fields**:
- `full_name` - Stores the user's full name for display purposes.
- `age` - (Optional) Stores the user's age.

#### Secure storage of user login details in a database.
![image](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/5d66da19-51d9-4839-97c0-4ffa524e6659)


### PolicyTracker
The core model of the application, tracking privacy policy URLs and changes.
``` bash
class PolicyTracker(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use the AUTH_USER_MODEL setting
        on_delete=models.CASCADE,
        related_name='tracked_policies'
    )
    policy_name = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    last_checked = models.DateTimeField(auto_now=True)
    last_changed = models.DateTimeField(null=True, blank=True)
    latest_content = models.TextField()
    content_dict = models.JSONField()

    class Meta:
        unique_together = ('user', 'policy_name',)  # Ensures that the combination of user and policy_name is unique

    def __str__(self):
        return f"{self.policy_name} ({self.user.username})"
```

**Fields**:
- `user` - Links policy entries to users, allowing multiple policies per user.
- `policy_name` - The name of the policy being tracked.
- `url` - The unique URL of the privacy policy.
- `last_checked` - Automatically updated with the current date and time when the policy is checked.
- `last_changed` - Stores when the policy content was last changed.
- `latest_content` - Stores the full content of the policy.
- `content_dict` - Stores a JSON structure of key content changes for analysis.
  #### Structured data stored in a database, illustrating the organized repository of information.
![image](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/66702dbb-20f5-45c3-9867-b15d7fcfdd73)

## Database Selection

PolicyTracker can work with various SQL databases, and here's why different options might be chosen:

- **PostgreSQL**: Offers advanced features and is well-suited for JSON operations, making it an ideal choice for the `content_dict` field in PolicyTracker.
- **MySQL**: Known for its vast community support and robustness.
- **SQLite**: Great for development due to its simplicity and ease of use.
- **Oracle**: Suited for enterprise-level applications with a need for extensive features.

### SQL in Django

Django's ORM abstracts SQL queries through Python code, enhancing security and developer productivity. For complex queries, Django allows raw SQL to be written when needed.

## Security

PolicyTracker uses several security measures to protect user data and ensure application integrity:

- Data encryption in transit and at rest.
- CSRF token implementation in forms.
- Secure password hashing and user session management.
- Regular security audits and updates.


# Known Issues and Bugs Documentation

As part of our commitment to transparency and continuous improvement, this document outlines the current known issues and bugs in PolicyTracker. We are actively working to address these problems and encourage our community to report any new issues they encounter. Below is a summary of the known issues that users might experience while using PolicyTracker.

## Current Known Issues

1. **Automated Tracking Limitations**: 
   - Description: Automated tracking might not detect minor changes or updates made in the privacy policies if they are not reflected in the main content body.
   - Impact: Users might miss out on minor yet significant policy updates.
   - Status: Under investigation for a more comprehensive scraping approach.

2. **User Interface Responsiveness**:
   - Description: Certain UI elements may not render optimally on all devices or screen sizes, affecting usability.
   - Impact: Affects the accessibility and user experience, especially on mobile devices.
   - Status: UI redesign planned for better responsiveness across devices.

3. **Data Parsing Inaccuracies**:
   - Description: The current data parsing algorithm may occasionally misinterpret or overlook specific policy sections.
   - Impact: Potential for incomplete or inaccurate representation of policy changes.
   - Status: Algorithm refinement in progress to improve accuracy and reliability.

## Reporting New Issues

We encourage the PolicyTracker community to report any bugs or issues they encounter. This collaborative effort helps us enhance the platform's stability and performance. To report an issue, please follow these steps:

1. Visit the [Issues section](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/issues) of our GitHub repository.
2. Check if the issue has already been reported to avoid duplicates.
3. Click on the `New Issue` button to create a new report.
4. Provide a detailed description of the issue, including steps to reproduce, expected behavior, and actual behavior.
5. Attach any relevant screenshots or error messages to help us better understand the problem.


# Testing Guidelines

Welcome to the Testing Guidelines for PolicyTracker. Our aim is to ensure the highest quality and reliability of our application through comprehensive testing. This document serves as a guide for developers, testers, and contributors to understand our testing practices, methodologies, and how to participate in making PolicyTracker more robust and efficient.

## Overview

Testing is an integral part of our development process, involving multiple levels of checks and balances to identify and fix issues before deployment. Here’s an overview of our testing approach:

- **Unit Testing**: Focuses on individual components or pieces of code to ensure they work correctly in isolation.
- **Integration Testing**: Examines the interactions between different parts of the application to detect interface defects.
- **Functional Testing**: Verifies that the features of the application function as expected from an end-user perspective.
- **Performance Testing**: Assesses the application’s stability, speed, and scalability under various conditions.
- **Security Testing**: Identifies vulnerabilities within the application to prevent potential security breaches.

## Testing Environment

The testing environment mirrors the production setting as closely as possible to ensure accuracy in testing results. All tests are run in isolated environments to prevent side effects and maintain consistency.

1. **Running Unit and Integration Tests**:
   - Install the necessary dependencies and set up your local development environment.
   - Use the following command to run the test suite: `./manage.py test`
   - Report any failures or issues encountered during testing.

2. **Functional and User Acceptance Testing**:
   - Engage with the application from an end-user perspective.
   - Follow test cases, if provided, or use exploratory testing techniques to uncover issues.
   - Document your findings and provide feedback on user experience improvements.

3. **Performance and Security Testing**:
   - Utilize recommended tools and methodologies for performance and security testing.
   - Identify potential bottlenecks or security vulnerabilities.
   - Share comprehensive reports and recommendations for improvement.

## Reporting Issues

Found a bug or issue? Please report it using the following steps:

1. Check if the issue is already reported in the [Issues section](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/issues) of our GitHub repository.
2. Create a new issue providing a detailed description, steps to reproduce, and the expected vs. actual results.
3. Include any relevant screenshots, error logs, or additional information that could help in diagnosing the issue.

## Continuous Integration (CI) and Continuous Deployment (CD)

Our CI/CD pipeline automates the testing and deployment process, ensuring that new code submissions are automatically built, tested, and prepared for staging or production environments.

# Installation and Configuration Instructions for PolicyTracker

Welcome to PolicyTracker! This document provides detailed instructions on how to install and configure PolicyTracker on your local development environment. Follow these steps to get started with tracking and managing privacy policy updates efficiently.

## Prerequisites

Before you begin the installation process, ensure you have the following prerequisites installed on your system:

- Python 3.8 or later
- pip (Python Package Installer)
- Virtualenv (optional, but recommended for isolating Python environments)
- Git (for cloning the repository)

## Step 1: Clone the Repository

First, clone the PolicyTracker repository to your local machine using Git:

```bash
git clone https://github.comsaikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service.git
```
cd PolicyTracker

## Step 2: Set Up a Virtual Environment
It's recommended to use a virtual environment for Python projects. This keeps dependencies required by different projects separate by creating isolated Python virtual environments for them. To create and activate a virtual environment:


```bash
# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS and Linux
source venv/bin/activate

```

## Step 3: Install Dependencies
With your virtual environment activated, install the project dependencies using pip:

```bash
pip install -r requirements.txt
```

## Step 4: Configure the Application
PolicyTracker uses environment variables for configuration. You'll need to set up these variables according to your environment. Create a file named .env in the project root directory and add your configurations:
```bash 

DEBUG=on
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=.localhost, .yourdomain.com
```

## Step 5: Initialize the Database
Before running the application, you need to make migrations and migrate the database schema:

## Step 6: Run the Development Server
Finally, you can run the Django development server:
```bash
python manage.py runserver


```

Navigate to http://localhost:8000 in your web browser. You should see the PolicyTracker home page, indicating the application is running successfully.

### Additional Configuration
- Email Backend Setup: For sending email notifications, configure your email backend by updating the .env file with your email service credentials.



## Architecture Overview
PolicyTracker is a robust web application designed to monitor and notify users of changes in privacy policies across various websites. This document outlines the detailed architecture of the system, illustrating how the different components interact and work together to provide a seamless experience for the end-user.

![Capstone project drawio](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/476f3a25-e1d9-43eb-94ad-cd92c20b06e6)


## User Interaction
- **Users** initiate HTTPS requests through their web browsers to perform actions such as logging in, submitting URLs for tracking, or receiving updates on policy changes.
- The **Website** serves as the front end, where user inputs are collected and policy changes are displayed.
- An **SMTP Server** handles the sending of periodic notifications and alerts to the users' emails.

## Application Server
- A **URL Dispatcher** in Django routes incoming HTTP requests to their corresponding views based on URL patterns.
- **Views** in Django process user requests, interact with models, and handle business logic.
- **Models** define the application's database schema using Django's ORM.
- **Templates** combine HTML with Django Template Language for dynamic content rendering.

## Backend Services and Data Management
- A **WSGI Server** acts as the middleman between the web server and the Django app.
- A **MySQL Database** is used for persistent storage of user data, tracking information, and change logs.
- **Beautiful Soup 4** is the web scraping library that parses HTML content of privacy policies and extracts relevant information.
- The application generates **HTML** content using templates and Django's rendering engine.

## Styling and Scripting
- **Tailwind CSS** is utilized for responsive and modular design across the application.
- **JavaScript** adds interactivity to webpages, such as client-side validations and dynamic content updates.

## Data Flow and Security
- **HTTPS** ensures secure transmission of data between the user and the application.
- **CSRF Protection** is implemented to safeguard against cross-site request forgery attacks.
- **User Authentication** manages the verification of user identities, with secure password handling.

## Regular Operations and Notifications
- The system performs **Policy Tracking** by regularly sending requests to tracked policy URLs.
- **Change Detection** is conducted by comparing new content against stored versions, logging any differences.
- **Notification Dispatch** sends timely email updates to users when policy changes are detected.

# Load Testing

This document outlines the process for conducting load testing on the PolicyTracker Django application using Postman.

## Overview

Load testing is performed to ensure that our Django-based PolicyTracker application can handle the projected traffic volume and perform optimally under stress.

## Prerequisites

- Django application with CSRF protection
- Postman for making API requests
- A testing environment similar to the production setup

## Setup

1. **Postman Collection**: Create a new collection for your load test in Postman.
2. **Environment Variables**: Set up environment variables for your Postman requests, like domain, endpoints, CSRF tokens, etc.
3. **CSRF Tokens**: If CSRF protection is enabled, make sure to extract and include the CSRF token in your requests.

## Load Testing Steps

1. **Prepare the Application**: Optimize database queries, set up caching, and ensure proper indexing.
2. **Configure Postman Request**: Set up your request method, URL, headers, and any body data required for POST requests.
3. **Include CSRF Token**: Add the retrieved CSRF token to your request headers or body as needed by your application.
4. **Run a Single Request**: Test a single request to ensure that your setup is correct and that you're receiving the expected response.
5. **Monitor Setup**: Configure Postman Monitors or use the Collection Runner to simulate multiple requests from different users.
6. **Analyze Results**: After running the tests, analyze the response times, error rates, and server resource utilization to identify bottlenecks.

## Optimization

![Screenshot 2024-03-30 233358](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/17ecd14f-a6b0-4a19-b317-e7e761c59208)


Based on the test results, make necessary optimizations to the application code, database, server configuration, or architecture.

## Running the Tests
![Screenshot 2024-03-30 233505](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/b4d9afa7-5778-4f9f-9db0-2ea12a923919)

Start the load test by running the configured monitor or collection runner.

## Test Results
![Screenshot 2024-03-30 233957](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/d2100a52-7e2a-4aaf-b8b0-6ceeabf742b7)
![Screenshot 2024-03-30 234042](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/2276efdd-d61f-462b-be5e-70003103577c)


By repeating these steps, you can iteratively improve the performance of your application. The successful handling of 1000 users in a login scenario is a positive indicator, and continuous testing can help maintain and improve this performance as the application evolves.
The application crash during the Postman API load testing with 10,000 users suggests significant resource utilization, likely surpassing the system's capacity. This scenario underscores the necessity for resource optimization and scalability enhancements to ensure stability under high load, highlighting the importance of continuous performance monitoring and system adjustments to accommodate growing user demands efficiently.



# Risk Assessment and Mitigation Strategies for PolicyTracker

The potential risks involved in the development, deployment, and usage of PolicyTracker, along with strategies to mitigate these risks. Our goal is to ensure the reliability, security, and user satisfaction of our application.

## Risk Identification

1. **Security Vulnerabilities**: The application could be vulnerable to various security threats, including SQL injection, Cross-Site Scripting (XSS), and Cross-Site Request Forgery (CSRF).
   
2. **Data Privacy Concerns**: Handling user data, especially in tracking privacy policies, poses a risk to data privacy if not managed properly.
   
3. **Compliance with Legal Regulations**: Non-compliance with legal regulations such as GDPR, CCPA, etc., could lead to legal repercussions and loss of user trust.

4. **Dependency on External Services**: The application relies on external services for data scraping, authentication (OAuth providers), and notifications (email/SMS services), which could lead to failures or disruptions in service.

5. **Performance and Scalability**: Handling a large volume of data and user requests may lead to performance bottlenecks or scalability issues.

## Mitigation Strategies

### Security Vulnerabilities

- **Regular Audits and Updates**: Conduct regular security audits and keep all dependencies up to date to address known vulnerabilities.
  
- **Secure Coding Practices**: Follow secure coding practices and use Django's built-in security features to protect against SQL injection, XSS, CSRF, etc.

### Data Privacy Concerns

- **Data Encryption**: Encrypt sensitive user data both in transit and at rest to protect user privacy.
  
- **Minimal Data Collection**: Collect only the essential data necessary for the application's functionality, adhering to the principle of data minimization.

### Compliance with Legal Regulations

- **Privacy Policy and Terms of Use**: Clearly outline a privacy policy and terms of use, detailing how user data is collected, used, and protected.

- **Regular Legal Consultation**: Consult with legal professionals to ensure ongoing compliance with all relevant regulations.

### Dependency on External Services

- **Fallback Mechanisms**: Implement fallback mechanisms to handle failures of external services gracefully, ensuring minimal impact on the user experience.

- **Service Monitoring**: Actively monitor the status and performance of external services and have contingency plans in place for service outages.

### Performance and Scalability

- **Optimization and Caching**: Optimize database queries and implement caching where appropriate to improve performance.

- **Scalable Architecture**: Design the application with scalability in mind, using cloud services that can automatically scale resources based on demand.

# Roadmap for Beta Release of PolicyTracker

The PolicyTracker team is dedicated to continuous improvement and expansion of our application's capabilities. As we transition from the alpha to the beta release, this document outlines our roadmap, highlighting the key features, enhancements, and milestones we aim to achieve. Our focus is on refining the application based on user feedback, addressing known issues, and incorporating additional functionalities to enrich the user experience.

## Key Features and Enhancements

### Enhanced Security Measures
- Implement advanced security protocols and encryption techniques to fortify user data protection.
  
### Improved Data Processing and Analysis
- Develop a more sophisticated data analysis engine to provide deeper insights into privacy policy changes and their implications.
- Introduce machine learning algorithms to predict potential future changes based on historical data trends.

### User Interface and Experience Improvements
- Redesign the user interface for enhanced usability and accessibility, ensuring a seamless experience across all devices.
- Incorporate user feedback to refine existing features and introduce new ones that address user needs more effectively.

### Expanded Policy Tracking Capabilities
- Introduce the ability for users to group and categorize tracked documents for better organization and access.

### Automated Alerts and Custom Notifications
- Enhance the notification system to allow for more personalized alert settings, including the frequency and types of notifications received.
- Implement AI-driven alerts that notify users of significant changes that could directly impact their privacy or user rights.

### Comprehensive Documentation and Support
- Expand the knowledge base and FAQ section to provide users with more comprehensive guidance on using the application.

# References

- Django Documentation: [Django Docs](https://docs.djangoproject.com/en/5.0/) - Official Django documentation for version 5.0.
- BeautifulSoup4 Package: [PyPI - BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) - Python library for pulling data out of HTML and XML files.
- Fahadul Shadhin's article on Django MVT pattern: [The MVT Design Pattern of Django](https://python.plainenglish.io/the-mvt-design-pattern-of-django-8fd47c61f582?gi=cd5a719aa5a4) - A comprehensive guide to understanding Django's design pattern.
- Django-Tailwind Documentation: [Django Tailwind Docs](https://django-tailwind.readthedocs.io/en/latest/installation.html) - Instructions on integrating Tailwind CSS with Django.
- Django-Tailwind GitHub Repository: [timonweb/django-tailwind](https://github.com/timonweb/django-tailwind) - The GitHub repository for the Django-Tailwind integration package.
- Stack Overflow Discussion on Tailwind CSS with Django: [How to use TailwindCSS with Django](https://stackoverflow.com/questions/63392426/how-to-use-tailwindcss-with-django) - Community solutions for using Tailwind CSS in Django projects.
- Lucidchart: [Lucidchart](https://lucid.app/) - Online diagram software for creating and sharing professional flowcharts, process maps, and more.



# PolicyTracker - Beta Release Overview

## Table of Contents


## Introduction
The beta iteration of PolicyTracker demonstrates 85% completion of our envisioned product suite, showing significant enhancements from the alpha release towards a robust, user-oriented full-scale deployment.

![System Architecture](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/8887619c-809f-439a-9531-b082b16c4c56)
*Figure 1: System Architecture Overview*

## Web Scraping System Flow
PolicyTracker automates the collection, analysis, and storage of online privacy policy data through a sophisticated sequence of operations:

### Website Interaction
- **Data Source**: Begins with websites hosting privacy policies in their native HTML format.
- **Data Gathering Process**: Executes systematic HTTP GET requests to fetch data comprehensively.

``` bash
# Main process begins here
print("Script started.")
url = input("Enter the URL of the privacy policy to scrape: ")
print(f"Fetching privacy policy from: {url}")

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

## Beta Functional Specifications
Our beta release integrates several advanced features designed for effective policy management and user interaction:

### User Management
- **Security**: Implements OAuth for secure authentication and streamlined user experiences.

### Policy Tracking and Management
- **Tracking Features**: Allows users to actively monitor and manage the privacy policies of their interest with automated updates and alerts.

### Data Processing
- **Efficiency**: Features optimized data processing routines to ensure rapid content retrieval and transformation.

## Quality Criteria for Beta Functionality
The beta release of PolicyTracker is assessed through rigorous quality criteria, ensuring its readiness for limited production deployment:

### Functionality Completion
- **Implementation Coverage**: About 85% of the planned features are fully functional, enhancing user interactions and system usability.

### System Resilience
- **Operational Continuity**: Ensures high availability and minimal downtime through resilient system design.
- **Stress Testing**: Demonstrates the system's capacity to handle peak loads and maintain performance.

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
![Screenshot 2024-04-21 222612](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/b2fb01fb-15c5-437b-bcff-7818a4a6ffd1)

## Execution and Results
Scalability and Performance: Confirmed the script's ability to process numerous privacy policy URLs concurrently without degradation in speed or accuracy.

![Screenshot 2024-04-21 222638](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/095ce474-3e4a-4753-8369-78a8ad95d974)


## Installation
Clone the repository and install the necessary dependencies to get PolicyTracker running:

``` bash
git clone https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service.git
cd Scripts_Store_History
pip install -r requirements.txt
```

## Conclusion
The PolicyTracker system has demonstrated significant capabilities in the field of privacy policy tracking, offering robust tools to users for managing and staying updated on policy changes. The alpha and beta releases showcase a solid foundation with essential functionalities that enhance user engagement and system reliability. Through comprehensive command line testing, the application has proven its ability to handle multiple operations simultaneously, ensuring scalability and performance under load.

The installation process has been streamlined to allow for easy setup, enabling users and developers alike to deploy PolicyTracker efficiently. With ongoing improvements and community feedback, PolicyTracker aims to become the leading solution in privacy policy management.



