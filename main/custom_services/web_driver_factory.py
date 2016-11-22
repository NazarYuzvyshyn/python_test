import os
import platform
import threading

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from main.custom_services.custom_logger import *


class WebDriverFactory:
    thLoc = threading.local()
    thLoc.__driver = None

    @staticmethod
    def driver():
        return WebDriverFactory.thLoc.__driver

    @staticmethod
    def chrome_settings(os_name):
        binary_path = ""
        directory = os.path.dirname(__file__)
        file = directory + '/drivers/chrome/'
        if os_name.__eq__("Windows"):
            binary_path = file + 'chromedriver.exe'
        if os_name.__eq__("Linux"):
            binary_path = file + 'chromedriver'
        return binary_path

    @staticmethod
    def set_driver(browser):
        if WebDriverFactory.thLoc.__driver is None:
            if browser.__eq__("ff"):
                WebDriverFactory.thLoc.__driver = webdriver.Firefox()
                info("Set Firefox driver")
            if browser.__eq__("chrome"):
                path = WebDriverFactory.chrome_settings(platform.system())
                WebDriverFactory.thLoc.__driver = webdriver.Chrome(executable_path=path)
                info("Set Chrome driver")
                WebDriverFactory.thLoc.__driver.maximize_window()
        else:
            error("WebDriver is initialized! : " + str(WebDriverFactory.thLoc.__driver))
            raise WebDriverException

    @staticmethod
    def kill_driver():
        if WebDriverFactory.thLoc.__driver is not None:
            WebDriverFactory.thLoc.__driver.quit()
            WebDriverFactory.thLoc.__driver = None
            info("Driver has been killed")
