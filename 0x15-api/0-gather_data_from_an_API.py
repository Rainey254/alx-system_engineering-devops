#!/usr/bin/python3

"""
Returns information about a given employee's
TODO list progress using REST API
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    todos = response.json()
    completed = 0
    total = 0
    tasks = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    todos2 = response2.json()

    for i in todos2:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')

    for i in todos:
        if i.get('userId') == int(argv[1]):
            total += 1

            if i.get('completed') is True:
                completed += 1
                tasks.append(i.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee, completed,
                                                          total))

    for i in tasks:
        print("\t {}".format(i))
