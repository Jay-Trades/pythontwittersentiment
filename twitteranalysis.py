# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tweepy
from textblob import TextBlob

consumer_key = "HfHoyutejB5fUJiUrYofzMZwt"
consumer_secret = "WX82ciGpcRhGXknfWANakkxyaAomTW81LzBtHVT68Q1hO9Qnv5"

access_token = "593136066-EmKPca1xW0n7IVm4QYxtj5WYKhpNiEzNP8e7y37K"
access_token_secret ="bkPYoyZAiPjhjsq5QHUOd628OlaNAtmpvg4jt6N2cODIt"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Dog')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    if analysis.sentiment[0]>0:       
        print ('Positive')    
    elif analysis.sentiment[0]<0:       
        print ('Negative')    
    else:       
        print ('Neutral')