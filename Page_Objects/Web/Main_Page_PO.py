class Main_Page:

    def __init__(self, driver):
        self.driver = driver

    def new_transaction_btn(self):
        return self.driver.find_element_by_xpath("//a[@data-test='nav-top-new-transaction']")

    def all_user_names(self):
        return self.driver.find_elements_by_xpath("//ul[@data-test='users-list']/li/div[2]/span")

    def amount_to_transfer(self):
        return self.driver.find_element_by_id("amount")

    def note_to_transfer_txt(self):
        return self.driver.find_element_by_xpath("//input[@placeholder='Add a note']")

    def make_transfer_btn(self):
        return self.driver.find_element_by_xpath("//button[@data-test='transaction-create-submit-payment']")

    def ask_transfer_btn(self):
        return self.driver.find_element_by_xpath("//button[@data-test='transaction-create-submit-request']")

    def verify_transfer(self):
        return self.driver.find_element_by_xpath("//div[@class='MuiGrid-root MuiGrid-item'][1]/h2")

    def search_box_txt(self):
        return self.driver.find_element_by_id("user-list-search-input")
