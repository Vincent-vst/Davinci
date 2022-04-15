#! /bin/bash 

port=3002

## prerequis 
prerequisite(){
	sudo apt update
	sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
	# source /venv/bin/activate.fish 
	# pip install -r requirements.txt 
	sudo ufw allow $port 
}

service_file=/etc/systemd/system/davinci.service
service(){
	if [[ ! -e $service_file ]]; then 
		touch /etc/systemd/system/davinci.service
		cat /bin/davinci.service >> $service_file
}

start_server(){
	{
		sudo systemctl start davinci
	} || {
		echo "can't start server"1&>2 
	}
}








