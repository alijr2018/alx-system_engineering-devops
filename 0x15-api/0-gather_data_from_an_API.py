#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress."""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

def check_tasks(filename):
    """ Fetch user name, number of tasks """

    resp = requests.get(todos_url).json()

    count = 0
    with open(filename, 'r') as f:
        next(f)  # Skip the first line
        for line in f:
            count += 1
            if line.startswith('\t '):
                print(f"Task {count} Formatting: OK")
            else:
                print(f"Task {count} Formatting: Incorrect")

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <student_output_file>")
        sys.exit(1)

    check_tasks(sys.argv[1])