#!/bin/bash
# A bash script that takes in a URL,send a post request
curl -sX POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD" -L
