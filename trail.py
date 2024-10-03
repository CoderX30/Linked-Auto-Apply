# Importing the libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.core.os_manager import ChromeType
from plyer import notification
import streamlit as st
import time
print("LIBRARIES IMPORTED")



def automation(linkedin_username, linkedin_password, search_query):
    # Linkedin credentials
    linkedin_username = linkedin_username
    linkedin_password = linkedin_password

    # Initialize the Chrome driver

    # Cache the resource to avoid creating multiple drivers during reruns
    @st.cache_resource
    def get_driver():
        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--start-maximized")
        # options.add_argument("--disable-gpu")
        # options.add_argument("--headless")  # Run in headless mode to avoid opening a browser
         driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
        options=options,
        )
        print("OPENED CHROME")
        return driver

    driver = get_driver()
    
    # Open LinkedIn login page
    def open_linkedin():
        driver.get('https://www.linkedin.com/login')
        print("OPENED LINKEDIN")

    # Logging in
    def credentials():
        # Enter username
        username_field = driver.find_element(By.ID, 'username')
        username_field.send_keys(linkedin_username)

        # Enter password
        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys(linkedin_password)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)

        # Wait for login to complete
        time.sleep(5)
        print("LOGGED IN")

    # -----------------------------------------------------------------------------------------------------

    # GETTING READY FOR JOB SEARCH
    open_linkedin()
    time.sleep(5)
    credentials()
    time.sleep(5)

    # GETTING READY FOR CONNECTION REQUESTS
    driver.execute_script("window.open('');")  # This opens a new blank tab
    driver.switch_to.window(driver.window_handles[-1])
    open_linkedin()
    time.sleep(5)


    # -----------------------------------------------------------------------------------------------------
    # JOB SEARCH
    driver.switch_to.window(driver.window_handles[0])


    ## Search
    # Define the search query
    search_query = search_query

    # Locate the search bar
    search_bar = driver.find_element(By.XPATH, '//input[@aria-label="Search"]')

    # Enter the search query
    search_bar.send_keys(search_query)

    # Submit the search
    search_bar.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(5)

    people_button = driver.find_element(By.XPATH, '//button[text()="Jobs"]')
    people_button.click()

    # Wait for the job results to load
    time.sleep(5)
    print("JOB PREFERENCE ENTERED")

    time.sleep(10)


    ## Adding Filter
    #### Function for clicking result button
    def show_result_button():
        timeout = 60  # Timeout after 60 seconds
        start_time = time.time()

        try:
            result_button = driver.find_element(By.CSS_SELECTOR, 'button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.ml2')
            initial_text = result_button.text

            notification.notify(
                title='Notification',
                message='Show Result',
                app_name='Selenium Script'
            )

            while True:
                current_text = result_button.text
                if current_text != initial_text:
                    print("The 'Result' button has been clicked.")
                    time.sleep(5)
                    break  # Exit the loop if the button has been clicked

                # Check if the timeout has been reached
                elapsed_time = time.time() - start_time
                if elapsed_time > timeout:
                    print("Timeout reached. The 'Result' button was not clicked.")
                    break

                time.sleep(5)  # Wait before checking again
        except Exception as e:
            print(e)  # Handle specific exceptions if needed

    ### Experience level
    exp_filter_button = driver.find_element(By.XPATH, '//button[text()="Experience level"]')
    exp_filter_button.click()
    time.sleep(2)

    exp_filter_option = driver.find_element(By.XPATH, '//span[text()="Entry level"]')
    exp_filter_option.click()
    time.sleep(5)
    show_result_button()


    ### Date Posted
    exp_filter_button = driver.find_element(By.XPATH, '//button[text()="Date posted"]')
    exp_filter_button.click()
    time.sleep(5)

    exp_filter_option = driver.find_element(By.XPATH, '//span[text()="Past 24 hours"]')
    exp_filter_option.click()
    time.sleep(5)

    show_result_button()


    # Implementation
    def check_fields():
        try:
            wait = WebDriverWait(driver, 10)
            form_sections = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.jobs-easy-apply-form-section__grouping')))

            c = 0

            for section in form_sections:
                print("FORM SECTION")
                inputs = section.find_elements(By.TAG_NAME, 'input')
                selects = section.find_elements(By.TAG_NAME, 'select')

                for input_field in inputs:
                    value = input_field.get_attribute('value')
                    print("inputs")
                    if not value:
                        print(f"Input field in section {section.get_attribute('outerHTML')} is empty.")
                        c = 1
                        break
                    else:
                        print(value + "\n")
                        time.sleep(1)

                if(c == 1):
                    next_button()
                    break

                for select_field in selects:
                    selected_option = select_field.get_attribute('value')
                    print("Selects")
                    if not selected_option or selected_option == 'Select an option':
                        print(f"Select field in section {section.get_attribute('outerHTML')} is not selected.")
                        c = 1
                        break
                    else:
                        print(selected_option + "\n") 
                        time.sleep(1)
                if(c == 1):
                    next_button()
                    break
            if(c == 0):
                result_button = driver.find_element(By.CSS_SELECTOR, 'button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
                result_button.click()
                
        except Exception as e:
            result_button = driver.find_element(By.CSS_SELECTOR, 'button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
            result_button.click()
            print(e)

    def next_button():
        
        timeout = 60  # Timeout after 60 seconds
        start_time = time.time()
        
        try:
            result_button = driver.find_element(By.CSS_SELECTOR, 'button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
            initial_text = result_button.text
            
            notification.notify(
                title='Notification',
                message='Some Fields are needed to be filled up',
                app_name='Selenium Script'
            )
            
            while True:
                current_text = result_button.text
                if current_text != initial_text:
                    print("The 'Next' button has been clicked.")
                    time.sleep(5)
                    break  # Exit the loop if the button has been clicked

                # Check if the timeout has been reached
                elapsed_time = time.time() - start_time
                if elapsed_time > timeout:
                    print("Timeout reached. The 'Next' button was not clicked.")
                    break

                time.sleep(5)  # Wait before checking again
        except Exception as e:
            print(e)  # Handle specific exceptions if needed

    def resume_check():
        element = driver.find_element(By.CLASS_NAME, "t-16.t-bold")
        if "Resume" or "Education" in element.text:
            result_button = driver.find_element(By.CSS_SELECTOR, 'button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
            result_button.click()
        else:
            next_button()

    #Connection
    def connection_request(company_name, i):
        all_tabs = driver.window_handles
        driver.switch_to.window(all_tabs[1])
        
        # Define the search query
        search_query = company_name
        

        # Locate the search bar
        search_bar = driver.find_element(By.XPATH, '//input[@aria-label="Search"]')

        search_bar.clear()

        # Enter the search query
        search_bar.send_keys(search_query)

        # Submit the search
        search_bar.send_keys(Keys.RETURN)

        # Wait for the search results to load
        time.sleep(5)

        people_button = driver.find_element(By.XPATH, '//button[text()="People"]')
        people_button.click()

        # Wait for the people results to load
        time.sleep(5)
        
        
        def send_connection_requests():
            connect_buttons = driver.find_elements(By.XPATH, '//button[contains(@aria-label, "Invite")]')
            for button in connect_buttons:
                try:
                    button.click()  # Click the "Invite" button
                    time.sleep(2)   # Wait for the modal to open
                    send_button = driver.find_element(By.XPATH, '//button[@aria-label="Send without a note"]')
                    send_button.click()  # Click the "Send now" button in the modal
                    time.sleep(2)   # Wait before sending the next request
                except Exception as e:
                    print(f"Error sending request: {e}")
                    continue
                    
        i = 0
        while i<2:
            send_connection_requests()

            try:
                # Find the "Next" button and click it to go to the next page
                next_button = driver.find_element(By.XPATH, '//button[@aria-label="Next"]')
                next_button.click()

                # Wait for the next page to load
                time.sleep(5)
                i = i+1

            except Exception as e:
                print(f"No more pages or error finding next button: {e}")
                break           
                
        all_tabs = driver.window_handles
        driver.switch_to.window(all_tabs[0])


    # MAIN CODE
    from selenium.webdriver.support.ui import Select

    i = 0
    company_elements = driver.find_elements(By.CSS_SELECTOR, ".job-card-container")  # Adjust selector as needed
    for company in company_elements:
        company.click()

        try:
            i = i+1
            element = driver.find_element(By.XPATH, '//div[@class="job-details-jobs-unified-top-card__company-name"]/a[@data-test-app-aware-link]')
            company_name = element.text
            print(company_name)
            
            button = driver.find_element(By.XPATH, "//div[@class='jobs-apply-button--top-card']//button")
            button_text = button.get_attribute("textContent").strip()

            if(button_text == 'Apply'):
    #             print(f"Button text: {button_text}")
                button.click()
                time.sleep(5)
                all_tabs = driver.window_handles
                driver.switch_to.window(all_tabs[0])
                time.sleep(10)
                name = driver.find_element(By.XPATH, "//div[@class='artdeco-entity-lockup__subtitle ember-view']")
                notification.notify(
                title='Notification',
                message=name,
                app_name='Selenium Script'
            )
                time.sleep(10)

            elif(button_text == 'Easy Apply'):
    #             print(f"Button text: {button_text}")
                button.click()
                print("Button clicked\n")
                time.sleep(2)
                check_fields()
                print("Fields Checked\n")
                time.sleep(2)
                resume_check()
                print("Resume Checked \n")
                time.sleep(2)
                
                element = driver.find_element(By.CSS_SELECTOR, 'button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
                while(True):
                    heading = driver.find_element(By.CLASS_NAME, "t-16.t-bold")
                    print(heading.text)
                    check_fields()
                    print("Fields Checked")        
                    element = driver.find_element(By.CSS_SELECTOR, 'button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
                    if "Review" in element.text:
                        heading = driver.find_element(By.CLASS_NAME, "t-16.t-bold")
                        print(heading.text)
                        check_fields()
                        print("Fields Checked")
                    break
                    
                element = driver.find_element(By.CSS_SELECTOR, 'button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
                if "Submit application" in element.text:
                    result_button = driver.find_element(By.CSS_SELECTOR, 'button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view')
                    result_button.click()
                    time.sleep(5)
                    
                    cross = driver.find_element(By.CSS_SELECTOR, 'svg.artdeco-button__icon ')
                    cross.click()
                
                time.sleep(10)
                
            
            connection_request(company_name, i)
            
            
        except Exception as e:
            print(e)

    print("Script execution completed. Press Enter to exit.")
    input()





