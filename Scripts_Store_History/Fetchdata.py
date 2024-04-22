import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json
from datetime import datetime
import difflib
import os
import polipy
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

def find_html_files(directory):
    print(f"Searching for HTML files in directory: {directory}")
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    print(f"Found {len(html_files)} HTML files.")
    return html_files

def scrape_privacy_policy(file_path, history_folder):
    print(f"Starting to scrape privacy policy from: {file_path}")
    soup = fetch_and_parse(file_path)
    if not soup:
        print("Could not parse the HTML file, skipping.")
        return
    content = extract_sections(soup)
    compare_and_update_history(file_path, content, history_folder)
    print(f"Finished processing: {file_path}")

# Main process begins here
print("Script started.")
url = input("Enter the URL of the privacy policy to scrape: ")
print(f"Fetching privacy policy from: {url}")

# Placeholder for actual scraping functionality
result = polipy.get_policy(url, screenshot=True)
result.save(output_dir='.')

print("Determining the output directory based on the domain of the URL.")
domain_prefix = urlparse(url).netloc.replace('www.', '').split('.')[0]

html_files = []
for folder in os.listdir():
    if os.path.isdir(folder) and folder.startswith(domain_prefix):
        folder_path = os.path.join(os.getcwd(), folder)
        html_files.extend(find_html_files(folder_path))

print("List of HTML files to process:")
print(html_files)

for html_file in html_files:
    history_folder = os.path.abspath(os.path.join(html_file, os.pardir))
    scrape_privacy_policy(html_file, history_folder)

print("Script completed.")

