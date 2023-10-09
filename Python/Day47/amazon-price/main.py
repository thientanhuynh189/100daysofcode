import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

url = "https://www.amazon.com/dp/B00X9JNWGS/ref=sbl_dpx_B008C9UCH2_0"
product_headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
product_response = requests.get(url, headers=product_headers)

soup = BeautifulSoup(product_response.content, "lxml")

product_price = soup.find("span", id="priceblock_ourprice").get_text()
price_without_currency = product_price.split("$")[1]
price_as_float = float(price_without_currency)
# print(price_as_float)

title = soup.find("span", id="productTitle").get_text().strip()
# print(title)

BUY_PRICE = 400

if price_as_float < 400:
    message = f"{title} is now {product_price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login("appbrewery.student2021@gmail.com", "####")
        connection.sendmail(
            from_addr="appbrewery.student2021@gmail.com",
            to_addrs="appbrewery.student2021@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )
