import allure

import Utilities
from Utilities.Manage_Pages import Page_Manager
from extension.Ui_Action import ui_action


class listview_edit:
    @staticmethod
    @allure.title("test listview edit section - appium")
    def listview_edit():
        Utilities.Manage_Pages.Edit_Section_PO.goBack()
        ui_action.click(
            Utilities.Manage_Pages.Edit_Section_PO.settings_btn()
        )
        ui_action.click(Utilities.Manage_Pages.Edit_Section_PO.edit_btn())
        ui_action.click(Utilities.Manage_Pages.Edit_Section_PO.first_item())
        ui_action.click(
            Utilities.Manage_Pages.Edit_Section_PO.second_item()
        )
        Utilities.Manage_Pages.Edit_Section_PO.goBack()
