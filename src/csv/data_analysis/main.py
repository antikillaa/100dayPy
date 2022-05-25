import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

new_csv = {"Fur Color": ["grey", "red", "black"],
           "Count": [gray, red, black]}

data = pandas.DataFrame(new_csv)
data.to_csv("squirrel_count.csv")
