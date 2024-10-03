from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import sys

def debug_info():
    print("Python version:", sys.version)
    print("Python executable:", sys.executable)
    print("Current working directory:", os.getcwd())
    print("Contents of current directory:", os.listdir())
    print("Environment variables:", dict(os.environ))

def automation(linkedin_username, linkedin_password, search_query):
    debug_info()
    
    # Set up Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    print("Initializing webdriver...")
    # Initialize the Chrome driver using selenium-wire
    driver = webdriver.Chrome(options=chrome_options)
    print("OPENED CHROME IN HEADLESS MODE")

    try:
        print("Navigating to Google Maps...")
        driver.get("https://www.google.com/maps")
        print("Opened Google Maps")

        print("Waiting for search box...")
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchboxinput"))
        )
        print("Search box found")
        
        print(f"Entering search query: {search_query}")
        search_box.send_keys(search_query)
        search_box.submit()

        print(f"Searched for: {search_query}")

        print("Waiting for search results...")
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "section-result"))
            )
            print("Search results loaded")
        except TimeoutException:
            print("Search results took too long to load")

        result_url = driver.current_url
        print(f"Search result URL: {result_url}")

        return result_url

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

    finally:
        print("Closing webdriver...")
        driver.quit()
