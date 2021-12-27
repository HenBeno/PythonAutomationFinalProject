import Utilities
from Utilities.Manage_Pages import Page_Manager
from extension.Appium_Actions import Appium_Actions


class listview_edit:

    @staticmethod
    def listview_edit():
        Utilities.Manage_Pages.Edit_Section_PO.goBack()
        Appium_Actions.Click_on_ele(Utilities.Manage_Pages.Edit_Section_PO.settings_btn())
        Appium_Actions.Click_on_ele(Utilities.Manage_Pages.Edit_Section_PO.edit_btn())
        Appium_Actions.Click_on_ele(Utilities.Manage_Pages.Edit_Section_PO.first_item())
        Appium_Actions.Click_on_ele(Utilities.Manage_Pages.Edit_Section_PO.second_item())
        Utilities.Manage_Pages.Edit_Section_PO.goBack()


