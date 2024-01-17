#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    API = 'https://jsonplaceholder.typicode.com'

    # Obtener informacion de un empleado en particular
    RES_TASK = requests.get(f'{API}/todos?userId={argv[1]}')
    RES_USERS = requests.get(f'{API}/users/{argv[1]}')

    # deserializado de datos
    tasks = RES_TASK.json()
    users = RES_USERS.json()

    completed = []
    # iteramos las task completadas y lo guardamos en completed.
    for task in tasks:
        if task['completed']:
            completed.append(task)

    # Empleado y cantidad de tareas completadas y total
    print(f"Employee {users['name']} is done with \
tasks({len(completed)}/{len(tasks)}):")

    # Iteramos todas las tareas completadas.
    for t in completed:
        print(f"\t {t['title']}")
