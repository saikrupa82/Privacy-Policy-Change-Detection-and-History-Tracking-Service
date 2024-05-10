import json



# Usage example:
file_path = 'policies_google_com_93d682f070/20240506_history.json'
keyword = 'maps'  # Example keyword to search for
sections = extract_section_by_keyword(file_path,keyword)
print(sections)