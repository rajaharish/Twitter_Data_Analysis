
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "199360570-yFGLbq8f51Fg9dUrq7S9vG8tfAYGS632DTl33NMJ"
access_token_secret = "rU1RZ0baNJ0S5j9Q5EUFuYcjNwOS5BWPSqRkPDsqQsMft"
consumer_key = "8GIn28ONAvpbmF5Y27ogmom7T"
consumer_secret = "MXdAlt5XBE6WaujmI2SF1Kzex7RSXJmaI5W1yOe8ucnfbbO7HR"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    try:
        #This handles Twitter authetification and the connection to Twitter Streaming API
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)

        #london=[-0.1257, 51.5085, 0.10, 52.50]
        
        seattle=[-122.3320,47.6062,-121.3320,48.6062]
        oklahoma=[-97.5164,35.4675,-96.5164,36.4675]
        
        seattle_oklahoma=[-122.3320,47.6062,-121.3320,48.6062,-97.5164,35.4675,-96.5164,36.4675]
        #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'""
        stream.filter(track=['seahawks','cowboys','national football league','nfl'],locations=seattle_oklahoma,languages = ["en"])
    except:
        print "waiting...   "