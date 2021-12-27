import allure
from smart_assertions import soft_assert

from Utilities import XLUtils
from Utilities.Read_Properties import get_data
from Work_Flows.Web.Login_WF import login_wf


class login_xml_wf:
    global path
    path = get_data("XMLPath")

    @staticmethod
    @allure.step("login_and_verify_from_xml")
    def login_and_verify_from_xml():
        login_xml_wf.send_login_details()
        return login_xml_wf.check_results()

    @staticmethod
    @allure.step("send_login_details")
    def send_login_details():
        for i in range(2, XLUtils.getRowCount(path, 'Sheet1') + 1):
            if login_wf.login_and_verify(XLUtils.readData(path, 'Sheet1', i, 1),
                                         XLUtils.readData(path, 'Sheet1', i, 2)) == XLUtils.readData(path, 'Sheet1', i,
                                                                                                     3):
                XLUtils.writeData(path, 'Sheet1', i, 4, "Pass")
            else:
                XLUtils.writeData(path, 'Sheet1', i, 4, "Fail")

    @staticmethod
    @allure.step("check_results")
    def check_results():

        for i in range(2, XLUtils.getRowCount(path, 'Sheet1') + 1):
            soft_assert((XLUtils.readData(path, 'Sheet1', i, 4) == "Pass"), ("Fail! login details: " +
                                                                              XLUtils.readData(path, 'Sheet1', i, 1) +
                                                                              " " + XLUtils.readData(path, 'Sheet1', i,
                                                                                                     2)))
