import json
import codecs

def loadFile(filename):
     with open('dump.txt') as file:
         content = file.read()
     return content

def parseFile(content):
    tweets = content.split('\n')
    fout = codecs.open('hash.csv', 'w', 'utf-8')
    print(len(tweets))
    data = []
    read=True
    for tweet in tweets:
        if 'EOF' in tweet:
            print('End of all')
            read=False
            exit(0) 
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
            
            
def parseTweets(content):
    obj = json.loads(content)
        
    lat = False
    long = False
    if obj['lang'] != 'en':
     	return ['','',0,0]
    id = obj['id']
    if obj['coordinates']:
        long = obj['coordinates']['coordinates'][0]
        lat = obj['coordinates']['coordinates'][1]
    hashtags = []    
    for hashtag in obj['entities']['hashtags']:
         hashtags.append(hashtag['text'])   
    return [id,hashtags,long,lat]    
    
    
if __name__ == '__main__':
    content = loadFile('dump.txt')
    data = parseFile(content)
 