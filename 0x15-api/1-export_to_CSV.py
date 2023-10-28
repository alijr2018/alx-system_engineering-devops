#!/usr/bin/python3
""" Python script to export data in the CSV format. """
import csv
import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            employee_id = int(sys.argv[1])
            user_url = '{}/users/{}'.format(REST_API, employee_id)
            user_response = requests.get(user_url)

            if user_response.status_code == 200:
                user_data = user_response.json()
                username = user_data.get('username')
                tasks_url = '{}/todos?userId={}'.format(REST_API, employee_id)
                tasks_response = requests.get(tasks_url)

                if tasks_response.status_code == 200:
                    tasks_data = tasks_response.json()
                    csv_filename = '{}.csv'.format(employee_id)

                    with open(csv_filename, mode='w', newline='') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        csv_writer.writerow([
                            "USER_ID",
                            "USERNAME",
                            "TASK_COMPLETED_STATUS",
                            "TASK_TITLE"
                            ])

                        for task in tasks_data:
                            task_completed = task.get('completed')
                            task_title = task.get('title')
                            csv_writer.writerow([
                                employee_id,
                                username,
                                task_completed,
                                task_title
                                ])
        else:
            pass
    else:
        pass
