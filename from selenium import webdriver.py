from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import calendar

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))

def wait_for_presence(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

# Initialize the WebDriver with WebDriver Manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the web page
    driver.get('https://www.frontlinepss.com/newprov')
    time.sleep(2)  # Wait for the page to load

    # Wait for the "Overnight Parking" button and click it
    overnight_parking_button = wait_for_element(driver, By.ID, 'MainContent_lbONP2')
    overnight_parking_button.click()
    time.sleep(2)  # Wait for the next elements to load

    # Wait for the checkbox to be visible and click it
    agree_checkbox = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_chkAgreeONPDisclaimer')
    agree_checkbox.click()
    time.sleep(2)  # Wait for the next elements to load

    # Wait for the plate text area, clear it, and enter the plate number
    plate_text_area = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_txtPlate')
    plate_text_area.clear()
    plate_text_area.send_keys('G44UCM')
    time.sleep(.5)  # Small delay to ensure text is entered

    # Wait for the reason dropdown and select "Overnight Guest"
    reason_dropdown = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_ddlReason')
    select_reason = Select(reason_dropdown)
    select_reason.select_by_visible_text('Overnight Guest')
    time.sleep(.5)  # Small delay to ensure selection is made

    # Select the car make as "Tesla"
    make_dropdown = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_ddlMake')
    select_make = Select(make_dropdown)
    select_make.select_by_visible_text('Tesla')
    time.sleep(.5)  # Small delay to ensure selection is made

    # Enter the model as "3"
    model_text_area = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_txtModel')
    model_text_area.clear()
    model_text_area.send_keys('3')
    time.sleep(.5)  # Small delay to ensure text is entered

    # Enter the vehicle color as "grey"
    color_text_area = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_txtVehicleColor')
    color_text_area.clear()
    color_text_area.send_keys('Grey')
    time.sleep(.5)  # Small delay to ensure text is entered

    # Select the state as "New Jersey"
    state_dropdown = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_ddlState')
    select_state = Select(state_dropdown)
    select_state.select_by_visible_text('New Jersey')
    time.sleep(.5)  # Small delay to ensure selection is made

    # Fill out the address
    address_text_area = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_txtAddress')
    address_text_area.clear()
    address_text_area.send_keys('47')
    time.sleep(.5)  # Small delay to ensure text is entered

    # Select the direction as "West"
    direction_dropdown = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_ddlDirection')
    select_direction = Select(direction_dropdown)
    select_direction.select_by_visible_text('West')
    time.sleep(.5)  # Small delay to ensure selection is made

    # Enter the street name and select from dropdown
    street_name_text_area = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_txtStreetName')
    street_name_text_area.send_keys('Ethan Dr')
    time.sleep(2)  # Wait for the autocomplete options to appear

    # Click on the autocomplete option for "Ethan Dr"
    autocomplete_option = wait_for_presence(driver, By.XPATH, "//li[contains(text(), 'ETHAN DR')]")
    autocomplete_option.click()
    time.sleep(3)  # Small delay to ensure the selection is made

    # Enter the suite/unit as "2a"
    suite_text_area = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_txtSuite')
    suite_text_area.send_keys('2A')
    time.sleep(.5)  # Small delay to ensure text is entered


    # Enter the zip code
    zip_text_area = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_txtAddressZip')
    zip_text_area.clear()
    zip_text_area.send_keys('07974')
    time.sleep(.5)  # Small delay to ensure text is entered
    # Open the calendar widget and select the next day for the start date
    date_picker = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_txtStartDate')
    date_picker.click()
    time.sleep(2)  # Wait for the calendar to appear

    # Find today's date
    today_element = wait_for_presence(driver, By.CLASS_NAME, 'ui-state-highlight')
    today_date = int(today_element.text)
    current_month = driver.find_element(By.CLASS_NAME, 'ui-datepicker-month').text
    current_year = int(driver.find_element(By.CLASS_NAME, 'ui-datepicker-year').text)

    # Calculate the next day
    last_day_of_month = calendar.monthrange(current_year, list(calendar.month_name).index(current_month))[1]
    if today_date == last_day_of_month:
        # Click on the next button to go to the next month
        next_button = wait_for_element(driver, By.CLASS_NAME, 'ui-datepicker-next')
        next_button.click()
        time.sleep(2)  # Wait for the calendar to update

        # Select the first day of the next month
        next_day_element = wait_for_presence(driver, By.XPATH, "//a[text()='1']")
    else:
        # Select the next day
        next_date = today_date + 1
        next_day_element = wait_for_presence(driver, By.XPATH, f"//a[text()='{next_date}']")
    next_day_element.click()

    # Open the end date picker and select the next day
    end_date_picker = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_txtEndDate')
    end_date_picker.click()
    time.sleep(2)  # Wait for the calendar to appear

    # Calculate the next day again for the end date
    if today_date == last_day_of_month:
        # Click on the next button to go to the next month
        next_button = wait_for_element(driver, By.CLASS_NAME, 'ui-datepicker-next')
        next_button.click()
        time.sleep(2)  # Wait for the calendar to update

        # Select the first day of the next month
        next_day_end_element = wait_for_presence(driver, By.XPATH, "//a[text()='1']")
    else:
        # Select the next day
        next_day_end_element = wait_for_presence(driver, By.XPATH, f"//a[text()='{next_date}']")
    next_day_end_element.click()


    # Wait for the first name text area, clear it, and enter the first name
    first_name_text_area = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_txtFirstName')
    first_name_text_area.send_keys('Aditya')
    time.sleep(.5)  # Small delay to ensure text is entered

    # Wait for the last name text area, clear it, and enter the last name
    last_name_text_area = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_txtLastName')
    last_name_text_area.send_keys('Shah')
    time.sleep(.5)  # Small delay to ensure text is entered

    # Wait for the phone text area, clear it, and enter the phone number
    phone_text_area = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_txtPhone')
    phone_text_area.send_keys('714-408-5316')
    time.sleep(.5)  # Small delay to ensure text is entered
    

    # Wait for the email text area, clear it, and enter the email address
    email_text_area = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_txtEmail')
    email_text_area.send_keys('adityashah82@gmail.com')
    time.sleep(.5)  # Small delay to ensure text is entered

    # Switch to the CAPTCHA iframe and click the checkbox
    iframe = wait_for_element(driver, By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")
    driver.switch_to.frame(iframe)
    time.sleep(2)  # Wait for a moment to ensure the iframe is loaded

    captcha_checkbox = wait_for_element(driver, By.ID, 'recaptcha-anchor')
    captcha_checkbox.click()
    time.sleep(2)  # Small delay to ensure the CAPTCHA is clicked

    # Switch back to the main content
    driver.switch_to.default_content()
    time.sleep(.5)  # Small delay to ensure the switch is complete

    # Wait for the submit button to be clickable
    submit_button = wait_for_element(driver, By.ID, 'MainContent_ctrlOverNightParking_btnSubmit')

    # Scroll the submit button into view (if necessary)
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(.5)  # Small delay to ensure the element is in view

    # Ensure the submit button is visible and clickable
    if submit_button.is_displayed() and submit_button.is_enabled():
        submit_button.click()
        print("Submit button clicked successfully.")
    else:
        print("Submit button is not clickable.")
        # Try clicking using JavaScript as a last resort
        driver.execute_script("arguments[0].click();", submit_button)
        print("Submit button clicked using JavaScript.")

    time.sleep(5)  # Wait to observe the result after submission

finally:
    # Close the browser
    driver.quit()

