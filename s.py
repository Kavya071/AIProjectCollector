from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
import re  # For cleaning illegal characters

# Function to clean illegal characters
def clean_text(text):
    # Remove non-printable or illegal characters
    return re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)

# Initialize Selenium WebDriver
service = Service('C:\\Users\\rj270\\Desktop\\chromedriver-win64\\chromedriver.exe  ')  # Replace with the actual path to your chromedriver
driver = webdriver.Chrome(service=service)

# Base URL for the job search
base_url = "https://www.freelancer.com/job-search/ai/"
all_projects = []  # List to store project details

# Loop through pages 1 to 40
for page in range(1, 41):
    print(f"Scraping Page {page}...")
    # Generate the page URL
    url = f"{base_url}{page}/" if page > 1 else base_url
    driver.get(url)
    
    # Wait for the page to load
    time.sleep(5)
    
    # Parse page content using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Find all project containers
    project_containers = soup.find_all('div', class_='JobSearchCard-item-inner')
    
    # Extract details for each project
    for project in project_containers:
        try:
            # Title
            title = project.find('a', class_='JobSearchCard-primary-heading-link')
            title_text = clean_text(title.text.strip()) if title else "N/A"
            
            # Average Bid
            avg_bid = project.find('div', class_='JobSearchCard-primary-price')
            avg_bid_text = clean_text(avg_bid.text.strip().split('\n')[0]) if avg_bid else "N/A"
            
            # Skills
            skills_container = project.find('div', class_='JobSearchCard-primary-tags')
            skills = [clean_text(skill.text.strip()) for skill in skills_container.find_all('a')] if skills_container else []
            
            # Number of Bids
            bids = project.find('div', class_='JobSearchCard-secondary-entry')
            bids_text = clean_text(bids.text.strip()) if bids else "N/A"
            
            # Description
            description = project.find('p', class_='JobSearchCard-primary-description')
            description_text = clean_text(description.text.strip()) if description else "N/A"
            
            # Add project details to the list
            all_projects.append({
                'Title': title_text,
                'Average Bid': avg_bid_text,
                'Skills': ', '.join(skills),
                'Number of Bids': bids_text,
                'Description': description_text
            })
        except Exception as e:
            print(f"Error extracting project details: {e}")
    
    # Break if no projects are found (indicating the last page)
    if not project_containers:
        print(f"No projects found on Page {page}. Ending scraping.")
        break

# Close the browser
driver.quit()

# Create a DataFrame from the collected data
df = pd.DataFrame(all_projects)

# Save the DataFrame to an Excel file
output_file = "projects_data_cleaned.xlsx"
df.to_excel(output_file, index=False, engine='openpyxl')  # Ensure `openpyxl` is installed for Excel export

print(f"\nScraping complete! Project details saved to '{output_file}'.")
