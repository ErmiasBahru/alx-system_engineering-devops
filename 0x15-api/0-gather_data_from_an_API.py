#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""
import requests as r
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    resp_user = r.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    resp_todos = r.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id))

    try:
        users = resp_user.json()
        user_todos = resp_todos.json()

        completed_task = list(
            filter(lambda x: x.get("completed") is True, user_todos))

        print("Employee {} is done with tasks({}/{}):".format(users.get('name'),
              len(completed_task), len(user_todos)))

        for todo in completed_task:
            print("\t {}".format(todo.get('title')))

    except Exception as e:
        print(e)
