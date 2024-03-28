#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the X-Request-Id"""
import urllib.request
import sys


url = sys.argv[1]

req = urllib.request.Request(url)
try:
    with urllib.request.urlopen(req) as response:
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            print(request_id)
        else:
            print("X-Request-Id header not found in the response.")
except urllib.error.HTTPError as e:
    print(f"HTTPError: {e.code} - {e.reason}")
except urllib.error.URLError as e:
    print(f"URLError: {e.reason}")
except Exception as e:
    print(f"An error occurred: {e}")
