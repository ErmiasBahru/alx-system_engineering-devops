#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests as r


if __name__ == "__main__":
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    resp_user = r.get(url_user)
    resp_todos = r.get(url_todos)

    try:
        users = resp_user.json()
        user_todos = resp_todos.json()

        data = {}

        for user in users:
            user_id = user.get('id')

            usr_todos = list(filter(lambda todo: (
                todo.get('userId') == user_id), user_todos))
            tasks = list(map(lambda todo: {
                "username": user.get('username'),
                "task": todo.get('title'),
                "completed": todo.get('completed')
            }, usr_todos))

            data[user_id] = tasks

            json_name = 'todo_all_employees.json'

            with open(json_name, mode='w', encoding='utf-8') as jsons:
                json.dump(data, jsons)

    except Exception as e:
        print(e)
