import requests 

url = 'http://127.0.0.1:3001/workers'

test = {'task':'test', 'pwd':'oui', 'audio_sample':'ha', 'status':'nope'}


requests.post(url, data=test)
