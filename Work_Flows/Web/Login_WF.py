import Utilities
from Utilities.Manage_Pages import Page_Manager
from Utilities.Read_Properties import get_data
from Work_Flows.Web.Logout_WF import logout_wf
from extension.Ui_Action import ui_action


class login_wf:

    @staticmethod
    def login_and_verify(user_name, password):
        login_wf.insert_login_details(user_name, password)
        return login_wf.verify_login()

    @staticmethod
    def login(user_name, password):
        login_wf.insert_login_details(user_name, password)

    @staticmethod
    def insert_login_details(user_name, password):
        ui_action.send_key_to_elem(Utilities.Manage_Pages.Login_PO.user_name_txt(), user_name)
        ui_action.send_key_to_elem(Utilities.Manage_Pages.Login_PO.password_txt(), password)
        ui_action.click_on_elem(Utilities.Manage_Pages.Login_PO.login_btn())

    @staticmethod
    def verify_login():
        result = ui_action.get_text_only_letters_from_elem(Utilities.Manage_Pages.Create_User_PO.present_user_name())
        logout_wf.logout()
        return result
