import requests
from datetime import datetime

USERNAME = "jesus-imken-20260417"
TOKEN = "jkhasgdjhasgdjhasgdkasjbdkajsgdjhuasbdkagduwjdnbasmdvajhdsfvawd23423423523sdjkahdhkjas"
GRAPH_ID = "graph1"
DATE = datetime.now().strftime("%Y%m%d")  # current date in YYYYMMDD format

PIXELA_BASE = "https://pixe.la/v1/users"

# Create user (only once)
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# r = requests.post(PIXELA_BASE, json=user_params)
# print("create user:", r.status_code, r.text)

# Create graph
graph_endpoint = f"{PIXELA_BASE}/{USERNAME}/graphs"
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

# View graph in browser:
# https://pixe.la/v1/users/jesus-imken-20260417/graphs/graph1.html

# Create pixel (add data point)
pixel_create_endpoint = f"{PIXELA_BASE}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": DATE,
    "quantity": "30",
}
r = requests.post(pixel_create_endpoint, json=pixel_data, headers=headers)
print("create pixel:", r.status_code, r.text)

# View pixel in browser for a specific date:
# https://pixe.la/v1/users/jesus-imken-20260417/graphs/graph1.html?date=20260417

# Update pixel
pixel_update_endpoint = f"{PIXELA_BASE}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

pixel_data = {
    "quantity": "40",
}
r = requests.put(pixel_update_endpoint, json=pixel_data, headers=headers)
print("update pixel:", r.status_code, r.text)

# Delete the pixel we just updated
pixel_delete_endpoint = f"{PIXELA_BASE}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
r = requests.delete(pixel_delete_endpoint, headers=headers)
print("delete pixel:", r.status_code, r.text)