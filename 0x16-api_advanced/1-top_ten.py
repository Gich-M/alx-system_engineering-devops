#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """Prints the titles of the 10 hottest posts for a given subreddit."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/G_zillah)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    for post in results.get("children"):
        print(post.get("data").get("title"))
