# -*- coding: utf-8 -*-

from urllib.parse import unquote

import allure
from nose.tools import assert_equal
from nose.tools import assert_in
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from main.custom_utils.constants import PROP_PATH
from main.custom_utils.wait_utils import wait_page_load
from main.custom_utils.web_driver_factory import WebDriverFactory
from .custom_logger import *


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


def get_url() -> str:
    decode_url = unquote(WebDriverFactory.driver().current_url)
    return decode_url


def is_equal(arg1, arg2):
    info("ASSERT: " + str(arg1) + " VS " + str(arg2))
    assert_equal(arg1, arg2)


def is_in(arg1, arg2):
    info("ASSERT: " + str(arg1) + " IS IN " + str(arg2))
    assert_in(arg1, arg2)


def property_reader(file_location) -> dict:
    return dict(line.strip().split('=') for line in open(PROP_PATH + file_location + '.txt'))


def make_screenshot(test_name):
    allure.attach(test_name, WebDriverFactory.driver().get_screenshot_as_png(), "image/png")


def press_key(key: Keys):
    action = ActionChains(WebDriverFactory.driver())
    action.send_keys(key).perform()
