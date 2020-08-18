#!/bin/bash
#script that sends a JSON POST request to a URL passed as the
curl -s "$1" -X POST -d @"$2" -H "Content-Type: application/json"
