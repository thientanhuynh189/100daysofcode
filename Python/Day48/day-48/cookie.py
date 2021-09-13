from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/home/ubunguu/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

condition = True
while condition:
    cookie.click()

    timeout = time.time() + 5
    if time.time() > timeout:
        all_prices = driver.find_elements_by_css_selector("#store b")

        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        items = driver.find_elements_by_css_selector("#store div")
        item_ids = [items.get_attribute("id") for item in items]
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        money = driver.find_element_by_id("money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        timeout = time.time() + 5

    five_min = time.time() + 60*5
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        five_min = time.time() + 60*5

    if driver.quit():
        condition = False



