#!/bin/bash
# A bash script that sends a request to url and displays you got me!
curl -o /dev/null -s -w "You got me!"  0.0.0.0:5000/catch_me
