import allure


class Appium_Actions:

    @staticmethod
    @allure.step("Click_on_Android_Element")
    def Click_on_ele(elem):
        elem.click()
