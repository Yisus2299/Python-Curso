import pandas as pd
import os

ARDILLAS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data = pd.read_csv(ARDILLAS)
gray_squirels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirels_count)
# print(cinnamon_squirels_count)
# print(black_squirels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirels_count, cinnamon_squirels_count, black_squirels_count ],
}

df = pd.DataFrame(data_dict)
df.to_csv("squirel_count.csv")
