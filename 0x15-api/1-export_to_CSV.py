#!/usr/bin/python3
""" Python script to export data in the CSV format. """
import csv
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

    employee = user_dict_list[0].get('username')

    with open("{}.csv".format(employee_id), "a+", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        rows = []

        for task in todo_dict_list:
            status = task['completed']
            title = task['title']
            rows.append(["{}".format(employee_id),
                         "{}".format(employee),
                         "{}".format(status),
                         "{}".format(title)])

        csvwriter.writerows(rows)
