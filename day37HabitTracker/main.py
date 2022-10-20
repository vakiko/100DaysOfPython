import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "victoriaemily"
TOKEN = "sdhasdasdsasdsasd"
# user_params = {
#     "token": "sdhasdasdsasdsasd",
#     "username": "victoriaemily",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID = "graph1"

# graph_config = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai",
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

date = str(datetime.now())
date = date[:10]
date = date.split('-')
DATE = ''.join(date)

graph_update = {
     "date": DATE,
     "quantity": "60",    
 }
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
headers = {
     "X-USER-TOKEN": TOKEN
}
response = requests.post(url=pixel_endpoint, json=graph_update, headers=headers)
print(response.text)