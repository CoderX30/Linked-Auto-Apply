import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Function to open a URL in a browser using Selenium
def open_url_in_browser(url):
    try:
        # Specify the path to the Chromium binary and driver
        options = webdriver.ChromeOptions()
        options.binary_location = "/usr/bin/chromium-browser"  # Path to Chromium
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")  # To run it in headless mode (if needed)
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")

        # Initialize the Chromium WebDriver
        service = Service('/usr/bin/chromedriver')  # Path to Chromium driver
        driver = webdriver.Chrome(service=service, options=options)

        # Open the given URL
        driver.get(url)

        # Keep the browser open for a certain time (e.g., 10 seconds)
        time.sleep(10)
        
        # Close the browser
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
