#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
export data in the JSON format.
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
    name = empInfo.json()['username']

    totalTasks = []
    updateUser = {}

    for task in tasks:
        totalTasks.append(
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": name,
            })
    updateUser[idEmp] = totalTasks

    file_Json = idEmp + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)
