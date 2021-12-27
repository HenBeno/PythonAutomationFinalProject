class Login:

    def __init__(self, driver):
        self.driver = driver

    def user_name_txt(self):
        return self.driver.find_element_by_id("username")

    def password_txt(self):
        return self.driver.find_element_by_id("password")

    def login_btn(self):
        return self.driver.find_element_by_css_selector("span.MuiButton-label")
