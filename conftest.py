from main.custom_services.general_services import make_screenshot
from main.custom_services.web_driver_factory import WebDriverFactory
from tests.custom_logger import *


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
    info_test("=============== " + name + " STARTED ==================")
    WebDriverFactory.set_driver(get_brows)


@pytest.yield_fixture(scope="function")
def end(request):
    yield end
    info_test("yield")
    name = request.module.__name__[6:-5]
    if request.node.rep_call.failed:
        make_screenshot(name + ' << FAILED TEST SCREENSHOT >>')
    WebDriverFactory.kill_driver()
    info_test("=============== " + name + " FINISHED ==================")
