class Electron_Page:
    def __init__(self, driver):
        self.driver = driver

    def colorPicker(self):
        return self.driver.find_element_by_xpath(
            "//div[@class='icons_MDNeU']/*[name()='svg'][1]"
        )

    def colorPicker_text(self):
        return self.driver.find_element_by_xpath("//input[@class='vc-input__input'][1]")

    def verifyHeaderColor(self):
        return self.driver.find_element_by_tagname("header")

    def taskField(self):
        return self.driver.find_element_by_xpath(
            "//input[@placeholder='Create a task']"
        )

    def deleteTask(self):
        return self.driver.find_elements_by_xpath(
            "//div[@class='view_2Ow90']/*[name()='svg']"
        )

    def taskText(self):
        return self.driver.find_elements_by_xpath(
            "//div[@class='textWrapper_X9gil']/label"
        )

    def openColorsList(self):
        return self.driver.find_element_by_xpath(
            "//div[@class='topWrapper_2caNE']/*[name()='svg']"
        )

    def listOfCreatedTask(self):
        return self.driver.find_elements_by_xpath("//div[@class='view_2Ow90']/span")

    def taskColorsList(self):
        return self.driver.find_elements_by_xpath(
            "//div[@class='wrapper_3Kpfj vertical_di1oV tagList_2NRe0']/span"
        )
