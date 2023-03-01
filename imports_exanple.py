"""
This script will be used to demonstrate how
to import external libraries.
"""

#%% Import Time
import time

print(time.asctime())
print(time.time()) # number of seconds since Unix epoch

# %% Import OS

# os has a lot of utilities for interacting with the system.

import os

# show the current working directory
print(os.getcwd())

# list files in the current directory
print(os.listdir())

# list a folder
print(os.listdir('labs/'))

# list the folder *above* the current directory
print(os.listdir('..'))

# %% store the results into a variable
lab_list = os.listdir('labs/')

# %% Requests Library
# requests is used to do HTTP stuff

import requests

# I want to time this
start = time.time() # store the current time
r = requests.get('https://www.albany.edu/business/faculty/lee-spitzley')        
print('the request took ', time.time() - start)


# %% see information from the request

print(r)

print(r.text)


# %% Today's lab

# show only files with .py extension
# https://stackoverflow.com/questions/3964681/
for file in os.listdir():
    if file.endswith(".sh"):
        print(file)

# %%
