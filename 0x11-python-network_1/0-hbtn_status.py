#!/usr/bin/python3
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    content_bytes = response.read()
    content_str = content_bytes.decode('utf-8')

print("Body response:")
print("\t- type:", type(content_bytes))
print("\t- content:", content_bytes)
print("\t- utf8 content:", content_str)
