# API Lab

In this lab, you will create an API key for Reddit and use it to 
download posts. You will need to use .env to store your API key.

## Reddit API

I recommend creating a new account for this project. You can create a new 
account without using an email address by going to old.reddit.com. You can
skip the email verification step by clicking `Next`.

Get an API key from Reddit. You can do this by going to your preferences and
clicking on the "apps" tab. You can create a new app and get a key. Go
to [The Apps page](https://www.reddit.com/prefs/apps/) and create an app. 
You will see a string of characters that is your API key. You will also 
see a string of characters that is your API secret. 

## .env

To store your API key and secret, you will need to create a file called `.env`. This file
should be in the same directory as your project. You should create an empty
file called `.env` and then add the following lineS to it (replacing the
`your_app_id` and `your_app_secret` with the your API key and secret):

```bash
APP_ID=your_app_id
APP_SECRET=your_app_secret
```

### .gitignore

You should also create a file called `.gitignore` (you might already have one)
and add the following line to it:

```bash
.env
```

This will prevent your API key from being uploaded to GitHub.


## Reddit API Wrapper

[Read the documentation](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html) before you begin. It has all of the information you need to get started.

You will need to install the `praw` package. You can do this by running the following command in your terminal:

```bash
pip install praw
```

Follow the instructions from today's class to set up API access.

## Completion

To get credit for this lab, you should:

- [ ] Load and print your API information from .env
- [ ] Create a Reddit connection
- [ ] Download a list of posts from a subreddit of your choice and print them
- [ ] Update your `.gitignore` to exclude `.env` files
- [ ] Commit and push your code to GitHub. 
        Show that your `.env` file is not in your repository.