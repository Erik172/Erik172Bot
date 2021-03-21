from config import api
import logging
import tweepy
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def follow_followers():
    logger.info("Seguir a Seguidores")
    # Buscar Seguidores
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f"Siguiendo a {follower.name}")
            follower.follow()

def main():
    while True:
        follow_followers()
        logger.info("Espere un momento...")
        time.sleep(60)

if __name__ == "__main__":
    main()