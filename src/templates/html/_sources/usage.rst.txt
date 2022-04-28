=================
usage
=================

In bash 
---------

**dump the database** 

curl http://$host:$port/api

**insert a row in the database** 

curl -X POST -F 'user='"$user"'' -F 'task='"$task"'' -F 'pwd='"$path"'' -F 'audio_sample='"$audio_sample"'' -F 'priority='"$priority"'' -F 'eta='"$eta"'' -F 'status='"$status"'' http://$host:$port/api

**delete a row in the database** 

curl -X DELETE http://$host:$port/api/$identifiant 

**update a row in the database**

curl -X PUT -F 'user='"$user"'' -F 'task='"$task"'' -F 'pwd='"$path"'' -F 'audio_sample='"$audio_sample"'' -F 'priority='"$priority"'' -F 'eta='"$eta"'' -F 'status='"$status"'' http://$host:$port/api/$id_request

In python 
-----------

*see tests/client.py* 