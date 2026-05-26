from datetime import datetime
import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()


# iss_position = {
#     "latitude": data["iss_position"]["latitude"],
#     "longitude": data["iss_position"]["longitude"],
# }
# print(iss_position)

response = requests.get(
    "https://api.sunrise-sunset.org/json",
    params={"lat": 36.7201600, "lng": -4.4203400, "formatted": 0}, 
)
response.raise_for_status()

data = response.json()

solar_noon = data["results"]["solar_noon"].split("T")[1].split(":")[0]
print(solar_noon)


time_now = datetime.now()
# print(time_now)












