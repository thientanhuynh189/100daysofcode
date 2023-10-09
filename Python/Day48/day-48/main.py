from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# chromeOptions = Options()
# chromeOptions.add_argument("start-maximized")
# chromeOptions.add_argument("--headless")
# chromeOptions.add_argument("--no-sandbox")
# chromeOptions.add_argument("--disable-dev-shm-using")

chrome_driver_path = "/home/ubunguu/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com/")
# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_1_sspa?crid=1RQE1OKS57JZT&dchild=1&keywords=instant+pot&qid=1630760311&sprefix=ins%2Caps%2C433&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExTlY1SEdUTEdNMVFEJmVuY3J5cHRlZElkPUEwMDE2NjI5MkdOWkZOMjFYVFdPUCZlbmNyeXB0ZWRBZElkPUEwMjE0NzMyNUlTVUg0V1BYQTZWJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")
driver.get("https://www.python.org/")

# time = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time')
# time_events = time.text
event_times = driver.find_elements_by_css_selector(".event-widget time")

# information = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')
# information_events = information.text
event_names = driver.find_elements_by_css_selector(".event-widget li a")

# dictionary = {
#     time_events: information_events
# }

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times,
        "name": event_names,
    }











# Get with id
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# Get with name
# search_bar = driver.find_element_by_name("q")
# # print(search_bar)
# print(search_bar.get_attribute("placeholder"))

# Get with class_name
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# Get with a href...
# documentation_link = driver.find_elements_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# Get the link with another ul li
# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)





driver.quit()






# price = driver.find_element_by_id("price_inside_buybox")
#
# # search_bar = driver.find_element_by_name("q")
# # print(search_bar.get_attribute("placeholder"))
#
# # logo = driver.find_element_by_class_name("python_logo")
#
# # documentation_link = driver.find_elements_by_css_selector(".documentation-widget a")
# # print(documentation_link.text)
#
# # bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# # print(bug_link.text)
#
# event_times = driver.find_elements_by_css_selector(".event-widget time")
# # for time in event_times:
# #     print(time.text)
# event_names = driver.find_elements_by_css_selector(".event-widget li a")
# # for name in event_names:
# #     print(name.text)
# events = {}
#
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text,
#     }
#
# # driver.close()
# driver.quit()
