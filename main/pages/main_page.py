from selenium import webdriver

from main.pages.base_page import BasePage
from ..custom_utils.custom_logger import log
from ..custom_utils.web_elem_servise import click_on


class MainPage(BasePage):

    register_page = "//*[contains(@class,'menu-header')]//*[text()='Реєстрація']"

    def goto_register_page(self):
        click_on(self.register_page)
        log().info("Expected page: Registration")
