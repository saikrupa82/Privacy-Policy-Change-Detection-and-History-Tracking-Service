from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup the Selenium WebDriver (e.g., Chrome)
driver = webdriver.Chrome("C:/Users/Owner/Desktop/chromedriver.exe")

# Open the web page
driver.get("https://privacy.microsoft.com/en-us/privacystatement")

# Wait for the element to be clickable, and then simulate a click
wait = WebDriverWait(driver, 10)

# IDs of elements to click
ids_to_click = [
    "divmainpersonaldatawecollect",
    "divmainhowweusepersonaldata",
    # Add all other IDs you need to click on
]

sections_data = {}

# Iterate through each ID, click the element, and then scrape the content
for element_id in ids_to_click:
    try:
        # Find the element and click it
        element = wait.until(EC.element_to_be_clickable((By.ID, element_id)))
        element.click()

        # After clicking, you can fetch the content that is now visible
        content = driver.find_element_by_id(f"{element_id}_ShortDescription").text
        sections_data[element_id] = content
    except Exception as e:
        print(f"An error occurred: {e}")

# Close the WebDriver
driver.quit()

# Now you would write sections_data to a file or process it as needed
