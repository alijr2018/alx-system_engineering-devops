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
            x = '{}/users/{}'.format(REST_API, input)
            f_request = requests.get(x).json()
            request = requests.get('{}/todos'.format(REST_API)).json()
            name = f_request.get('name')
            t_req = list(filter(lambda x: x.get('userId') == input, request))
            c_tasks = list(filter(lambda x: x.get('completed'), t_req))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    name,
                    len(c_tasks),
                    len(t_req)
                )
            )
            if len(c_tasks) > 0:
                for task in c_tasks:
                    print('\t {}'.format(task.get('title')))
