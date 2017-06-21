# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 01:56:57 2017

@author: Muhammad Salek Ali
"""

# 1- Importing libraries for twitter and NLP
#--------------------------------------------
import numpy as np
import tweepy
from textblob import TextBlob


# 2- Authentication
#-------------------
consumerKey= 'enter_yours_here'
consumerSecret= 'enter_yours_here'

accessToken='enter_yours_here'
accessTokenSecret='enter_yours_here'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)


# 3- Prepare query features
#---------------------------

teams = ['India', 'Pakistan']
hashtag = "PAKvsIND" 

#Tweets to be collected:
fromDate = "2017-06-17"


# 4- Analysis Result Labels
#----------------------------
def senti(analysis, threshold = 0):
    if analysis.sentiment[0]>threshold:
        return 'Positive'
    elif analysis.sentiment[0]==threshold:
        return 'Neutral'
    else:
        return 'Negative'


# 5- Retrieve Tweets and Save Them
#----------------------------------

meanPolarities = dict()

for team in teams:
    teamPolarities = []

    #Save the tweets in csv
    with open('%s_tweets.csv' % team, 'w') as teamFile:
        teamFile.write('tweet,label,sentiment\n')
        maxQuery=5000
        for tweet in tweepy.Cursor(api.search,
                                   q=[hashtag,team],
                                   include_entities=True
                                   ).items():
            text = TextBlob(tweet.text)
            #Get the label corresponding to the sentiment analysis
            teamPolarities.append(text.sentiment[0])
            print (len(teamPolarities))
            print (senti(text))
            teamFile.write('%s,%s,%s\n' % (tweet.text.encode('utf8'), senti(text),str(text.sentiment[0])))
            if (len(teamPolarities)>=maxQuery):
                break
    #Save the mean for final results
    meanPolarities[team] = np.mean(teamPolarities)


# 6- Output a Result
#--------------------

print ('Mean Sentiment Polarities:')
print(meanPolarities)
