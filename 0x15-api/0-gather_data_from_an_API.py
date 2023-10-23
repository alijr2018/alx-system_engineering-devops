#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data["name"]

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])

    print(f"Employee {employee_name} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")

    for todo in todos_data:
        if todo["completed"]:
            print(f"    {todo['title']}")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
