from Page_Objects.Electron.Electron_PO import Electron_Page
from extension.Ui_Action import ui_action


class electron_change_task_color:

    @staticmethod
    def change_task_color(hex_color):
        electron_change_task_color.click_pick_color_btn()
        electron_change_task_color.insert_hex_color(hex_color)
        return electron_change_task_color.verify_color()

    @staticmethod
    def click_pick_color_btn():
        ui_action.click_on_elem(Electron_Page.colorPicker())

    @staticmethod
    def insert_hex_color(hex_color):
        ui_action.send_key_to_elem(Electron_Page.colorPicker_text(), hex_color)


    @staticmethod
    def verify_color():
        return Electron_Page.verifyHeaderColor().get_attribute("style")