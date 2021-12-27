import re

import allure

regex = re.compile('[^a-zA-Z1-9_]')


class ui_action:

    @allure.step("Send value to elem")
    def send_key_to_elem(elem, value):
        elem.send_keys(value)

    @allure.step("Click on elem")
    def click_on_elem(elem):
        elem.click()

    @allure.step("Clean all non letter from text elem")
    def get_text_from_elem(elem):
        return elem.text


    @allure.step("Clean all non letter from text elem")
    def get_text_only_letters_from_elem(elem):
        return regex.sub('', elem.text)

