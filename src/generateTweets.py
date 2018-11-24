#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "263851696-GbtvKb3DLU7Gud06qjNy1rub6FKnGGMd0DILmBjW"
access_token_secret = "jSFT3jttoroCEdAKXEDM5vYxMxsmSosjsTh3eRP4iortP"
consumer_key = "joViRtVRFDnQVEyGaOWFcdXOm"
consumer_secret = "iMSHHuVj1ODKw0e1Iiec547g9mcB2uNUIy3JEVaB7Jj4BhcXxH"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    GEOBOX_WORLD = [-180, -90, 180, 90]
    GEOBOX_USA = [-179.1506, 18.9117, -66.9406, 71.4410]
    GEOBOX_GERMANY = [5.0770049095, 47.2982950435, 15.0403900146, 54.9039819757]
    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(locations=GEOBOX_WORLD)
