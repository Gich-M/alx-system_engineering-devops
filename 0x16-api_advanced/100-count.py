#!/usr/bin/python3
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """
        Parses the title of all hot articles, and
            prints a sorted count of given keywords
            (case-insensitive, delimited by spaces).
        Args:
            subreddit (str): The subreddit to parse.
            word_list (list): A list of keywords to count.
            instances (dict): A dictionary (key/value pairs) of keyword counts.
            after (str): The ID of the last article parsed.
            count (int): The number of articles to parse.
    """
    url = f"https://www.reddit.com/r/{subreddit}.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/G_zillah)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for child in results.get("children"):
        title = child.get("data").get("title")
        for word in word_list:
            if word.lower() in title.lower():
                insts = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = insts
                else:
                    instances[word] += insts
    if after is None:
        if len(instances) == 0:
            print("")
            return

        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        for k, v in instances:
            print("{}: {}".format(k, v))
    else:
        count_words(subreddit, word_list, instances, after, count)
