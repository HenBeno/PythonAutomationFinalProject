class Edit_Section_OP:

    def __init__(self, driver):
        self.driver = driver

    def settings_btn(self):
        return self.driver.find_element_by_xpath( "//*[@contentDescription='נווט למעלה']")

    def edit_btn(self):
        return  self.driver.find_element_by_xpath("(//*[@class='android.widget.ListView']/*[@text])[2]")

    def first_item(self):
        return self.driver.find_element_by_xpath("(//*[@id='list']/*[./*[@id='icon']])[1]")

    def second_item(self):
        return self.driver.find_element_by_xpath("(//*[@id='list']/*[./*[@id='icon']])[2]")

    def listView_items(self):
        return self.driver.find_elements_by_xpath("(//*[@id='mainGrid']/*[./*[@id='icon']])")

    def goBack(self):
        return self.driver.back()












