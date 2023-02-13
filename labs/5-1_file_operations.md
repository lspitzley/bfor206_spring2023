# BFOR 206 Lab
## Class 5-1: read/write


# Task Description

Write a script that pings a website
and logs the date/time and the ping
result to a log file.



# Normal Scenario

## Input
**File:** File containing a URL or IP address

## Output
**File:** The date/time and output of the ping
          ping command.





# Test Cases

```shell
######## Normal scenarios ##########

# Input (from file):
google.com

# Output (in a file)

Script Started at Tue Feb 15 18:30:59 EST 2021

PING google.com (142.250.65.174): 56 data bytes
64 bytes from 142.250.65.174: icmp_seq=0 ttl=117 time=12.907 ms
64 bytes from 142.250.65.174: icmp_seq=1 ttl=117 time=12.508 ms
64 bytes from 142.250.65.174: icmp_seq=2 ttl=117 time=12.790 ms

--- google.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 12.508/12.735/12.907/0.167 ms

Done.

Script Started at Tue Feb 15 18:40:00 EST 2021

PING google.com (142.250.65.174): 56 data bytes
64 bytes from 142.250.65.174: icmp_seq=0 ttl=117 time=7.091 ms
64 bytes from 142.250.65.174: icmp_seq=1 ttl=117 time=13.129 ms
64 bytes from 142.250.65.174: icmp_seq=2 ttl=117 time=12.938 ms

--- google.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 7.091/11.053/13.129/2.802 ms

Done.
```




# Submission instructions

**Scripts that output bash errors will not be accepted!**

Run the script at least twice to show the
results being appendend to the file.

When you are finished, show the instructor:
1.  Your code.
2.  An output **file** that looks very
    similar to the output in the test cases.
