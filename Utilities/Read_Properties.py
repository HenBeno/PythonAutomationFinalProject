import xml.etree.ElementTree as ET

import allure


@allure.step("get data")
def get_data(node_name):
    root = ET.parse(r'C:\Users\ebrah\PycharmProjects\PythonAutomationFinalProject\Configurations\config.xml').getroot()
    return root.find(".//" + node_name).text
