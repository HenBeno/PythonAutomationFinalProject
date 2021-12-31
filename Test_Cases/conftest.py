import os

import allure
import pytest
from applitools.selenium import Eyes
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Utilities.Listeners import EventListener
from Utilities.Manage_Pages import Page_Manager
from Utilities.CommOps import get_data

driver = None
action = None
eyes = Eyes()


@allure.step("init web driver")
@pytest.fixture(scope="class")
def init_web(request):
    browser_type = os.getenv("Browser")
    if "chrome" == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_type == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif browser_type == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise TypeError("Wrong input, unrecognized browser")

    # driver = EventFiringWebDriver(edriver, EventListener())
    driver.maximize_window()
    driver.implicitly_wait(4)
    driver.get(get_data("conf", "Url"))

    globals()["driver"] = driver

    request.cls.driver = driver
    Page_Manager.init_web_page(driver)

    yield
    driver.quit()


def open_eye():
    eyes.api_key = get_data("conf", "api_key")
    eyes.open(
        driver, get_data("test", "eyes_header"), get_data("test", "eyes_test_name")
    )


@allure.step("init Desktop driver")
@pytest.fixture(scope="class")
def init_desktop(request):
    desired_caps = {}
    desired_caps["app"] = get_data("conf", "desired_caps")
    desired_caps["platformName"] = get_data("conf", "platformName")
    desired_caps["deviceName"] = get_data("conf", "deviceName")
    driver = webdriver.Remote(get_data("conf", "server"), desired_caps)
    driver.implicitly_wait(4)
    globals()["driver"] = driver
    request.cls.driver = driver
    Page_Manager.init_desktop_page(driver)
    yield
    driver.quit()


@allure.step("init electron driver")
@pytest.fixture(scope="class")
def init_electron(request):
    electron_app = get_data("conf", "electron_app_path")
    edriver = get_data("conf", "electron_driver")
    options = webdriver.ChromeOptions()
    options.binary_location = electron_app
    driver = webdriver.Chrome(chrome_options=options, executable_path=edriver)
    driver.implicitly_wait(4)
    globals()["driver"] = driver
    request.cls.driver = driver
    Page_Manager.init_electron_page(driver)
    yield
    driver.quit()


@allure.step("init appium driver")
@pytest.fixture(scope="class")
def init_appium(request):
    dc = {}
    dc["reportDirectory"] = get_data("conf", "reportDirectory")
    dc["reportFormat"] = get_data("conf", "reportFormat")
    dc["testName"] = get_data("conf", "testName")
    dc["udid"] = get_data("conf", "udid")
    dc["appPackage"] = get_data("conf", "appPackage")
    dc["appActivity"] = get_data("conf", "appActivity")
    dc["platformName"] = get_data("conf", "platformNameAppium")
    driver = webdriver.Remote(get_data("conf", "server_appium"), dc)
    globals()["driver"] = driver
    request.cls.driver = driver
    Page_Manager.init_android(driver)
    yield
    driver.quit()


@allure.step("init api")
@pytest.fixture(scope="class")
def init_api(request):
    url = get_data("conf", "base_url")
    globals()["url"] = url
    request.cls.url = url
