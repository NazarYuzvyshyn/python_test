from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait

from main.custom_utils.general_utils import press_key
from main.custom_utils.wait_utils import wait_element_enable
from .custom_logger import *
from .web_driver_factory import WebDriverFactory


def click_on(name, by_what: By, locator):
    try:
        wait = WebDriverWait(WebDriverFactory.driver(), 5)
        wait.until(element_to_be_clickable(locator))
        get_element(by_what, locator).click()
        info("Click on %s  %s" % (name, locator))
    except TimeoutException:
        error("Element %s  %s  isn't clickable" % (name, locator))
        assert 0


def input_keys(elem_name, by_what: By, locator, text):
    wait_element_enable(elem_name, by_what, locator, 15)
    get_element(by_what, locator).send_keys(text)
    info("Input %s into %s" % (text, elem_name))


def input_keys_with_enter(elem_name, by_what: By, locator, text):
    input_keys(elem_name, by_what, locator, text)
    press_key(Keys.ENTER)
    info("Send key: ENTER")


def get_element(by_what: By, locator):
    return WebDriverFactory.driver().find_element(by_what, locator)


def get_elements(by_what: By, locator) -> list:
    return WebDriverFactory.driver().find_elements(by_what, locator)


def element_text_content(element):
    text = element.get_attribute('textContent')
    return text
