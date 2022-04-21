#! /bin/bash

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

set -e


prerequisite(){
	if [  -n "$(uname -a | grep Ubuntu)" ]; then
		sudo apt update
		sudo apt install nodejs
		npm install pm2@latest -g
	else
		echo "${red}[error] : ${reset}unsuported distro"
	fi  
}

davinci_daemon(){
	{
		# pm2 start python3 ./src/app.py
		pm2 start src/app.py --name Davinci --interpreter python3
	} &> /dev/null
}

usage(){
    help="Usage: \n
    davinci [options] \n
    Options: \n
    -v, --version      get version \n
    -l, --list         list pm2 daemon and their status \n
    -logs              print davinci logs \n
    -h, --help         help page
    " 

    for arg in "$@"
    do
        case $arg in
            "-h" | "--help" )
                echo -e $help
            ;;
            "-v" | "--version" )
                echo "version 0.1"
            ;;
            "-l" | "--list" )
                pm2 list
            ;;
            "--logs" )
                pm2 logs
            ;;
            *)
                echo -e "unknown argument \n-h | --help for help"
            ;;
            
        esac
    done
}

install(){ 

	# activating venv
	case $SHELL in 
		*/zsh) 
			echo "${green}[ZSH] : ${reset} installing Davinci ... "
			source ./venv/bin/activate
			# ^ this isn't gonna make the terminal (venv) once the script is done
			# cause a subprocess can't change its parent environment ... 
			;;
		*/bash) 
			echo "${green}[BASH] : ${reset} installing Davinci ... "
			source ./venv/bin/activate
			;; 
		*/fish) 
			echo "${green}[FISH] : ${reset} installing Davinci ... "
			{
				source ./venv/bin/activate.fish
			} || {
				echo -e "${red}[error] : \n${reset}venv is running on some problem in fish \ndunno why tho ...\n[suggestion] : source venv/bin/activate.fish"  
			}
			;;
		*) 
			echo "unsuported $SHELL"
	esac 
	
	# install requierements
	{
		pip install -r requirements.txt
	} &> /dev/null

}

summary(){
	pm2 list 
}


prerequisite
install 
davinci_daemon
summary
