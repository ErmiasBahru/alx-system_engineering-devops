#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests as r


if __name__ == "__main__":
    resp_user = r.get('https://jsonplaceholder.typicode.com/users')
    resp_todos = r.get('https://jsonplaceholder.typicode.com/todos')

    try:
        users = resp_user.json()
        user_todos = resp_todos.json()

        data = {}

        for user in users:
            user_id = user.get('id')

            usr_todos = list(filter(lambda todo: (
                todo.get('userId') == user_id), user_todos))
            tasks = list(map(lambda todo: {
                "title": todo.get('title'),
                "completed": todo.get('completed'),
                "username": user.get('username')
            }, usr_todos))

            data[user_id] = tasks

            json_name = 'todo_all_employees.json'

            with open(json_name, mode='w', encoding='utf-8') as jsons:
                json.dump(data, jsons)

    except Exception as e:
        print(e)
