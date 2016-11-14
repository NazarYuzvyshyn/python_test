import platform
import threading

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from main.custom_utils.constants import DRIVER_PATH
from ..custom_utils.custom_logger import log


class WebDriverFactory:
    thLoc = threading.local()
    thLoc.__driver = None

    @staticmethod
    def driver():
        return WebDriverFactory.thLoc.__driver

    @staticmethod
    def chrome_settings(os_name):
        binary_path = ""
        if os_name.__eq__("Windows"):
            binary_path = DRIVER_PATH + 'chrome/chromedriver.exe'
        if os_name.__eq__("Linux"):
            binary_path = DRIVER_PATH + 'chrome/chromedriver'
        return binary_path

    @staticmethod
    def set_driver(browser):
        if WebDriverFactory.thLoc.__driver is None:
            if browser.__eq__("ff"):
                log().info("Set Firefox driver")
                WebDriverFactory.thLoc.__driver = webdriver.Firefox()
            if browser.__eq__("chrome"):
                path = WebDriverFactory.chrome_settings(platform.system())
                WebDriverFactory.thLoc.__driver = webdriver.Chrome(executable_path=path)
                log().info("Set Chrome driver")
                WebDriverFactory.thLoc.__driver.maximize_window()
        else:
            log().warn("WebDriver is initialized! : " + str(WebDriverFactory.thLoc.__driver))
            raise WebDriverException

    @staticmethod
    def kill_driver():
        if WebDriverFactory.thLoc.__driver is not None:
            WebDriverFactory.thLoc.__driver.quit()
            log().info("Driver has been killed")
