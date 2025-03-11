from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def scrape_learning_resources(role):
    # Set up Selenium with headless Chrome
    options = Options()
    options.add_argument("--headless")  # Run without opening a browser window
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    resources = []

    try:
        # Scrape Coursera
        coursera_url = f"https://www.coursera.org/search?query={role}%20skills"
        driver.get(coursera_url)
        time.sleep(3)  # Wait for page to load
        
        coursera_elements = driver.find_elements(By.CSS_SELECTOR, "a[data-click-key='search.search.click.search_card']")
        for element in coursera_elements[:5]:  # Limit to top 5
            title = element.text.strip()
            href = element.get_attribute("href")
            if title and href:
                resources.append(f"Coursera: {title} - {href}")

        
        

        return resources if resources else ["No resources found."]
    except Exception as e:
        return [f"Error fetching resources: {e}"]
    finally:
        driver.quit()

