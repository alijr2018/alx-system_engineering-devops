#!/usr/bin/python3
""" Python script to export data in the JSON format. """
import json
import requests

if __name__ == '__main':
    user_tasks = {}
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url_user).json()

    for user in users:
        employee_id = user['id']
        todo = requests.get(url_todo, params={'userId': employee_id})

        todo_dict_list = todo.json()
        task_list = []
        employee = user['username']

        for task in todo_dict_list:
            status = task.get('completed')
            title = task.get('title')
            task_dict = {}
            task_dict['task'] = title
            task_dict['completed'] = status
            task_dict['username'] = employee
            task_list.append(task_dict)
        user_tasks[employee_id] = task_list

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(user_tasks, jsonfile, indent=4)
