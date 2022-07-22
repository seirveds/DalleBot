from dotenv import load_dotenv
import tweepy
import os


class DalleBot:

    def __init__(self):
        self.api = self.auth()

    def auth(self):
        load_dotenv()
        auth_token = tweepy.OAuth1UserHandler(
            os.environ["APIKEY"], os.environ["APISECRET"],
            os.environ["ACCESTOKEN"], os.environ["ACCESTOKENSECRET"]
        )
        return tweepy.API(auth_token)

    def post_tweet(self, body):
        self.api.update_status(status=body)

if __name__ == "__main__":
    bot = DalleBot()
