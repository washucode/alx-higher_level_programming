#!/bin/bash
# A bash script that takes in a URL,send a delete request
curl -sX DELETE $1 -L
