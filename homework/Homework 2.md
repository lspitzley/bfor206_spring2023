# Homework 2

In this homework, we will analyze social media posts to
understand patterns of posting behavior and content.

From this analysis, we will learn how to collect data. summarize
data with timestamps, use grouping with `pandas`, and
apply some basic text analysis techniques.

# Data

We will collect data about comments and posts from reddit
with a script that interfaces with the reddit API. The data
will be stored in a `csv` file.

# Setup

You will want to create a Jupyter Notebook to analyze the data.
The analysis will consist of data summarization, visualization,
and text analysis.

<!--  -->
# Scoring

This assignment will be graded out of [16] points. There is a
maximum of [18] possible points.

## 1. Collect the data (5 points)

1. Choose at least ten subreddits to collect data from. You can choose
   any that you like, or go with some of the most popular,
   [listed here](https://www.reddit.com/best/communities/1/).
   Store the list in a `.txt` file and read it into your script (1pt).
2. Collect data from the subreddits. Get the top 100 posts and their
   comments from each subreddit. Store the following data for each post:
   - `subreddit`: the name of the subreddit
   - `id`: the unique identifier for the post
   - `score`: the score of the post
   - `author`: the author of the post
   - `created_utc`: the time the post was created

   For submissions, also add:
   - `title`: the title of the post
   - `selftext`: the body of the post
   - `num_comments`: the number of comments on the post

   For comments, add:
   - `comment`: the body of the comment
   - `parent_id`: the unique identifier of the parent post

   Store the data in two `csv` files, one for the submissions and
   one for the comments (4pts).

## 2. Summarize the data (3 points)

1. Which users have the most submissions/comments (top 5)?
2. Which subreddit has the most distinct comment authors?
3. Which subreddit contains the greatest percentage of submissions
   with a body (i.e. contains a value in the `body` column)?

## 3. Visualize the data (4 points)

1. Plot the total number of comments across all subreddits over time (line plot).
2. Plot a histogram showing the distribution of comment scores.
3. Plot the average number of comments per day of the week.
4. Plot the average number of comments by hour of the day.

## 4. Get insights from the data (4 points)

1. Does the length of a post title correlate with score of the post?
2. What are the top 20 words used in post titles?
3. What are the top 10 most linked website domains?
4. [Short Answer] What would be some other interesting things to analyze? 

## 4. Make your results professionally pretty (2 pts)

Use a **Jupyter Notebook** to produce your results. This tool is
easy to use and will produce professional output. They are also
rendered by Github, so you do not need to do any screenshots
or other trickery to make things look nice.

For an example of a notebook, check out this example on
[basic `pandas` functionality](https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.03-Operations-in-Pandas.ipynb).

# Submission

You may work individually or in pairs.

The homework is due April 15.

Create a new repository using this
[Github Classroom link](https://classroom.github.com/a/y7dX4Doo).

Commit and push your code to this Git repository. The
instructor will grade the last commit before the due
date.

# Checkpoints

These are some quantities/values that you can use to check the
correctness of your code. I will update these as needed.
