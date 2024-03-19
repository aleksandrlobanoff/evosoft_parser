import requests
from bs4 import BeautifulSoup


def get_last_10_tweets():
    url = "https://twitter.com/elonmask"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    tweets = []

    tweet_elements = soup.find_all("span", {"class": "css-1qaijid r-bcqeeo r-qvutc0 r-poiln3"})
    for tweet in tweet_elements[:10]:
        tweet_text = tweet.get_text(strip=True)
        tweets.append(tweet_text)

    return tweets


tweets = get_last_10_tweets()
for tweet in tweets:
    print(tweet)
