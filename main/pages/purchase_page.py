from enum import Enum

from selenium.webdriver.common.by import By

from main.business_object.ticket import Ticket
from main.custom_utils.custom_logger import *
from main.custom_utils.web_driver_factory import WebDriverFactory
from main.custom_utils.web_elem_utils import element_text_content, click_on, get_elements


class PurchasePage:
    class PayBy(Enum):
        CREDIT_CARD = "Банковской картой"
        PRIVAT_24 = "Приват 24"
        WEBMONEY = "Webmoney"

    def pay(self, method: PayBy):
        locator = "//*[text()='%s']/.." % method.name
        click_on(method.name, By.XPATH, locator)

    def check_ticket_info(self, ticket: Ticket):
        info = "//*[contains(@class,'one_offer-booking')]"
        list =
        tickets_list = get_elements(By.XPATH, info)
        tickets_list = map(lambda i: i.text, tickets_list)
        tickets_list = filter(lambda i: train in i, trains_list)
        if trains_list:
            info("%s <<contains>> %s" % (trains_list, train))
            return True
        else:
            error("%s <<doesn't contains>> %s" % (trains_list, train))
            return False

    def confirm_date_and_city(self, date, city):
        date_city = "//*[contains(@class,'one_offer-booking')]//*[contains(@class,'departure-time')]"
        date_city_list = get_elements(By.XPATH, date_city)
        date_city_list = map(lambda i: i.text, date_city_list)
        date_city_list = filter(lambda i: date in i and city in i, date_city_list)
        if date_city_list:
            info("%s <<contains>> %s and %s" % (date_city_list, date, city))
            return True
        else:
            error("%s <<doesn't contains>> %s and %s" % (date_city_list, date, city))
            return False

    def confirm_passenger_and_