from selenium import webdriver
from main.business_object.user import User
from main.pages.base_page import BasePage
from ..custom_utils.custom_logger import log
from ..custom_utils.web_elem_servise import click_on
from ..custom_utils.web_elem_servise import input_keys


class RegisterPage(BasePage):

    email = "//*[@id='reg_username']"
    password = "//*[@id='reg_pass1']"
    confirm_pass = "//*[@id='reg_pass2']"
    subscribe_checkbox = "//*[@id='reg_subscribe']"
    send = "//*[@id='register']"


    def fill_register_form(self, user: User):
        input_keys(user.email, self.email)
        input_keys(user.password, self.password)
        input_keys(user.password, self.confirm_pass)


    def uncheck_subscribe(self):
        if self.driver.find_element_by_xpath(self.subscribe_checkbox).is_selected():
            click_on(self.subscribe_checkbox)
            log().info("Deselect subscribe")
        if self.driver.find_element_by_xpath(self.subscribe_checkbox).is_selected():
            log().error("Checkbox still selected")
            assert 0

    def submit_register(self):
        click_on(self.send)
