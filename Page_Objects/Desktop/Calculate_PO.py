class Calculate_Page:

    def __init__(self, driver):
        self.driver = driver

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

    def equal_btn(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='equalButton']")

    def plus_btn(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='plusButton']")

    def minus_btn(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='minusButton']")

    def mult_btn(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='multiplyButton']")

    def result(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='CalculatorResults']")
