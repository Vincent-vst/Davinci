import requests

BASE = "http://127.0.0.1:3002/"

# response = requests.patch(BASE + "video/2", {})
response = requests.get(BASE + "video/1", {})
print(response.json())
