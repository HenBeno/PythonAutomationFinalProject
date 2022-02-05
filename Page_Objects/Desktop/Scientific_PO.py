class Scientific_Page:
    def __init__(self, driver):
        self.driver = driver

    def power_button_btn(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='powerButton']")

    def open_parenthesis(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='openParenthesisButton']")

    def close_parenthesis(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='closeParenthesisButton']")

    def clear_after_entry_btn(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='clearEntryButton']")
