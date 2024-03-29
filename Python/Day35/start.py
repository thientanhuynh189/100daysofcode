import requests
import datetime
import os
from twilio.rest import Client

API_KEY = "#####"
LATITUDE = #####
LONGITUDE = #####

account_sid = "#####"
auth_token = "#####"

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

# response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
# response.raise_for_status()
# data = response.json()
#
# now = datetime.datetime.now()
# hour = now.time().hour
# next_hour = hour + 12
#
# high_id = 0
# for item in range(hour, next_hour):
#     current_id = data["hourly"][item]["weather"][0]["id"]
#     if current_id > high_id:
#         high_id = current_id
#
# if high_id < 700:
#     print("Bring an Umbrella")

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.☔",
        from_='+####',
        to='+####'
    )
    print(message.status)

