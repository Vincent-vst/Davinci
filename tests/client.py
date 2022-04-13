from urllib import response
import requests 

url = "http://10.16.0.250:5000/transcript/" 

# response = requests.get(url)
response = requests.post(url + "avion.mp3")

print(response.json())
