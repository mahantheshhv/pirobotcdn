import tweepy

CONSUMER_KEY ="wMVDcLXR4kTXGUqJX0e0sUuMv"
CONSUMER_SECRET = "tYGWxxmO8LjiwdrlqamB8N1Ia53mLQbUioQbrPgjqVas8TDNUu"   
ACCESS_KEY = "4384993475-4nl6kNzqeM1KzbrpWUW0sENOEH1l8AJgaj8Knia"    
ACCESS_SECRET = "E9AgwH7WE1qq26VoFtrUrLi7BLCpVNHRRZZOYCIjxfXRe"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
api.update_status('from pi robote!')
