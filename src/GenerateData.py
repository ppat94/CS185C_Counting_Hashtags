import json
import codecs
import math
import random

# =============================================================================
# Make sure to store raw json files under raw folder and processed csv in processed folder
# =============================================================================
csv_filename = 'processed/hash.csv'

# =============================================================================
# Captures the contents of the file
# =============================================================================
def loadFile(filename):
     with open(filename) as file:
         content = file.read()
     return content

# =============================================================================
# Reads the json file and split record wise. If record does not have required values
# then do not write to csv file
# =============================================================================
def readFile(content):
    tweets = content.split('\n')
    fout = codecs.open(csv_filename, 'a', 'utf-8')
    print(len(tweets))
    data = []
    read=True
    for tweet in tweets:
        if read:
            [id,hashtags,long,lat] = parseTweets(tweet)
            hashes = ""
            for hash in hashtags:
                hashes = hashes + '#' +hash
            if id and long and hashes:
                print (id)
                record =  str(id) + ',' + hashes + ',' + str(long) + ',' + str(lat)
                fout.write(record + "\n")
    fout.close()
    return data

# =============================================================================
# Generate Random latitude and longitude for different locations to fill up empty twitterjson
# =============================================================================
def generateRandomCoordinates():
    radius =10000
    radiusInDegrees=radius/111300

    x0 = 33.748997
    y0 = -84.387985
    u = float(random.uniform(0.0,1.0))
    v = float(random.uniform(0.0,1.0))

    w = radiusInDegrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)

    xLat  = x + x0
    yLong = y + y0
    return yLong,xLat

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
        if obj['coordinates']:
            long = obj['coordinates']['coordinates'][0]
            lat = obj['coordinates']['coordinates'][1]
        else:
            long,lat = generateRandomCoordinates()

        hashtags = []
        for hashtag in obj['entities']['hashtags']:
            hashtags.append(hashtag['text'])
        if len(hashtags) == 0:
            hashtags = ['instagood','fashion']          # Some Default Hashtags
        return [id,hashtags,long,lat]
    except:
        return ['','',0,0]


if __name__ == '__main__':
    #The folder structure for data has total 60 json files for each day
# =============================================================================
#     day = '09'
#     for i in range(0,59):
#         if i < 10:
#             filename = 'raw/'+day+'/0'+ str(i) +'.json'
#         else:
#             filename = 'raw/'+day+'/'+ str(i) +'.json'
#         content = loadFile(filename)
#         data = readFile(content)
# =============================================================================

# =============================================================================
# # =============================================================================
     filename = 'raw/tweet15.txt'#17/09.json'
     content = loadFile(filename)
     data = readFile(content)
# =============================================================================
