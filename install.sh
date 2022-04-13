#! /bin/bash  

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

function ctr_c_handler(){
	echo -e "\n${green}closing API...\n${reset}see you later..." 
	{
		{
		deactivate
		} &> /dev/null
	}||{
		echo -e "${red}deactivate ${reset}the venv with : deactivate"
	}
}

trap ctr_c_handler SIGINT 

echo "------------------------------"

case $SHELL in 
	*/zsh) 
		echo "${green}[ZSH] : ${reset} installing Davinci ... "
		source venv/bin/activate
		;;
	*/bash) 
		echo "${green}[BASH] : ${reset} installing Davinci ... "
		source venv/bin/activate
		;; 
	*/fish) 
		echo "${green}[FISH] : ${reset} installing Davinci ... "
		{
			source venv/bin/activate.fish
		} || {
			echo -e "${red}[error] : \n${reset}venv is running on some problem in fish \ndunno why tho ...\n[suggestion] : source venv/bin/activate.fish"  
		}
		;;
esac 
	
{
	pip install -r requirements.txt
} &> /dev/null

echo "------------------------------"


{ 
	python3 src/api.py	
	} || { 
	echo -e "${red}[error] : ${reset}the API ran in some errors" 1>&2
}

