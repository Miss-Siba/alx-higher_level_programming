#!/bin/bash
# Script to send a request to a URL and display only the status code of the response
curl -s -w "%{http_code}" -o /dev/null "$1"
