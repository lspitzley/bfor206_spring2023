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

	submissions = reddit.subreddit(subreddit).top(limit=limit)

    # add list to the master list
	df_rows = []
	for submission in submissions:
		# print(submission.id)
		# print([submission.author.name])

		"""
		If the user has deleted their account, there 
		will not be any value for the author name. We 
		will replace this with the name [deleted].
		"""
		if not hasattr(submission.author, 'name'):
			print('found deleted user')
			author_name = '[deleted]'
		else:
			author_name = submission.author.name

		df_rows.append([submission.id, submission.score, submission.title, submission.num_comments, submission.subreddit.display_name, author_name, submission.created_utc, submission.selftext])

	post_df = pd.DataFrame(df_rows, columns=['id', 'score', 'title', 'num_comments', 'subreddit', 'author', 'created_utc', 'selftext'])

	return post_df

def create_submission_df(submissions: praw.reddit.Submission) -> pd.DataFrame:
	"""
	This function will create a dataframe from a list of submissions.
	"""

	df_rows = []
	for submission in submissions:
		# print(submission.id)
		# print([submission.author.name])

		"""
		If the user has deleted their account, there 
		will not be any value for the author name. We 
		will replace this with the name [deleted].
		"""
		if not hasattr(submission.author, 'name'):
			print('found deleted user')
			author_name = '[deleted]'
		else:
			author_name = submission.author.name

		df_rows.append([submission.id, submission.score, submission.title, submission.num_comments, submission.subreddit.display_name, author_name, submission.created_utc, submission.selftext])

	post_df = pd.DataFrame(df_rows, columns=['id', 'score', 'title', 'num_comments', 'subreddit', 'author', 'created_utc', 'selftext'])

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
		"""
		If the user has deleted their account, there 
		will not be any value for the author name. We 
		will replace this with the name [deleted].
		"""
		if not hasattr(comment.author, 'name'):
			print('found deleted user')
			author_name = '[deleted]'
		else:
			author_name = comment.author.name
		
		comment_rows.append([comment.id, comment.score, comment.created_utc, comment.body, comment.parent_id, author_name, comment.subreddit.display_name])

	comments_df = pd.DataFrame(comment_rows, columns=['id', 'score', 'created_utc', 'body', 'parent_id', 'author', 'subreddit'])

	return comments_df

# %% test our functions

# authentication function
reddit = reddit_connection()

# check the get submissions function
submission_df = get_submissions(reddit, 'cybersecurity')

# check the comments dataframe function
comments_df = get_comments_from_post(reddit, post_id='120j74c')

print(comments_df.shape)
# %% read in the list of subreddits

# read in the list of subreddits from a txt file
with open('subreddit_list.txt', 'r') as f:
	subreddits = f.read().splitlines()


# %% get the top 100 posts from each subreddit

submission_df_list = []

for sr in subreddits:
	print(sr)
	submission_df_list.append(get_submissions(reddit, sr, 100))

# %% concatenate the dataframes

submissions_df = pd.concat(submission_df_list)

# %% sample 10 posts

# get the id column, randomly sample 10 rows, convert to list
post_ids = submissions_df['id'].sample(10).to_list()

# %% get comments for the posts

comment_df_list = []

for post in post_ids:
	print('working on', post)
	comment_df_list.append(get_comments_from_post(reddit, post))

# %% concatenate all comments into one df

comments_df = pd.concat(comment_df_list)

# %% write data into csv

comments_df.to_csv('data/comments_df_10.csv')

# %%
