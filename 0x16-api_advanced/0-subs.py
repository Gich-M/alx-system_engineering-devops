#!/usr/bin/python3
"""Queries the `Reddit API` and returns the number of
    subscribers (not active users, total subscribers)
    for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """
        subreddit - the subreddit to query
        Return: 0, If the subreddit is invalid
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/G_zillah)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0

    results = response.json().get("data")
    return results.get("subscribers")
