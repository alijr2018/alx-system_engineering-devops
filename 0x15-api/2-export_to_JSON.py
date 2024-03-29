#!/usr/bin/python3
""" Python script to export data in the JSON format. """
import csv
import json
import requests
from sys import argv

url_todo = 'https://jsonplaceholder.typicode.com/todos/'
url_user = 'https://jsonplaceholder.typicode.com/users/'


if __name__ == '__main__':
    employee_id = argv[1]
    todo = requests.get(url_todo, params={'userId': employee_id})
    user = requests.get(url_user, params={'id': employee_id})

    todo_dict_list = todo.json()
    user_dict_list = user.json()
    task_list = []
    user_tasks = {}
    employee = user_dict_list[0].get('username')

    with open("{}.json".format(employee_id), "w+") as jsonfile:
        for task in todo_dict_list:
            status = task.get('completed')
            title = task.get('title')
            task_dict = {}
            task_dict['task'] = title
            task_dict['completed'] = status
            task_dict['username'] = employee
            task_list.append(task_dict)
        user_tasks[employee_id] = task_list

        data = json.dumps(user_tasks)
        jsonfile.write(data)
