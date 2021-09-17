import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = "/home/ubunguu/Downloads/chromedriver_linux64/chromedriver"
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = ""
PASSWORD = ""

class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        # username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys(USERNAME)
        # password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys(PASSWORD)
        sleep(2)
        password_input.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

selenium_bot = InstaFollower(CHROME_DRIVER_PATH)
selenium_bot.login()
selenium_bot.find_followers()
selenium_bot.follow()
