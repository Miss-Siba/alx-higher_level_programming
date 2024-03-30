#!/usr/bin/python3

"""
Script to send a request to a URL and display the value of the X-Request-Id header.
"""

import requests
import sys

def get_x_request_id(url):
    """
    Sends a GET request to the specified URL and retrieves the value of the X-Request-Id header.

    Parameters:
    - url (str): The URL to send the GET request to.

    Returns:
    - str: The value of the X-Request-Id header if present, otherwise an error message.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            return x_request_id
        else:
            return "X-Request-Id header not found in the response."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    url = 'http://0.0.0.0:5050'

    x_request_id = get_x_request_id(url)
    print("X-Request-Id:", x_request_id)
