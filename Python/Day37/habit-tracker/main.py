import requests
from datetime import datetime

USERNAME = "studentappbrewery"
TOKEN = "hawief2j3842341h1u3h1h2oinfd"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#
# today = datetime(year=2021, month=8, day=20)
#
# graph_config = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "1"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210822"
#
# today = datetime.now()
#
# graph_config = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "1"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# response = requests.put(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

today = datetime.now()
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.delete(url=graph_endpoint, headers=headers)
print(response)
