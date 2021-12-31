import allure
import pytest
from smart_assertions import soft_assert, verify_expectations

from Utilities.CommOps import get_data
from Work_Flows.Electron.Change_task_color_WF import electron_change_task_color
from Work_Flows.Electron.Create_Task_WF import create_task


@pytest.mark.usefixtures("init_electron")
class Test_Electron:
    @allure.title("Electron Tests")
    @allure.description("Verify change of color")
    def test_01_verify_change_of_color(self):
        assert electron_change_task_color.change_task_color(
            get_data("test", "HexColor")
        ) == get_data("test", "ExpectedHexColor")

    @allure.description("Verify create of 3 tasks")
    def test_02_create_new_task(self):
        create_task.create_task_wf(),
        verify_expectations()
