# import json
from datetime import datetime

# colour palette for printing bri'ish text


class PrintColours:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    UNDERLINE = '\033[4m'
    STOP = '\033[0m'

colours = PrintColours()

class Parse:
    def __init__(self):
        pass

    def parse(self, data, listName):
        """
        Parse the data coming from fetch.py
        """
        postNumber = data["data"]["children"]
        for post in postNumber:
            postDate = datetime.utcfromtimestamp(post["data"]["created"])
            print(f"{colours.YELLOW}{post['data']['title']}{colours.STOP} \n")
            print(
                f"Link: {colours.UNDERLINE}{post['data']['url']}{colours.STOP}\n")
            print(
                f"Posted on {colours.PURPLE}{post['data']['subreddit_name_prefixed']}{colours.STOP} by {colours.BLUE}u/{post['data']['author']}{colours.STOP} on {postDate}")
            print("---------------------")

        print(f"Fetch {len(postNumber)} posts from list \"{listName}\".")
