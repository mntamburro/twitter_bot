import tweepy
import keys
from time import sleep
import datetime


def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)


def retweet(tweepy_api: tweepy.API, hashtag: str, delay=60):
    print(f"*** \n{datetime.datetime.now()}\n***")

    for tweet in tweepy.Cursor(tweepy_api.search_tweets, q=hashtag).items(10):
        try:
            # print(tweet) # prints all the metadata that the tweet has
            tweet_id = dict(tweet._json)["id"]
            tweet_text = dict(tweet._json)["text"]

            print("id: " + str(tweet_id))
            print("text: " + str(tweet_text)[0:70] + "...")

            # Retweets the tweet
            api.retweet(tweet_id)

            # Adds the tweet as a favourite
            api.create_favorite(tweet_id)

        except tweepy.TweepyException as error:
            print(error)
            sleep(.5)

    print("")
    sleep(delay)


if __name__ == '__main__':
    api = api()

    while True:
        retweet(api, '#pythonize', 10)
