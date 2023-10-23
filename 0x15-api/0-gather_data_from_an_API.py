#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress."""
import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get user details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()
    
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return

    # Get user's TODO list
    todo_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()
    
    # Calculate the number of completed tasks
    completed_tasks = [task for task in todo_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_data)
    
    # Display progress
    print(f"Employee {user_data['name']} is done with tasks({num_completed_tasks}/{total_tasks}):")
    
    # Display titles of completed tasks
    for task in completed_tasks:
        print(f"     {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

