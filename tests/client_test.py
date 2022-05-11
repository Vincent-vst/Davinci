import requests 

url = 'http://127.0.0.1:3000/api'

data_post={'user':'tom', 'task':'TRAP', 'pwd':'/home', 'occ_id':'BEA' , 'audio_sample':'{"hello":"world", "test":2}', 'priority':1, 'eta':'datetime()', 'status':'pending', 'log':'return 404'}
# print(requests.post(url , data=data_post).text)

# print(requests.get(url).text)

data_put={'user':'vincent'}
print(requests.put('127.0.0.1:300/api/1', data=data_put).text)


