from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/home/ubunguu/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_elements_by_css_selector("#articlecount a")
# print(article_count.text)
# #Click the emethod
# # article_count.click()
#
# # Link in method and click
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
#
# search = driver.find_element_by_name("search")
# #input the key
# search.send_keys("Python")
# #Press enter
# search.send_keys(Keys.ENTER)

#Herokuapp
driver.get("http://secure-retreat-92358.herokuapp.com/")
# first_name = driver.find_element_by_class_name(".top")
first_name = driver.find_element_by_name("fName")
first_name.send_keys("Angela")

# last_name = driver.find_element_by_class_name(".middle")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Yu")

# email = driver.find_element_by_class_name(".bottom")
email = driver.find_element_by_name("email")
email.send_keys("angela.yu@example.com")

# button = driver.find_element_by_class_name("btn")
button = driver.find_elements_by_css_selector("form button")
button.click()
button.send_keys(Keys.ENTER)




# drive.get("https://secure-retreat-82358.herokuapp.com/")
#
# first_name = drive.find_element_by_name("fName")
# first_name.send_keys("Angela")
# last_name = drive.find_element_by_name("lName")
# last_name.send_keys("Yu")
# email = drive.find_element_by_name("email")
# email.send_keys("angela@gmail.com")
#
# submit = drive.find_element_by_css_selector("form button")

# while True:
#     submit.click()
#     if submit.quit():
#         return False