# PolicyTracker - Privacy Policy Tracking System

PolicyTracker is an innovative solution designed to keep users informed about the updates and changes to the privacy policies of various online services. This document outlines the core functionalities of PolicyTracker, focusing on its features, security measures, and the future direction of the platform.

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
![image](https://github.com/saikrupa82/Privacy-Policy-Change-Detection-and-History-Tracking-Service/assets/46783175/67384de9-1848-4142-bc1e-2e835a53d8eb)

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

Include a summary of the test results here, outlining performance metrics and any identified issues.

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

