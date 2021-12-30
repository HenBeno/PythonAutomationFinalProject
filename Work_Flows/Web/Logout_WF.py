import allure

import Utilities
from Utilities.Manage_Pages import Page_Manager
from extension.Ui_Action import ui_action


class logout_wf:
    @staticmethod
    @allure.step("logout method")
    def logout():
        ui_action.click(Utilities.Manage_Pages.Left_Bar_PO.logout_btn())
