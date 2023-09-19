#!/usr/bin/python3
"""
This module makes a request to an API to extract specific data
"""
import json
import requests


url = 'https://jsonplaceholder.typicode.com'

# Solicitud hacia la API
response = requests.get(url)


def make_request():
    # Hacer las solicitudes para obtener los datos del usuarios de la API
    response_user = requests.get(f"{url}/users/")
    users = response_user.json()

    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        #Hacer una solicitud para obtener las tareas de un usuario x
        response_tasks = requests.get(f"{url}/todos?Id={user_id}")
        tasks = response_tasks.json()
    
        data = [
                {
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed'],
                    }
                for task in tasks
                ]

        #almacenar todo los datos en formato diccionario
        all_tasks[user_id] = data

    # Archivo x.json
    file_json = f"todo_all_employees.json"

    # Escribir todos los datos obtenidos en el archivo file_json serializados
    with open(file_json, 'w') as file:
        json.dump(all_tasks, file)


if __name__ == '__main__':
    make_request()
