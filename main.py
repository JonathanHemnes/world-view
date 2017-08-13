import imageio
import tweepy
from urllib.request import urlopen
from constants import Constants 
import os

auth = tweepy.OAuthHandler(Constants.consumer_key, Constants.consumer_secret)
auth.set_access_token(Constants.access_token, Constants.access_token_secret)
api = tweepy.API(auth)

source = 'dscovr_epic'

tweets = api.user_timeline(screen_name = source, count = 24)
tweets.sort(key=lambda t: t.created_at)

images = []

for tweet in tweets:
    media_items = tweet.entities.get('media')[0]
    if media_items:
        image_url = media_items.get('media_url')
        data = urlopen(image_url).read()
        im = imageio.imread(data, 'jpg')
        images.append(im)
        print('appended image')

print('writing gif')
cwd = os.getcwd()
imageio.mimsave(cwd + '/world.gif', images)
print('done')