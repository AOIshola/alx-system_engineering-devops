#!/usr/bin/python3
""" Export data in json format """

import json
import requests
import sys

if __name__ == "__main__":
    url = f"https://jsonplaceholder.typicode.com/todos/"
    users_url = f"https://jsonplaceholder.typicode.com/users"

    tasks = requests.get(url).json()
    users = requests.get(users_url).json()

    objs = {}
    for user in users:
        task_list = []
        for task in tasks:
            if task["userId"] == user["id"]:
                todos = {
                        "username": user["username"],
                        "task": task["title"], "completed": task["completed"]
                        }
                task_list.append(todos)
        objs[user["id"]] = task_list

    with open("todo_all_employees.json", mode="w") as f:
        json.dump(objs, f)
