# import json
from datetime import datetime

# colour palette for printing bri'ish text
class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    UNDERLINE = '\033[4m'
    STOP = '\033[0m'


def parse(data):
    """
    Parse the data coming from fetch.py
    """
    postNumber = data["data"]["children"]
    for post in postNumber:
        postDate = datetime.utcfromtimestamp(post["data"]["created"])
        print(f"{bcolors.YELLOW}{post['data']['title']}{bcolors.STOP} \n")
        print(f"Link: {bcolors.UNDERLINE}{post['data']['url']}{bcolors.STOP}\n")
        print(
            f"Posted on {bcolors.PURPLE}{post['data']['subreddit_name_prefixed']}{bcolors.STOP} by {bcolors.BLUE}u/{post['data']['author']}{bcolors.STOP} on {postDate}")
        print("---------------------")

    print(f"{len(postNumber)} posts shown.")


