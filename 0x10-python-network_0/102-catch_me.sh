#!/bin/bash
# Script to make a request to 0.0.0.0:5000/catch_me and get the server response with "You got me!"
curl -s -X POST -H "Origin: HolbertonSchool" -d "user_id=98" http://0.0.0.0:5000/catch_me
