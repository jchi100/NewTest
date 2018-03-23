
# coding: utf-8

# In[1]:


# Dependencies
import tweepy
import time
import json

# Twitter API Keys
consumer_key = "JeOpBYvN38K6jwVKoQTuKhofj"
consumer_secret = "qNKYIpKRxVR95w3BzfD9CITJ2xhq7MM3I36yEqh2U6WsJAfB9q"
access_token = "975022209948413954-FxRMca7HQaLq01HP9YoXj3tk6HrHx2w"
access_token_secret = "gt4ZvTpOfSb69flVrWfLcEtpVmZCxhL0ly4BUq8n8GfUf"

# Target Term
target_term = "UnitedAirline"

# Twitter Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Search for all tweets
public_tweets = api.search(target_term, count=5, result_type="recent")

# Loop through all public_tweets
for tweet in public_tweets["statuses"]:

    # Get ID and Author of most recent tweet directed to me
    tweet_id = tweet["id"]
    tweet_author = tweet["user"]["screen_name"]
    tweet_text = tweet["text"]

    # Print Tweet Text and Tweet Author
    print(tweet_text)
    print(tweet_author)

