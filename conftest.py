import platform

import pytest
from selenium import webdriver

from main.custom_utils.constants import DRIVER_PATH
from main.custom_utils.custom_logger import log
from main.custom_utils.web_driver_factory import WebDriverFactory


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="browser type")


@pytest.fixture()
def get_brows(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="function")
def web_driver(request, get_brows):
    name = request.module.__name__[0:-5]
    log().info("=============== " + name + " STARTED ==================")

    driver = None
    if get_brows.__eq__("firefox"):
        log().info("Set Firefox driver")
        driver = webdriver.Firefox()
    if get_brows.__eq__("chrome"):
        path = chrome_settings(platform.system())
        driver = webdriver.Chrome(executable_path=path)
        log().info("Set Chrome driver")

    yield web_driver
    if driver is not None:
        driver.quit()
        log().info("Driver has been killed")
        log().info("=============== " + name + " FINISHED ==================")
    return driver


def chrome_settings(os_name):
    binary_path = ""
    if os_name.__eq__("Windows"):
        binary_path = DRIVER_PATH + 'chrome\\chromedriver.exe'
    if os_name.__eq__("Linux"):
        binary_path = DRIVER_PATH + 'chrome\\chromedriver'
    return binary_path
