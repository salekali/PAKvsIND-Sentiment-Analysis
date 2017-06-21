# PAKvsIND-Sentiment-Analysis
# twitter_sentiment_challenge

## Overview

This code is a sentiment analysis of the PAKvsIND hashtag, from the ICC Champions Trophy 2017 final.
The code uses [tweepy](http://www.tweepy.org/) to access the Twitter API and [TextBlob](https://textblob.readthedocs.io/en/dev/) for sentiment analysis.

The code takes a sample of 5000 tweets with the search terms 'PAKvsIND' and 'Pakistan', and 5000 tweets with the search terms 'PAKvsIND' and 'India'. These tweets are stored in separate .csv files, and the code outputs an average polarity of both sets of tweets. 
The range of polarity is from 1 to -1, representing a range in positive and negative sentiments. 


## Dependencies
* numpy (https://docs.scipy.org/doc/numpy-1.12.0/reference/)
* tweepy (http://www.tweepy.org/)
* textblob (https://textblob.readthedocs.io/en/dev/)

Install missing dependencies using [pip](https://pip.pypa.io/en/stable/installing/)

## Usage

After installing dependencies, open a terminal and navigate into the directory containing the code. Then run the code via:

```
python demo.py
```

# Future Work

Will add a python notebook file with visualisation of sentiment analysis data.
