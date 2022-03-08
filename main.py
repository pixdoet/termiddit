#!/usr/bin/env python3

import sys


from parse import Parse
from fetch import Fetch, Construct


f = Fetch()
p = Parse()
c = Construct()

def main(argv):
    # argument handling for single subreddit
    """try:
        opts, args = getopt.getopt(argv, "r", ["subreddit="])
    except getopt.GetoptError:
        FETCHED_DATA = fetch.fetch(None)
        parse.parse(FETCHED_DATA)

    for opt, arg in opts:
        if opt == "-r":
            FETCHED_DATA = fetch.fetch(arg)"""

    FETCHED_DATA = f.fetch(None)
    FETCHED_POSTS_NO = c.postListName()
    p.parse(FETCHED_DATA, FETCHED_POSTS_NO)


if __name__ == "__main__":
    main(sys.argv[1:])
