#Data Processor module and methods
import json
import codecs
import math
import random
import os
import bz2

# =============================================================================
# Make sure to store raw json files under raw folder and processed csv in processed folder
# =============================================================================
csv_filename = 'processed/hash.txt'
COORDINATES = 'coordinates'
ENTITIES = 'entities'
HASHTAGS = 'hashtags'

# =============================================================================
# Captures the contents of the file
# =============================================================================
def loadFile(filename):
     with open(filename) as file:
            content = file.read()
            return content

def get_clean_files(raw_tweets):
    files = os.listdir(raw_tweets)
    if '.DS_Store' in files:
        files.remove('.DS_Store')
    return files
# =============================================================================
# Reads the json file and split record wise. If record does not have required values
# then do not write to csv file
# =============================================================================
def readFile(content):
    tweets = content.split('\n')
    fout = codecs.open(csv_filename, 'a', 'utf-8')
    #print("Number of tweets collected in this stream: ",len(tweets))
    data = []
    read=True
    for tweet in tweets:
        if read:
            [id,hashtags,long,lat] = parseTweets(tweet)
            hashes = ""
            #print("Tweets with all required features")
            for hash in hashtags:
                hashes = hashes + '#' +hash
            if id and long and hashes:
                print(id)
                record =  str(id) + ',' + hashes + ',' + str(long) + ',' + str(lat)
                fout.write(record + "\n")
    fout.close()
    return data        
           
# =============================================================================
# Loads the json and also fill up default values            
# =============================================================================
def parseTweets(content):
    try:
        obj = json.loads(content)
        lat = False
        long = False
        if 'limit' in obj:
            return ['','',0,0]
        if 'delete' in obj:
            return ['','',0,0]
        if obj['lang'] != 'en':
            return ['','',0,0]
        id = obj['id']
        if obj[COORDINATES]:
            long = obj[COORDINATES][COORDINATES][0]
            lat = obj[COORDINATES][COORDINATES][1]
        else:
            return ['','',0,0]
            
        hashtags = []    
        for hashtag in obj[ENTITIES][HASHTAGS]:
            hashtags.append(hashtag['text'])   
        if len(hashtags) == 0:
            return ['','',0,0]          # Some Default Hashtags
        return [id,hashtags,long,lat] 
    except:
        return ['','',0,0]
    
    
if __name__ == '__main__':
    raw_tweets = 'raw_tweets/'
    files = get_clean_files(raw_tweets)
    for file in files:
        print("---------------------------------------------------------------")
        print(file)
        content = loadFile(raw_tweets+file)
        data = readFile(content)
