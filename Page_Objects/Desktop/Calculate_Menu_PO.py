class Calculate_Menu_Page:
    def __init__(self, driver):
        self.driver = driver

    def toggle_panel_btn(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='TogglePaneButton']")

    def standard_calculator(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='Standard']")

    def scientific_calculator(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='Scientific']")

    def currency_calculator(self):
        return self.driver.find_element_by_xpath("//*[@AutomationId='Currency']")
