# -*- coding: utf-8 -*-

import re
from urllib.parse import unquote

import allure
from nose.tools import assert_equal
from nose.tools import assert_in
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from main.custom_services.element_services import get_element
from main.custom_services.wait_services import wait_page_load
from main.custom_services.web_driver_factory import WebDriverFactory
from tests.custom_logger import *


def go_to(url):
    """ Use module constants.py to make full url """
    WebDriverFactory.driver().get(url)
    wait_page_load(30)
    info("Go to " + url)


def lines_from_file(path):
    file = open(path)
    lines = file.readlines()
    file.close()
    return lines


def clear_price(price):
    return re.search("[\d\s]+", price).group().strip().replace(" ", "")


def get_url() -> str:
    decode_url = unquote(WebDriverFactory.driver().current_url)
    return decode_url


def is_equal(arg1, arg2):
    info("ASSERT: " + str(arg1) + " VS " + str(arg2))
    assert_equal(arg1, arg2)


def is_in(arg1, arg2):
    info("ASSERT: " + str(arg1) + " IS IN " + str(arg2))
    assert_in(arg1, arg2)


def make_screenshot(test_name):
    allure.attach(test_name, WebDriverFactory.driver().get_screenshot_as_png(), allure.attach_type.PNG)
    info(test_name + " << FAILED SCREENSHOT >>")


def press_key(key: Keys, by_what: By, locator):
    elem = get_element(by_what, locator)
    elem.send_keys(key)
