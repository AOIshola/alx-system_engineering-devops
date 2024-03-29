#!/usr/bin/python3
""" Export data to csv """

import csv
import requests
import sys

if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/todos/"
    users_url = f"https://jsonplaceholder.typicode.com/users"

    tasks = requests.get(url).json()
    users = requests.get(users_url).json()
    uname = users[int(sys.argv[1]) - 1]['username']
    id = sys.argv[1]

    with open(f"{sys.argv[1]}.csv", mode="w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks:
            if task["userId"] == int(sys.argv[1]):
                writer.writerow(
                        [id,
                            uname,
                            task['completed'],
                            task['title']])
