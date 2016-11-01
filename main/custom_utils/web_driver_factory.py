import platform

from main.custom_utils.constants import DRIVER_PATH
from ..custom_utils.custom_logger import log

from selenium import webdriver


class WebDriverFactory:
    driver = None
    def chrome_settings(self, os_name):
        binary_path = ""
        if os_name.__eq__("Windows"):
            binary_path = DRIVER_PATH + 'chrome\\chromedriver.exe'
        if os_name.__eq__("Linux"):
            binary_path = DRIVER_PATH + 'chrome\\chromedriver'
        return binary_path

    def set_driver(self, browser):
        if browser.__eq__("firefox"):
            log().info("Set Firefox driver")
            self.driver = webdriver.Firefox()
        if browser.__eq__("chrome"):
            path = self.chrome_settings(platform.system())
            self.driver = webdriver.Chrome(executable_path=path)
            log().info("Set Chrome driver")

    def kill_driver(self):
        if self.driver is not None:
            self.driver.quit()
            log().info("Driver has been killed")
