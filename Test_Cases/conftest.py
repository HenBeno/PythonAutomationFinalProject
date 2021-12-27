import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import Utilities
from Utilities.Manage_Pages import Page_Manager
from Utilities.Read_Properties import get_data
from Work_Flows.Web.Login_WF import login_wf
from extension.Ui_Action import ui_action

driver = None
action = None

@pytest.fixture(scope='class')
@allure.step("init web driver")
def init_web(request):
    if get_data("Browser") == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif get_data("Browser") == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif get_data("Browser") == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver = None
        print("Wrong input, unrecognized browser")
    driver.maximize_window()
    driver.implicitly_wait(4)

    globals()['driver'] = driver
    request.cls.driver = driver
    Page_Manager.init_web_page(driver)

    yield
    driver.quit()


@pytest.fixture(scope='class')
@allure.step("init Desktop driver")
def init_desktop(request):
    desired_caps = {}
    desired_caps["app"] = get_data("desired_caps")
    desired_caps["platformName"] = get_data("Windows")
    desired_caps["deviceName"] = get_data("WindowsPC")
    driver = webdriver.Remote(get_data("server"), desired_caps)
    driver.implicitly_wait(4)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope='class')
@allure.step("init electron driver")
def init_electron(request):
    electron_app = get_data("electron_app_path")
    edriver = get_data("electron_driver")
    options = webdriver.ChromeOptions()
    options.binary_location = electron_app
    driver = webdriver.Chrome(chrome_options=options, executable_path=edriver)
    driver.implicitly_wait(4)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope='class')
@allure.step("init appium driver")
def init_appium(request):
    dc = {}
    dc['reportDirectory'] = get_data("reportDirectory")
    dc['reportFormat'] = get_data("reportFormat")
    dc['testName'] = get_data("testName")
    dc['udid'] = get_data("udid")
    dc['appPackage'] = get_data("appPackage")
    dc['appActivity'] = get_data("appActivity")
    dc['platformName'] = get_data("platformName")
    driver = webdriver.Remote(get_data("server_appium"), dc)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope='class')
@allure.step("init api")
def init_api(request):
    url = get_data("base_url")
    globals()['url'] = url
    request.cls.url = url
