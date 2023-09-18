#!/usr/bin/python3
import requests
from sys import argv


url = 'https://jsonplaceholder.typicode.com'

#Acceso a la API
response = requests.get(url)

def make_request():

    #Hacer las solicitudes para obtener los datos de la API
    response_tasks = requests.get(f"{url}/todos?userId={argv[1]}")
    response_user = requests.get(f"{url}/users/{argv[1]}")


    #Convertir de JSON a estrucutura de datos
    ALL_OF_TASKS = response_tasks.json()
    EMPLOYEE_NAME = response_user.json().get('name')

    #Lista de tareas completadas por el usuario x
    NUMBER_OF_DONE_TASKS = []
    for task in ALL_OF_TASKS:
        if task.get('completed'):
            NUMBER_OF_DONE_TASKS.append(task)

    print(f"Employee {EMPLOYEE_NAME} is done with tasks({len(NUMBER_OF_DONE_TASKS)}/{len(ALL_OF_TASKS)}):")
    for task in NUMBER_OF_DONE_TASKS:
        print(f"\t {task.get('title')}")

if __name__ == '__main__':
    make_request()
