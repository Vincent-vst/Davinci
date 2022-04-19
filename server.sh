#! /bin/bash

echo -n "[port] : "

read port

echo -n "[localhost] :"

hostname -i | awk '{print $2}'

echo '---------------'

{
    
    python3 main.py
    
    
    } || {
    
    echo "error"1>&2
    
    while true;
    
    do echo -e 'http://10.16.0.250 OK\n\n$(iostat)' \
        
        nc -l -k -p $port -q 1;
        
    done
    
    
}


