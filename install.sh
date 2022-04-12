#! /bin/bash  

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

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
		} &> /dev/null
		echo -e "${red}[error] : \n${reset}venv is running on some problem in fish \ndunno why tho ...\n[suggestion] : source venv/bin/activate.fish"  
		;;
esac 
	
{
	pip install -r requirements.txt
} &> /dev/null

echo "------------------------------"

python3 src/api.py
