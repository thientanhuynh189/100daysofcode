from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

# FB_EMAIL = ""
# FB_PASSWORD = ""

GG_EMAIL = ""
GG_PASSWORD = ""

chrome_driver_path = "/home/ubunguu/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")
sleep(5)

login_button = driver.find_element_by_xpath('//*[@id="c-690079234"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()
sleep(2)

# fb_login = driver.find_element_by_xpath('//*[@id="c1564682258"]/div/div/div[1]/div/div[3]/span/div[2]/button')
# fb_login.click()
gg_login = driver.find_element_by_xpath('//*[@id="c1564682258"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
gg_login.click()
sleep(2)

# # Switch to Facebook login window
# base_window = driver.window_handles[0]
# fb_login_window = driver.window_handles[1]
# driver.switch_to.window(fb_login_window)
# print(driver.title)
#
# fb_email = driver.find_element_by_xpath('*[@id="email"]')
# fb_password = driver.find_element_by_xpath('//*[@id="pass"]')
# fb_login_button = driver.find_element_by_xpath('//*[@id="u_0_0_Yh"]')
# email.send_keys(FB_EMAIL)
# password.send_keys(FB_PASSWORD)
#
# password.send_keys(Keys.ENTER)
# # fb_login_button.click()
# sleep(2)

# Switch to Google login window
base_window = driver.window_handles[0]
gg_login_window = driver.window_handles[1]
driver.switch_to.window(gg_login_window)
print(driver.title)

gg_email = driver.find_element_by_xpath('//*[@id="identifierId"]')
gg_email.send_keys(GG_EMAIL)
gg_email.send_keys(Keys.ENTER)
gg_password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
gg_password.send_keys(GG_PASSWORD)
gg_password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)
sleep(5)

allow_location_button = driver.find_element_by_xpath('//*[@id="c1564682258"]/div/div/div/div/div[3]/button[1]/span')
allow_location_button.click()
sleep(2)

cookies_button = driver.find_element_by_xpath('//*[@id="c-690079234"]/div/div[2]/div/div/div[1]/button')
cookies_button.click()
sleep(2)

notification_button = driver.find_element_by_xpath('//*[@id="c1564682258"]/div/div/div/div/div[3]/button[2]')
notification_button.click()
sleep(2)

for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element_by_xpath('//*[@id="c-690079234"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_elements_by_css_selector(".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()