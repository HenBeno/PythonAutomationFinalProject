class Left_Bar_Page:

    def __init__(self, driver):
        self.driver = driver

    def logout_btn(self):
        return self.driver.find_element_by_xpath("//div[@data-test='sidenav-signout']")
