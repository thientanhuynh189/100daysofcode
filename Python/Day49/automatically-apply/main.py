import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "/home/ubunguu/Downloads/chromedriver_linux64/chromedriver"

ACCOUNT_EMAIL = ""
ACCOUNT_PASSWORD = ""
ACCOUNT_PHONENUMBER = ""

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(2)
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element_by_id("login-email")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("login-password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# time.sleep(5)
# apply_button = driver.find_elements_by_css_selector(".jobs-s-apply button")
# apply_button.click()
#
# time.sleep(5)
# phone = driver.find_element_by_class_name("fb-single-line-text_input")
# if phone.text == "":
#     phone.send_keys(ACCOUNT_PHONENUMBER)
#
# submit_button = driver.find_elements_by_css_selector("footer button")
# submit_button.click()

time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    try:
        apply_button = driver.find_elements_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        phone = driver.find_element_by_class_name("fb-single-line-text_input")
        if phone.text == "":
            phone.send_keys(ACCOUNT_PHONENUMBER)

        submit_button = driver.find_elements_by_css_selector("footer button")

        # If the submit_button is a "Next" button, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.Click()

        # close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
