from enum import Enum

from selenium.webdriver.common.by import By

from main.custom_services.custom_logger import *
from main.custom_services.general_services import clear_price
from main.custom_services.wait_services import wait_for_url
from main.custom_services.web_elem_services import click_on, get_elements, element_text_content, get_element


class PayBy(Enum):
    CREDIT_CARD = "Банковской картой"
    PRIVAT_24 = "Приват 24"
    WEBMONEY = "Webmoney"


class PurchasePage:
    def pay(self, method: PayBy):
        locator = "//*[text()='%s']/.." % method.name
        click_on(method.name, By.XPATH, locator)

    def check_ticket_info(self, ticket_info: list):
        info_locator = "//*[contains(@class,'one_offer-booking')]"
        tickets = get_elements(By.XPATH, info_locator)
        tickets = list(map(lambda i: i.text, tickets))
        return self.text_list_in_text(tickets, ticket_info)

    def get_price(self):
        price_locator = "//*[@data-payment-data='tarif']"
        price = element_text_content(get_element(By.XPATH, price_locator))
        info("Price before paying: " + price)
        return int(clear_price(price))

    def submit(self):
        submit = "//*[contains(@class,'booking_price_button')]//*[@type='submit']"
        click_on("Продолжить", By.XPATH, submit)
        wait_for_url("checkout", 30)

    def text_list_in_text(self, main_text, text_list: list):
        checker = 0
        for itr in main_text:
            checker = 0
            for k in text_list:
                if k not in itr:
                    checker = 1
                    break
            if checker is 0:
                info("%s <<contains>> %s" % (itr, text_list))
                return True
        if checker is 1:
            error("%s <<doesn't contains>> %s" % (main_text, text_list))
            return False
