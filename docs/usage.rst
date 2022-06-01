=================
usage
=================

Starting the API  
---------

``python3 src/app.py`` 


Using the API 
---------

For the following code, in bash, we will consider $host=127.0.0.1 and $port=32, 
and in python url=127.0.0.1:3002

**dump the database** 

| ``curl http://$host:$port/api``  
| *or in python* 
| ``requests.get(url)``

**insert a row in the database** 


| ``curl -X POST -F 'user='"$user"'' -F 'task='"$task"'' -F 'pwd='"$path"'' -F 'audio_sample='"$audio_sample"'' -F 'priority='"$priority"'' -F 'eta='"$eta"'' -F 'status='"$status"'' -F 'log'='" "'' http://$host:$port/api``
| *or in python* 
| ``item={'user':'tom', 'task':'trap', 'pwd':'/usr',  'occ_id':'bea2022', 'audio_sample':'{"name": "tom"}', 'priority' : 2, 'eta':'timedate()', 'status':'pending', 'log':' '}``
| ``requests.post(url, data=item)``


**delete a row in the database** 

| ``curl -X DELETE http://$host:$port/api/$id_row`` 
| *or in python* 
| ``requests.delete(url + '/' + str(id_row))``

**update a row in the database**

| ``curl -X PUT -F 'user='"username"'' http://$host:$port/api/$id_request``
| *or in python* 
| ``user_update={'user':'test'}``
| ``requests.put('http://127.0.0.1:3001/api/1' , data={"user":"test"})``