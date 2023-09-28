#!/bin/bash
# A bash script that takes in a URL,send a get request
curl  -sI $1 | grep Allow | cut -d " " -f2-
