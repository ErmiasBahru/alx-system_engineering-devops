#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""

from sys import argv
import csv
import requests as r

if __name__ == "__main__":
    employee_id = argv[1]
    url_user = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    url_todos = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    resp_user = r.get(url_user)
    resp_todos = r.get(url_todos)

    try:
        users = resp_user.json()
        user_todos = resp_todos.json()
        csv_name = f"{users.get('id')}.csv"

        with open(csv_name, mode='w', encoding='utf-8',
                  newline='') as csv_data:
            csv_writer = csv.writer(csv_data, quoting=csv.QUOTE_ALL)

            for todo in user_todos:
                row = [
                    users.get('id'),
                    users.get('username'),
                    todo.get('completed'),
                    todo.get('title')
                ]
                csv_writer.writerow(row)

    except Exception as e:
        print(e)
