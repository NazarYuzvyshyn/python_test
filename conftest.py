import pytest
from main.custom_utils.custom_logger import log
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
    log().info("=============== " + name + " STARTED ==================")
    WebDriverFactory.set_driver(get_brows)
    yield web_driver
    if request.node.rep_call.failed:
        WebDriverFactory.driver().get_screenshot_as_file(
            'D:/PROGRAMMIROVANIE/MY_JAVA/pycharmProjects/newproj/tests/screenshots/' + name + '.png')
    WebDriverFactory.kill_driver()
    log().info("=============== " + name + " FINISHED ==================")
    return web_driver
