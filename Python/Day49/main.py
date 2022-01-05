from selenium import webdriver

firefox_driver_path = "/home/ttannium/Documents/geckodriver"
driver = webdriver.Firefox(executable_path=firefox_driver_path)
driver.get("https://www.amazon.com")

driver.close()