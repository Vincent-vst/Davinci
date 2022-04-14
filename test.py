import requests

BASE = "http://10.16.0.250:5000/"

# response = requests.patch(BASE + "video/2", {})
response = requests.get(BASE + "workers/1", {})
print(response.json())
