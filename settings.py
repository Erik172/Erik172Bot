from dotenv import load_dotenv
import tweepy
import os

load_dotenv()

# Authenticacion
auth = tweepy.OAuthHandler(os.getenv('API_KEY_TWITTER'), os.getenv('API_KEY_SECRET_TWITTER'))
auth.set_access_token(os.getenv('ACCES_TOKEN_TWITTER'), os.getenv('ACCES_TOKEN_SECRET_TWITTER'))

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)