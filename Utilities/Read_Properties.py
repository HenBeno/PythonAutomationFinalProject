import xml.etree.ElementTree as ET

import allure


@allure.step("get data")
def get_data(node_name):
    root = ET.parse('.\\Configuration\config.xml').getroot()
    return root.find(".//" + node_name).text
