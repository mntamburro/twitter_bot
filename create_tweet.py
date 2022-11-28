import tweepy
import keys
import json
from json import JSONEncoder
from urllib.request import urlopen

url= "http://official-joke-api.appspot.com/random_joke"
data = urlopen(url)
#print(r.getcode())
jsonData = json.loads(data.read())

#print(jsonData['setup'])
#print(jsonData['punchline'])

setup = jsonData['setup']
punchline = jsonData['punchline']

def Joke():
    return setup, punchline


def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)


def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print('Tweeted successfully!')

fulljoke = Joke()

if __name__ == '__main__':
    api = api()
    tweet(api, fulljoke, 'cat.png')
