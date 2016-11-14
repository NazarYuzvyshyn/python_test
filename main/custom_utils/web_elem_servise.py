import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait

from .custom_logger import log
from .web_driver_factory import WebDriverFactory


def click_on(xpath):
    try:
        wait = WebDriverWait(WebDriverFactory.driver(), 5)
        wait.until(element_to_be_clickable((By.XPATH, xpath)))
        get_element(xpath).click()
        log().info("Click on " + xpath)
    except TimeoutException:
        log().error(xpath + " isn't clickable")
        assert 0


def input_keys(text, xpath):
    """ Sent some text into input field """
    try:
        wait = WebDriverWait(WebDriverFactory.driver(), 25)
        wait.until(presence_of_element_located((By.XPATH, xpath)))
        is_element_enable(xpath, 15)
        get_element(xpath).send_keys(text)
        log().info("Input '" + text + "' into " + xpath)
    except TimeoutException:
        log().error(xpath + " isn't clickable")


def get_element(xpath):
    return WebDriverFactory.driver().find_element_by_xpath(xpath)


def is_element_enable(xpath, timeout):
    t = time.time() + timeout
    while time.time() < t:
        elem = get_element(xpath)
        if elem.is_enabled(): return True
        time.sleep(0.5)
    log().error("Element " + xpath + " isn't enable")
    raise TimeoutException


def element_text_content(xpath):
    elem = get_element(xpath)
    text = elem.get_attribute('textContent')
    return text
