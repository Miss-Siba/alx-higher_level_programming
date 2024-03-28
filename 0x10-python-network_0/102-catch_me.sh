#!/bin/bash
# Script to make a request to 0.0.0.0:5000/catch_me and get the server response with "You got me!"
curl -s -X POST -H "X-HolbertonSchool-User-Id: 98" http://0.0.0.0:5000/catch_me --data "user_id=98"
