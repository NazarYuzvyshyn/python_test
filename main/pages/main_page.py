from main.custom_utils.general_servise import wait_change_url, page_url
from ..custom_utils.web_elem_servise import click_on
from ..custom_utils.custom_logger import log
from ..custom_utils.web_driver_factory import WebDriverFactory


class MainPage:
    driver = WebDriverFactory.driver()
    register_page = "//*[contains(@class,'menu-header')]//*[text()='Реєстрація']"

    def goto_register_page(self):
        current_url = page_url()
        click_on(self.register_page)
        wait_change_url(current_url, 20)
        log().info("Expected page: Registration")
