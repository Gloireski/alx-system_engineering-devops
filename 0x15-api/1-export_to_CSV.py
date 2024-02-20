#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
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

    filename = idEmp+'.csv'

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([idEmp, name, task.get('completed'),
                             task.get('title')])
