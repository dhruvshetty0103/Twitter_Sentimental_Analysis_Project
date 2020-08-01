#!/usr/bin/env python
# coding: utf-8


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

twitterfile = pd.read_csv('hydrated_lockdownextension.csv')

twitterfile

twitterfile.info()

twitterfile.describe()

data = twitterfile.drop(['coordinates','created_at','hashtags','media','urls','favorite_count','id','in_reply_to_screen_name','in_reply_to_status_id','in_reply_to_user_id','lang','place','possibly_sensitive','retweet_count','retweet_id','retweet_screen_name','source','tweet_url','user_created_at','user_screen_name','user_followers_count','user_default_profile_image','user_description','user_favourites_count','user_followers_count','user_friends_count','user_listed_count','user_location','user_name','user_screen_name','user_statuses_count','user_time_zone','user_urls','user_verified'],axis=1)
data

data['length']=data['text'].apply(len)
data
data['length'].plot(bins=100, kind='hist')

data.describe()

import re

def remove_urls (vTEXT):
  vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', str(vTEXT), flags=re.MULTILINE)
  return(vTEXT)
punc_removed=remove_urls(data['text'])

import string

table=str.maketrans("","",string.punctuation)
punc_removed=[w.translate(table) for w in data['text']]
punc_removed=''.join(punc_removed)

def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')
print(deEmojify(punc_removed))

'''import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
# ...
filtered_words = [word for word in punc_removed if word not in stopwords.words('english')]
filtered_words=''.join(filtered_words)
print(filtered_words)
'''