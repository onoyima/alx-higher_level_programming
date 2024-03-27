#!/bin/bash

# Make a PUT request with curl to the specified endpoint
curl -sX PUT 0.0.0.0:5000/catch_me --output /dev/null --header "Origin: HolbertonSchool"

