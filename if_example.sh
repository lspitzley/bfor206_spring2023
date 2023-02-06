#!/bin/bash 

# this script will show some examples of if statements
# in bash.

echo "script started"

if [ $1 -gt 0 ]
	then echo "Passed the first if"
elif [ $1 -lt 0 ]
	then echo "The elif is true"
else 
	echo "no true statements"

fi


echo "Done."
