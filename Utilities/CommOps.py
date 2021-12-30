import xml.etree.ElementTree as ET
from datetime import datetime

import allure

from Test_Cases import conftest


@allure.step("get data")
def get_data(date_type, node_name):
    if date_type == "test":
        root = ET.parse("../Configurations/TestData.xml").getroot()
    elif date_type == "conf":
        root = ET.parse("../Configurations/Config.xml").getroot()
    else:
        raise TypeError("Wrong input, unrecognized date type: ", date_type)
    return root.find(".//" + node_name).text


def attach_screenshot():
    now = datetime.now()
    image_name = "screen_" + now.strftime("%d-%b-%Y_%H%M%p")
    image = "../Screenshot/" + image_name + ".png"
    conftest.driver.get_screenshot_as_file(image)
    allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
