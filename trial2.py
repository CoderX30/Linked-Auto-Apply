import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

# Cache the resource to avoid creating multiple drivers during reruns
@st.cache_resource
def get_driver():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")  # Run in headless mode to avoid opening a browser
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
        options=options,
    )
    return driver

# Streamlit code
st.title("Selenium with Streamlit")

# Fetching the page using Selenium
driver = get_driver()
driver.get("http://example.com")

# Display the HTML page source in the Streamlit app
st.code(driver.page_source)
