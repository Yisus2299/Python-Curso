import requests
from datetime import datetime

USERNAME = "jesus-imken-20260417"
TOKEN = "jkhasgdjhasgdjhasgdkasjbdkajsgdjhuasbdkagduwjdnbasmdvajhdsfvawd23423423523sdjkahdhkjas"
GRAPH_ID = "graph1"
DATE = datetime.now().strftime("%Y%m%d") #fecha actual en formato YYYYMMDD

pixela = "https://pixe.la/v1/users"

# Crear usuario (solo 1 vez)
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# r = requests.post(pixela, json=user_params)
# print("create user:", r.status_code, r.text)

# Crear graph
graph_endpoint = f"{pixela}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "minutes",
    "type": "int",
    "color": "momiji",
}
headers = {"X-USER-TOKEN": TOKEN}

# r = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print("create graph:", r.status_code, r.text)

# https://pixe.la/v1/users/jesus-imken-20260417/graphs/graph1.html - link para ver el graph

#crear pixel

pixel_create_endpoint = f"{pixela}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": DATE,
    "quantity": "30",
}
r = requests.post(pixel_create_endpoint, json=pixel_data, headers=headers)
print("create pixel:", r.status_code, r.text)

# https://pixe.la/v1/users/jesus-imken-20260417/graphs/graph1.html?date=20260417 - link para ver el pixel

#actualizar pixel

pixel_update_endpoint = f"{pixela}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

pixel_data = {
    "quantity": "40",
}
r = requests.put(pixel_update_endpoint, json=pixel_data, headers=headers)
print("update pixel:", r.status_code, r.text)

# acabamos de actualizar el pixel, ahora vamos a borrarlo:

pixel_delete_endpoint = f"{pixela}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
r = requests.delete(pixel_delete_endpoint, headers=headers)
print("delete pixel:", r.status_code, r.text)