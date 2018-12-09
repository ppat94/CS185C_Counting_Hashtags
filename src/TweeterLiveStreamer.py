#module to stream data
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 09:05:23 2018

@author: aparnakale
"""

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from urllib3.exceptions import ProtocolError
from tweepy import OAuthHandler
from tweepy import Stream
import numpy as np
import time
import io

#Variables that contains the user credentials to access Twitter API
access_token = "263851696-GbtvKb3DLU7Gud06qjNy1rub6FKnGGMd0DILmBjW"
access_token_secret = "jSFT3jttoroCEdAKXEDM5vYxMxsmSosjsTh3eRP4iortP"
consumer_key = "joViRtVRFDnQVEyGaOWFcdXOm"
consumer_secret = "iMSHHuVj1ODKw0e1Iiec547g9mcB2uNUIy3JEVaB7Jj4BhcXxH"
start_time = time.time()
print(start_time)

class l(StreamListener):
    def __init__(self, start_time, time_limit=100):
        print("-------------------------------------------------------------------------")
        print("----------Downloading Tweeter's Live Stream for 10seconds ---------------")
        print("-------------------------------------------------------------------------")
        
        self.time = start_time
        self.limit = time_limit
        self.tweet_data = ""
        i = np.random.randint(999999,size=1)
        self.filename = "raw_tweets/TweetStream"+str(i[0])+".txt"
        
    def on_data(self, data):
        saveFile = io.open(self.filename, 'a', encoding='utf-8')
        while (time.time() - self.time) < self.limit:
            self.tweet_data = self.tweet_data  + str(data) 
            print('---Time Remaining in seconds to Collect Tweets---')
            print((self.limit+self.time) - time.time())
            return True
        
        saveFile = io.open(self.filename, 'w')
        saveFile.write(self.tweet_data)
        saveFile.close()
        exit(0)
        return False

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l(start_time, time_limit=100))

    GEOBOX_WORLD = [-180, -90, 180, 90]
    GEOBOX_USA = [-179.1506, 18.9117, -66.9406, 71.4410]
    GEOBOX_GERMANY = [5.0770049095, 47.2982950435, 15.0403900146, 54.9039819757]
   
    stream.filter(locations=GEOBOX_WORLD)
    
