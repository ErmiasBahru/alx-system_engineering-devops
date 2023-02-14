#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""

import requests as r
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    url_user = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    url_todos = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    resp_user = r.get(url_user)
    resp_todos = r.get(url_todos)

    try:
        users = resp_user.json()
        user_todos = resp_todos.json()

        completed_task = list(
            filter(lambda x: x.get("completed") is True,
                   user_todos))

        print(
            f"Employee {users.get('name')} is done with tasks({len(completed_task)}/{len(user_todos)}):"
        )

        for todo in completed_task:
            print(f"\t {todo.get('title')}")

    except Exception as e:
        print(e)
