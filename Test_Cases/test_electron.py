import allure
import pytest
from smart_assertions import soft_assert, verify_expectations

from Utilities.CommOps import get_data
from Work_Flows.Electron.Change_task_color_WF import electron_change_task_color
from Work_Flows.Electron.Create_Task_WF import create_task


@pytest.mark.usefixtures("init_electron")
class Test_Electron:
    @allure.title("")
    @allure.description("Verify change of color")
    def test_01_verify_change_of_color(self):
        assert electron_change_task_color.change_task_color(
            get_data("test", "HexColor")
        ) == get_data("test", "ExpectedHexColor")

    @allure.description("Verify change of color")
    def test_02_create_new_task(self):
        for i in range(3):
            soft_assert(
                create_task.create_task_wf("Task" + str(i), "red"),
                "Fail To create task" + str(i),
            )
        verify_expectations()
