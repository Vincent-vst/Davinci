#! /bin/bash 

host=127.0.0.1
port=3002 

get(){
	curl http://$host:$port/workers
}

insert(){
	echo -e 'task : '
	read task
	echo -e 'pwd : '
	read path
	echo -e 'status : '
	read status 
	curl -X POST -F 'task=$task' -F 'pwd=$path' -F 'status=$status' http://$host:$port/workers 
	
}

# get
insert 

# # insert in database 
# curl -X POST -F 'author=vincent' -F 'language=en' -F 'title=UwU' http://127.0.0.1:3002/books 

# # get all database 
# curl http://127.0.0.1:3002/books  

# # get one item 
# curl http://127.0.0.1:3002/book/1

# # delete from database  
# curl -X DELETE http://127.0.0.1:3002/book/1 


