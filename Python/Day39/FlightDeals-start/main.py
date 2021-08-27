from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager

flightsearch = FlightSearch()
dataManager = DataManager()
sheet_data = dataManager.get_data()
notificationManager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

for item in sheet_data:
    # print(item)
    if item["iataCode"] == "":
        item["iataCode"] = flightsearch.search_iata(item["city"])
        dataManager.sheet_data = sheet_data
        dataManager.put_data()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flightsearch.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        article = f"Low price alert! Only ${flight.price} to fy from {flight.origin_airport}-{flight.origin_city} to {flight.destination_airport}-{flight.detination_city}, from {flight} to {flight}"
        notificationManager.send_message(body=article)
