# import json
from datetime import datetime

def parse(data):
    """
    Parse the data coming from fetch.py
    """
    postNumber = data["data"]["children"]
    for post in postNumber:
        postDate = datetime.utcfromtimestamp(post["data"]["created"])
        print(f"{post['data']['title']} \n")
        print(f"Link: {post['data']['url']}\n")
        print(
            f"Posted on {post['data']['subreddit_name_prefixed']} by u/{post['data']['author']} on {postDate} ")
        print("---------------------")

    print(f"{len(postNumber)} posts shown.")
