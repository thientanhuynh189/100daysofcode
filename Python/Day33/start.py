import requests

MY_LAT = 51.587351
MY_LONG = -0.127758

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # if response.status_code == 404:
# #     raise Exception("That resource does not exist.")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorised to access this data.")
# response.raise_for_status()
#
# data = response.json()
# # data = response.json()["iss_position"]["longitude"]
# # print(data)
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

reponse = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
reponse.raise_for_status()
data = reponse.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)


