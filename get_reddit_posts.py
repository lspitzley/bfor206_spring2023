"""
This script will use praw to get posts from reddit.
"""

#%% imports

import os
import praw
from dotenv import load_dotenv

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


# %%
