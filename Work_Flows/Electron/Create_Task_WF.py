from selenium.webdriver.common.keys import Keys
from smart_assertions import soft_assert

import Utilities
from extension.Ui_Action import ui_action
from Utilities.Manage_Pages import Page_Manager


class create_task:

    @staticmethod
    def create_task_wf():
        for i in range(3):
            color = "red"
            task_name = "Task" + str(i)
            create_task.pick_color(color)
            create_task.create_task_by_name(task_name)
            create_task.insert_task()
            soft_assert(create_task.verify_creation(task_name), "Fail To create task" + str(i))

    @staticmethod
    def pick_color(color):
        ui_action.click(Utilities.Manage_Pages.Electron_PO.openColorsList())
        ui_action.click(Utilities.Manage_Pages.Electron_PO.taskColorsList()[create_task.color_to_num(color.lower())])

    @staticmethod
    def create_task_by_name(task_name):
        ui_action.send_key(Utilities.Manage_Pages.Electron_PO.taskField(), task_name)

    @staticmethod
    def insert_task():
        ui_action.click(Utilities.Manage_Pages.Electron_PO.taskField())
        Utilities.Manage_Pages.Electron_PO.taskField().send_keys(Keys.RETURN)

    @staticmethod
    def verify_creation(task_name):
        for name in Utilities.Manage_Pages.Electron_PO.taskText():
            if name.text == task_name:
                return True
        return False

    @staticmethod
    def color_to_num(color):
        match color:
            case 'red':
                return 1
            case 'orange':
                return 2
            case 'yellow':
                return 3
            case 'green':
                return 4
            case 'blue':
                return 5
            case 'purple':
                return 6
            case 'gray':
                return 7
            case _:
                return 0
