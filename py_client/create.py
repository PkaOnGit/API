import requests

headers = {'Authorization': 'Bearer a7325dc1fd760c4aa6519e95a81a1296c43d86e3'}
endpoint = "http://localhost:8000/api/products/"
#"http://localhost:8000/admin/"
#sesion -> post data
#selenium

data = {
    "title": "This is done",
    "price": 32.99
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
