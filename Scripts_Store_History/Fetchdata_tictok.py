import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        print(f"Failed to fetch the page: status code {response.status_code}")
        return None

def extract_content(soup):
    sections = {}

    # Extract the pre-content section
    pre_content = soup.find('section', {'data-testid': 'policy-card-pre-content'})
    if pre_content:
        sections['Introduction'] = pre_content.get_text(separator='\n', strip=True)

    # Extract the post-content sections with headings and paragraphs
    post_content_sections = soup.find_all('section', {'data-testid': 'policy-card-post-content'})
    for section in post_content_sections:
        h3_headings = section.find_all('h3')
        for h3 in h3_headings:
            heading_text = h3.get_text(strip=True)
            # Find all subsequent <p> tags until the next <h3> tag
            content_paragraphs = []
            next_sibling = h3.find_next_sibling()
            while next_sibling and next_sibling.name != 'h3':
                if next_sibling.name == 'p':
                    content_paragraphs.append(next_sibling.get_text(strip=True))
                next_sibling = next_sibling.find_next_sibling()
            sections[heading_text] = '\n'.join(content_paragraphs)
    
    return sections

def save_to_file(filename, sections):
    with open(filename, 'w', encoding='utf-8') as file:
        for heading, content in sections.items():
            file.write(f"{heading}\n{content}\n\n")

# The URL for the TikTok privacy policy
url = "https://www.tiktok.com/legal/privacy-policy?lang=en"

# Scrape the content
soup = fetch_and_parse(url)
if soup:
    content = extract_content(soup)
    # Save the content to a text file
    filename = 'tiktok_privacy_policy.txt'
    save_to_file(filename, content)
    print(f"Content saved to {filename}")
else:
    print("Content could not be scraped.")
