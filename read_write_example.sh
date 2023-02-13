#!/bin/bash

# This script will be used to demonstrate
# different ways of reading and writing data
# to files with bash.

# add some echos to print some text

# echo "test1"
# echo "test2"

# read contents of input.txt into a variable named input
read input < input.txt

echo "The value of \$input = $input"

# we want to put the date and time into the log
# the ` ` will run the command contained inside
echo `date` >> output.log
# echo $(date) # alternative syntax

# We can ping a website using the input from the input file
# The ping command will do this.
# The -c3 flag runs 3 pings and stops. Without this, it will run forever.

ping -c3 $input >> output.log

echo >> output.log # this just adds an extra line for better formatting



echo "Done."
