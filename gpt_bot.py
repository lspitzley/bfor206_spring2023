"""
This script will be used to send prompts to the 
GPT API and post the replies to reddit.
"""

# %% imports

import os
import openai
from dotenv import load_dotenv
import get_reddit_posts as grp

# %%

# store API credntials
load_dotenv()
openai.api_key = os.environ.get('OPEN_AI_KEY')
openai.Model.list()

def find_relevant_posts(submission_df):
	"""
	Find posts that seem good to respond to.
	You can adjust your criteria to choose what you like.
	This could be based on score, keywords, etc.
	"""

	top_post = submissions_df.sort_values(by='created_utc', ascending=False).head(1)

	return top_post

def prompt_gpt(prompt: str): 
	"""
	Take a string and send it to GPT as a prompt
	"""
	completion = openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
	messages=[{"role": "user", "content": prompt}])

	return completion.choices[0].message

# %% main 

if __name__ == '__main__':


		print('Running GPT Bot')

		reddit = grp.reddit_connection()

		# get posts
		submissions = reddit.subreddit('AskReddit').hot(limit=5)

		# this function is a simpler version of what we had earlier
		submissions_df = grp.create_submission_df(submissions)

		# find relevant posts
		top_post = find_relevant_posts(submissions_df)

		prompt = top_post['title'].values[0]

		print("Post title:", prompt)

		# prompt GPT
		response = prompt_gpt(prompt)

		print("GPT response:", response.content)
