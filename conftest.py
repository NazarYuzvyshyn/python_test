import pytest
from main.custom_utils.custom_logger import log
from main.custom_utils.web_driver_factory import WebDriverFactory


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="ff")


@pytest.fixture()
def get_brows(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="function")
def web_driver(request, get_brows):
    name = request.module.__name__[0:-5]
    log().info("=============== " + name + " STARTED ==================")

    WebDriverFactory.set_driver(get_brows)
    yield web_driver
    WebDriverFactory.kill_driver()
    log().info("=============== " + name + " FINISHED ==================")
    return web_driver
