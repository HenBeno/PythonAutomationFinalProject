from time import sleep

import Utilities
from Utilities.Manage_Pages import Page_Manager
from extension.Ui_Action import ui_action


class electron_change_task_color:
    @staticmethod
    def change_task_color(hex_color):
        electron_change_task_color.click_pick_color_btn()
        electron_change_task_color.insert_hex_color(hex_color)
        return electron_change_task_color.verify_color()

    @staticmethod
    def click_pick_color_btn():
        ui_action.click(Utilities.Manage_Pages.Electron_PO.colorPicker())

    @staticmethod
    def insert_hex_color(hex_color):
        ui_action.clear_key(
            Utilities.Manage_Pages.Electron_PO.colorPicker_text()
        )
        ui_action.send_key(
            Utilities.Manage_Pages.Electron_PO.colorPicker_text(), hex_color
        )

    @staticmethod
    def verify_color():
        return Utilities.Manage_Pages.Electron_PO.verifyHeaderColor().get_attribute(
            "style"
        )
