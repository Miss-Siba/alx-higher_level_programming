#!/usr/bin/python3
"""
Script to send a POST request with an email parameter to a specified URL.
"""
import urllib.parse
import urllib.request
import sys


def send_post_request(url, email):
    """
    Sends a POST request with the specified email parameter to the given URL.

    Parameters:
    - url (str): The URL to send the POST request to.
    - email (str): The email parameter to include in the request.

    Returns:
    - str: The body of the response (decoded in utf-8).
    """

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        return content


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script_name.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response_body = send_post_request(url, email)
    print(response_body)
