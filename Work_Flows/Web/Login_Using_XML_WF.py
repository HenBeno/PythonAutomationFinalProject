import Utilities
from Utilities import XLUtils
from Utilities.Manage_Pages import Page_Manager
from Utilities.Read_Properties import get_data
from Work_Flows.Web.Login_WF import login_wf
from Work_Flows.Web.Logout_WF import logout_wf
from extension.Ui_Action import ui_action
from smart_assertions import soft_assert, verify_expectations


class login_xml_wf:
    global path
    path = get_data("XMLPath")

    @staticmethod
    def login_and_verify_from_xml():
        login_xml_wf.send_login_details()
        return login_xml_wf.check_results()

    @staticmethod
    def send_login_details():
        for i in range(2, XLUtils.getRowCount(path, 'Sheet1') + 1):
            if login_wf.login_and_verify(XLUtils.readData(path, 'Sheet1', i, 1),
                                         XLUtils.readData(path, 'Sheet1', i, 2)) == XLUtils.readData(path, 'Sheet1', i,
                                                                                                     3):
                XLUtils.writeData(path, 'Sheet1', i, 4, "Pass")
            else:
                XLUtils.writeData(path, 'Sheet1', i, 4, "Fail")

    @staticmethod
    def check_results():

        for i in range(2, XLUtils.getRowCount(path, 'Sheet1') + 1):
            soft_assert((XLUtils.readData(path, 'Sheet1', i, 4) == "Pass"), ("Fail! login details: " +
                                                                              XLUtils.readData(path, 'Sheet1', i, 1) +
                                                                              " " + XLUtils.readData(path, 'Sheet1', i,
                                                                                                     2)))
