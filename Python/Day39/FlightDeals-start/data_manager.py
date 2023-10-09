import requests

SHEET_PRICE_ENDPOINT = 

class DataManager:
    def __init__(self):
        self.sheet_data = {}

    def get_data(self):
        sheet_response = requests.get(SHEET_PRICE_ENDPOINT)
        sheet_result = sheet_response.json()
        self.sheet_data = sheet_result["prices"]
        return self.sheet_data

    def put_data(self):
        for city in self.sheet_data:
            put_endpoint = f"{SHEET_PRICE_ENDPOINT}/{city['id']}"
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=put_endpoint, json=new_data)
            print(response.text)
