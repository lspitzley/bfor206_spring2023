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



# %%
