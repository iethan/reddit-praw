import praw
import json

# create a file called cred.json and put it in the folder with this py file
data = json.load(open('cred.json'))

# the following must be keys in the dictionary, obtained from reddit, see https://praw.readthedocs.io/en/latest/getting_started/quick_start.html

client_secret = data['client_secret']
client_id = data['client_id']
user_agent =data['user_agent'] 

r = praw.Reddit(client_id=client_id,
		client_secret=client_secret,
		user_agent=user_agent)

for submission in r.subreddit('learnpython').hot(limit=10):
    print submission.title
