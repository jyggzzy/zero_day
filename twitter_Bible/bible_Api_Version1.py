import tweepy
import time
import requests
from bs4 import BeautifulSoup

# Twitter API credentials
consumer_key = 'vXTiiZg9HTFiuXMC4qV2bp5D2'
consumer_secret = 'eZJCE7uIOJ4kzblyQEaKUEbK6hOMgvs9ZBpUPgxr10TiLuKlXk'
access_token = '181908096-84qjgPv8FxK9yItSUmMAQAmvbZfpQ3mIFIgcSLNt'  # unsure
access_token_secret = 'JpDZLJyYB3LdXaAW2i5iDV72xORpfqHDOvGF8d7D25vat'  # unsure

# Authenticate the API credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create the Tweepy API object
api = tweepy.API(auth)

# Retrieve a random Bible verse from BibleGateway.com using web scraping
url = "https://www.biblegateway.com/usage/votd/rss/votd.rdf"
verse = ""
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    verse = soup.findAll("description")[1].text.replace('\n', '')

# Tweet the Bible verse once every hour
while True:
    try:
        api.update_status(verse)
        print("Tweeted: " + verse)
    except tweepy.errors.TweepyException as error:
        print(error.reason)
    time.sleep(3600)  # Wait 1 hour before tweeting again