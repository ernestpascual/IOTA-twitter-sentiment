"""
IOTA Twitter Sentiment Analyzer: 
It gets all IOTA tweets of the day and outputs the overall sentiment.

Author: eep
based on the twitter senitment challenge by Siraj Parval
https://github.com/llSourcell/twitter_sentiment_challengey
"""
import tweepy
import numpy
from textblob import TextBlob

# Twitter Authentication
consumer_key= 'KEY_HERE
consumer_secret= 'SECRET_KEY_HERE'

access_token= 'ACCESS_TOKEN_HERE'
access_token_secret= 'TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Search IOTA tweets
tweets = api.search('IOTA')

# avg_polarity list declartion
avg_polarity = []

# Feed tweets to TextBlob and filter needed tweets
for tweet in tweets:
    analysis = TextBlob(tweet.text)
    # Eliminate use only objective tweets to prevent bias
    if (analysis.sentiment.subjectivity < 0.5):
            avg_polarity.append(analysis.sentiment.polarity)

# Get average of polarity of sentiments
avg_polarity = numpy.average(avg_polarity)

# Output decision 
if (avg_polarity > 0):
    print "IOTA is looking pretty good. Check your technical analysis for points of entry."
else:
    print "You might want to check other cryptos."










    