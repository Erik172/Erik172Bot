from config import api
import logging
import tweepy
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class LikeAndRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        logger.info(f"Precesando tweet con id: {tweet.id} y usuario: {tweet.user.name}")
        if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # This tweet is a reply or I'm its author so, ignore it
            return
        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
            except Exception as e:
                logger.error("Error en like", exc_info=True)
        if not tweet.retweeted:
            # Retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
            except Exception as e:
                logger.error("Error en Retweet", exc_info=True)

    def on_error(self, status):
        logger.error(status)

def main(keywords):
    tweets_listener = LikeAndRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=['es'])

if __name__ == "__main__":
    logger.info('Iniciando Bot de Like and Retweet')
    main(['platzi', 'python', 'hacktzi'])