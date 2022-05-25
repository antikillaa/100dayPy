# with open("weather_data.csv", "r") as csv:
#     list_data = csv.readlines()
#     print(list_data)

# import csv
#
# with open("weather_data.csv", "r") as data_file:
#     csv = csv.reader(data_file)
#     temperature = []
#     for row in csv:
#         temperature.append(row[1])
#
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
dita_dict = data.to_dict()
temperatures = data.get("temp")
temp_sum = 0
# for t in temperatures:
#     temp_sum += t
# avg_temp = temp_sum / len(temperatures)
# print(data["temp"].max())
# print(data.temp.mean())
#
# print(data[data.day == "Monday"])

# high_temp = data.temp.max()
#
# print(data[data.temp == high_temp])

monday = data[data.day == "Monday"]
monday_temp = monday.temp
f_temp = monday_temp * 1.8 + 32
print(f_temp)

# avg_temp = sum(temp_list) / len(temp_list)

