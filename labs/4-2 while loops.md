# BFOR 206 Lab
## Class 4-2: While Loops


# Task Description

Write a script that accepts an integer argument or
reads user input, and then outputs the Fibonacci
sequence up to that number, or the last number 
is less than the input.

For example, an input of 5 should yield
0 1 1 2 3 5

and an input of 6 should also yield
0 1 1 2 3 5

For more information about Fibonacci numbers,
see the
[Wikipedia page](https://en.wikipedia.org/wiki/Fibonacci_number).



# Normal Scenario

## Input
**Arguments:** an integer *limit*.


## Output
**Terminal:** The sequence up to the value *limit*.



# Test Cases

```shell
######## Normal scenarios ##########

# Input:
4

# Output:
0 1 1 2 3  

# Input:
8

# Output:
0 1 1 2 3 5 8

# Input: 
100

# Output:
0 1 1 2 3 5 8 13 21 34 55 89

######### Special Cases ##########

#---- The 0th number of the sequence ----#
# Input:
0

# Output:
0

#---- The 1st number of the sequence ----#
# Input:
1

# Output:
0 1
# OR
0 1 1

```


# Submission instructions

**Scripts that output bash errors will not be accepted!**

When you are finished, submit two screenshots on Blackboard:
1.  A screenshot of your code.
2.  A screenshot of correct output as defined in the
    test  cases.
