#!/usr/bin/python3
""" Python script to export data in the JSON format. """
import requests
import json
import sys


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        user_data = user_response.json()
        todo_data = todo_response.json()

        employee_id = user_data.get('id')
        employee_name = user_data.get('name')

        # Create a dictionary with the required format
        data = {
            employee_id: [
                {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": employee_name
                }
                for task in todo_data
            ]
        }

        # Create and write the JSON file
        json_filename = f"{employee_id}.json"
        with open(json_filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"Data exported to {json_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
