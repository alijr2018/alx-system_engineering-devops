#!/usr/bin/python3
""" Python script to export data in the CSV format. """
import requests
import sys
import csv


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

        # Define the CSV file name
        csv_file_name = f"{employee_id}.csv"

        with open(csv_file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for task in todo_data:
                task_id = task['id']
                task_title = task['title']
                task_completed = task['completed']
                csv_writer.writerow([employee_id, employee_name, task_completed, task_title])

        print(f"Data exported to {csv_file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
