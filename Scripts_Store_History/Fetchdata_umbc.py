import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        print(f"Failed to fetch the page: status code {response.status_code}")
        return None

def extract_policy_sections(soup):
    sections = {}
    content = soup.find(class_="entry-content")  # Adjust the class name if necessary

    if content:
        for h2 in content.find_all('h2'):
            section_title = h2.get_text(strip=True)
            section_paragraphs = []
            
            # Iterate through next siblings of h2 until another h2 or non-<p> is found
            for sibling in h2.find_next_siblings():
                if sibling.name == 'h2':
                    break  # Stop if we hit another section heading
                if sibling.name == 'p':
                    section_paragraphs.append(sibling.get_text(strip=True))
            
            # Combine paragraphs to form the section content
            sections[section_title] = ' '.join(section_paragraphs)
    else:
        print("Could not find the content section.")
        
    return sections

def scrape_privacy_policy(url):
    soup = fetch_and_parse(url)
    if not soup:
        print("Could not parse the webpage.")
        return

    policy_sections = extract_policy_sections(soup)
    for title, content in policy_sections.items():
        print(f"Section: {title}\nContent: {content}\n{'-'*80}\n")

# URL to scrape
url = "https://privacy.umbc.edu/web-site-privacy-statement/"
scrape_privacy_policy(url)
