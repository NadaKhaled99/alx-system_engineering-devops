#!/usr/bin/python3
"""
Holder Place
"""

if __name__ == "__main__":

    import requests
    from sys import argv

    if len(argv) < 2:
        exit()
    
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={A}&completed=true"
        .format(argv[1]))
    
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={A}"
        .format(argv[1]))
    name = name.json()
    name = name[0]["name"]
    
    todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={A}".format(argv[1]))
    todo = todo.json()
    todo = len(todo)
    todos = todos.json()
    todo_list = []

    for x in todos:
        todo_list.append("\t {}".format(x["title"]))
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(todos), todo))
    for y in todo_list:
        print(y)
