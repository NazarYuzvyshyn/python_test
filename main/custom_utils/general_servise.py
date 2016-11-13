import time
from urllib.parse import unquote

from nose.tools import assert_equal
from nose.tools import assert_in
from selenium.common.exceptions import TimeoutException

from main.custom_utils.web_driver_factory import WebDriverFactory
from .custom_logger import log


def wait_page_load(timeout):
    """ Wait until page is entire changed """
    t = time.time() + timeout
    while time.time() < t:
        boo = WebDriverFactory.driver().execute_script("return document.readyState")
        if boo == "complete": return True
        time.sleep(0.5)
    log().error("Timeout on page load")
    raise TimeoutException


def get_url(url):
    """ Use module constants.py to make full url """
    WebDriverFactory.driver().get(url)
    wait_page_load(30)
    log().info("Go to " + url)


def lines_from_file(path):
    file = open(path)
    lines = file.readlines()
    file.close()
    return lines


def wait_change_url(url, timeout):
    t = time.time() + timeout
    while time.time() < t:
        new_url = WebDriverFactory.driver().current_url
        if new_url != url:
            wait_page_load(30)
            return True
        time.sleep(0.5)
    log().error("URL still " + url)
    raise TimeoutException


def page_url() -> str:
    decode_url = unquote(WebDriverFactory.driver().current_url)
    return decode_url


def is_equal(arg1, arg2):
    log().info("ASSERT: " + str(arg1) + " VS " + str(arg2))
    assert_equal(arg1, arg2)


def is_in(arg1, arg2):
    log().info("ASSERT: " + str(arg1) + " IS IN " + str(arg2))
    assert_in(arg1, arg2)
