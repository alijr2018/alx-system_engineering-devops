#!/usr/bin/python3
""" Python script to export data in the CSV format. """
import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info(id):
    total_tasks = 0
    response = requests.get(todos_url).json()
    for i in response:
        if i['userId'] == id:
            total_tasks += 1

    csv_filename = f"{id}.csv"
    num_lines = 0

    with open(csv_filename, 'r') as f:
        csv_reader = csv.reader(f)
        # Skip the header row
        next(csv_reader)
        for _ in csv_reader:
            num_lines += 1

    if total_tasks == num_lines:
        print(f"Number of tasks in CSV: OK ({num_lines}/{total_tasks})")
    else:
        print(f"Number of tasks in CSV: Incorrect ({num_lines}/{total_tasks})")


if __name__ == "__main__":
    user_info(int(sys.argv[1]))
