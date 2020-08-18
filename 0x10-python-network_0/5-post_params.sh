#!/bin/bash
#script that takes in a URL, sends a POST
curl -s -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
