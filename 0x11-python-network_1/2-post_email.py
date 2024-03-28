#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

# Get the URL and email from command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Encode the email parameter
data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')

req = urllib.request.Request(url, data=data, method='POST')
with urllib.request.urlopen(req) as response:
    content = response.read().decode('utf-8')

print(content)
