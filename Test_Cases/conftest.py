import os

import allure
import pytest
from applitools.selenium import Eyes
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Utilities.Manage_Pages import Page_Manager
from Utilities.Read_Properties import get_data

driver = None
action = None
eyes = Eyes()


@allure.step("init web driver")
@pytest.fixture(scope='class')
def init_web(request):
    browser_type = os.getenv("Browser")
    if browser_type == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_type == "edge":
        edriver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif browser_type == "firefox":
        edriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        driver = None
        print("Wrong input, unrecognized browser")
    # driver = EventFiringWebDriver(edriver, EventListener())
    driver.maximize_window()
    driver.implicitly_wait(4)

    globals()['driver'] = driver

    request.cls.driver = driver
    Page_Manager.init_web_page(driver)

    yield
    driver.quit()


def open_eye():
    eyes.api_key = 'fvJvl7ElSUjzARieAXzLB1035bsvifVMfka3PzDiUXrcM110'
    eyes.open(driver, "Test App Graphic", "Check if bank account change")


@allure.step("init Desktop driver")
@pytest.fixture(scope='class')
def init_desktop(request):
    desired_caps = {}
    desired_caps["app"] = get_data("desired_caps")
    desired_caps["platformName"] = get_data("platformName")
    desired_caps["deviceName"] = get_data("deviceName")
    driver = webdriver.Remote(get_data("server"), desired_caps)
    driver.implicitly_wait(4)
    globals()['driver'] = driver
    request.cls.driver = driver
    Page_Manager.init_desktop_page(driver)
    yield
    driver.quit()


@allure.step("init electron driver")
@pytest.fixture(scope='class')
def init_electron(request):
    electron_app = get_data("electron_app_path")
    edriver = get_data("electron_driver")
    options = webdriver.ChromeOptions()
    options.binary_location = electron_app
    driver = webdriver.Chrome(chrome_options=options, executable_path=edriver)
    driver.implicitly_wait(4)
    globals()['driver'] = driver
    request.cls.driver = driver
    Page_Manager.init_electron_page(driver)
    yield
    driver.quit()


@allure.step("init appium driver")
@pytest.fixture(scope='class')
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
    globals()['driver'] = driver
    request.cls.driver = driver
    Page_Manager.init_android(driver)
    yield
    driver.quit()


@allure.step("init api")
@pytest.fixture(scope='class')
def init_api(request):
    url = get_data("base_url")
    globals()['url'] = url
    request.cls.url = url
