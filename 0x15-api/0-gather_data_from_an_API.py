#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress."""
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

def get_employee_todo_progress(employee_id):
    emp_req = requests.get(f"{REST_API}/users/{employee_id}").json()
    task_req = requests.get(f"{REST_API}/todos?userId={employee_id}").json()
    emp_name = emp_req.get('name')
    total_tasks = len(task_req)
    completed_tasks = [task for task in task_req if task.get('completed')]

    print(
        f'Employee {emp_name} is done with tasks({len(completed_tasks)}/{total_tasks}):'
    )

    for task in completed_tasks:
        print(f'\t{task.get("title")}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)