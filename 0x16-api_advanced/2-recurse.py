#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
        subreddit: The name of the subreddit to search.
        hot_list: A list to store the titles of hot articles.
        after: The ID of the last article retrieved.
        count: The total number of articles retrieved.
        Return: A list containing the titles of all hot articles
            for the given subreddit or None if no results found.
    """
    url = "https://www.reddit.com/r/{}".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1..0.0 (by /u/G_zillah)"
    }
    params = {
        "after": after,
        "limit": 100,
        "count": count
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
