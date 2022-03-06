"""
    Constructs a URL for fetching the data based on subreddits.json
"""

import json

FEED_URL = "https://reddit.com/r/"

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