#!/usr/bin/python3
"""
Script to fetch status from a specified URL using the requests module.
"""

import requests


def fetch_status(url):
    """
    Fetches the status from the specified URL using requests.

    Parameters:
    - url (str): The URL to fetch the status from.

    Returns:
    - str: The status text if the request is successful, otherwise
    an error message.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        formatted_output = f"Body response:\n" \
                           f"    - type: {type(response.text)}\n" \
                           f"    - content: {response.text}\n"
        return formatted_output
    except requests.exceptions.HTTPError as he:
        return f"HTTP error: {he}"
    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"


if __name__ == "__main__":
    url1 = 'https://alx-intranet.hbtn.io/status'
    url2 = 'http://0.0.0.0:5050/status'

    print("Fetching status from", url1)
    print(fetch_status(url1))

    print("\nFetching status from", url2)
    print(fetch_status(url2))
