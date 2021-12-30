import allure

import Utilities
from Utilities.Manage_Pages import Page_Manager
from Utilities.CommOps import get_data
from Work_Flows.Web.Login_WF import login_wf
from Work_Flows.Web.Logout_WF import logout_wf
from extension.Ui_Action import ui_action


class create_user_wf:
    @staticmethod
    @allure.step("")
    def create_user():
        create_user_wf.singup()
        create_user_wf.fill_new_user_data()
        return create_user_wf.verify_login()

    @staticmethod
    @allure.step("Insert new user details")
    def singup():
        ui_action.click(Utilities.Manage_Pages.Create_User_PO.create_user_btn())
        ui_action.click(Utilities.Manage_Pages.Create_User_PO.create_user_btn())
        ui_action.send_key(
            Utilities.Manage_Pages.Create_User_PO.first_name_txt(),
            get_data("test", "RealWorldApp_name_txt"),
        )
        ui_action.send_key(
            Utilities.Manage_Pages.Create_User_PO.last_name_txt(),
            get_data("test", "RealWorldApp_last_name_txt"),
        )
        ui_action.send_key(
            Utilities.Manage_Pages.Create_User_PO.user_name_txt(),
            get_data("test", "RealWorldApp_user_name_txt"),
        )
        ui_action.send_key(
            Utilities.Manage_Pages.Create_User_PO.password_txt(),
            get_data("test", "RealWorldApp_password_txt"),
        )
        ui_action.send_key(
            Utilities.Manage_Pages.Create_User_PO.password_conf_txt(),
            get_data("test", "RealWorldApp_password_txt"),
        )
        ui_action.click(Utilities.Manage_Pages.Create_User_PO.submit_btn())

    @staticmethod
    @allure.step("Insert first login details (bank details)")
    def fill_new_user_data():
        login_wf.login(
            get_data("test", "RealWorldApp_user_name_txt"),
            get_data("test", "RealWorldApp_password_txt"),
        )
        ui_action.click(Utilities.Manage_Pages.Create_User_PO.next_after_login_btn())
        ui_action.send_key(
            Utilities.Manage_Pages.Create_User_PO.bank_name_txt(),
            get_data("test", "RealWorldApp_bank_name_txt"),
        )
        ui_action.send_key(
            Utilities.Manage_Pages.Create_User_PO.routing_number_txt(),
            get_data("test", "RealWorldApp_routing_number_txt"),
        )
        ui_action.send_key(
            Utilities.Manage_Pages.Create_User_PO.bank_account_number_txt(),
            get_data("test", "RealWorldApp_bank_account_number_txt"),
        )
        ui_action.click(Utilities.Manage_Pages.Create_User_PO.save_info_btn())
        ui_action.click(Utilities.Manage_Pages.Create_User_PO.next_after_login_btn())

    @staticmethod
    @allure.step("Return clean user name after login")
    def verify_login():
        result = ui_action.get_text_without_symbol(
            Utilities.Manage_Pages.Create_User_PO.present_user_name()
        )
        logout_wf.logout()
        return result
