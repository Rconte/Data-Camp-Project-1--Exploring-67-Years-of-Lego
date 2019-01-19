#Streaming tweets
#Now that you have set up your authentication credentials, 
#it is time to stream some tweets! We have already defined the tweet stream listener class, MyStreamListener, 
#just as Hugo did in the introductory video. You can find the code for the tweet stream listener class here.

#Your task is to create the Streamobject and to filter tweets according to particular keywords.

#Class has been copy-pasted from Hugo's Github @ https://gist.github.com/hugobowne/18f1c0c0709ed1a52dc5bcd462ac69f4

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)


# Initialize Stream listener
l = MyStreamListener()

# Create your Stream object with authentication
stream = tweepy.Stream(auth, l)


# Filter Twitter Streams to capture data by the keywords:
stream.filter(track = ['clinton','trump','sanders','cruz'])

