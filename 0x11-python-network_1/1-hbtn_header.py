#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the X-Request-Id"""
import urllib.request
import sys


def get_x_request_id(url):
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        request_id = headers.get('X-Request-Id')
        return request_id if request_id else None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_request_id.py <URL>")
    else:
        url = sys.argv[1]
        x_request_id = get_x_request_id(url)
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
