import Utilities
from Test_Cases.conftest import *
from Utilities.Manage_Pages import Page_Manager
from Work_Flows.Android.Calculator_Calc_WF import Calculator_calc
from Work_Flows.Android.Listview_Edit_WF import listview_edit


@pytest.mark.usefixtures("init_appium")
class Test_appium:
    @allure.title("Reporting System Test")
    @allure.description("Android")
    def test_test01_testing_calculator(self):
        Calculator_calc.calc_test()
        res = Utilities.Manage_Pages.Calculator_PO.result().text
        assert res == "49"

    @allure.title("Reporting System Test")
    @allure.description("listview_edit")
    def test_test01_listview_edit(self):
        listview_edit.listview_edit()
        res = Utilities.Manage_Pages.Edit_Section_PO.listView_items()
        assert len(res) == 16
