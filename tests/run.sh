#! /bin/bash 

server=/home/v_descatoire/Developer/Davinci/src/api.py

if [[ ! -e $server ]]; then 
	echo "can't find api.py"
else 
	{
		python3 $server
	} || {
		echo "error" 
	}
fi 

