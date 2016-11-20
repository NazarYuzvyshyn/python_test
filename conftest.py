import pytest
from main.custom_utils.custom_logger import *
from main.custom_utils.general_utils import make_screenshot
from main.custom_utils.web_driver_factory import WebDriverFactory


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="ff")


@pytest.fixture()
def get_brows(request):
    return request.config.getoption("--browser")


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def web_driver(request, get_brows):
    name = request.module.__name__[6:-5]
    info("=============== " + name + " STARTED ==================")
    WebDriverFactory.set_driver(get_brows)
    yield web_driver
    if request.node.rep_call.failed:
        make_screenshot(name + ' << FAILED TEST SCREENSHOT >>')
    WebDriverFactory.kill_driver()
    info("=============== " + name + " FINISHED ==================")
    return web_driver
