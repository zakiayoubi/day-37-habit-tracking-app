import requests
import datetime
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "kajdfkjadkfj2323jkldjfa"
USER_NAME = "ayoubim"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs"

graph_id = "graph1"
graph_config = {
    "id": graph_id,
    "name": "Coding Graph",
    "unit": "minute",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.datetime(year=2023, month=10, day=21)
formatted_date = today.strftime("%Y%m%d")

pixel_params = {
    "date": formatted_date,
    "quantity": "180",
}

pixel_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{graph_id}"


# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)


update_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{graph_id}/{formatted_date}"


# response = requests.put(url=update_endpoint, json={"quantity": "80"}, headers=headers)
# print(response.text)

delete_endpoint = f"{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{graph_id}/{formatted_date}"
response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)




