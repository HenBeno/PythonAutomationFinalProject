import allure

import Utilities
from Utilities.Manage_Pages import Page_Manager
from extension.Appium_Actions import Appium_Actions


class Calculator_calc:

    @staticmethod
    @allure.title("test calculator - appium")
    def calc_test():
        Appium_Actions.Click_on_ele(Utilities.Manage_Pages.Calculator_PO.enter_to_calculator())
        Appium_Actions.Click_on_ele(Utilities.Manage_Pages.Calculator_PO.num_9())
        Appium_Actions.Click_on_ele(Utilities.Manage_Pages.Calculator_PO.op_mul())
        Appium_Actions.Click_on_ele(Utilities.Manage_Pages.Calculator_PO.num_5())
        Appium_Actions.Click_on_ele(Utilities.Manage_Pages.Calculator_PO.op_sub())
        Appium_Actions.Click_on_ele(Utilities.Manage_Pages.Calculator_PO.num_3())
        Appium_Actions.Click_on_ele(Utilities.Manage_Pages.Calculator_PO.op_add())
        Appium_Actions.Click_on_ele(Utilities.Manage_Pages.Calculator_PO.num_7())



