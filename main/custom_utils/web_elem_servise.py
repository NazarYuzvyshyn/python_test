from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait

from main.custom_utils.general_servise import GeneralService
from .custom_logger import log


class WebelementService(GeneralService):

    def click_on(self, xpath):
        try:
            wait = WebDriverWait(self.driver, 15)
            wait.until(element_to_be_clickable((By.XPATH, xpath)))
            self.get_element(xpath).click()
            log().info("Click on " + xpath)
        except TimeoutException:
            log().error(xpath + " isn't clickable")


    def input_keys(self, text, xpath):
        """ Sent some text into input field """
        try:
            wait = WebDriverWait(self.driver, 15)
            wait.until(self.driver.find_element_by_xpath(xpath).is_enabled())
            self.get_element(xpath).send_keys(text)
            log().info("Input '" + text + "' into " + xpath)
        except TimeoutException:
            log().error(xpath + " isn't clickable")


    def get_element(self, xpath):
        return self.driver.find_element_by_xpath(xpath)
