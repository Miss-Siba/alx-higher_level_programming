#!/bin/bash
# Script to display all HTTP methods accepted by the server
curl -s -i -X OPTIONS "$1" | awk '/Allow/{print $2}'
