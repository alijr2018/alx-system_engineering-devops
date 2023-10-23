#!/usr/bin/python3
""" Python script to export data in the CSV format. """
import re
import requests
import sys
import csv

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            employee_id = int(sys.argv[1)
            user_url = f'{REST_API}/users/{employee_id}'
            todo_url = f'{REST_API}/todos'
            
            user_data = requests.get(user_url).json()
            todos_data = requests.get(todo_url).json()

            user_name = user_data.get('name')
            employee_csv_file = f'{employee_id}.csv'

            with open(employee_csv_file, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

                for task in todos_data:
                    if task['userId'] == employee_id:
                        user_id = task['userId']
                        task_completed = task['completed']
                        task_title = task['title']
                        csv_writer.writerow([user_id, user_name, task_completed, task_title])

            print(f"Data exported to {employee_csv_file}")
