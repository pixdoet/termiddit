#!/usr/bin/env python3

import sys, getopt  # stuff for arguments

from parse import Parse
from fetch import Fetch, Construct

f = Fetch()
p = Parse()
c = Construct()


def main(argv):
    if len(argv) == 0:
        # fetch from subreddits.json
        FETCHED_DATA = f.fetch(None)
        FETCHED_POSTS_NO = c.postListName()
        p.parse(FETCHED_DATA, FETCHED_POSTS_NO)
    else:
        try:
            opts, args = getopt.getopt(argv, "hs:", ["subreddit="])
            for opt, arg in opts:
                if opt == "-s":
                    data = f.fetch(arg)
                    p.parse(data, "custom feed")
                elif opt == "-h":
                    print(
                        """Usage: main.py [-s <subreddit(s)>] [-h]
                    -s: Request with subreddits. Create a multireddit by adding the plus symbol (+) between different subreddits. E.g.: python+php+java. This option overrides the subreddits.json file.
                    -h: Print this help message.
                    """
                    )
        except getopt.GetoptError as ge:
            print(ge)
        # start forming the requeSt url


if __name__ == "__main__":
    main(sys.argv[1:])
