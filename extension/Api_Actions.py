import requests


def get(url):
    response = requests.get(url)
    return response


def post(url, payload):
    response = requests.post(
        url, json=payload, headers={"Content-Type": "application/json"}
    )
    return response


def delete(url, id):
    response = requests.delete(url + id)
    return response


def assertion(actual, expected):
    assert actual == expected
