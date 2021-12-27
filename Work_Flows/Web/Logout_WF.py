import allure

import Utilities
from extension.Ui_Action import ui_action
from Utilities.Manage_Pages import Page_Manager


class logout_wf:

    @staticmethod
    @allure.step("logout method")
    def logout():
        ui_action.click_on_elem(Utilities.Manage_Pages.Left_Bar_PO.logout_btn())
