import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json
from datetime import datetime
import difflib
import os
import polipy
import smtplib
from email.mime.text import MIMEText
import logging
import re

from collections import defaultdict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(subject, body, sender, recipients, password):
    if isinstance(body, list):
        body = "\n\n".join(f"Section: {section}\n" + "\n".join(diff) for section, diff in body)

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
            smtp_server.starttls()
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
        logging.info("Email sent successfully!")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def fetch_and_parse(file_path):
    logging.info(f"Attempting to read and parse the file at: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')
            logging.info("File successfully parsed.")
            return soup
    except Exception as e:
        logging.error(f"Failed to read or parse the file due to: {e}")
    return None

def extract_sections(soup):
    logging.info("Extracting sections from HTML content.")
    sections = {}
    current_heading = None
    for element in soup.find_all(['h2', 'p']):
        if element.name == 'h2':
            current_heading = element.get_text(strip=True)
            sections[current_heading] = []
        elif element.name == 'p' and current_heading:
            sections[current_heading].append(element.get_text(strip=True))
    logging.info("Sections successfully extracted.")
    return sections

def compare_and_update_history(file_path, new_content, history_folder):
    recipients = input("Enter the recipient's email (comma-separated if multiple): ").split(',')
    subject = "Privacy Policy Changes Report"
    logging.info(f"Checking for existing history in: {history_folder}")
    os.makedirs(history_folder, exist_ok=True)
    history_filename = os.path.join(history_folder, os.path.basename(file_path).replace('.html', '_history.json'))

    history = {}
    try:
        with open(history_filename, 'r', encoding='utf-8') as file:
            history = json.load(file)
            logging.info("Existing history found and loaded.")
    except FileNotFoundError:
        logging.info("No history file found, creating a new one.")

    changes_detected, detailed_changes = compare_contents(history.get('last_update', {}), new_content)

    if changes_detected:
        logging.info("Changes detected. Updating history and sending email.")
        update_history_file(history, history_filename, new_content, detailed_changes)
        send_email(subject, detailed_changes, 'your_email@example.com', recipients, 'your_password')
    else:
        logging.info("No changes detected.")

def compare_contents(last_update, new_content):
    changes_detected = False
    detailed_changes = []
    for section, texts in new_content.items():
        old_texts = last_update.get('content', {}).get(section, [])
        diff = list(difflib.unified_diff(old_texts, texts, lineterm=''))
        if diff:
            changes_detected = True
            detailed_changes.append((section, diff))
    return changes_detected, detailed_changes

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
            if date_int > latest_date:
                latest_date = date_int

    # Debug output: latest date found
    print("Latest date overall:", latest_date)

def update_history_file(history, filename, new_content, changes):
    timestamp = datetime.now().isoformat()
    history.setdefault('changes', []).append({
        'timestamp': timestamp,
        'content': new_content
    })
    history['last_update'] = {
        'content': new_content,
        'timestamp': timestamp,
        'detailed_changes': changes
    }
    history['last_checked'] = datetime.now().isoformat()
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(history, file, ensure_ascii=False, indent=4)
    logging.info("History updated and saved.")

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
    print(f"Finished processing: {file_path}")

def process_url(url, history_folder):
    """
    Process the privacy policy by scraping directly from the provided URL and handling only the latest HTML file.
    
    Args:
        url (str): URL to scrape.
        history_folder (str): Directory where history is tracked.
    """
    logging.info(f"Fetching privacy policy from: {url}")
    # Assuming polipy.get_policy returns an object that can save HTML content locally
    result = polipy.get_policy(url, screenshot=True)
    # Save to a directory named after the domain to avoid conflicts
    domain_prefix = urlparse(url).netloc.replace('www.', '').split('.')[0]
    result.save(output_dir='.')
    

    # Find the latest HTML file in the saved directory
    latest_html_file = find_latest_html_file(history_folder)
    if latest_html_file:
        logging.info(f"Processing the latest HTML file: {latest_html_file}")
        scrape_privacy_policy(latest_html_file, history_folder)
    else:
        logging.warning("No HTML files found to process.")

def find_latest_html_file(directory):
    """
    Identify the most recently modified HTML file in a directory.
    
    Args:
        directory (str): Directory to search for HTML files.
    
    Returns:
        str: Path to the latest HTML file.
    """
    html_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.html')]
    if not html_files:
        logging.info("No HTML files found.")
        return None
    # Get the file with the latest modification time
    latest_html_file = max(html_files, key=os.path.getmtime)
    return latest_html_file




def process_file(file_path, history_folder):
    """Process the privacy policy from an existing HTML file."""
    logging.info(f"Processing file from path: {file_path}")
    scrape_privacy_policy(file_path, history_folder)

def find_html_files(directory):
    print(f"Searching for HTML files in directory: {directory}")
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    print(f"Found {len(html_files)} HTML files.")
    return html_files


def main():
    logging.info("Script started.")
    user_choice = input("Do you want to provide a URL or a file path? Enter 'url' or 'file': ").strip().lower()

    if user_choice == 'url':
        url = input("Enter the URL of the privacy policy to scrape: ").strip()
        history_folder = os.path.join(os.getcwd(), "history")
        process_url(url, history_folder)
    elif user_choice == 'file':
        file_path = input("Enter the path of the HTML file to process: ").strip()
        history_folder = os.path.join(os.path.dirname(file_path), "history")
        process_file(file_path, history_folder)
    else:
        logging.error("Invalid input. Please enter either 'url' or 'file'.")

    logging.info("Script completed.")

if __name__ == "__main__":
    main()
