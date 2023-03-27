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
def reddit_connection():
	reddit = praw.Reddit(client_id=APP_ID,
		client_secret=API_SECRET,
		user_agent='Post Downloader')
	print('Successful app authentication:', reddit.read_only)

	return reddit

# TypeHints (-> ) tell you what should be returned 
def get_submissions(reddit, subreddit, limit=10) -> pd.DataFrame:
	"""
	This function will get posts from a subreddit
	and return them as a dataframe.
	"""

	submissions = reddit.subreddit(subreddit).hot(limit=limit)

    # add list to the master list
	df_rows = []
	for submission in submissions:
		df_rows.append([submission.id, submission.score, submission.title, submission.num_comments])

	post_df = pd.DataFrame(df_rows, columns=['id', 'score', 'title', 'num_comments'])

	return post_df

def get_comments_from_post(reddit, post_id) -> pd.DataFrame:
	"""
	This function will return a dataframe of comments for a 
	post. 
	"""
	# get the submission
	submission = reddit.submission(id=post_id)

	# get a list of the comments
	submission.comments.replace_more(limit=0)
	comments_list = submission.comments.list()

	comment_rows = []
	for comment in comments_list:
		comment_rows.append([comment.id, comment.score, comment.created_utc, comment.body, comment.parent_id])

	comments_df = pd.DataFrame(comment_rows, columns=['id', 'score', 'created_utc', 'body', 'parent_id'])

	return comments_df

# %% test our functions

# authentication function
reddit = reddit_connection()

# check the get submissions function
submission_df = get_submissions(reddit, 'cybersecurity')

# check the comments dataframe function
comments_df = get_comments_from_post(reddit, post_id='120j74c')

# %%
