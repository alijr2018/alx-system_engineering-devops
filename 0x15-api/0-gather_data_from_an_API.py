#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress."""
import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            input = int(sys.argv[1])
            first_request = requests.get('{}/users/{}'.format(REST_API, input)).json()
            request = requests.get('{}/todos'.format(REST_API)).json()
            name = first_request.get('name')
            list_emp = list(filter(lambda x: x.get('userId') == input, request))
            completed_tasks = list(filter(lambda x: x.get('completed'), list_emp))
            print(
                'Employee {} is done with list_emp({}/{}):'.format(
                    name,
                    len(completed_tasks),
                    len(tasks)
                )
            )
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))