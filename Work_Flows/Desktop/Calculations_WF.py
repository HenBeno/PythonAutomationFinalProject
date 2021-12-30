import allure

import Utilities
from Utilities.Manage_Pages import Page_Manager
from extension.Ui_Action import ui_action


class calculations_wf:

    @staticmethod
    @allure.step("Math workflows")
    def calc_wf(math_to_calc):
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
    @allure.step("Check if the letter is a number or a math symbol")
    def get_type_of_letter(letter_to_calc):
        return ui_action.get_calc_letter_type(letter_to_calc)

    @staticmethod
    @allure.step("Convert string to num click")
    def click_on_number(letter):
        match letter:
            case "0":
                ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_0())
            case "1":
                ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_1())
            case "2":
                ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_2())
            case "3":
                ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_3())
            case "4":
                ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_4())
            case "5":
                ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_5())
            case "6":
                ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_6())
            case "7":
                ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_7())
            case "8":
                ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_8())
            case "9":
                ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_9())

    @staticmethod
    @allure.step("Convert string to math action click")
    def click_on_math_action(letter):
        match letter:
            case "+":
                ui_action.click(Utilities.Manage_Pages.Calculate_PO.plus_btn())
            case "*":
                ui_action.click(Utilities.Manage_Pages.Calculate_PO.mult_btn())
            case "-":
                ui_action.click(Utilities.Manage_Pages.Calculate_PO.minus_btn())
            case "/":
                ui_action.click(Utilities.Manage_Pages.Calculate_PO.divide_btn())

    @staticmethod
    @allure.step("Click on equal")
    def calc_result():
        ui_action.click(Utilities.Manage_Pages.Calculate_PO.equal_btn())

    @staticmethod
    @allure.step("Get Clear result")
    def get_result():
        return ui_action.get_result_only_numbers(Utilities.Manage_Pages.Calculate_PO.get_calc_result())

    @staticmethod
    @allure.step("Get Clear result")
    def clear_result():
        return ui_action.click(Utilities.Manage_Pages.Calculate_PO.clear_btn())

    # @staticmethod
    # @allure.step("addition workflows")
    # def addition():
    #     ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_1())
    #     ui_action.click(Utilities.Manage_Pages.Calculate_PO.plus_btn())
    #     ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_2())
    #     ui_action.click(Utilities.Manage_Pages.Calculate_PO.equal_btn())
    #     return ui_action.get_result_only_numbers(Utilities.Manage_Pages.Calculate_PO.result())
    #
    # @staticmethod
    # @allure.step("minus workflows")
    # def minus():
    #     ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_3())
    #     ui_action.click(Utilities.Manage_Pages.Calculate_PO.minus_btn())
    #     ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_1())
    #     ui_action.click(Utilities.Manage_Pages.Calculate_PO.equal_btn())
    #     return ui_action.get_result_only_numbers(Utilities.Manage_Pages.Calculate_PO.result())
    #
    # @staticmethod
    # @allure.step("multiple Workflows")
    # def mult():
    #     ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_1())
    #     ui_action.click(Utilities.Manage_Pages.Calculate_PO.mult_btn())
    #     ui_action.click(Utilities.Manage_Pages.Calculate_PO.btn_5())
    #     ui_action.click(Utilities.Manage_Pages.Calculate_PO.equal_btn())
    #     return ui_action.get_result_only_numbers(Utilities.Manage_Pages.Calculate_PO.result())

