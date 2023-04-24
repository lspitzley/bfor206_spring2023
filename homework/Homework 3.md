# Homework 3: Bot Operations

In this homework, you will create a bot that 
is able to choose a post to make a comment on,
generate a response to that post, and post the response.

There are five parts to this homework:

1. Scanning reddit to choose a post to comment on.
2. Create a bot that can generate a response and post it.
3. Collect post history from your bot and store the history in a 
    CSV file.
4. Run the bot on a schedule.
5. Analyze statistics about your bot.


This homework has 22 points available and is graded out of 18. 
Any additional points will be counted as extra credit.

The homework is due on **May 10th at 11:59pm**. 

## Part 1: Scanning reddit

1. What is your method to choose a post or comment to respond to? 
   What are the pros and cons of your method? (2pts)

   Write the response to this in your Jupyter Notebook or 
   document it in the function docstring.

2. Provide two examples of posts or comments that your bot 
   would respond to. (2pts)

3. Check your bot's post history to avoid duplicate posts (2pts).


## Part 2: Create a bot to generate a response

1. Send prompts to a language-generating API (e.g. GPT; 1pt).
2. Check the response for suitablity (1pt).
3. Post the response. 
    [Documentation](https://praw.readthedocs.io/en/stable/code_overview/models/submission.html#praw.models.Submission.reply)(1pt).
4. Append the id of the submission or comment to a text file. 
   This will be used to check for duplicate posts (1pt).

## Part 3: Collect post history

1. Add a function in the `get_reddit_posts.py` file to format 
   the post history of your bot as a dataframe. Save the dataframe 
   to a file (2pts). 

2. Save the post history with a timestamp in the filename to 
    create a new file each time the bot is run. The filename
    should look something like 
    `bot_history_2023-03-30_03-29-22-AM.csv`. The code snippet 
    below can be used for this (1pt).

```python
import datetime

filename = 'bot_history_' + datetime.now().strftime("%Y-%m-%d_%I-%M-%S-%p")
```

## Part 4: Run the bot on a schedule


1. Set the bot script to run automatically. What time
   intervals did you choose? Why? (2pts)

2. Include a screenshot showing the bot schedule configuration.
    (1pt)



## Part 5: Analyze statistics about your bot

Use a Jupyter Notebook to analyze the following questions. Use
the latest version of your bot history file when submitting.

1. How many total comments has your bot made? (1pt)
2. Plot a histogram showing the hours of your bot's posts. (1pt)
3. How many replies has your bot received? (1pt)
4. What is the average score of your bot's posts? (1pt)
5. What is the highest score of your bot's posts? (1pt)
6. Have any comments been deleted? If so, how many? (1pt)
7. Has any reply labeled your bot as a bot? If so, how many? (1pt)


## Guides

### Scheduling a script to run automatically

1. On a Mac, you can use the automator tool to schedule a script to run.
   See [this guide](https://stackoverflow.com/questions/6442364/)
   for more information.

2. On Windows, you can use the Task Scheduler to schedule a script 
    to run.
   See [this guide](https://www.windowscentral.com/how-create-automated-task-using-task-scheduler-windows-10)
   for more information.

3. On Linux, you can use the cron tool to schedule a script to run.
   See [this guide](https://opensource.com/article/17/11/how-use-cron-linux)
   for more information.


## Submission

You may do this homework individually or with a partner. If you
work with a partner, you must include both of your names in
the README.md file.

Commit and push your code to this Git repository. The instructor will grade the last commit before the due date.

The link to the Github Classroom submission folder is: 
[Homework 3](https://classroom.github.com/a/O_kYm6FI). 