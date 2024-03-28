#!/bin/bash
#Script takes in a URL, sends a request to that URL and dispalays the size of the body of the response.

# Check if a URL argument is provided
if [ -z "$1" ]; then
    echo "Error: Please provide a URL as an argument."
    exit 1
fi

url="$1"

# If Content-Length header is not present, calculate the size by fetching the content
size=$(curl -s "$url" | wc -c)

# Display the size of the response body in bytes
echo "$size"
