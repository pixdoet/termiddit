#!/usr/bin/env python3.10


import sys, getopt  # stuff for arguments

from parseJson import Parse
from fetchUrl import Fetch, Construct

f = Fetch()
p = Parse()
c = Construct()

class PrintColours:
    PURPLE = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    FAIL = "\033[91m"
    UNDERLINE = "\033[4m"
    STOP = "\033[0m"

cl = PrintColours()

def main(argv):
    print(f"{cl.FAIL}Save 3rd party apps!{cl.STOP}")
    if len(argv) == 0:
        # fetch from subreddits.json
        FETCHED_DATA = f.fetch(None, None)
        FETCHED_POSTS_NO = c.postListName()
        p.parse(FETCHED_DATA, FETCHED_POSTS_NO)

    else:
        # WHAT IN JESUS"S WORLD ARE WE FUCKING DOING WITHT HIS ONE FILE OH MY FUCKING GOD LMAOOOOOOOO HOW ABOUT WE JUST WRITE main2.py AND CALL IT A DAY INSTEAD

        try:
            opts, args = getopt.getopt(argv, "hsu:", ["subreddit="])
            for opt, arg in opts:
                if opt == "-s":
                    data = f.fetch(arg, None)
                    p.parse(data, "custom feed")
                elif opt == "-u":
                    data = f.fetch(None, arg)
                    p.parse(data, )

                elif opt == "-h":
                    print(
                        """Usage: main.py [-s <subreddit(s)>] [-u <json file>] [-h]
                    -s: Request with subreddits. Create a multireddit by adding the plus symbol (+) between different subreddits. E.g.: python+php+java. This option overrides the subreddits.json file.
                    -u: Request with a custom JSON feed. This should take only one argument, the path of the JSON feed file.
                    -h: Print this help message.
                    """
                    )
        except getopt.GetoptError as ge:
            print(ge)


if __name__ == "__main__":
    main(sys.argv[1:])
