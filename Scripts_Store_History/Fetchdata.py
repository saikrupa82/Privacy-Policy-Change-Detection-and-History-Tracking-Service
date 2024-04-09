import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json
from datetime import datetime
import difflib

def fetch_and_parse(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
        else:
            print(f"Failed to fetch the page: status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    return None

def extract_sections(soup):
    sections = {}
    current_heading = None
    for element in soup.find_all(['h2', 'p']):
        if element.name == 'h2':
            current_heading = element.get_text(strip=True)
            sections[current_heading] = []
        elif element.name == 'p' and current_heading:
            sections[current_heading].append(element.get_text(strip=True))
    return sections

def compare_and_update_history(url, new_content):
    history_filename = urlparse(url).netloc.replace('www.', '') + '_history.json'
    try:
        with open(history_filename, 'r', encoding='utf-8') as file:
            history = json.load(file)
    except FileNotFoundError:
        history = {}

    last_update = history.get('last_update', {})
    changes_detected = False
    detailed_changes = []

    for section, texts in new_content.items():
        old_texts = last_update.get(section, [])
        diff = list(difflib.unified_diff(old_texts, texts, lineterm=''))
        if diff:
            changes_detected = True
            detailed_changes.append((section, diff))

    timestamp = datetime.now().isoformat()
    if changes_detected or not history:
        if not history.get('changes'):
            history['changes'] = []
        history['changes'].append({
            'timestamp': timestamp,
            'content': new_content
        })

        # Marking the new content explicitly
        new_content_with_meta = {'content': new_content, 'timestamp': timestamp, 'status': 'new'}
        history['last_update'] = new_content_with_meta

        with open(history_filename, 'w', encoding='utf-8') as file:
            json.dump(history, file, ensure_ascii=False, indent=4)

        print(f"Changes detected and saved on {timestamp}")
        for section, changes in detailed_changes:
            print(f"Changes in '{section}':")
            for change in changes:
                print(change)
    else:
        print("No changes detected.")
    
    # Always update 'last_checked' to reflect the script's latest run
    history['last_checked'] = timestamp
    with open(history_filename, 'w', encoding='utf-8') as file:
        json.dump(history, file, ensure_ascii=False, indent=4)
    print(f"Last checked: {history.get('last_checked', 'N/A')}")

def scrape_privacy_policy(url):
    soup = fetch_and_parse(url)
    if not soup:
        print("Could not parse the webpage.")
        return

    content = extract_sections(soup)
    compare_and_update_history(url, content)

# Example usage:
url = input("Enter the URL of the privacy policy to scrape: ")
scrape_privacy_policy(url)
