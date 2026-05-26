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

data = pandas.read_csv(WEATHER_DATA) #almacenamos todo en una variable

data_dict = data.to_dict() #te lista todos los datos del excel
temp_list = data["temp"].to_list() #lista todos los datos de las temperaturas del excel
# media_temp = statistics.mean(temp_list) # esto aplica la misma forma pero es mas directo
# max_temp = data["temp"].max()

# si quieres obtenerlo de una columna entera

# print(data["temp"])
# print(data.temp)

#conseguir informacion de una fila entera

(data[data.day == "Monday"])
(data[data["temp"] == data["temp"].max()]) #muestra la fila entera con la temperatura maxima

#====================================================================================================#
# convertir la temperatura de celsius a Farhrenheid - Ejercicio

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday.temp * 9/5 + 32
# print(monday_temp_F)

#=====================================================================================================#

# Crear un datarame desde el inicio

data_dict = { #creamos un diccionario
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict) #lo guardamos con la regla de. DataFrame y lo guardamos en una variable
data.to_csv("old_data.csv") #esto lo usamos para convertir este diccionario creado a un csv (excel) y que se cree un nuevo archivo



