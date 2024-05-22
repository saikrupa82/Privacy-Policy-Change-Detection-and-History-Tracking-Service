import json

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

# Usage example:
file_path = 'policies_google_com_93d682f070/20240506_history.json'
keyword = 'maps'  # Example keyword to search for
sections = extract_section_by_keyword(file_path,keyword)
print(sections)