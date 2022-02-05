import allure

import Utilities
from Utilities.Manage_Pages import Page_Manager
from Work_Flows.Desktop.Calculations_WF import calculations_wf
from extension.Ui_Action import ui_action


class scientific_calculations_wf:

    @staticmethod
    @allure.step("Math workflows")
    def calc_wf(math_to_calc):

        scientific_calculations_wf.open_calculator_menu()
        scientific_calculations_wf.change_to_scientific_mode()

        for letter in math_to_calc:
            type = calculations_wf.get_type_of_letter(letter)
            if type == "symbol":
                calculations_wf.click_on_math_action(letter)
            elif type == "number":
                calculations_wf.click_on_number(letter)
            elif type != "space":
                raise TypeError("Wrong input, unrecognized input: " + type)
        calculations_wf.calc_result()
        result = calculations_wf.get_result()
        print(result)
        calculations_wf.clear_result()
        return result

    @staticmethod
    @allure.step("Open calculator menu")
    def open_calculator_menu():
        ui_action.click(Utilities.Manage_Pages.Calculate_Menu_PO.toggle_panel_btn)

    @staticmethod
    @allure.step("Change to scientific mode")
    def change_to_scientific_mode():
        ui_action.click(Utilities.Manage_Pages.Calculate_Menu_PO.scientific_calculator)
