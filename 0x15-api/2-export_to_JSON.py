#!/usr/bin/python3
""" Export data in json format """

import json
import requests
import sys

url = f"https://jsonplaceholder.typicode.com/todos/"
users_url = f"https://jsonplaceholder.typicode.com/users"

tasks = requests.get(url).json()
users = requests.get(users_url).json()
uname = users[int(sys.argv[1]) - 1]["username"]

objs = {}
task_list = []
for task in tasks:
    if task["userId"] == int(sys.argv[1]):
        todo = {"task": task["title"], "completed": task["completed"],
                "username": uname}
        task_list.append(todo)
objs[sys.argv[1]] = task_list

with open(f"{sys.argv[1]}.json", mode="w") as f:
    json.dump(objs, f)
