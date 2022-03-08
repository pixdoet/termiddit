#!/usr/bin/env python3

import sys

from parse import Parse
from fetch import Fetch


f = Fetch()
p = Parse()

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
    p.parse(FETCHED_DATA)


if __name__ == "__main__":
    main(sys.argv[1:])
