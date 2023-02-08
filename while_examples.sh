#!/bin/bash

# This script has a couple of examples of while loops

if [ $# -ne 1 ]
then
	echo "Please input exactly one argument"
	exit
fi

LIMIT=10

# if statements to control which example runs

if [ $1 -eq 1 ]
then
	counter=0

	# this loop is functionally equivalent to a for loop
	while [ $counter -le $LIMIT ]
	do
		echo "\$counter = $counter"
		let "counter += 1"
	done

elif [ $1 -eq 2 ]
then
	a=0
	while [ $a -lt $LIMIT ]
	do
		let "a += 1"

		# check if a is 3 or 9

		if [ $a -eq 3 ] || [ $a -eq 9 ]
			then continue # also try this with break 
		fi

		# print out the value of a
		echo "\$a = $a"
	done

fi



