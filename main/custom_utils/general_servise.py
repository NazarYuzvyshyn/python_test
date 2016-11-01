from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from main.base_class import BaseClass
from .custom_logger import log


class GeneralService(BaseClass):

    def wait_page_load(self):
        """ Wait until page is entire loaded """
        try:
            wait = WebDriverWait(self.driver, 30)
            wait.until(self.driver.execute_script("return document.readyState").__eq__("complete"))
        except TimeoutException:
            log().error("Timeout exception on page load")

    def get_url(self, url):
        """ Use module constants.py to make full url """
        self.driver.get(url)
        log().info("Go to " + url)

    def lines_from_file(self, path):
        file = open(path)
        lines = file.readlines()
        file.close()
        return lines
