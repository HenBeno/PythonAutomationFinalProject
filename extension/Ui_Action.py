import re
from time import sleep

import allure

regex = re.compile("[^a-zA-Z1-9_]")
regex2 = re.compile("[^1-9]")
valid_symbols = "+-*/"


class ui_action:
    @staticmethod
    @allure.step("Send value to elem")
    def send_key(elem, value):
        elem.send_keys(value)

    @staticmethod
    @allure.step("Click on elem")
    def click(elem):
        elem.click()

    @staticmethod
    @allure.step("Clean all non letter from text elem")
    def get_text(elem):
        return elem.text

    @staticmethod
    @allure.step("Clean all symbol from text elem")
    def get_text_without_symbol(elem):
        return regex.sub("", elem.text)

    @staticmethod
    @allure.step("Get Calculation Result")
    def get_result_only_numbers(elem):
        return regex2.sub("", elem.text)

    @staticmethod
    @allure.step("Get letter type")
    def get_calc_letter_type(letter):
        if letter.isdigit():
            return "number"
        elif letter in valid_symbols:
            return "symbol"
        elif letter == " ":
            return "space"
        else:
            return letter
