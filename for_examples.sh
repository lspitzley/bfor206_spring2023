#!/bin/bash

echo "Started $0"


# check if there is one argument
if [ $# -ne 1 ]
then
	echo "Please enter exactly one argument to see an example."
	exit # the script will end here. 
fi


# EXAMPLE 1: use a range
if [ $1 -eq 1 ]
then
	for i in {0..5}
	do
		echo "The value of \$i is $i"
	done


elif [ $1 -eq 2 ]
then
	name="Lee A Spitzley"

	for part in $name
	do
		echo "$part"
	done


elif [ $1 -eq 3 ]
then
	for n in {0..10..2}
	do
		let "sum=$sum + $n"
		echo "The sum at \$n = $n is $sum"
	done

elif [ $1 -eq 4 ]
then
	N=10
	for (( i=0; i<=N; i++ ))
	do
		echo "The value of \$i is $i"

	done
fi





echo "Done."
