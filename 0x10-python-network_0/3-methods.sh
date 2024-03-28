#!/bin/bash
# Script to display all HTTP methods accepted by the server
curl -s -X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-
