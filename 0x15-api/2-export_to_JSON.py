#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import requests as r
import json
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

        tasks = list(map(lambda todo: {
            "title": todo.get('title'),
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
