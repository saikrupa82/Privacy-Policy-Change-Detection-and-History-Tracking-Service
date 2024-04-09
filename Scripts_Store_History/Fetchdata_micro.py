import requests
from bs4 import BeautifulSoup

def scrape_privacy_policy(url):
    # Send a GET request to the given URL
    response = requests.get(url)
    
    # If the GET request is successful, proceed to scrape the page
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Initialize a dictionary to store the sections and their content
        sections = {}
        
        # Find the heading using its ID and then find the corresponding content by ID
        heading_id = 'mainpersonaldatawecollect_Header'  # This might need to be adjusted based on actual ID
        content_id = 'mainpersonaldatawecollect_ShortDescription'  # This is the ID you provided
        
        # Find the heading element
        heading_element = soup.find(id=heading_id)
        if heading_element:
            # Extract the heading text
            heading_text = heading_element.get_text(strip=True)
            
            # Find the content element by ID
            content_element = soup.find(id=content_id)
            if content_element:
                # Extract the content text
                content_text = content_element.get_text(separator=' ', strip=True)
                
                # Store the content in the dictionary
                sections[heading_text] = content_text
            else:
                print(f"No content found for ID {content_id}")
        else:
            print(f"No heading found for ID {heading_id}")
            
        # Save the content to a file
        filename = 'privacy_policy_content.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            for heading, content in sections.items():
                file.write(f"Section: {heading}\nContent: {content}\n\n")
                
        print(f"Content saved to {filename}")
        
    else:
        print(f"Failed to fetch the page: status code {response.status_code}")

# URL of the Microsoft Privacy Statement
url = "https://privacy.microsoft.com/en-us/privacystatement"
scrape_privacy_policy(url)
