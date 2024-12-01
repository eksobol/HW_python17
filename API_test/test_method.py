import requests

url = 'https://reqres.in/api/'


def test_single_user():
    user_id = 4
    response = requests.get(url + f"users/{user_id}")
    assert response.status_code == 200


def test_negative_single_user():
    user_id = 32
    response = requests.get(url + f"users/{user_id}")
    assert response.status_code == 404


def test_create_user():
    payload = {
        "name": "nika",
        "job": "tester"
    }
    response = requests.post(url + "users", json=payload)
    assert response.status_code == 201


def test_update_user():
    payload = {
        "name": "nika",
        "job": "developer"
    }
    user_id = 4
    response = requests.put(url + f"users/{user_id}", json=payload)
    assert response.status_code == 200


def test_delete_user():
    user_id = 4
    response = requests.delete(url + f"users/{user_id}")
    assert response.status_code == 204


def test_negative_register_user():
    payload = {
        "email": "abc@ab.ru",
    }
    response = requests.post(url + "register", json=payload)
    assert response.status_code == 400
