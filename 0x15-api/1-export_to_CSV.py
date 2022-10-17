#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import requests as r
import csv
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
        csv_name = "{}.csv".format(users.get('id'))

        with open(csv_name, mode='w', encoding='utf-8', newline='') as csv_data:
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
