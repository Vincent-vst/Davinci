#! /bin/bash

prerequisite(){
    sudo apt update
    sudo apt install nodejs
    npm install pm2@latest -g
}

daemon(){
    pm2 start python3 src/app.py
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

