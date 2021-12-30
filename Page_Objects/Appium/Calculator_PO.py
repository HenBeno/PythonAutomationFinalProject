class Calculator:
    def __init__(self, driver):
        self.driver = driver

    def enter_to_calculator(self):
        return self.driver.find_element_by_xpath(
            "(//*[@id='mainGrid']/*/*[@id='icon'])[8]"
        )

    def num_9(self):
        return self.driver.find_element_by_xpath("//*[@id='digit_9']")

    def num_5(self):
        return self.driver.find_element_by_xpath("//*[@id='digit_5']")

    def num_3(self):
        return self.driver.find_element_by_xpath("//*[@id='digit_3']")

    def num_7(self):
        return self.driver.find_element_by_xpath("//*[@id='digit_7']")

    def op_mul(self):
        return self.driver.find_element_by_xpath("//*[@id='op_mul']")

    def op_sub(self):
        return self.driver.find_element_by_xpath("//*[@id='op_sub']")

    def op_add(self):
        return self.driver.find_element_by_xpath("//*[@id='op_add']")

    def result(self):
        return self.driver.find_element_by_xpath("//*[@id='result']")
