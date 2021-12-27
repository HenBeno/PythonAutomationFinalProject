import allure
import pytest as pytest

from Test_Cases.conftest import *
from Work_Flows.Api.api_workflows import assert_status_code, get_request, post_request, delete_request

from Utilities.Read_Properties import get_data


@pytest.mark.usefixtures("init_api")
class Test_Api_Server:
    @allure.title("api post request")
    def test_01_get_post_list(self):
        response = get_request(self.url)
        post_list = response.text
        print(post_list)
        assert_status_code(response.status_code, 200)

    @allure.title("api create user ")
    def test_02_create_post(self):
        payload = {'userId': get_data("user_Id"), 'id': get_data("id"), 'title': get_data("title"),
                   'body': get_data("body")}
        response = post_request(self.url, payload)
        assert_status_code(response.status_code, 201)

    @allure.title("api delete user")
    def test_03_delete_post(self):
        response = delete_request(self.url, get_data("id_for_delete"))
        assert_status_code(response.status_code, 200)
