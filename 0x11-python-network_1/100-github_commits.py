#!/usr/bin/python3
"""
    Takes two arguments and lists commits in github repository.
"""

import requests
import sys


def fetch_commits(url, owner, repo):
    """
        Takes two arguments and lists commits in github repository.

        Args:
            url : resource url
            owner : github username
            repo : github repository name
    """
    r = requests.get(url, params={'per_page': 10, 'page': 1})
    try:
        for commit in r.json():
            print("{}: {}".format(commit['sha'],
                                  commit['commit']['author']['name']))
    except Exception as e:
        print('None')


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
        .format(sys.argv[2], sys.argv[1])
    owner = sys.argv[2]
    repo = sys.argv[1]
    fetch_commits(url, owner, repo)
