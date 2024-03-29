from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = YOUR SHEETY PRICES ENDPOINT
SHEETY_USERS_ENDPOINT = YOUR SHEETY USERS ENDPOINT


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_customer_emails():
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
