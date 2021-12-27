import xml.etree.ElementTree as ET


def get_data(node_name):
    root = ET.parse('C:\Automation\python\pythonProject\\final_project_python\Configurations\config.xml').getroot()
    return root.find(".//" + node_name).text
