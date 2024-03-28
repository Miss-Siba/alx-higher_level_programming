#!/bin/bash
#Script takes in a URL, sends a request to that URL and dispalays the size of the body of the response.
curl -sI "$1" | grep "Content-Length" | wc -c
