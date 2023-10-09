# with open("weather_data.csv") as file:
#     data = file.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

import pandas

# data = pandas.read_csv("weather_data.csv")  # dataframe
#
# print(data["temp"])  # series
# temp_list = data["temp"].to_list()
# for temp in temp_list:
#     print(temp)
#
# average = sum(temp_list) / len(temp_list)
# print(average)
# print(data["temp"].mean())
#
# highest_temp = data["temp"].max()
#
# #Get data in column
# print(data["condition"])
# print(data.condition)
#
# #Get Data in Row
# print(data[data.day == "Monday"])
#
# print(data[data.temp == highest_temp])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 + 32

# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Any", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")