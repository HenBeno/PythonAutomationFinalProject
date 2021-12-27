import allure

from Test_Cases.conftest import *
from Utilities.Read_Properties import get_data
from Work_Flows.Desktop.Calculations_WF import calculations_wf


@pytest.mark.usefixtures("init_desktop")
class Test_Desktop:

    @allure.title("verify add function")
    def test_01_verify_addition(self):
        # print(calculations_wf.addition(self.driver))
        assert calculations_wf.addition(self.driver) == get_data("expected_add")
    @allure.title("verify minus function")
    def test_02_verify_minus(self):
        assert calculations_wf.minus(self.driver) == get_data("expected_minus")
    @allure.title("verify mult function")
    def test_03_verify_mult(self):
        assert calculations_wf.mult(self.driver) == get_data("expected_mult")

