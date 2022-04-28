#! /bin/bash 

host=127.0.0.1
port=3001 

get(){
	curl http://$host:$port/api
}

insert(){
	echo -n 'user : '
	read user 
	echo -n 'task : '
	read task
	echo -n 'pwd : '
	read path
	echo -n 'occ_id : '
	read occ_id
	echo -n 'audio_sample : '
	read audio_sample
	echo -n 'priority : '
	read priority
	echo -n 'eta : '
	read eta
	echo -n 'status : '
	read status
	curl -X POST -F 'user='"$user"'' -F 'task='"$task"'' -F 'pwd='"$path"'' -F 'occ_id='"$occ_id"'' -F 'audio_sample='"$audio_sample"'' -F 'priority='"$priority"'' -F 'eta='"$eta"'' -F 'status='"$status"'' http://$host:$port/api
	
}

delete(){
	echo -n 'id : '
	read identifiant 
	curl -X DELETE http://$host:$port/api/$identifiant 
}

update(){

	echo -n 'id : '
	read id_request
	echo -n 'user : '
	read user 
	echo -n 'task : '
	read task
	echo -n 'pwd : '
	read path
	echo -n 'occ_id : '
	read occ_id
	echo -n 'audio_sample : '
	read audio_sample
	echo -n 'priority : '
	read priority
	echo -n 'eta : '
	read eta
	echo -n 'status : '
	read status
	curl -X PUT -F 'user='"$user"'' -F 'task='"$task"'' -F 'pwd='"$path"'' -F 'occ_id='"$occ_id"''   -F 'audio_sample='"$audio_sample"'' -F 'priority='"$priority"'' -F 'eta='"$eta"'' -F 'status='"$status"'' http://$host:$port/api/$id_request
	

	# echo -n 'id : '
	# read id_request
	# echo -n 'task : '
	# read task
	# echo -n 'pwd : '
	# read path
	# echo -n 'status : '
	# read status 
	# echo -n 'audio_sample : '
	# read audio_sample
	# curl -X PUT -F 'task='"$task"'' -F 'pwd='"$path"'' -F 'status='"$status"'' -F 'audio_sample='"$audio_sample"'' http://$host:$port/workers/$id_request
	
}

main(){
	echo -n 'what do you want to do ? [get/insert/delete/update]'
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
		update)
			echo "updating db"
			update
			;;
		*) 
			echo 'we dont do that here' 
			;; 
	esac 
}

main 
