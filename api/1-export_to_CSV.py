#!/usr/bin/python3
"""
This module makes a request to an API to extract specific data
"""
import requests
from sys import argv
import csv


url = 'https://jsonplaceholder.typicode.com'

# Solicitud hacia la API
response = requests.get(url)


def make_request():
    # Hacer las solicitudes para obtener los datos de la API
    response_tasks = requests.get(f"{url}/todos?userId={argv[1]}")
    response_user = requests.get(f"{url}/users/{argv[1]}")

    # Convertir de JSON a estrucutura de datos
    all_tasks = response_tasks.json()
    username = response_user.json().get('name')
    user_id = response_user.json().get('id')

    # Archivo x.csv
    csv_filename = f"{user_id}.csv"

    # Configuracion del archivo x.csv 
    with open(csv_filename, 'w') as file:
        write = csv.writer(
                file,
                delimiter=',',
                quotechar='"',
                quoting=csv.QUOTE_ALL)


        for task in all_tasks:
            task_status = task.get('completed')
            task_title = task.get('title')

            # Escribe una fila en el archivo csv  con los datos de la API
            write.writerow([user_id, username, task_status, task_title])


if __name__ == '__main__':
    make_request()
