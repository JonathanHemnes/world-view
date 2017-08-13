import imageio
import tweepy
from constants import Constants 

auth = tweepy.OAuthHandler(Constants.consumer_key, Constants.consumer_secret)
auth.set_access_token(Constants.access_token, Constants.access_token_secret)
api = tweepy.API(auth)

source = 'dscovr_epic'

tweets = api.user_timeline(screen_name = source)

for tweet in tweets:
    media_items = tweet.entities.get('media')[0]
    if media_items:
        print(media_items.get('expanded_url'))
    

print('hello')