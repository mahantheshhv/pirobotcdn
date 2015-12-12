import tweepy
from datetime import datetime
import sys

sys.path.append('/home/pi')

from keys import *


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
status = str(datetime.now())

api.update_status(status)
