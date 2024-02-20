#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    s = requests.Session()

    idEmp = argv[1]
    idUrl = "https://jsonplaceholder.typicode.com/users/{}/todos".format(idEmp)
    infUrl = "https://jsonplaceholder.typicode.com/users/{}".format(idEmp)

    empTasks = s.get(idUrl)
    empInfo = s.get(infUrl)

    tasks = empTasks.json()
    name = empInfo.json()['name']

    number_of_done_tasks = 0

    for task in tasks:
        if task['completed']:
            number_of_done_tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, number_of_done_tasks, len(tasks)))

    for done_task in tasks:
        if done_task['completed']:
            print("\t " + done_task.get('title'))
