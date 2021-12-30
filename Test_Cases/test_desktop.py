from Test_Cases.conftest import *
from Utilities.CommOps import get_data
from Work_Flows.Desktop.Calculations_WF import calculations_wf


@pytest.mark.usefixtures("init_desktop")
class Test_Desktop:

    @allure.title("verify add function")
    def test_01_verify_addition(self):
        assert calculations_wf.calc_wf(get_data("test", "Clac_Plus")) == get_data("test", "expected_Clac_Plus")

    @allure.title("verify add function")
    def test_02_verify_minus(self):
        assert calculations_wf.calc_wf(get_data("test", "Clac_Minus")) == get_data("test", "expected_Clac_Minus")

    @allure.title("verify add function")
    def test_03_verify_mult(self):
        assert calculations_wf.calc_wf(get_data("test", "Clac_Mult")) == get_data("test", "expected_Clac_Mult")

    @allure.title("verify add function")
    def test_04_verify_dev(self):
        assert calculations_wf.calc_wf(get_data("test", "Clac_Dev")) == get_data("test", "expected_Clac_Dev")

    # @allure.title("verify add function")
    # def test_01_verify_addition(self):
    #     assert calculations_wf.addition() == get_data("test", "expected_add")
    #
    # @allure.title("verify minus function")
    # def test_02_verify_minus(self):
    #     assert calculations_wf.minus() == get_data("test", "expected_minus")
    #
    # @allure.title("verify mult function")
    # def test_03_verify_mult(self):
    #     assert calculations_wf.mult() == get_data("test", "expected_mult")
