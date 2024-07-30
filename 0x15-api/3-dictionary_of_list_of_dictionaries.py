#!/usr/bin/python3

"""
Returns information about a given employee's
TODO list progress using REST API and export data in the JSON format
"""

from requests import get
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    todos2 = response2.json()

    new_dict1 = {}

    for j in todos2:

        row = []
        for i in todos:

            new_dict2 = {}

            if j['id'] == i['userId']:

                new_dict2['username'] = j['username']
                new_dict2['task'] = i['title']
                new_dict2['completed'] = i['completed']
                row.append(new_dict2)

        new_dict1[j['id']] = row

    with open("todo_all_employees.json",  "w") as f:

        json_obj = json.dumps(new_dict1)
        f.write(json_obj)
