import requests 

url = 'http://127.0.0.1:3000/api'

data_post={'user':'tom', 'task':'TRAP', 'pwd':'/home', 'occ_id':'BEA' , 'audio_sample':'{"hello":"world", "test":2}', 'priority':1, 'eta':'datetime()', 'status':'pending'}
print(requests.post(url , data=data_post).text)



