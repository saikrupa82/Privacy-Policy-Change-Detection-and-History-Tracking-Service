import os
import json
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def fetch_and_parse(file_path):
    """Reads a local HTML file and parses it into a BeautifulSoup object."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return BeautifulSoup(file.read(), 'html.parser')
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

def extract_sections(soup):
    """Extracts text sections from the parsed HTML based on heading and paragraph tags."""
    sections = {}
    current_heading = None
    for element in soup.find_all(['h2', 'p']):
        if element.name == 'h2':
            current_heading = element.get_text(strip=True)
            sections[current_heading] = []
        elif element.name == 'p' and current_heading:
            sections[current_heading].append(element.get_text(strip=True))
    return sections

def compare_and_update_history(file_path, new_content):
    """Compares new content with existing history, updates if changes are detected."""
    base_folder = os.path.dirname(file_path)
    os.makedirs(base_folder, exist_ok=True)
    history_file = os.path.join(base_folder, os.path.basename(file_path).replace('.html', '_history.json'))
    
    try:
        with open(history_file, 'r', encoding='utf-8') as file:
            history = json.load(file)
    except FileNotFoundError:
        history = {}

    if 'last_update' not in history or history['last_update']['content'] != new_content:
        timestamp = datetime.now().isoformat()
        history.setdefault('changes', []).append({'timestamp': timestamp, 'content': new_content})
        history['last_update'] = {'timestamp': timestamp, 'content': new_content}
        print(f"Changes detected; history updated on {timestamp}.")
    else:
        print("No changes detected since the last update.")

    # Always update the last_checked timestamp
    history['last_checked'] = datetime.now().isoformat()
    with open(history_file, 'w', encoding='utf-8') as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

def scrape_privacy_policy(file_path):
    """Scrapes a privacy policy from a local HTML file and manages its historical data."""
    soup = fetch_and_parse(file_path)
    if not soup:
        print("Failed to parse the file.")
        return
    content = extract_sections(soup)
    compare_and_update_history(file_path, content)

def main():
    # Placeholder import and scraping mechanism
    import polipy  

    url = input("Enter the URL of the privacy policy to scrape: ")
    result = polipy.get_policy(url, screenshot=True)
    domain_name = urlparse(url).netloc.replace('www.', '').split('.')[0]
    output_dir = os.path.join(os.getcwd(), domain_name)

    os.makedirs(output_dir, exist_ok=True)
    # Save the result in a standardized location
    result.save(output_dir)
    
    html_files = [f for f in os.listdir(output_dir) if f.endswith('.html')]
    print("HTML files found:", html_files)

    for file in html_files:
        scrape_privacy_policy(os.path.join(output_dir, file))

if __name__ == "__main__":
    main()
