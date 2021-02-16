from cairo import falafel
import speedtest
import requests
from requests_oauthlib import OAuth1

PROMISED_DOWN = 150
PROMISED_UP = 50
DRV_PATH = "/Users/svetulka/PycharmProjects/chromedriver"
URL = "https://api.twitter.com/1.1/statuses/update.json"
USER_AUTH = OAuth1(
    falafel["CONSUMER_KEY"],
    falafel["CONSUMER_SECRET"],
    falafel["ACCESS_KEY"],
    falafel["ACCESS_SECRET"]
)


class InternetSpeedBot:
    def __init__(self):
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN
        self.st = speedtest.Speedtest()
        self.url = URL

    def get_speed(self):
        print("Fetching speeds...")
        upld = round(self.st.upload() / 1000000, 2)
        dwnld = round(self.st.download() / 1000000, 2)
        print("Speed fetched")
        return [upld, dwnld]

    def create_tweet(self, tweet):
        print("Starting Twitter...")
        msg = {"status": tweet}
        response = requests.post(url=self.url, auth=USER_AUTH, params=msg)
        response.raise_for_status()
        print(f"Posted {tweet}.")
