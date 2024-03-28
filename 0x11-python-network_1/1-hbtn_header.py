#!/usr/bin/python3
import urllib.request
import sys

# Get the URL from command-line argument
url = sys.argv[1]

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    request_id = response.headers.get('X-Request-Id')
    print(request_id)
