"""
    Fetch the data with the constructed URL
"""

import requests
import json


FEED_URL = "https://reddit.com/r/"


class Construct:
    def __init__(self):
        pass

    def constructUrl(override):
        if override is None:
            with open("subreddits.json", 'r') as f:
                data = json.load(f)

            url = FEED_URL

            for subreddit in data["subreddits"]:
                url = f"{url}+{subreddit}"

            return f"{url}.json"
        else:
            # custom subreddit feed
            url = f"{FEED_URL}{override}.json"
            return url


construct = Construct()

class Fetch:
    def __init__(self):
        pass

    def fetch(override):

        if override is None:
            CONSTRUCTED_URL = construct.constructUrl(None)
        else:
            CONSTRUCTED_URL = construct.constructUrl(override)

        r = requests.get(
            CONSTRUCTED_URL,
            headers={
                "Accept": "application/json",
                # usefirefox
                "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:100.0) Gecko/20100101 Firefox/100.0"
            }
        )
        return r.json()
