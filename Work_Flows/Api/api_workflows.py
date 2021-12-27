import allure

from extension import api_actions

@allure.step("api - get request")
def get_request(url):
    response = api_actions.get(url)
    return response

@allure.step("api - post request")
def post_request(url, payload):
    response = api_actions.post(url, payload)
    return response

@allure.step("api - delete request")
def delete_request(url, id):
    response = api_actions.delete(url, id)
    return response

@allure.step("api - staus code")
def assert_status_code(actual, expected):
    api_actions.assertion(actual, expected)
