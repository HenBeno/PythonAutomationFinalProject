import Utilities
from extension.Ui_Action import ui_action
from Utilities.Manage_Pages import Page_Manager


class calculations_wf:

    def addition(self):
        ui_action.click_on_elem(Utilities.Manage_Pages.Calculate_PO.btn_1())
        ui_action.click_on_elem(Utilities.Manage_Pages.Calculate_PO.plus_btn())
        ui_action.click_on_elem(Utilities.Manage_Pages.Calculate_PO.btn_2())
        ui_action.click_on_elem(Utilities.Manage_Pages.Calculate_PO.equal_btn())
        return ui_action.get_text_from_elem(Utilities.Manage_Pages.Calculate_PO.result())

    def minus(self):
        ui_action.click_on_elem(Utilities.Manage_Pages.Calculate_PO.btn_3())
        ui_action.click_on_elem(Utilities.Manage_Pages.Calculate_PO.minus_btn())
        ui_action.click_on_elem(Utilities.Manage_Pages.Calculate_PO.btn_1())
        ui_action.click_on_elem(Utilities.Manage_Pages.Calculate_PO.equal_btn())
        return ui_action.get_text_from_elem(Utilities.Manage_Pages.Calculate_PO.result())

    def mult(self):
        ui_action.click_on_elem(Utilities.Manage_Pages.Calculate_PO.btn_1())
        ui_action.click_on_elem(Utilities.Manage_Pages.Calculate_PO.mult_btn())
        ui_action.click_on_elem(Utilities.Manage_Pages.Calculate_PO.btn_5())
        ui_action.click_on_elem(Utilities.Manage_Pages.Calculate_PO.equal_btn())
        return ui_action.get_text_from_elem(Utilities.Manage_Pages.Calculate_PO.result())
