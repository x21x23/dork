#!/bin/bash
cat googledorks_full.txt | while read line; 
do 
	python3 search.py $line; 
done
#EOF