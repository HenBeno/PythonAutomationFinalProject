class Create_User_Page:

    def __init__(self, driver):
        self.driver = driver

    def create_user_btn(self):
        return self.driver.find_element_by_xpath("//a[@href='/signup']")

    def first_name_txt(self):
        return self.driver.find_element_by_id("firstName")

    def last_name_txt(self):
        return self.driver.find_element_by_id("lastName")

    def user_name_txt(self):
        return self.driver.find_element_by_id("username")

    def password_txt(self):
        return self.driver.find_element_by_id("password")

    def password_conf_txt(self):
        return self.driver.find_element_by_id("confirmPassword")

    def submit_btn(self):
        return self.driver.find_element_by_css_selector("span.MuiButton-label")

    def next_after_login_btn(self):
        return self.driver.find_element_by_xpath("//button[@data-test='user-onboarding-next']/span")

    def bank_name_txt(self):
        return self.driver.find_element_by_id("bankaccount-bankName-input")

    def routing_number_txt(self):
        return self.driver.find_element_by_id("bankaccount-routingNumber-input")

    def bank_account_number_txt(self):
        return self.driver.find_element_by_id("bankaccount-accountNumber-input")

    def save_info_btn(self):
        return self.driver.find_element_by_xpath("//button[@data-test='bankaccount-submit']")

    def present_user_name(self):
        return self.driver.find_element_by_xpath("//h6[@data-test='sidenav-username']")