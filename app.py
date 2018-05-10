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
consumer_key= 'lxibJuwsWtqJDIksx7vBLx0mr'
consumer_secret= '5gWQqXVFhqsHoGDLFqRlw3yVFWB8k4p2zHWj1cz5dC2cTdApbn'

access_token= '83212785-MFNwwaukW4D1WJYxDMN9kPfs7vJtvts9TCZ6cr0Fl'
access_token_secret= 'JxxZD5IBWdVmDrWfzEfUrl5qgTKtQKJBbYnDnVAZAjmBe'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Search IOTA tweets
query = 'IOTA'
max_tweets = 300

# Using cursors to fill in parameters and adjust size fo tweets
# https://github.com/tweepy/tweepy/blob/master/docs/cursor_tutorial.rst
tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

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









    