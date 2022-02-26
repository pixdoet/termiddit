import requests
import construct
import json

CONSTRUCTED_URL = construct.constructUrl()


def fetch():
    """
    Fetch the data with the constructed URL
    """
    r = requests.get(
        CONSTRUCTED_URL,
        headers={
            #usefirefox
            "Accept": "application/json",
            "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:100.0) Gecko/20100101 Firefox/100.0"
        }
    )
    return r.json()

