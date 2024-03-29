#!/usr/bin/python3
"""Script to take in an URL , send request and decode. """


import urllib.request
import urllib.error
import sys


def send_request(url):
    """
    Sends a request to the specified URL and handles HTTP errors.

    Parameters:
    - url (str): The URL to send the request to.

    Returns:
    - str: The body of the response (decoded in utf-8) if successful,
           otherwise an error message with the HTTP status code.
    """
    try:
        with urllib.request.urlopen(url) as response:
            status_code = response.getcode()
            body = response.read().decode('utf-8')
            return f"Request successful with status code {status_code}\n{body}"
    except urllib.error.HTTPError as e:
        return f"Error code: {e.code}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = send_request(url)
    print(response)
