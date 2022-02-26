#!/usr/bin/env python3

import parse
import fetch

FETCHED_DATA = fetch.fetch()


def main():
    parse.parse(FETCHED_DATA)


if __name__ == "__main__":
    main()
