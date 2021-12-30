import allure

import Utilities
from Utilities.Manage_Pages import Page_Manager
from Utilities.CommOps import get_data
from Work_Flows.Web.Login_WF import login_wf
from Work_Flows.Web.Logout_WF import logout_wf
from extension.Ui_Action import ui_action


class make_transfer_wf:
    @staticmethod
    @allure.step("transfer money method")
    def transfer_money_wf(name, amount, note):
        login_wf.login(get_data("test", "BaseUser"), get_data("test", "BasePassword"))
        make_transfer_wf.go_to_transfer_page()
        make_transfer_wf.insert_name_to_search_box(name)
        make_transfer_wf.choose_transfer_by_name(name)
        make_transfer_wf.insert_transfer_details(amount, note)
        make_transfer_wf.send_money()
        return make_transfer_wf.verify_transfer()

    @staticmethod
    @allure.step("request money method")
    def req_transfer_money_wf(name, amount, note):
        login_wf.login(get_data("test", "BaseUser"), get_data("test", "BasePassword"))
        make_transfer_wf.go_to_transfer_page()
        make_transfer_wf.insert_name_to_search_box(name)
        make_transfer_wf.choose_transfer_by_name(name)
        make_transfer_wf.insert_transfer_details(amount, note)
        make_transfer_wf.ask_for_money()
        return make_transfer_wf.verify_transfer()

    @staticmethod
    @allure.step("transfer page")
    def go_to_transfer_page():
        ui_action.click(Utilities.Manage_Pages.Main_Page_PO.new_transaction_btn())

    @staticmethod
    @allure.step("search by name")
    def insert_name_to_search_box(name):
        ui_action.send_key(Utilities.Manage_Pages.Main_Page_PO.search_box_txt(), name)

    @staticmethod
    @allure.step("transfer by name")
    def choose_transfer_by_name(name):
        for current_name in Utilities.Manage_Pages.Main_Page_PO.all_user_names():
            print(ui_action.get_text(current_name))
            if ui_action.get_text(current_name) == name:
                ui_action.click(current_name)
                break

    @staticmethod
    @allure.step("insert transfer details")
    def insert_transfer_details(amount, note):
        ui_action.send_key(
            Utilities.Manage_Pages.Main_Page_PO.amount_to_transfer(), amount
        )
        ui_action.send_key(
            Utilities.Manage_Pages.Main_Page_PO.note_to_transfer_txt(), note
        )

    @staticmethod
    @allure.step("ask for money")
    def ask_for_money():
        ui_action.click(Utilities.Manage_Pages.Main_Page_PO.ask_transfer_btn())

    @staticmethod
    @allure.step("send money")
    def send_money():
        ui_action.click(Utilities.Manage_Pages.Main_Page_PO.make_transfer_btn())

    @staticmethod
    @allure.step("verify transfer")
    def verify_transfer():
        result = ui_action.get_text(
            Utilities.Manage_Pages.Main_Page_PO.verify_transfer()
        )
        logout_wf.logout()
        return result
