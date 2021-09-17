import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

url = "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")
print(soup.prettify())

# all_link_elements = soup.select(".list-card-info a")
# print(all_link_elements)
# all_links = []
# for link in all_link_elements:
#     href = link["href"]
#     print(href)
#     if "http" not in href:
#         all_links.append(f"https://www.zillow.com{href}")
#     else:
#         all_links.append(href)
#
# all_price_elements = soup.select(".list-card-price")
# print(all_price_elements)
# all_prices = [price.get_text().split("+")[0] for price in all_price_elements if "$" in price.text]
#
# all_address_elements = soup.select(".list-card-info address")
# print(all_address_elements)
# all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]
#
# chrome_driver_path = "/home/ubunguu/Downloads/chromedriver_linux64/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
#
# for n in range(len(all_links)):
#     driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf-BmklmnM-jSGN02qLJCetzNfWxtECVCWjKvpAMx-Gq7AmPA/viewform?usp=sf_link")
#
#     sleep(2)
#     address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
#
#     address.send_keys(all_addresses[n])
#     price.send_keys(all_prices[n])
#     link.send_keys(all_links[n])
#     submit_button.click()
