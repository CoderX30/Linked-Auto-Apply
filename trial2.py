import os
import shutil

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_logpath() -> str:
    return os.path.join(os.getcwd(), 'selenium.log')

def get_chromedriver_path() -> str:
    return shutil.which('chromedriver')


def get_webdriver_service(logpath) -> Service:
    service = Service(
        executable_path=get_chromedriver_path(),
        log_output=logpath,
    )
    return service




def get_webdriver_options(proxy: str, socksStr: str) -> Options:
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument('--ignore-certificate-errors')
    if proxy is not None:
        options.add_argument(f"--proxy-server={socksStr}://{proxy}")
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    return options




logpath = get_logpath()
service = get_webdriver_service(logpath=logpath)



print(logpath)

def get_ip_address(options, service):
    with webdriver.Chrome(options=options, service=service) as driver:
        driver.get("https://www.google.com/")
        print(driver.find_element(By.TAG_NAME, "body").text)
