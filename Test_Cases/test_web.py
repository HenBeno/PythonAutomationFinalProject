from smart_assertions import verify_expectations

from Test_Cases.conftest import *
from Utilities.Read_Properties import get_data
from Work_Flows.Web.Create_User_WF import create_user_wf
from Work_Flows.Web.Login_Using_DB_WF import login_use_database_wf
from Work_Flows.Web.Login_Using_XML_WF import login_xml_wf
from Work_Flows.Web.Make_Transfer_WF import make_transfer_wf


@pytest.mark.usefixtures("init_web")
class Test_Web:

    @allure.title("Reporting System Test")
    @allure.description("This tests create new user and verify creation of user")
    def test_01_verify_create_new_user(self):
        self.driver.get(get_data("Url"))
        assert create_user_wf.create_user() == get_data("RealWorldApp_user_name_txt")

    @allure.description("This tests create new transfer and verify")
    def test_02_verify_transfer_by_name(self):
        self.driver.get(get_data("Url"))
        assert make_transfer_wf.transfer_money_wf("Edgar Johns", get_data("AmountToTransfer"),
                                                  get_data("NoteToTransfer")) == "Paid $" + \
               get_data("AmountToTransfer") + ".00 for " + get_data("NoteToTransfer")

    @allure.description("This tests create new transfer request and verify")
    def test_03_verify_transfer_req_by_name(self):
        self.driver.get(get_data("Url"))
        assert make_transfer_wf.req_transfer_money_wf("Edgar Johns", get_data("AmountToTransfer"),
                                                      get_data("NoteToTransfer")) == "Requested $" + \
               get_data("AmountToTransfer") + ".00 for " + get_data("NoteToTransfer")

    @allure.description("This tests login using login details from DDT (XML)")
    def test_04_verify_transfer_req_by_name(self):
        self.driver.get(get_data("Url"))
        login_xml_wf.login_and_verify_from_xml()
        verify_expectations()

    @allure.description("This tests login using login details from DB")
    def test_04_verify_transfer_req_by_name(self):
        login_use_database_wf.log_in_db()
        verify_expectations()
