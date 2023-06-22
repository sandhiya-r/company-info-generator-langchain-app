import tweepy
import logging
import os
import datetime

logger = logging.getLogger("twitter")
os.environ['TWITTER_API_KEY']='DQbLPQfwJiiM7Mbx0ef1sM5Hl'
os.environ['TWITTER_API_SECRET']='vmuB3JfWHTdKcdPIZyzSgOahr1dMTAABlxi5lyN1iYGZqEvqCp'
os.environ['TWITTER_ACCESS_TOKEN']='705723008-BTeExXIwTywRUIkUNiFacZq0ULUCI5ov2MuYI4SF'
os.environ['TWITTER_ACCESS_SECRET']='iZDIA1UJctkDN0mZQkaars02CK5N3a9Qhs738wtvuuIeX'

#interacting with twitter API

twitter_client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAExwoQEAAAAAVQkiA9jrng6jO3uW7CTA1ivfio8%3DsFnXxWmMGkQYha2hWmSxWxLGJrPridhaP4CEusZKo5e1Ve3NBD',consumer_key='DQbLPQfwJiiM7Mbx0ef1sM5Hl', consumer_secret='vmuB3JfWHTdKcdPIZyzSgOahr1dMTAABlxi5lyN1iYGZqEvqCp',access_token='705723008-BTeExXIwTywRUIkUNiFacZq0ULUCI5ov2MuYI4SF',access_token_secret='iZDIA1UJctkDN0mZQkaars02CK5N3a9Qhs738wtvuuIeX')

def scrape_tweets(username,num_tweets):
    userid = twitter_client.get_user(username=username).data.id
    tweets = twitter_client.get_users_tweets(id=userid,max_results=num_tweets,exclude=['retweets,replies'])

    tweet_list = []
    #want to return a list of dictionaries
    for tweet in tweets.data:
        tweet_dict = {}
        tweet_dict['text']=tweet['text']
        tweet_dict['url']=f"https://twitter.com/{username}/status/{tweet.id}"
        tweet_list.append(tweet_dict)
    return tweet_list