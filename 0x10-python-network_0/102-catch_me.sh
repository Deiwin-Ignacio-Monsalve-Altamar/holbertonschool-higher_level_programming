#!/bin/bash
#that causes the server to respond with a message containing
curl -sLX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
