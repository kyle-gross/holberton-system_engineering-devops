#!/usr/bin/python3
"""This module saves employee task information to CSV"""
import csv
import requests
from sys import argv


if __name__ == "__main__":

    all_tasks = []

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(argv[1]))

    name = user.json().get('username')
    tasks = todo.json()

    for task in tasks:
        task_row = []
        task_row.append(argv[1])
        task_row.append(name)
        task_row.append(task.get('completed'))
        task_row.append(task.get('title'))

        all_tasks.append(task_row)

    filename = '2.csv'

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(all_tasks)
