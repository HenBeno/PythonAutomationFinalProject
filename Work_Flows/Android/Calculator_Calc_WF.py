import allure

import Utilities
from Utilities.Manage_Pages import Page_Manager
from extension.Ui_Action import ui_action


class Calculator_calc:
    @staticmethod
    @allure.title("test calculator - appium")
    def calc_test():
        ui_action.click(Utilities.Manage_Pages.Calculator_PO.enter_to_calculator())
        ui_action.click(Utilities.Manage_Pages.Calculator_PO.num_9())
        ui_action.click(Utilities.Manage_Pages.Calculator_PO.op_mul())
        ui_action.click(Utilities.Manage_Pages.Calculator_PO.num_5())
        ui_action.click(Utilities.Manage_Pages.Calculator_PO.op_sub())
        ui_action.click(Utilities.Manage_Pages.Calculator_PO.num_3())
        ui_action.click(Utilities.Manage_Pages.Calculator_PO.op_add())
        ui_action.click(Utilities.Manage_Pages.Calculator_PO.num_7())
