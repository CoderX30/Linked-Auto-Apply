import os
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Function to open a URL in a browser using Selenium
def open_url_in_browser(url):
    try:
        # Get chromium binary path from the environment or set default
        chrome_bin = os.getenv('CHROME_BIN', '/usr/bin/chromium-browser')
        chrome_driver_bin = os.getenv('CHROMEDRIVER', '/usr/bin/chromedriver')

        # Configure Selenium options for Chromium
        options = webdriver.ChromeOptions()
        options.binary_location = chrome_bin
        options.add_argument("--headless")  # Run headless for cloud or CI/CD environments
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # Initialize the WebDriver
        service = Service(chrome_driver_bin)
        driver = webdriver.Chrome(service=service, options=options)

        # Open the provided URL
        driver.get(url)

        # Keep browser open for a while (e.g., 10 seconds)
        time.sleep(10)
        driver.quit()

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit UI
st.title("URL Opener with Selenium (Chromium)")

# Input for URL
url = st.text_input("Enter the URL you want to open:")

# Button to trigger the URL opening
if st.button("Open URL"):
    if url:
        open_url_in_browser(url)
    else:
        st.error("Please enter a valid URL.")
