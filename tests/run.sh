#! /bin/bash 

{
	python3 ../src/api.py
} || { 
	echo "error"
}
