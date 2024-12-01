import json

import requests
from jsonschema import validate

url = 'https://reqres.in/api/'


def test_schema_get_single_user():
    user_id = 4
    response = requests.get(url + f"users/{user_id}")
    assert response.status_code == 200
    with open('files/get_single.json') as file:
        schema = json.load(file)
    validate(instance=response.json(), schema=schema)

def test_schema_login_user():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(url + "login", json=payload)
    assert response.status_code == 200
    with open('files/login.json') as file:
        schema = json.load(file)
    validate(response.json(), schema)

def test_schema_register_user():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(url + "register", json=payload)
    assert response.status_code == 200
    with open('files/register.json') as file:
        schema = json.load(file)
    validate(response.json(), schema)

def test_schema_update_user():
    payload = {
        "name": "nika",
        "job": "developer"
    }
    user_id = 4
    response = requests.put(url + f"users/{user_id}", json=payload)
    assert response.status_code == 200
    with open('files/update.json') as file:
        schema = json.load(file)
    validate(instance=response.json(), schema=schema)