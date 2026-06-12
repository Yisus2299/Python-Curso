'''import os
import csv

WEATHER_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "weather_data.csv")

temperatures = []

with open(WEATHER_DATA, mode="r", encoding="utf-8") as weather:
    clima = csv.DictReader(weather)

    for row in clima:
        if "temp" in row and row["temp"] != "":
            temperatures.append(int(row["temp"]))

print(temperatures)'''

#==================================================================================================#
import os
import pandas as pandas
import statistics

WEATHER_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "weather_data.csv")

data = pandas.read_csv(WEATHER_DATA) #we store all the data in a variable

data_dict = data.to_dict() #it lists all the data from the excel
temp_list = data["temp"].to_list() #it lists all the data from the temperatures from the excel
# media_temp = statistics.mean(temp_list) # this applies the same form but is more direct
# max_temp = data["temp"].max()

# if you want to get it from a whole column

# print(data["temp"])
# print(data.temp)

#get information from a whole row

(data[data.day == "Monday"])
(data[data["temp"] == data["temp"].max()]) #shows the whole row with the maximum temperature

#====================================================================================================#
# convert the temperature from celsius to Farhrenheid - Exercise

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday.temp * 9/5 + 32
# print(monday_temp_F)

#=====================================================================================================#

# Create a data frame from scratch

data_dict = { #we create a dictionary
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict) #we save it with the rule of. DataFrame and we save it in a variable
data.to_csv("old_data.csv") #this is used to convert this created dictionary to a csv (excel) and create a new file



