from main.custom_utils.general_servise import *
from main.custom_utils.web_elem_servise import click_on


def test_001(web_driver):
    get_url("http://www.top-best.com")
    wait_page_load(15)
    raise TimeoutException

