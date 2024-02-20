#!/usr/bin/python3
""" Use REST-API to gather data from an APi """

import requests
import sys

if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/todos/"
    users_url = f"https://jsonplaceholder.typicode.com/users"
    no_done_task = 0
    total_tasks = 0
    done_tasks = []

    users = requests.get(users_url).json()
    name = users[int(sys.argv[1]) - 1]["name"]
    request = requests.get(url)
    data = request.json()

    for todo in data:
        if todo["userId"] == int(sys.argv[1]):
            total_tasks += 1
            if todo["completed"]:
                no_done_task += 1
                done_tasks.append(todo["title"])
    print(f"Employee {name} is done with tasks({no_done_task}/{total_tasks}):")
    for title in done_tasks:
        print(f"\t{title}")
