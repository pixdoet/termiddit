"""
    Fetch the data with the constructed URL

    @author Ian Hiew(pixdo.et@gmail.com)
"""

import requests
import json


FEED_URL = "https://old.reddit.com/r/"


class Construct:
    def __init__(self):
        pass

    def customConstruct(self, url):
        """
        not sure why this is here... not referenced anywhere in the code

        customConstruct - construct a custom feed url

        :param url: url to construct into feed
        """
        # for custom feeds
        try:
            f = open(url)
            data = json.load(f)

            url = FEED_URL

            for subreddit in data["subreddits"]:
                url = f"{url}+{subreddit}"

            return f"{url}.json"
        except IOError as ioe:
            print(ioe)

    def constructUrl(self, override, listName):
        """
        constructUrl - constructs the feed url
        :param override: override subreddits.json with a custom url string
        """
        # check for custom url override
        if override is None:
            # check if is using a custom feed
            if listName is None:
                with open("subreddits.json", "r") as f:
                    data = json.load(f)
            else:
                with open(listName, "r") as f:
                    data = json.load(f)
            url = FEED_URL

            for subreddit in data["subreddits"]:
                # append the subreddit into the constructed url
                url = f"{url}+{subreddit}"

            return f"{url}.json"
        else:
            # custom subreddit feed
            url = f"{FEED_URL}{override}.json"
            return url

    def postListName(self):
        with open("subreddits.json", "r") as f:
            data = json.load(f)

        return data["name"]


construct = Construct()


class Fetch:
    def __init__(self):
        pass

    def fetch(self, override, listOverride):
        """
        fetch - fetches the data from the constructed url

        :param override: the subreddit(s) to override the request on (subreddit1+subreddit2)
        """
        if override is None:
            CONSTRUCTED_URL = construct.constructUrl(None, None)
        else:
            if listOverride is not None:  # tf lmaoooooo
                CONSTRUCTED_URL = construct.constructUrl(override, listOverride)
            else:
                CONSTRUCTED_URL = construct.constructUrl(override, None)

        r = requests.get(
            CONSTRUCTED_URL,
            headers={
                "Accept": "application/json",
                # usefirefox
                "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:100.0) Gecko/20100101 Firefox/100.0",
            },
        )
        return r.json()
