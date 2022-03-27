from urllib import response
import requests 

url = "http://127.0.0.1:5000/transcript/" 

# response = requests.get(url)
response = requests.post(url + "avion.mp3")

print(response.json())