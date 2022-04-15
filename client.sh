#! /bin/bash 

host=127.0.0.1
port=3002 

get(){
	curl http://$host:$port/workers
}

insert(){
	echo -n 'task : '
	read task
	echo -n 'pwd : '
	read path
	echo -n 'status : '
	read status 
	echo -n 'audio_sample : '
	read audio_sample
	curl -X POST -F 'task='"$task"'' -F 'pwd='"$path"'' -F 'status='"$status"'' -F 'audio_sample='"$audio_sample"'' http://$host:$port/workers 
	
}

delete(){
	echo -n 'id : '
	read identifiant 
	curl -X DELETE http://$host:$port/workers/$identifiant 
}

main(){
	echo -n 'what do you want to do ? [get/insert/delete]'
	read choice 
	case $choice in 
		get)
			# echo "printing db"
			get
			;;
		insert) 
			# echo "insert into db"
			insert
			;; 
		delete)
			# echo "deleting db"
			delete
			;; 
		*) 
			echo 'dafuk you want'
			;; 
	esac 
}

main 
