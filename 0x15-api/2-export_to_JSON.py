#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests as r
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_id)
    url_todos = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        employee_id)

    resp_user = r.get(url_user)
    resp_todos = r.get(url_todos)

    try:
        users = resp_user.json()
        user_todos = resp_todos.json()

        tasks = list(map(lambda todo: {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": users.get('username')
        }, user_todos))

        json_data = {
            users.get('id'): tasks
        }
        json_file = "{}.json".format(users.get('id'))

        with open(json_file, mode='w', encoding='utf-8') as jsons:
            json.dump(json_data, jsons)

    except Exception as e:
        print(e)
