from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

# firefox_driver_path = "/home/ttannium/Documents/geckodriver"
# driver = webdriver.Firefox(executable_path=firefox_driver_path)
# driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=104195383&keywords=python%20developer&location=Vietnam&sortBy=R")

ACCOUNT_EMAIL = os.getenv('QT_IM_MODULE')
print(ACCOUNT_EMAIL)

# driver.close()