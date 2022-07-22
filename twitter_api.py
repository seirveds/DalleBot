from dotenv import load_dotenv
import tweepy
import os


class TwitterAPI:

    def __init__(self):
        self.api = self.auth()

    def auth(self):
        """ Loads tokens from env variables and authenticates. """
        load_dotenv()

        auth_token = tweepy.OAuth1UserHandler(
            os.environ["APIKEY"], os.environ["APISECRET"],
            os.environ["ACCESTOKEN"], os.environ["ACCESTOKENSECRET"]
        )
        return tweepy.API(auth_token)

    def post_tweet(self, status, filename):
        self.api.update_status_with_media(status=status, filename=filename)

if __name__ == "__main__":
    api = TwitterAPI()
