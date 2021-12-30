from Page_Objects.Appium.Calculator_PO import Calculator
from Page_Objects.Appium.Edit_Section_PO import Edit_Section_OP
from Page_Objects.Desktop.Calculate_PO import Calculate_Page
from Page_Objects.Electron.Electron_PO import Electron_Page
from Page_Objects.Web.Create_User_PO import Create_User_Page
from Page_Objects.Web.Left_Bar_PO import Left_Bar_Page
from Page_Objects.Web.Login_PO import Login
from Page_Objects.Web.Main_Page_PO import Main_Page

# Web
Create_User_PO = None
Login_PO = None
Main_Page_PO = None
Left_Bar_PO = None

# Android
Calculator_PO = None
Edit_Section_PO = None

# Desktop
Calculate_PO = None

# Electron
Electron_PO = None


class Page_Manager:
    def init_web_page(driver):
        globals()["Create_User_PO"] = Create_User_Page(driver)
        globals()["Login_PO"] = Login(driver)
        globals()["Main_Page_PO"] = Main_Page(driver)
        globals()["Left_Bar_PO"] = Left_Bar_Page(driver)

    def init_android(driver):
        globals()["Calculator_PO"] = Calculator(driver)
        globals()["Edit_Section_PO"] = Edit_Section_OP(driver)

    def init_desktop_page(driver):
        globals()["Calculate_PO"] = Calculate_Page(driver)

    def init_electron_page(driver):
        globals()["Electron_PO"] = Electron_Page(driver)
