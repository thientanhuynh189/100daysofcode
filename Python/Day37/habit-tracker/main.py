import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ["SHEET_ENDPOINT"]

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

GENDER = "female"
WEIGHT_KG = 65
HEIGHT_CM = 165
AGE = 20

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_text = input("Tell me which exercises you did: ")
params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=EXERCISE_ENDPOINT, headers=headers, json=params)
results = response.json()
print(results)

now = datetime.now()
today = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

data = requests.get(SHEETY_ENDPOINT)
for exercise in results["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, auth=(USERNAME, PASSWORD))
    print(sheet_response.text)
