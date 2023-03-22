"""
This script will use praw to get posts from reddit.
"""

#%% imports

import os
import praw
from dotenv import load_dotenv
import pandas as pd

#%% load credentials
# store API credntials
load_dotenv()
APP_ID = os.environ.get('APP_ID')
API_SECRET = os.environ.get('API_SECRET')
print('APP_ID:\t\t', APP_ID)
print('API_SECRET:\t', API_SECRET)

# %% connect to reddit
reddit = praw.Reddit(client_id=APP_ID,
	client_secret=API_SECRET,
	user_agent='Post Downloader')
print('Successful app authentication:', reddit.read_only)


# %%  Use PRAW to download posts
submissions = reddit.subreddit("test").hot(limit=10)
for submission in submissions:
	print(submission.title)


# %% get posts from AskReddit and put them in a dataframe

submissions = reddit.subreddit("AskReddit").hot(limit=100)

# use a for loop to store the posts in a list

# create an empty list
df_rows = []

# for loop over the submissions
for submission in submissions:
	
    # add list to the master list
	df_rows.append([submission.id, submission.score, submission.title])


# %% show the data

# make sure to add import pandas as pd at the top of the script

post_df = pd.DataFrame(df_rows, columns=['id', 'score', 'title'])

# %% histogram of post scores

post_df['score'].plot.hist()

# %%
