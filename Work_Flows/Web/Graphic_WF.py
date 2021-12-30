import allure

from Test_Cases.conftest import open_eye, eyes
from Work_Flows.Web.Login_WF import login_wf
from Work_Flows.Web.Logout_WF import logout_wf


class graphic_elements_wf:
    @staticmethod
    @allure.step("")
    def graphic_verify(username1, password1, username2, password2):
        graphic_elements_wf.open_eye()
        graphic_elements_wf.login_as_user(username1, password1)
        graphic_elements_wf.take_screen_pic(username1)
        graphic_elements_wf.login_as_user(username2, password2)
        graphic_elements_wf.take_screen_pic(username2)
        graphic_elements_wf.close_eye()

    @staticmethod
    @allure.step("Insert new user details")
    def open_eye():
        open_eye()

    @staticmethod
    def take_screen_pic(username):
        eyes.check_window("Screen Shot - login as " + username)
        logout_wf.logout()

    @staticmethod
    def login_as_user(username, password):
        login_wf.login(username, password)

    @staticmethod
    def close_eye():
        eyes.close()
