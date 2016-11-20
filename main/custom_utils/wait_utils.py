import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    presence_of_all_elements_located
from selenium.webdriver.support.wait import WebDriverWait

from main.custom_utils.custom_logger import error
from main.custom_utils.web_driver_factory import WebDriverFactory
from main.custom_utils.web_elem_utils import get_element


def wait_page_load(timeout):
    """ Wait until page is entire changed """
    t = time.time() + timeout
    while time.time() < t:
        if WebDriverFactory.driver().execute_script("return document.readyState") == "complete":
            return True
        time.sleep(0.5)
    error("Timeout on page load")
    raise TimeoutException


def wait_change_url(stale_url, timeout):
    t = time.time() + timeout
    while time.time() < t:
        new_url = WebDriverFactory.driver().current_url
        if new_url != stale_url:
            wait_page_load(30)
            return True
        time.sleep(0.5)
    error("URL still " + stale_url)
    raise TimeoutException


def wait_for_url(new_url, timeout):
    t = time.time() + timeout
    url = None
    while time.time() < t:
        url = WebDriverFactory.driver().current_url
        if new_url in url:
            wait_page_load(30)
            return True
        time.sleep(0.5)
    error("URL: %s doesn't contains '%s'" % (url, new_url))
    raise TimeoutException


def wait_element_enable(name, by_what: By, locator, timeout):
    t = time.time() + timeout
    while time.time() < t:
        try:
            elem = get_element(by_what, locator)
            if elem.is_enabled(): return True
        except NoSuchElementException:
            pass
        time.sleep(0.5)
    error("Element %s  %s isn't enable" % (name, locator))
    raise TimeoutException


def wait_element_visible(name, locator, timeout):
    try:
        wait = WebDriverWait(WebDriverFactory.driver(), timeout)
        wait.until(visibility_of_element_located(locator))
        return True
    except TimeoutException:
        error("Element %s  %s isn't visible" % (name, locator))
        assert 0


def wait_list_elements(name, locator, timeout):
    try:
        wait = WebDriverWait(WebDriverFactory.driver(), timeout)
        wait.until(presence_of_all_elements_located(locator))
        return True
    except TimeoutException:
        error("List of elements %s  %s is empty" % (name, locator))
        assert 0
