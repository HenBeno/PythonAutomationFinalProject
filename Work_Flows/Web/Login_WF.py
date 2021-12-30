import allure

import Utilities
from Utilities.Manage_Pages import Page_Manager
from Work_Flows.Web.Logout_WF import logout_wf
from extension.Ui_Action import ui_action


class login_wf:
    @staticmethod
    @allure.step("login and verify")
    def login_and_verify(user_name, password):
        login_wf.insert_login_details(user_name, password)
        return login_wf.verify_login()

    @staticmethod
    @allure.step("login")
    def login(user_name, password):
        login_wf.insert_login_details(user_name, password)

    @staticmethod
    @allure.step("insert login details")
    def insert_login_details(user_name, password):
        ui_action.send_key(Utilities.Manage_Pages.Login_PO.user_name_txt(), user_name)
        ui_action.send_key(Utilities.Manage_Pages.Login_PO.password_txt(), password)
        ui_action.click(Utilities.Manage_Pages.Login_PO.login_btn())

    @staticmethod
    @allure.step("verify login")
    def verify_login():
        result = ui_action.get_text_without_symbol(
            Utilities.Manage_Pages.Create_User_PO.present_user_name()
        )
        logout_wf.logout()
        return result
