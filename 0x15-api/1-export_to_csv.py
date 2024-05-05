#!/usr/bin/python3
"""Exports to-do list information for a given employee ID  to USER_ID.csv."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "http://jsonplaceholder.typicode.com/"
    user = requests.get(url + "user/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTEALL)

    [writer.writerow(
        [user_id, username, t.get("completed"), t.get("title")]
    ) for t in todos]
