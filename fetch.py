"""
    Fetch the data with the constructed URL
"""

import requests
import construct

def fetch(override):
    
    if override is None:
        CONSTRUCTED_URL = construct.constructUrl(None)
    else:
        CONSTRUCTED_URL = construct.constructUrl(override)

    r = requests.get(
        CONSTRUCTED_URL,
        headers={
            #usefirefox
            "Accept": "application/json",
            "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:100.0) Gecko/20100101 Firefox/100.0"
        }
    )
    return r.json()

