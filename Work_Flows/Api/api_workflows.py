from extension import api_actions


def get_request(url):
    response = api_actions.get(url)
    return response


def post_request(url, payload):
    response = api_actions.post(url, payload)
    return response


def delete_request(url, id):
    response = api_actions.delete(url, id)
    return response


def assert_status_code(actual, expected):
    api_actions.assertion(actual, expected)
