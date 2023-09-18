#!/usr/bin/python3
"""
This module makes a request to an API to extract specific data
"""
import json
import requests
from sys import argv


url = 'https://jsonplaceholder.typicode.com'

# Solicitud hacia la API
response = requests.get(url)


def make_request():
    # Hacer las solicitudes para obtener los datos de la API
    response_tasks = requests.get(f"{url}/todos?userId={argv[1]}")
    response_user = requests.get(f"{url}/users/{argv[1]}")

    # Convertir de JSON a estrucutura de datos
    all_tasks = response_tasks.json()
    username = response_user.json().get('username')
    user_id = response_user.json().get('id')

    data = {
            user_id: [
                {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": username
            }
            for task in all_tasks
        ]
    }

    # Archivo x.json
    file_json = f"{user_id}.json"

    # Configuracion del archivo x.json
    with open(file_json, 'w') as file:
        file.write(json.dumps(data))


if __name__ == '__main__':
    make_request()
