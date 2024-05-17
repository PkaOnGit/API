import requests

#endpoint = "https://httpbin.org/status/200/"
#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" #http://127.0.0.1:8000/

get_response = requests.post(endpoint, json={"title":"Abc123", "content": "Hello", "price": "abc134"}) #http request 
#REST API Http Request -> JSON

#print(get_response.headers)
#print(get_response.text) #print raw tex
print(get_response.json())
#print(get_response.status_code)