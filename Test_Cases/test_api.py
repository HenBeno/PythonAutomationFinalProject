from Test_Cases.conftest import *
from Utilities.Read_Properties import get_data
from Work_Flows.Api.Api_WF import assert_status_code, get_request, post_request, delete_request


@pytest.mark.usefixtures("init_api")
class Test_Api_Server:
    @allure.title("get post list")
    def test_01_get_post_list(self):
        response = get_request(self.url)
        post_list = response.text
        print(post_list)
        assert_status_code(response.status_code, 200)

    @allure.title("create new post")
    def test_02_create_post(self):
        payload = {'userId': get_data("user_Id"), 'id': get_data("id"), 'title': get_data("title"),
                   'body': get_data("body")}
        response = post_request(self.url, payload)
        assert_status_code(response.status_code, 201)

    @allure.title("delete post")
    def test_03_delete_post(self):
        response = delete_request(self.url, get_data("id_for_delete"))
        assert_status_code(response.status_code, 200)
