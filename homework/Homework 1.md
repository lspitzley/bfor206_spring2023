# Homework 1


The purpose of this homework is to develop a bash script that uses the ping
command to test whether a device is online. The results of this script
should be logged with a timestamp. The script should be run as a cron job.
If a server is not responding, email the system administrator (you).

## Useful commands
### ping
You can use this to check a device is responding.

```console
ping 192.168.1.1 -c3
ping google.com -c3
```

### grep
The grep command uses regular expressions to match text.

A good overview of how to use this to get the percentage
of packet loss can be found on this
[StackOverflow Answer](https://stackoverflow.com/questions/8314219/how-to-get-the-percent-of-packets-received-from-ping-in-bash)


### cut
Split a string using the percentage sign and
get the first part of the split:



```console
echo “100% awesome” | cut -d”%” -f1
```
Get the second split:

```console
echo “100% awesome” | cut -d”%” -f2
```

Split using space instead of percentage:

```console
echo “100% awesome” | cut -d” ” -f1
```

You might also use the commands `sed` or `awk`, which
can use regular expressions to find the percentage of
packets returned.

### mail (from mailutils package)

To install:
```bash
sudo apt update # update software sources

sudo apt install mailutils # install mail package
```

```bash
# to send a message using echo
echo “message body” | mail -s “subject” kali@kali

# check mail with:
cat /var/mail/kali
```

## Script functionality

- Use a list of IP addresses using an input file or arguments
- Use a loop to ping a list of devices
- Parse the output of the ping command
- Check the output status
- If the ping is not responding or is missing packets, report this to the log
and send an email
- If the device is normal, report this to the log
- The script should run every five minutes.


# Grading

### 1. Ping devices (2 pts)
- 1.1  Show that the script pings addresses (1pt)
- 1.2  The script should be able to handle an arbitrary number of addresses to ping.
To demonstrate this, ping at least *3* addresses.
One of the addresses should contain your UAlbany NetID. For
example, a NetID of AB123456 should ping 12.34.56.1. (1pt)

### 2. Log information (2 pts)
- Show the log file with script output.
The logs *must* have a
timestamp for each entry (2pts)

### 3. Email when getting errors (3 pts)
- Show the emails you receive from the failed pings for the out-of-service IP address.
  To receive credit for this, ping one address that does not respond and show the
  email that is sent as a result of the failed ping.

### 4. Run task at regular intervals (3 pts)
- Show the crontab file and the log demonstrating the program
  runs at the specified intervals.

### 5. Avoid hard coded inputs (3 pts)
To recive credit for the following points, they must all be in a single script.

- 5.1 Accept addresses as arguments (1pt)
- 5.2 Read addresses from a text file (1pt)
- 5.3 Read *multiple* addresses from a text file (1pt)

### 6. Code Management (1 pt)
- 6.1 Have at least 5 commits showing progress (1pt)
- 6.2 If two people worked on the assignment, then have at least 2 commits per person 
  (1pt deduction if not included). 



## Scoring
The assignment is graded out of 12 points. Any score
above 12 is worth extra credit, meaning the highest
possible grade is 14/12.

# Submission

## Submission Format

Submissions include your code (no screenshots of your code) and screenshots for each of
the items you wish to receive credit for. Each screenshot should
be named according to the item, e.g. `Q5-1.jpg`. Submission materials
should be submitted to you the assignment repository.

## Point Reductions
I will deduct points for certain things:
- Submitting code as a screenshot instead of the actual `.sh` file (-1 pt).
- Submitting screenshots that are not clearly labeled (-1 pt).

## Submission Location
All homework will be submitted through Github
Classroom.
The link for this is assignment is on
[Github Classroom](https://classroom.github.com/classrooms/60333327-bfor-206-classroom-b02d2c).

## Teams (Optional)
You may work with one other person. If working with someone else,
then make sure to create a group submission. Include both names
in the README.md to make grading easier.
