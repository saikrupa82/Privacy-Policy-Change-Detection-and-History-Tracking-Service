import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json
from datetime import datetime
import difflib
import os
import polipy  # Ensure polipy is properly installed and configured
import re
from collections import defaultdict
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender, recipients, password):
    """Sends an email to specified recipients with the given subject and body.
    Arguments:
        subject (str): Subject line of the email.
        body (str or list): Body of the email. If list, it is formatted before sending.
        sender (str): Email address of the sender.
        recipients (list): List of email addresses of the recipients.
        password (str): Password for the sender's email account.
    Returns:
        None: Outputs success or failure message to console.
    """
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


def fetch_and_parse(file_path):
    """Reads and parses an HTML file into a BeautifulSoup object.
    Arguments:
        file_path (str): Path to the HTML file.
    Returns:
        soup (BeautifulSoup object or None): Parsed HTML content or None if failed.
    """
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
    """Extracts and organizes text sections from the parsed HTML by headings.
    Arguments:
        soup (BeautifulSoup object): Parsed HTML content.
    Returns:
        sections (dict): Dictionary of sections with headings as keys and list of paragraphs as values.
    """
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


def compare_and_update_history(file_path, new_content, history_folder):
    """Compares new content with the last recorded history, updates the history, and sends email notifications if changes are detected.
    Arguments:
        file_path (str): Path of the current HTML file being processed.
        new_content (dict): Dictionary containing the latest content to be compared.
        history_folder (str): Path to the directory where the history files are stored.
    Returns:
        None: Outputs process status messages to console.
    """
    recipients = input("Enter the recipient's email (comma-separated if multiple): ").split(',')
    subject = "Privacy Policy Changes Report for " + domain_email
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
        send_email(subject, detailed_changes, 'saikrupar82@gmail.com', recipients, 'vbdd sxlv kdug pwes')
    else:
        print("No changes detected.")

    print("Updating the last checked timestamp.")
    history['last_checked'] = datetime.now().isoformat()

    print("Saving the history to file.")
    with open(history_filename, 'w', encoding='utf-8') as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

def find_html_files(directory):
    """Finds all HTML files within a given directory and its subdirectories.
    Arguments:
        directory (str): Path to the directory to search.
    Returns:
        html_files (list): List of paths to HTML files found.
    """
    print(f"Searching for HTML files in directory: {directory}")
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    print(f"Found {len(html_files)} HTML files.")
    return html_files

# Function to clean old history files


# Function to clean old history files, excluding `.html` files
def clean_old_history_files(directory):
    pattern = re.compile(r'(\d{8})\.(json|meta|png|history\.json)$')
    latest_date = 0
    all_files = []

    # First pass to gather all files and determine the latest date
    print("Scanning directory:", directory)
    for file_name in os.listdir(directory):
        match = pattern.search(file_name)
        if match:
            date_str = match.group(1)
            date_int = int(date_str)
            all_files.append((date_int, file_name))
            if date_int < latest_date:
                latest_date = date_int

    # Debug output: latest date found
    print("Latest date overall:", latest_date)

    # Second pass to delete old history files (excluding `.html` files)
    print("\nStarting deletion of old files...")
    print(all_files)
    for date_int, file_name in all_files:
        if date_int != latest_date:
            file_path = os.path.join(directory, file_name)
            print(f"Deleting: {file_path}")
            os.remove(file_path)

    print("Deletion completed.")

def extract_section_by_keyword(file_path, keyword):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Store results in a dictionary
    results = {}
    # Loop through each change record in the JSON file
    for change in data['changes']:
        # Search each section within the content
        for section, content in change['content'].items():
            # Check if keyword is in any text within the content list
            if any(keyword.lower() in text.lower() for text in content):
                results[section] = content
    
    return results

domain_email =''
# Modify scrape_privacy_policy to call clean_old_history_files
def scrape_privacy_policy(file_path, history_folder):
    print(f"Starting to scrape privacy policy from: {file_path}")
    soup = fetch_and_parse(file_path)
    if not soup:
        print("Could not parse the HTML file, skipping.")
        return

    content = extract_sections(soup)
    compare_and_update_history(file_path, content, history_folder)
    
    # Clean old history files in the given history folder
    clean_old_history_files(history_folder)
    print(history_folder)
    keyword = input('Enter the keyword :')
    print(extract_section_by_keyword(history_folder,keyword))
    print(f"Finished processing: {file_path}")


def get_user_input():
    """
    Prompt the user to specify whether they want to provide a URL or a file path.
    Returns:
        choice (str): The user's choice as either 'url' or 'file'.
    """
    choice = input("Do you want to provide a URL or a file path? Enter 'url' or 'file': ").strip().lower()
    return choice

def process_url(url, history_folder):
    """
    Fetches the privacy policy from a URL using polipy, saves it locally, and processes the policy.
    Arguments:
        url (str): URL of the privacy policy to scrape.
        history_folder (str): Path to the directory where the history of policy changes will be stored.
    Returns:
        None: Outputs processing status messages to console and handles files directly.
    """
    result = polipy.get_policy(url, screenshot=True)
    result.save(output_dir='.')
    domain_email = urlparse(url).netloc.replace('www.', '').split('/')[0]
    domain_prefix = urlparse(url).netloc.replace('www.', '').split('.')[0]
    html_files = []
    for folder in os.listdir():
        if os.path.isdir(folder) and folder.startswith(domain_prefix):
            folder_path = os.path.join(os.getcwd(), folder)
            html_files.extend(find_html_files(folder_path))
    latest_html_file = max(html_files, key=os.path.getmtime)
    print("folder_path:", folder_path, "history_folder :", history_folder)
    scrape_privacy_policy(latest_html_file, folder_path)

def process_file(file_path, history_folder):
    """
    Processes an existing HTML file to extract and compare privacy policy changes.
    Arguments:
        file_path (str): Path to the HTML file to process.
        history_folder (str): Path to the directory where the history of policy changes will be stored.
    Returns:
        None: Processes the HTML file and updates history accordingly.
    """
    scrape_privacy_policy(file_path, history_folder)

def main():
    """
    Main function to orchestrate the process based on user input. This function directs whether to process a URL or a file based on user's choice.
    Returns:
        None: Completes the user-directed action and terminates.
    """
    print("Script started.")
    user_choice = get_user_input()

    if user_choice == 'url':
        url = input("Enter the URL of the privacy policy to scrape: ").strip()
        history_folder = os.path.join(os.getcwd(), "history")
        process_url(url, history_folder)
    elif user_choice == 'file':
        file_path = input("Enter the path of the HTML file to process: ").strip()
        history_folder = os.path.join(os.path.dirname(file_path), "history")
        process_file(file_path, history_folder)
    else:
        print("Invalid input. Please enter either 'url' or 'file'.")

    print("Script completed.")

if __name__ == "__main__":
    main()

