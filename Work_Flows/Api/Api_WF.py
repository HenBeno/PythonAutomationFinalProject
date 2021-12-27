import allure

from extension import Api_Actions


@allure.step("api - get request")
def get_request(url):
    response = Api_Actions.get(url)
    return response


@allure.step("api - post request")
def post_request(url, payload):
    response = Api_Actions.post(url, payload)
    return response


@allure.step("api - delete request")
def delete_request(url, id):
    response = Api_Actions.delete(url, id)
    return response


@allure.step("api - staus code")
def assert_status_code(actual, expected):
    Api_Actions.assertion(actual, expected)
