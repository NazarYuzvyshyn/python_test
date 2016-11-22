from enum import Enum

from selenium.webdriver.common.by import By

from main.business_object.ticket import Ticket
from main.custom_services.custom_logger import *
from main.custom_services.element_services import click_on, get_elements, element_text_content, get_element
from main.custom_services.general_services import clear_price
from main.custom_services.wait_services import wait_for_url


class PayBy(Enum):
    CREDIT_CARD = "direct"
    PRIVAT_24 = "ecommerce"
    WEBMONEY = "webmoney"


class PurchasePage:
    def __init__(self, ticket: Ticket):
        self.ticket = ticket

    def pay(self, method: PayBy):
        locator = "//*[contains(@class,'payment_tab') and @data-pay_group='%s']" % method.value
        click_on(method.name, By.XPATH, locator)

    def check_ticket_info(self, ticket_info: list):
        """ Gets ticket/s subscribing information like text and checks
             that train,place type,place,date and city,which were chosen,
             are involved and are the sames"""
        info_locator = "//*[contains(@class,'result-list') and parent::*[@id='content']]"
        tickets = get_elements(By.XPATH, info_locator)
        tickets = list(map(lambda i: i.text, tickets))
        return self.text_in_text(tickets, ticket_info)

    def get_price(self):
        price_locator = "//*[@data-payment-data='tarif']"
        price = element_text_content(get_element(By.XPATH, price_locator))
        price = int(clear_price(price))
        info("Price before paying is: %s and single tickets price are: %s + %s"
             % (price, self.ticket.price, self.ticket.round_price))
        return price

    def submit(self):
        submit = "//*[contains(@class,'booking_price_button')]//*[@type='submit']"
        click_on("Продолжить", By.XPATH, submit)
        wait_for_url("checkout", 30)

    def text_in_text(self, text_for_checking: list, text_have_to_be_in: list):
        """ Checks presence some text in other text. Give each text like a list for
            multiple variants for checking. Example: form list of texts choose only one
            which contains set of all strings."""
        checker = 0
        for i in text_for_checking:
            checker = 0
            for k in text_have_to_be_in:
                if k not in i:
                    checker = 1
                    break
            if checker is 0:
                info("###### %s ###### << contains >> %s" % (i, text_have_to_be_in))
                return True
        if checker is 1:
            for q in text_for_checking:
                error("###### %s ######" % q)
            error("Text above << doesn't contains >> %s" % text_have_to_be_in)
            return False
