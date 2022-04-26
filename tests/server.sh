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
}

