"""
This script will contain a few examples of regular expressions.

To test regular expressions, I recommend https://regex101.com
"""

#%% imports
import re

#%% Example 1

"""
re.search only returns the first match it finds.
"""

test_string1 = 'BFOR 206: Programming for Analytics'

print(re.search(r'bfor', test_string1)) # None (because it is lowercase)

print(re.search(r'BFOR', test_string1)) # finds a match

# %% create a url finder function

def find_urls(text):
    """
    This function checks a string and returns 
    a list of URLs from that string. If there are
    none, it will return an empty list.
    """

    print('find_urls received the text:', text)

    url_re = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    
    # regex to find urls
    urls = re.findall(url_re, str(text))

    print('find_urls found:', urls)

    return urls

#%% define a function to run tests

def test_find_urls():
    """
    This contains a few tests to make sure that
    the function is working correctly.
    """

    case0_input = "This string has no URLs."
    case0_output = []

    # send data to function and see if output matches.
    assert find_urls(case0_input) == case0_output

    # try with one URL
    case1_input = "This has a url at https://github.com"
    case1_output = ['https://github.com']

    assert find_urls(case1_input) == case1_output

    # try with multiple URLs
    # note that the comma is included for github
    # TODO - fix this
    case2_input = "Some people use https://github.com, others use https://bitbucket.com"
    case2_output = ["https://github.com,", "https://bitbucket.com"]

    assert find_urls(case2_input) == case2_output

    # try with a numpy nan value
    # to fix this, the function needs to convert input to a string
    import numpy as np
    case3_input = np.nan
    case3_output = []

    assert find_urls(case3_input) == case3_output

# %% call the test function

test_find_urls()

# %%
