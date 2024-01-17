# API

- In this project, we will see more about APIs as a means of communication between server and web page:

```py
    import requests

    url = 'https://api.ejemplo.com/endpoint'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Trabaja con los datos obtenidos
    else:
        print(f'Error: {response.status_code}')

```
