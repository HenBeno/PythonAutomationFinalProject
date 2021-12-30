class Calculate_Page:
    def __init__(self, driver):
        self.driver = driver

    def btn_0(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='num0Button']")

    def btn_1(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='num1Button']")

    def btn_2(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='num2Button']")

    def btn_3(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='num3Button']")

    def btn_4(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='num4Button']")

    def btn_5(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='num5Button']")

    def btn_6(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='num6Button']")

    def btn_7(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='num7Button']")

    def btn_8(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='num8Button']")

    def btn_9(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='num9Button']")

    def equal_btn(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='equalButton']")

    def plus_btn(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='plusButton']")

    def minus_btn(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='minusButton']")

    def mult_btn(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='multiplyButton']")

    def divide_btn(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='divideButton']")

    def clear_btn(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='clearButton']")

    def get_calc_result(self):
        return self.driver.find_element_by_xpath(
            "//*[@AutomationId='CalculatorResults']"
        )
