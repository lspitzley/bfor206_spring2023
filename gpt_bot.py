"""
This script will be used to send prompts to the 
GPT API and post the replies to reddit.
"""

# %% imports

import os
import openai
from dotenv import load_dotenv

# %%

# store API credntials
load_dotenv()
openai.api_key = os.environ.get('OPEN_AI_KEY')
openai.Model.list()

# %% send prompt to GPT

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
	{"role": "user", "content": "What was the weirdest part of the pandemic?"}
  ]
)

#%% 
print(completion.choices[0].message.content)



# %% instruct prompt

# Send a prompt to davinci-001 (cheaper than GPT3.5)
AlbResponse = openai.Edit.create(
model="text-davinci-edit-001",
input="Why is Albany, NY the largest city in America?",
instruction="Reply with a very angry sentence."
)

#%% 
print(AlbResponse.choices[0].text)


# %%
